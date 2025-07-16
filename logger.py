# logger.py
import logging

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("lucy.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
