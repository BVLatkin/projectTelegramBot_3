import datetime
import time

from db import Base, Word
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


async def words(update, context):
    words1 = session.query(Word).all()
    for word in words1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=word.word)


def send_message(context):
    context.bot.send_message(chat_id=context.job.context, text="Hello! This is a scheduled message.")


# Function to start the scheduler
def start_scheduler(update, context):
    job_queue = context.job_queue
    chat_id = update.message.chat_id
    job_queue.run_daily(send_message, time=datetime.time(hour=0, minute=0, second=10), context=chat_id)