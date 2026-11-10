from fastapi import FastAPI
from api.router import router

# import the base 
from models.model import Base

# import the engine
from core.db import engine

# create all the tables in the database
Base.metadata.create_all(engine)

app = FastAPI()

# include the router
app.include_router(router=router)


@app.get('/')
def port():
    return {'message' : 'server is working'}