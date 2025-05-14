import logging
import torch
from pathlib import Path
from torch.utils.data import DataLoader
import pytest

from ai.src.data.dataset import CarClassificationDataset

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"
IMAGES_DIR = DATA_DIR / "images"

print(DATA_DIR , "+",  IMAGES_DIR)



@pytest.mark.parametrize("mode", ["train", "val", "test"])
class TestCarDataset:
    def test_dataset_initialization(self, mode):

        dataset = CarClassificationDataset(
            data_dir=str(DATA_DIR),
            df_path=None,
            img_dir=str(IMAGES_DIR),
            transform=None,
            mode=mode,
        )

        assert len(dataset) == len(dataset.df)
        assert hasattr(dataset, "__getitem__")

    def test_dataset_getitem(self, mode, sample_image, test_transform):

        dataset = CarClassificationDataset(
            data_dir=str(DATA_DIR),
            df_path=None,
            img_dir=str(IMAGES_DIR),
            transform=test_transform,
            mode=mode,
        )

        item = dataset[0]

        assert isinstance(item["image"], torch.Tensor) or isinstance(item["image"], str)
        if mode != "test":
            assert "label" in item
            assert "class_name" in item
        assert "image_id" in item

    def test_dataloader_integration(self, mode, test_transform):

        dataset = CarClassificationDataset(
            data_dir=str(DATA_DIR),
            df_path=None,
            img_dir=str(IMAGES_DIR),
            transform = test_transform,
            mode=mode,
        )

        dataloader = DataLoader(dataset, batch_size=2, shuffle=False)

        batch = next(iter(dataloader))

        assert isinstance(batch, dict)
        assert "image" in batch
        assert batch["image"].shape == (2, 3, 224, 224)
        assert batch["image"].shape[0] == 2