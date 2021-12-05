from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
import os

load_dotenv()
from routes import router
app = FastAPI(title="chat api", description="chat app backend showcase")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(router)

register_tortoise(app,db_url=os.getenv("DB_URL"),
                  modules={"models":["models"]},
                  generate_schemas=True,
                  add_exception_handlers=True)
