import os
import pandas as pd
from PIL import Image

def create_sample_dataset():
    data_dir = "./data/processed"
    image_dir = os.path.join(data_dir, "images")
    os.makedirs(image_dir, exist_ok=True)

    # 샘플 이미지 생성
    for color, filename in [("red", "0001.jpg"), ("blue", "0002.jpg")]:
        img = Image.new('RGB', (224, 224), color=color)
        img.save(os.path.join(image_dir, filename))
        print(f"샘플 이미지 생성: {filename}")

    # 샘플 CSV 데이터
    df = pd.DataFrame({
        "image_id": ["0001.jpg", "0002.jpg"],
        "class": ["SUV", "Sedan"]
    })

    for mode in ["train", "val", "test"]:
        csv_path = os.path.join(data_dir, f"{mode}.csv")
        df.to_csv(csv_path, index=False)
        print(f"샘플 {mode}.csv 생성")

if __name__ == "__main__":
    create_sample_dataset()

