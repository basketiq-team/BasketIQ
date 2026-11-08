from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def port():
    return {'message' : 'server is working'}