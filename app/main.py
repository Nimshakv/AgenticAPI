from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

import requests
import os

app = FastAPI()


# Get agent details from environment variables
AI_FOUNDRY_ENDPOINT = "westus.api.azureml.ms;831352c0-db5c-4b45-a2c3-3b05baf07718;rg-nimshaakv-8998;hub-project"  # Orchestrator agent endpoint
AI_FOUNDRY_KEY = "1MXbrmRy4XvQXmx97GkVgt1RzktKARgGG0xCm8lZfy3jaqwmpXWLJQQJ99BIACHYHv6XJ3w3AAAAACOGESSF"  # API Key (or replace with Managed Identity)

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


