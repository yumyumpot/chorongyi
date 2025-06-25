from torchvision.models import efficientnet_b4
from torch import nn

def get_model_b4(config):
    model = efficientnet_b4(pretrained=True)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, config.NUM_CLASSES)
    return model