import logging
import sys

def setup_logger(name="logger", level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s : %(name)s : %(levelname)s : %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        
        file_handler = logging.FileHandler("app.log")
        file_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
    
    return logger

logger = setup_logger()