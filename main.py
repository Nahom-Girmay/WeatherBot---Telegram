from fastapi import FastAPI, Request
import uvicorn
from contextlib import asynccontextmanager

from aiogram.types import Update

from bot import bot, dp
import handlers

from config import WEBHOOK_URL



@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup
    webhook_url = f"{WEBHOOK_URL}/webhook"

    await bot.set_webhook(webhook_url)

    print(f"Webhook set: {webhook_url}")


    yield


    # Shutdown
    await bot.delete_webhook(drop_pending_updates=True)

    await bot.session.close()



app = FastAPI(lifespan=lifespan)



@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    update = Update.model_validate(data)

    await dp.feed_update(
        bot,
        update
    )

    return {"status": "ok"}



@app.get("/")
async def home():

    return {
        "status": "Weather Bot is running"
    }



if __name__ == "__main__":

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )