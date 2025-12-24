from fastapi import FastAPI
from api1 import router

app = FastAPI(title="Contact Manager API", version="1.0.0")

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)