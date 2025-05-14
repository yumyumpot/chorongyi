import os
from PIL import Image
import PIL
import warnings
from glob import glob
import numpy as np
import math
import time

from s3.s3_client import S3Client

def run_dataset():
    start = time.time()
    warnings.filterwarnings(action="ignore")

    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    path = "data/raw/ai_hub/원천데이터/TS1/BE_벤츠/"

    training_images = []
    training_labels = []

    for filename in glob(path + "*"):
        print(f"processing {filename}")
        found_images = glob(filename + "/**/*.jpg", recursive=True)
        print(f"found {len(found_images)} images")
        for img in glob(filename + "/**/*.jpg", recursive=True):
            an_img = PIL.Image.open(img)
            img_array = np.array(an_img)
            training_images.append(img_array)
            label = os.path.basename(filename)
            training_labels.append(label)

    training_images = np.array(training_images)
    training_labels = np.array(training_labels)

    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()
    print(f"데이터 라벨링 포맷 정리 : {le}")
    training_labels = le.fit_transform(training_labels)
    training_labels = training_labels.reshape(-1, 1)

    print(training_images.shape)
    print(training_labels.shape)

    math.factorial(100000)
    end = time.time()

    print(f"{end - start:.5f} sec" )
