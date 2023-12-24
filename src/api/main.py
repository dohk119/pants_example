from src.repo1.hello import Hello
from loguru import logger

cosa: Hello = Hello()
print(cosa.greet())

logger.info('Logging!!!!')

