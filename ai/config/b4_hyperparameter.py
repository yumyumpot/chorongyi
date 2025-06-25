from dataclasses import dataclass

import torch


@dataclass
class B4Hyperparameter:
    IMG_SIZE: int = 224                                             # 이미지 크기
    BATCH_SIZE: int = 32                                            # 학습 시 배치 사이즈
    EPOCHS: int = 10                                                # 전체 학습 epoch수
    LEARNING_RATE: float = 1e-4                                     # 학습률
    SEED: int = 42                                                  # 랜덤 시드 (재현성 확보)
    MODEL_NAME: str = "efficientnet_b4"                             # 모델 이름
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"    # 사용 장치
    NUM_WORKERS: int = 4                                            # DataLoader에서 사용할 병렬 처리 수
    NUM_CLASSES: int = 50                                           # 클래스 수 (데이터셋에 따라 조정 가능)
