from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello world! "
                       "Welcome to the API!"}

@app.get("/favicon.ico", tags=["Favicon"])
async def favicon():
    return Response(status_code = HTTP_204_NO_CONTENT)