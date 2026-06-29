from __future__ import annotations

import json

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from custodian_labs import create_assistant

app = FastAPI()


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket) -> None:
    await websocket.accept()

    sdk_app = create_assistant(
        model="gpt-4o",
        prompt="You are a helpful assistant exposed through a websocket bridge.",
        name="WebSocket Bridge AI",
        privacy_enabled=True,
    )

    try:
        while True:
            raw = await websocket.receive_text()
            try:
                payload = json.loads(raw)
                message = str(payload.get("message") or "").strip()
            except json.JSONDecodeError:
                message = raw.strip()

            if not message:
                await websocket.send_json({"error": "message is required"})
                continue

            reply = sdk_app.chat(message)
            await websocket.send_json(
                {
                    "response": reply.response if reply is not None else "",
                    "session_id": reply.session_id if reply is not None else None,
                    "chat_url": sdk_app.chat_url,
                }
            )
    except WebSocketDisconnect:
        return