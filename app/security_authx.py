from fastapi import FastAPI
from authx import AuthX, AuthXConfig

app = FastAPI()

config = AuthXConfig()

config.JWT_SECRET_KEY =''
config.JWT_ACCESS_COOKIE_NAME = 'my_access_token'
config.JWY_TOKEN_LOCATION = ['cookies']


security = AuthX(config=config)