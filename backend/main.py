from fastapi import FastAPI, WebSocket
from interviewer import InterviewSession
import uvicorn

app = FastAPI()

# Store active sessions
sessions = {}

@app.post("/start-interview")
async def start_interview(config: dict):
    # config: { difficulty: 'Hard', company: 'Microsoft', experience: 4 }
    session_id = "test_user_123" 
    sessions[session_id] = InterviewSession(config)
    first_question = sessions[session_id].get_initial_greeting()
    return {"session_id": session_id, "message": first_question}

@app.post("/chat")
async def chat(session_id: str, user_message: str):
    session = sessions.get(session_id)
    response = session.process_message(user_message)
    return response

@app.post("/evaluate-code")
async def evaluate_code(session_id: str, code: str, language: str):
    session = sessions.get(session_id)
    feedback = session.check_code(code, language)
    return feedback

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)