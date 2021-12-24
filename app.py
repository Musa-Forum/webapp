import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/authorization/")
#@app.get("../webapp_quiz/webapp/")
async def read_item(emailad:str, row:str):
    permission(emailad,row)
    return{"ping":"pong"}

if __name__ == "__main__":
    app.debug = True
    #app.run(host='127.0.0.1', port=8080)
    uvicorn.run(app)
