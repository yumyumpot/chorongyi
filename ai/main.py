import logging

from cowpy.cow import Cowacter
from src.data.dataset import run_dataset
logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s.%(levelname)s %(module)s - %(funcName)s: %(message)s",
)

def banner_message():
    message = Cowacter().milk("yumyum AI Challenge")
    print(message)


if __name__ == "__main__":
    banner_message()
    run_dataset()