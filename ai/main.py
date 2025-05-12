import logging

from ai.tests.data.test_dataset import test_dataset_loading
from cowpy.cow import Cowacter

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def banner_message():
    message = Cowacter().milk("yumyum AI Challenge")
    print(message)

def run_tests():
    logger.info("테스트 실행 시작")

    test_dataset_loading()
    logger.info("테스트 실행 완료")

if __name__ == "__main__":
    banner_message()
    run_tests()