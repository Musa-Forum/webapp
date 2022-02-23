import uvicorn
from fastapi import FastAPI
import authorization

app = FastAPI()

@app.get("/authorization")
async def read_item(emailad:str, row:str):
    authorization.permission(emailad,row)
    return{"ping":"pong"}

def main():
    app.debug = True
    uvicorn.run(app)

if __name__ == "__main__":
    main()
    #app.debug = True
    #app.run(host='127.0.0.1', port=8080)
    #uvicorn.run(app)
