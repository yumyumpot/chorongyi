import os
from pathlib import Path
import pytest
import torch
import pandas as pd
import torchvision.transforms as T

def pytest_addoption(parser) :
    parser.addini("test_image_size", "default image size", default="244")
    parser.addini("test_batch_size", "default batch size", default="4")
    parser.addini("test_rgb", "default batch size", default="3")


@pytest.fixture
def test_transform():
    return T.ToTensor()

@pytest.fixture
def test_data_dir():
    return os.path.join(os.path.dirname(__file__), "test_data")

@pytest.fixture
def sample_image(request):
    size = int(request.config.getini("test_image_size"))
    rgb = int(request.config.getini("test_rgb"))
    return torch.rand(rgb, size, size)

@pytest.fixture
def sample_car_dataset():
    df = pd.DataFrame({
        'image_path' :
            [
                '0001.png',
                '0002.png',
            ],
        'car_type' : [
            'sedan',
            'suv'
        ],
        'manufacture_year' : [2015,2018],
        'condition_score': [8.5, 7.1],
    })
    return df

@pytest.fixture
def sample_batch(request):
    size = int(request.config.getini("test_image_size"))
    batch = int(request.config.getini("test_batch_size"))
    rgb = int(request.config.getini("test_rgb"))
    images = torch.rand(batch, rgb, size, size)
    labels = torch.tensor([0, 1, (batch,)])
    return images, labels

@pytest.fixture
def temp_test_dir(tmpdir):
    test_dir = Path(tmpdir) / "test_output"
    test_dir.mkdir(exist_ok=True)
    yield test_dir