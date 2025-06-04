from sklearn.model_selection import train_test_split
from ai.config import b4_hyperparameter
from torchvision import transforms
from ai.src.data.dataloader import get_dataloader
from ai.src.models.efficientnet import get_model_b4
from ai.src.utils.seed import set_seed
from torch.optim import optim
from torch import nn
from ai.src.trainer.b4_trainer import B4Trainer

image_paths = []
labels = []

def objective(trial):
    cfg = b4_hyperparameter()
    set_seed(cfg.SEED)
    cfg.LEARNING_RATE = trial.suggest_float("learning_rate", 1e-5, 1e-3, log=True)
    cfg.BATCH_SIZE = trial.suggest_categorical("batch_size", [8, 16, 32])
    cfg.EPOCHS = trial.suggest_int("epochs", 10, 20, step=5)

    transform = transforms.Compose([
        transforms.Resize((cfg.IMG_SIZE, cfg.IMG_SIZE)),
        transforms.ToTensor(),
    ])

    train_img, val_img, train_label, val_label = train_test_split(image_paths, labels, test_size=0.2)
    train_loader = get_dataloader(train_img, train_label, cfg, transform)
    val_loader = get_dataloader(val_img, val_label, cfg, transform, shuffle=False)

    model = get_model_b4(cfg)
    optimizer = optim.Adam(model.parameters(), lr=cfg.LEARNING_RATE)
    criterion = nn.CrossEntropyLoss()

    trainer = B4Trainer(model, optimizer, criterion, cfg, cfg.DEVICE)

    for _ in range(cfg.EPOCHS):
        trainer.train_one_epoch(train_loader)

    accuracy = trainer.evaluate(val_loader)
    return accuracy
