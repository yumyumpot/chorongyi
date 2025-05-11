import logging
from src.data.dataset import create_dataloaders

logger = logging.getLogger(__name__)

def test_dataset_loading():
    data_dir = "./data/processed"

    dataloaders = create_dataloaders(data_dir, batch_size=2)

    for mode, dataloader in dataloaders.items():
        logger.info(f"Mode: {mode}, Total Batches: {len(dataloader)}")

        for batch_idx, batch in enumerate(dataloader):
            logger.debug(f"Batch {batch_idx + 1} Loaded")
            logger.debug(f"Image Tensor Shape: {batch['image'].shape}")
            if mode != 'test':
                logger.debug(f"Labels: {batch['label']}")
                logger.debug(f"Class Names: {batch['class_name']}")
            logger.debug(f"Image IDs: {batch['image_id']}")
            break