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


'''def remove_job_if_exists(name: str, context):
    """Удаляет задание с указанным именем. Возвращает, было ли задание удалено."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def alarm(context):
    """Отправляет сообщение-напоминание каждые 3 секунды."""
    job = context.job
    while True:
        await context.bot.send_message(chat_id=job.chat_id, text='words')
        await asyncio.sleep(3)


async def set_timer(update, context):
    """Добавляет задание в очередь."""
    chat_id = update.effective_message.chat_id
    due = 3

    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)

    text = "Timer successfully set!"
    if job_removed:
        text += " Old one was removed."
    await update.effective_message.reply_text(text)
'''