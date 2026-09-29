from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message": "StudyFlow backend is running"}
@app.get("/hello")
def hello():
    return{"message": "StudyFlow backend is running222"}