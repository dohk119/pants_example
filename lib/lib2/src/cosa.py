from pydantic import BaseModel
from loguru import logger


class Cosa(BaseModel):
    logger.info('Creating COSA from BaseModel')
    id: int
    name: str