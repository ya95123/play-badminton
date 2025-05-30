from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
import uuid

app = FastAPI()

# 允許前端跨域
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# 房間資料暫存於記憶體
rooms: Dict[str, dict] = {}
connections: Dict[str, List[WebSocket]] = {}

@app.post("/create_room")
def create_room(payload: dict):
  room_id = str(uuid.uuid4())[:8]
  room = {
    "id": room_id,
    "password": payload.get("password"),
    "court_count": payload.get("court_count", 1),
    "players_per_court": payload.get("players_per_court", 4),
    "owner": payload.get("owner"),
    "players": [],
    "queue": [],
    "settings": payload.get("settings", {}),
  }
  rooms[room_id] = room
  connections[room_id] = []
  return {"room_id": room_id}

@app.post("/join_room")
def join_room(payload: dict):
  room_id = payload.get("room_id")
  password = payload.get("password")
  name = payload.get("name")
  room = rooms.get(room_id)
  if not room or room["password"] != password:
    raise HTTPException(status_code=403, detail="房間不存在或密碼錯誤")
  if name not in room["players"]:
    room["players"].append(name)
  return {"msg": "joined", "room": room}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
  await websocket.accept()
  if room_id not in connections:
    connections[room_id] = []
  connections[room_id].append(websocket)
  try:
    while True:
      data = await websocket.receive_json()
      # 廣播給同房間所有人
      for conn in connections[room_id]:
        if conn.application_state == conn.application_state.CONNECTED:
          await conn.send_json(data)
  except WebSocketDisconnect:
      connections[room_id].remove(websocket) 