from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()

notes = [
{"id":1,
"title":"FastAPI Intro",

"content":"FastAPI is used to build backend APIs in Python.",

"category":"Backend",

"priority":"High"
}
,
{ "id":2,

"title":"Request Body",

"content":"A request body carries data sent by the client.",

"category":"API",
"priority":"Medium"
}
]
@app.get('/')
def home():
    return{'message': 'Notes API is running successfully'}

@app.get("/notes")
def get_notes():
    return notes

class NoteCreate(BaseModel):
    title: str
    content: str
    category: str
    priority: str

@app.post("/notes", status_code= status.HTTP_201_CREATED)
def create_note(note: NoteCreate):
    if notes:
        next_id = max(item["id"] for item in notes) + 1
    else:
        next_id = 1

    new_note = {
        "id": next_id,
        "title": note.title,
        "content": note.content,
        "category": note.category,
        "priority": note.priority
    }


    notes.append(new_note)

    return {
        "message": "Note created successfully!",
        "note": new_note
    }