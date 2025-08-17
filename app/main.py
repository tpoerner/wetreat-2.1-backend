from fastapi import FastAPI
import threading
import time
import uvicorn

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

# Dummy background thread to keep the app alive on Railway
def keep_alive():
    while True:
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=keep_alive, daemon=True).start()
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
