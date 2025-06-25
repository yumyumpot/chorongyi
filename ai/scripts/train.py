from sklearn.model_selection import train_test_split
import torch
from src.data.dataloader import get_dataloader
from src.data.dataset import CarDataset
from src.trainer.b4_trainer import B4Trainer
from config.b4_hyperparameter import B4Hyperparameter
from src.utils.seed import set_seed
from torchvision import transforms
from src.models.efficientnet import get_model_b4

def main():
    cfg = B4Hyperparameter()
    set_seed(cfg.SEED)

    transform = transforms.Compose([
        transforms.Resize((cfg.IMG_SIZE, cfg.IMG_SIZE)),
        transforms.ToTensor(),
    ])

    train_img, val_img, train_label, val_label = train_test_split(image_paths, labels, test_size=0.2)
    train_loader = get_dataloader(train_img, train_label, cfg, transform)
    val_loader = get_dataloader(val_img, val_label, cfg, transform, shuffle=False)

    model = get_model_b4(cfg)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.LEARNING_RATE)
    criterion = torch.nn.CrossEntropyLoss()

    trainer = B4Trainer(model, optimizer, criterion, cfg, cfg.DEVICE)

    for epoch in range(cfg.EPOCHS):
        loss = trainer.train_one_epoch(train_loader)
        acc = trainer.evaluate(val_loader)
        print(f"Epoch {epoch+1}/{cfg.EPOCHS}, Train Loss: {loss:.4f}, Val Loss: {loss:.4f}, Val Acc: {acc:.4f}")



