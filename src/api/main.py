from repo1.hello import Hello
from loguru import logger

from user import User
from cosa import Cosa

from typing import Union

from fastapi import FastAPI
import uvicorn

logger.info('Creating!!!!')

app = FastAPI()


@app.get("/")
async def read_root():
    user = User(id=1, name='Kitty')
    cosa = Cosa(id=2, name='Cosa')
    return [user, cosa]
    # return {"Hello": "World"}


if __name__ == "__main__":
    logger.info('Starting....')
    uvicorn.run(app, port=8000, log_level="debug")
