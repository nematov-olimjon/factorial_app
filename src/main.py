from fastapi import FastAPI, WebSocket, Request
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse
import math

app = FastAPI()

templates = Jinja2Templates(directory="templates")


async def process_data(data: str) -> str:
    try:
        # Calculate the factorial of incoming data
        result = math.factorial(int(data))
        return str(result)
    except ValueError:
        return "Error: Invalid input. Please enter a valid integer."


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Handle incoming messages from the client
        processed_data = await process_data(data)

        # Send the processed data back to the client
        await websocket.send_text(processed_data)


@app.get("/")
async def get(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {"request": request})
