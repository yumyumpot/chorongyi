import os
import pandas as pd
from typing import Optional, Callable, Dict
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torch
from torchvision import transforms

class CarClassificationDataset(Dataset):

    def __init__(self,
                 data_dir: str,
                 df_path: Optional[str] = None,
                 img_dir: Optional[str] = None,
                 transform: Optional[Callable] = None,
                 mode: str = 'train'):
        self.data_dir = data_dir
        self.mode = mode
        self.transform = transform

        if df_path is None:
            self.df_path = os.path.join(data_dir, f"{mode}.csv")
        else:
            self.df_path = df_path

        if img_dir is None:
            self.img_dir = os.path.join(data_dir, "images")
        else:
            self.img_dir = img_dir

        self.df = pd.read_csv(self.df_path)

        if mode != 'test':
            self.classes = sorted(self.df['class'].unique())
            self.class_to_idx = {cls_name: i for i, cls_name in enumerate(self.classes)}
        else:
            self.classes = None
            self.class_to_idx = None

    def __len__(self) -> int:
        return len(self.df)

    def __getitem__(self, idx: int) -> Dict:
        """
        :arg
            idx (int) : 샘플 인덱스
        :return:
            Dict: 샘플 데이터 ( 이미지, 라벨 (테스트 모드 제외)]
        """

        img_name = self.df.iloc[idx]['image_id']
        img_path = os.path.join(self.img_dir, img_name)

        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        sample = {'image': image}

        if self.mode != 'test':
            label_name = self.df.iloc[idx]['class']
            label = self.class_to_idx[label_name]
            sample['label'] = torch.tensor(label, dtype=torch.long)
            sample['class_name'] = label_name

        sample['image_id'] = img_name

        return sample

def get_transforms(mode: str = 'train', img_size: int = 224) -> transforms.Compose:
    """
    :arg
        mode (str) : 'train', 'val', 'test 중 택 1
        img_size (int) : 이미지 크기
    :return:
        transforms.Compose: 변환 파이프라인
    """

    normalize = transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    )

    if mode == 'train' :
        return transforms.Compose([
            transforms.RandomResizedCrop(img_size),
            transforms.RandomHorizontalFlip(),
            transforms.RandomAffine(degrees=10, translate=(0.1, 0.1)),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
            transforms.ToTensor(),
            normalize,
        ])

    else:
        return transforms.Compose([
            transforms.Resize(int(img_size * 1.14)),
            transforms.CenterCrop(img_size),
            transforms.ToTensor(),
            normalize,
        ])

def create_dataloaders(
        data_dir: str,
        batch_size: int = 32,
        img_size: int = 224,
        num_workers: int = 4,
) -> Dict[str, Dataset]:
    """
    :arg
        data_dir (str) : 데이터 디렉터리 경로
        batch_size (int) : 배치 크기
        img_size (int) : 이미지 크기
        num_workers (int) : 데이터 로딩에 사용할 워커 수
    :return:
        Dict[str, Dataset]: 모드별 데이터 로더
    """
    dataloaders = {}

    for mode in ['train', 'val', 'test']:
        if mode == 'test' and not os.path.exists(os.path.join(data_dir, "test.csv")):
            continue

        dataset = CarClassificationDataset(
            data_dir=data_dir,
            transform=get_transforms(mode, img_size),
            mode=mode,
        )

        dataloaders[mode] = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=(mode == 'train'),
            num_workers=num_workers,
            pin_memory = True
        )
    return dataloaders
