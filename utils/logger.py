import logging
from pathlib import Path

from config import LOG_DIR

LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR/"stockai.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

logger = logging.getLogger(__name__)