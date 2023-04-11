import logging
from .logger.formatters import RedactingFormatter

logging.basicConfig(
    level=logging.DEBUG,  # set the log level to DEBUG
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()  # log to the console
    ]
)

# Use the redacting formatter
formatter = RedactingFormatter('%(asctime)s [%(levelname)s] %(message)s')
logging.getLogger().handlers[0].setFormatter(formatter)