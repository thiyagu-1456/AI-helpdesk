from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import helpdesk_agent


app = FastAPI(
    title="AI IT Helpdesk Agent",
    description="AI-powered IT troubleshooting system using Agent + RAG + Tools",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserQuery(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI IT Helpdesk Agent is running!"
    }


@app.post("/ask")
def ask_helpdesk(query: UserQuery):

    answer = helpdesk_agent(query.message)

    return {
        "user_query": query.message,
        "answer": answer
    }