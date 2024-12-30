import logging
from datetime import datetime
from pathlib import Path


class CustomTextFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        timestamp = datetime.now().strftime('%H:%M:%S')
        level = record.levelname
        message = record.getMessage()
        file = record.filename
        line = record.lineno
        function = record.funcName
        path = record.pathname
        return f"{timestamp} ({level}) {message} | {file} (line {line}) | {function} | {path}"


def setup_logger(
    name: str = __name__,
    log_dir: str = "logs",
    level: int = logging.INFO,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger.handlers.clear()

    text_formatter = CustomTextFormatter()

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(text_formatter)
    logger.addHandler(console_handler)

    date_str = datetime.now().strftime('%Y-%m-%d')  # Format as YYYY-MM-DD
    log_file = Path(log_dir) / f"{date_str}.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(text_formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger(
    name='app_logger',
    log_dir='logs',
    level=logging.DEBUG
)

if __name__ == '__main__':

    try:
        logger.info("Application started")
        logger.debug("Debug message")
        raise ValueError("Example error")
    except Exception as e:
        logger.exception("An error occurred")
