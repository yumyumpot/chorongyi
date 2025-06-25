from .dataset import CarDataset
from torch.utils.data import DataLoader

def get_dataloader(image_paths, labels, config, transform, shuffle=True):
    dataset = CarDataset(image_paths, labels, transform=transform)
    return DataLoader(
        dataset, 
        batch_size=config.BATCH_SIZE, 
        shuffle=shuffle, 
        num_workers=config.NUM_WORKERS, 
        num_workers=config.NUM_CLASSES)