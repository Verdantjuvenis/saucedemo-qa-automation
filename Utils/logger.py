import logging
import os

def get_logger():
    logger = logging.getLogger("qa_logger")

    if not logger.handlers:
        logger.setLevel(logging.INFO)
        os.makedirs("logs", exist_ok=True)

        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("logs/test_run.log")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger