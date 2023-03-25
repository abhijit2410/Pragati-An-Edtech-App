from fastapi import FastAPI, Request, status,BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from app.process import process
import requests,json

app = FastAPI()


@app.get('/')
def welcome():
    return "Welcome to Pragati API"

@app.post('/',status_code=status.HTTP_200_OK)
async def response(resquest:Request,background_tasks: BackgroundTasks):
    try:
        r = await resquest.json()
        background_tasks.add_task(process,r)
    except json.decoder.JSONDecodeError:
        pass

    return {"message": "Received"}
    

    

@app.get('/news')
def html():
    resposne = requests.request('GET','https://newsapi.org/v2/everything?q=education&from=2022-11-06&sortBy=publishedAt&apiKey=da9d1c5a4e954cdfbb770d05c4a571fc')
    return resposne.json()

origins = ["*"]

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
