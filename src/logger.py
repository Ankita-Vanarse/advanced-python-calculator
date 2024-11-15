import logging
import src.config as config

logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=config.LOG_FILE,
    filemode='a'
)

logger = logging.getLogger(__name__)
