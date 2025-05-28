
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, List

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, order_id: int, websocket: WebSocket):
        await websocket.accept()
        if order_id not in self.active_connections:
            self.active_connections[order_id] = []
        self.active_connections[order_id].append(websocket)

    def disconnect(self, order_id: int, websocket: WebSocket):
        self.active_connections[order_id].remove(websocket)
        if not self.active_connections[order_id]:
            del self.active_connections[order_id]

    async def broadcast(self, order_id: int, message: str):
        for connection in self.active_connections.get(order_id, []):
            await connection.send_text(message)


manager = ConnectionManager()

@router.websocket("/ws/chat/{order_id}")
async def websocket_endpoint(websocket: WebSocket, order_id: int):
    ...
