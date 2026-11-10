from fastapi import FastAPI
from api.router import router


app = FastAPI()

# include the router
app.include_router(router=router)


@app.get('/')
def port():
    return {'message' : 'server is working'}