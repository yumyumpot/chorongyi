import torch
from ai.config import b4_hyperparameter
from ai.src.utils.seed import set_seed

def main():
    cfg = b4_hyperparameter()
    set_seed(cfg.SEED)

    model = get_model_b4(cfg)
    model.load_state_dict(torch.load("models/checkopints/EfficientNet_B4_"))
