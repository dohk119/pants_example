from src.repo1.hello import Hello
from loguru import logger

from user import User

cosa: Hello = Hello()
print(cosa.greet())

logger.info('Logging!!!!')

user = User(id=1, name='Hello')
print(user)


