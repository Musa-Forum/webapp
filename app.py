import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.put("/authorization/{emailad}")
#@app.get("../webapp_quiz/webapp/")
def authorization():
    return permission(emailad)


if __name__ == "__main__":
    app.debug = True
    #app.run(host='127.0.0.1', port=8080)
    uvicorn.run(app)
