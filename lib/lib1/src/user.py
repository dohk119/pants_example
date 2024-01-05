from pydantic import BaseModel
from loguru import logger


class User(BaseModel):
    logger.info('Creating user from BaseModel')
    id: int
    name: str
