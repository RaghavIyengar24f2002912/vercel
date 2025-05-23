from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load and transform marks data
with open("q-vercel-python.json") as f:
    data_list = json.load(f)
    marks_data = {entry["name"]: entry["marks"] for entry in data_list}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    results = [marks_data.get(name, 0) for name in names]
    return {"marks": results}
