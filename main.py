from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Learn with Jiji Backend")

class QueryRequest(BaseModel):
    query: str
    user_id: str


@app.get("/health")
def health():
    return {"status": "Server is running"}


@app.post("/ask-jiji")
def ask_jiji(request: QueryRequest):

    return {
        "answer": f"This is a simple explanation for '{request.query}'.",
        "resources": [
            {
                "title": "Introduction to RAG",
                "type": "presentation",
                "url": "https://example.com/rag-ppt"
            },
            {
                "title": "RAG Tutorial Video",
                "type": "video",
                "url": "https://example.com/rag-video"
            }
        ]
    }