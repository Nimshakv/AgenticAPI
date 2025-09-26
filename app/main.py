from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

import requests
import os

app = FastAPI()


# Get agent details from environment variables
AI_FOUNDRY_ENDPOINT = os.getenv("AGENT_ENDPOINT")  # Orchestrator agent endpoint
AI_FOUNDRY_KEY = os.getenv("AGENT_KEY")  # API Key (or replace with Managed Identity)

@app.get("/")
async def root():
    return {"message": "Azure AI Foundry Orchestrator API is running!"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    headers = {
        "Authorization": f"Bearer {AI_FOUNDRY_KEY}",
        "Content-Type": "application/json"
    }

    payload = {"input": user_message}

    response = requests.post(AI_FOUNDRY_ENDPOINT, headers=headers, json=payload)

    return response.json()


