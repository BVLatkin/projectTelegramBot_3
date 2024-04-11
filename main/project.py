import logging
import threading

import schedule
import time
import datetime

import telegram
from telegram.ext import Application, MessageHandler, CommandHandler, CallbackQueryHandler, CallbackContext, Updater, \
    JobQueue, Job
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import filters
from db import Base, Word
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import asyncio

import telebot
import threading


engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

application = Application.builder().token('7148131509:AAEN3LjmdH0RlhkSRW3wKfks6qaHb2S1tsI').build()

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_keyboard_selection = [['Present Simple'],
                            ['Present Continuous'],
                            ['Present Perfect'],
                            ['Present Perfect Continuous'],

                            ['Past Simple'],
                            ['Past Continuous'],
                            ['Past Perfect'],
                            ['Past Perfect Continuous'],

                            ['Future Simple'],
                            ['Future Continuous'],
                            ['Future Perfect'],
                            ['Future Perfect Continuous']]

reply_keyboard_selection_test = [['1) Present Simple'],
                            ['2) Present Continuous'],
                            ['3) Present Perfect'],
                            ['4) Present Perfect Continuous'],

                            ['5) Past Simple'],
                            ['6) Past Continuous'],
                            ['7) Past Perfect'],
                            ['8) Past Perfect Continuous'],

                            ['9) Future Simple'],
                            ['10) Future Continuous'],
                            ['11) Future Perfect'],
                            ['12) Future Perfect Continuous']]

async def present_simple_photo(update):
    photo_file = open('photo/presentSimple.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def present_continuous_photo(update):
    photo_file = open('photo/presentContinuous.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def present_perfect_photo(update):
    photo_file = open('photo/presentPerfect.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def present_perfect_continuous_photo(update):
    photo_file = open('photo/presentPerfectContinuous.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def past_simple_photo(update):
    photo_file = open('photo/pastSimple.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def past_continuous_photo(update):
    photo_file = open('photo/pastContinuous.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def past_perfect_photo(update):
    photo_file = open('photo/pastPerfect.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def past_perfect_continuous_photo(update):
    photo_file = open('photo/pastPerfectContinuous.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def future_simple_photo(update):
    photo_file = open('photo/futureSimple.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def future_continuous_photo(update):
    photo_file = open('photo/futureContinuous.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def future_perfect_photo(update):
    photo_file = open('photo/futurePerfect.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def future_perfect_continuous_photo(update):
    photo_file = open('photo/futurePerfectContinuous.png', 'rb')
    await update.message.reply_photo(photo=photo_file)


async def hello(update, context):
    await update.message.reply_text(
        'Привет! Я бот-помощник, который может обучить вас новым словам в английском языке!\n'
        'Для продолжения напишите /start\n'
        'Если есть вопросы, нажмите /help')


async def start(update, context):
    reply_keyboard = [['Времена'], ['Слова'], ['Тесты по временам']]
    markup = ReplyKeyboardMarkup(reply_keyboard)
    await update.message.reply_text(
        'Выберите, что хотите изучить',
        reply_markup=markup)


async def time1(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text(
        'Выберите время, которое хотите изучить',
        reply_markup=markup)


async def present_simple(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Present Simple (Простое настоящее время)',
                                    reply_markup=markup)

    await present_simple_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'always (всегда)\n'
            'usually (обычно)\n'
            'never (никогда)\n'
            'sometimes (иногда)\n'
            'rarely (нечасто)\n'
            'seldom (редко)\n'
            'regularly (регулярно)\n'
            'every day (каждый день)\n'
            'often (часто)\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Present Simple')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I / He / She / It / You / We / They + V1\n'
            '\n'
            'I go to school every day. — Я хожу в школу каждый день.\n'
            'She walks with her dog three times a day. — Она гуляет со своей собакой трижды в день\n'
            'I always go to school. — Я всегда хожу в школу.\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I / He / She / It / You / We / They + do/does + not + V1\n'
            '\n'
            'I do not live in Volgograd. — Я не живу в Волгограде.\n'
            'You do not study at school. — Ты не учишься в школе.\n'
            'She does not work in a bank. — Она не работает в банке.\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Do/Does + I / He / She / It / You / We / They + V1?\n'
            '\n'
            'Do you work or study? — Ты работаешь или учишься?\n'
            'Do you live in Moscow? — Ты живешь в Москве?\n'
            'Does she like rock music? — Она любит рок-музыку?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def present_continuous(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Present Continuous (Настоящее продолженное время)',
                                    reply_markup=markup)

    await present_continuous_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'today (сегодня)\n'
            'tomorrow (завтра)\n'
            'this/next year (в этом/следующем году)\n'
            'tonight (вечером))\n'
            'now (сейчас)\n'
            'still (всё ещё)\n'
            'at this moment (в текущий момент)\n'
            'currently (в настоящее время)\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Present Continuous')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I / He / She / It / You / We / They + am/is/are + Ving\n'
            '\n'
            'I am eating breakfast. — Я ем завтрак.\n'
            'Students (they) are working on essays. — Студенты работают над эссе.\n'
            'Bob (he) is sleeping. — Боб спит.\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I / He / She / It / You / We / They + am/is/are + not + Ving\n'
            '\n'
            'I am not playing football. — Я не играю в футбол.\n'
            'Mary (she) isn’t playing piano. — Мэри не играет на пианино.\n'
            'Students (they) aren’t sitting in the classroom. — Студенты не сидят в классе.\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Am/Is/Are + I / He / She / It / You / We / They + Ving?\n'
            '\n'
            'Are students (they) watching a film? — Студенты смотрят фильм?\n'
            'Is Bob (he) singing “Let It Be”? — Боб поет “Let It Be”?\n'
            'Is Mary (she) studying right now? — Мэри сейчас учится?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def present_perfect(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Present Perfect (Настоящее совершенное время)',
                                    reply_markup=markup)

    await present_perfect_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'never (никогда)\n'
            'just (только что)\n'
            'already (уже)\n'
            'yet (еще)\n'
            'ever (когда-либо)\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Present Perfect')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I/You/We/They + have + V3 / He/She/It + has + V3\n'
            '\n'
            'We have bought a new house. — Мы купили новый дом.\n'
            'I have lost my phone! — Я телефон потерял!\n'
            'She has broken her leg. — Она сломала ногу. \n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I/You/We/They + have/has not + V3\n'
            '\n'
            'We have not been to Australia - Мы не были в Австралии\n'
            'He has not started - Он не начал\n'
            'They have not made the project - Они не сделали проект\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Have/Has + I/You/We/They + V3?\n'
            '\n'
            'Has it turned on? - Оно включилось?\n'
            'Have we done anything wrong? -	Мы что-то сделали не так?\n'
            'What has he carried? -	Что он перенес?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def present_perfect_continuous(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Present Perfect Continuous (Настоящее совершенное продолженное)',
                                    reply_markup=markup)

    await present_perfect_continuous_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'for a week (в течение недели)\n'
            'since morning (с утра)\n'
            'lately (в последнее время)\n'
            'all my life (всю мою жизнь)\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Present Perfect Continuous')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I/You/We/They + have been + Ving / He/She/It + has been + Ving\n'
            '\n'
            'We have been living in Canada for 10 years. — Мы живем в Канаде 10 лет.\n'
            'He has been studying English for 5 years. – Он изучает английский 5 лет.\n'
            'Andy is very tired.He’s been training hard.– Энди очень устал.У него была тяжелая тренировка.\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I/You/We/They + have/has not been + Ving\n'
            '\n'
            'Lucas has not been feeling well for three weeks. — Лукас плохо себя чувствует уже три недели.\n'
            'She has not been dancing for 2 hours. — Она не танцевала уже 2 часа.\n'
            'My father has not been working since 2020. — Мой отец не работает с 2020 года.\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Have/Has + I/You/We/They + been Ving?\n'
            '\n'
            'Has Lucas been studying in this university for 5 years? — Лукас учится в этом университете уже 5 лет?\n'
            'How long have you been looking for a job? — Как долго вы ищете работу?\n'
            'Who has been living here since November? — Кто живет здесь с ноября?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def past_simple(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Past Simple (Простое прошедшее)',
                                    reply_markup=markup)

    await past_simple_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'yesterday (вчера)\n'
            'the day before yesterday (позавчера)\n'
            'that day (в тот день)\n'
            'last week (на прошлой неделе)\n'
            'last month (в прошлом месяце)\n'
            'last year (в прошлом году).\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Past Simple')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I / He / She / It / You / We / They + V2\n'
            '\n'
            'I saw the movie last week - Я видел фильм на прошлой неделе\n'
            'We asked a teacher - Мы спросили учителя\n'
            'He helped his father - Он помог отцу\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I / He / She / It / You / We / They + did + not + V1\n'
            '\n'
            'Students (they) did not listen to the lecture. — Студенты не слушали лекцию.\n'
            'The dog (it) didn not jump. — Собака не прыгала.\n'
            'Mary (she) didn not play football. — Мэри не играла в футбол.\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Did + I / He / She / It / You / We / They + V1?\n'
            '\n'
            'Did Bob study medicine? — Боб изучал медицину?\n'
            'Did the dog eat? — Собака ела?\n'
            'Did students like the film? — Студентам понравился фильм?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def past_continuous(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Past Continuous (Прошедшее продолженное время)',
                                    reply_markup=markup)

    await past_continuous_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'At 7 a.m. (в 7 утра), вместо 7 a.m. можно подставить любое другое время\n'
            'All day/night (весь день/всю ночь).\n'
            'All the time (все время).\n'
            'At that moment (в тот момент).\n'
            'While (в то время как).\n'
            'When (когда).\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Past Continuous')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I/He/She/It/You/We/They + was/were + Ving\n'
            '\n'
            'I was reading a book at 9 pm last night. - Я читал книгу вчера в 9 вечера.\n'
            'He was singing when I entered the room. - Он пел, когда я зашел в комнату.\n'
            'They were having dinner when the phone rang. - Они ужинали, когда зазвонил телефон.\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I/He/She/It/You/We/They + was/were not + Ving\n'
            '\n'
            'I wasn’t doing anything at 8 pm yesterday. - Я ничего не делал вчера в 8 вечера.\n'
            'He wasn’t listening to my story. - Он не слушал мой рассказ.\n'
            'They weren’t looking at the clock during the test. - Они не смотрели на часы во время теста.\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Was/Were + I/He/She/It/You/We/They + Ving?\n'
            '\n'
            'Were you cooking breakfast when you heard the noise? - Ты готовил завтрак, когда услышал шум?\n'
            'Was she wearing a hat at the party? - Она носила шляпу на вечеринке?\n'
            'Were they doing sport at 6 am yesterday? - Они занимались спортом в 6 утра вчера?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def past_perfect(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Past Perfect (Прошедшее совершенное время)',
                                    reply_markup=markup)

    await past_perfect_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'if (если)\n'
            'by (к)\n'
            'hardly… when / no sooner… than (как только, едва, не успел я)\n'
            'after (после)\n'
            'earlier (ранее), before (до)\n'
            'first (сперва)\n'
            'when (когда)\n'
            'just (только что)\n'
            'already (уже)\n'
            'yet (уже, еще не).\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Past Perfect')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I/You/He/She/It/We/They + had + V3\n'
            '\n'
            'I had lost my old phone. — Я потеряла свой старый телефон.\n'
            'We had talked it over before. — Мы это обсуждали раньше.\n'
            'He had called his mom. — Он позвонил маме.\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I/You/He/She/It/We/They + had not + V3\n'
            '\n'
            'They had not talked much. — Они не говорили много.\n'
            'I hadn’t finished my make-up by that time. — Я еще не закончила краситься к тому времени.\n'
            'The script had not been written by 2005. - Сценарий не был написан к 2005 году.\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Had + I/You/He/She/It/We/They + V3?\n'
            '\n'
            'Had you washed your hands? — Ты вымыл руки?\n'
            'Had she come home? — Она пришла домой?\n'
            'How many times had she been to Finland by that time? - Сколько раз она была в Финляндии к тому времени?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def past_perfect_continuous(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Past Perfect Continuous (Прошедшее совершенное продолженное)',
                                    reply_markup=markup)

    await past_perfect_continuous_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'For (на протяжении, в течение (за ним следует количество времени, например, all morning, five years)).\n'
            'Before (прежде чем).\n'
            'Since (с тех пор, как)\n'
            'How long (как долго)\n'
            'Until/till (пока, до тех пор как).\n'
            'All morning, all day, all night long (всё утро, весь день, всю ночь).\n'
            'By (к определённому моменту (в прошлом)).\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Past Perfect Continuous')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I/You/He/She/It/We/They + had been + Ving\n'
            '\n'
            'I had been learning English for 2 years before I came to USA. - Я изучал английский 2 года до '
            'приезда в США.\n'
            'He had been working on the project for two years when I joined his team. - Он работал над '
            'проектом два года, когда я присоединился к его команде.\n'
            'Peter arrived yesterday. He had been driving all day long. - Питер приехал вчера. Он ехал весь день.\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I/You/He/She/It/We/They + had not been + Ving\n'
            '\n'
            'They had not talked much. — Они не говорили много.\n'
            'I hadn’t finished my make-up by that time. — Я еще не закончила краситься к тому времени.\n'
            'The script had not been written by 2005. - Сценарий не был написан к 2005 году.\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Had + I/You/He/She/It/We/They + been Ving?\n'
            '\n'
            'Had you been doing homework for two hours when mum came home? - Ты уже два часа делал '
            'домашнее задание, когда мама вернулась домой?\n'
            'He looked exhausted when I met him in September. Had he been building a country house all summer? - '
            'Он выглядел изможденным, когда я встретила его в сентябре. Он все лето строил загородный дом?\n'
            'Had they been building the bridge when you moved there? - Они строили мост, когда вы туда переехали?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def future_simple(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Future Simple (Будущее простое)',
                                    reply_markup=markup)

    await future_simple_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            'tomorrow (завтра).\n'
            'the day after tomorrow (послезавтра)\n'
            'someday (однажды, когда-нибудь)\n'
            'next week (на следующей неделе)\n'
            'next month (в следующем месяце)\n'
            'next year (в следующем году)\n'
            'later (потом, позже)\n'
            'in the future (в будущем)\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Future Simple')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I / She / He / It / We / You / They + will (shall) + V\n'
            '\n'
            'I will play football next week - Я буду играть в футбол на следующей неделе\n'
            'She will go to Boston - Она отправится в Бостон\n'
            'They will write to her in the hospital - Они напишут ей в больнице\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I / She / He / It / We / You / They + will not (shall not) + V\n'
            '\n'
            'Don’t drink coffee before you go to bed. You will not sleep. — Не пей кофе на ночь. Ты не уснешь.\n'
            'I’m leaving tonight, so I will not be at home tomorrow. — Я уезжаю сегодня, так что '
            'завтра меня не будет дома.\n'
            'I’m sorry I was late this morning. It will not happen again. — Извините, я сегодня утром опоздал. '
            'Это больше не повторится.\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Will (Shall) + I / She / He / It / We / You / They + V\n'
            '\n'
            'Have a good trip! Will you send me a postcard? — Хорошего путешествия! Пришлешь мне открытку?\n'
            'Will you show me how to use this camera? — Покажешь мне, как пользоваться этим фотоаппаратом?\n'
            'Will you call Jenny tomorrow evening? — Позвонишь Дженни завтра вечером?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def future_continuous(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Future Continuous (Будущее продолженное время)',
                                    reply_markup=markup)

    await future_continuous_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            "at 5 o'clock (в пять часов)\n"
            'at that moment (в этот момент);\n'
            'in an hour (через час)\n'
            'this time tomorrow (в это же время завтра)\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Future Continuous')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I / He / She / It / You / We / They + will + be Ving\n'
            '\n'
            'I will be dancing — Я буду танцевать\n'
            'She will be writing — Она будет писать\n'
            'You will be thinking — Ты будешь думать\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I / He / She / It / You / We / They + will not + be Ving\n'
            '\n'
            'I will not be swimming — Я не буду плавать\n'
            'He will not be dancing — Он не будет танцевать\n'
            'You will not be coming — Ты не придешь\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            '\n'
            'Will + I / He / She / It / You / We / They + be Ving\n'
            'Will I be driving all night long? — Я буду вести машину всю ночь?\n'
            'Will she be drawing? — Она будет рисовать?\n'
            'Will we be walking? — Мы будем гулять?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def future_perfect(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Future Perfect (Будущее совершенное время)',
                                    reply_markup=markup)

    await future_perfect_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            "before (до; перед тем, как)\n"
            'till / until (до)\n'
            'by the time (к тому времени; когда)\n'
            'be then (к тому времени)\n'
            'by tomorrow (до завтра)\n'
            'by next week (к следующей неделе)\n'
            'by next month (к следующему месяцу)\n'
            'by next year (к следующему году)\n'
            'by 7 pm (к 7 вечера)\n'
            'by 9 o’clock (к девяти часам)\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Future Perfect')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'She/He/It/You/They/I/We + will (shall) + have V3\n'
            '\n'
            'She will have arrived at the station by midnight — Она прибудет на станцию к полуночи\n'
            'Kids will have finished their homework by dinner — Дети закончат со своей домашней работой к ужину\n'
            'Tom will have repaired the car by the end of next week — Том закончит ремонтировать машину до конца '
            'следующей недели\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'She/He/It/You/They/I/We + will not + have V3\n'
            '\n'
            'I will not have received my order by Friday — Я не получу свой заказ к пятнице\n'
            'John will not have finished the presentation by 6 o’clock — Джон не закончит презентацию до шести часов\n'
            'She will not have written the book by the end of the year — Она не напишет книгу к концу года\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Will + She/He/It/You/They/I/We have V3\n'
            '\n'
            'Will they have made a decision by noon? — Они примут решение к полудню?\n'
            'Will he have done his design project by Friday? — Он закончит свой дизайн-проект к пятнице?\n'
            'Will you have cooked dinner when I come home? — Ты приготовишь ужин к моменту моего возвращения домой?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def future_perfect_continuous(update, context):
    markup = ReplyKeyboardMarkup(reply_keyboard_selection)
    await update.message.reply_text('Future Perfect Continuous (Будущее совершенное продолженное)',
                                    reply_markup=markup)

    await future_perfect_continuous_photo(update)

    await update.message.reply_text(
            'Слова маркеры:\n'
            '\n'
            "for 3 hours (в течение 3 часов)\n"
            'for 5 days (в течение 5 дней)\n'
            'by the end of the year (к концу года)\n'
            'by next week (к следующей неделе)\n'
            'when (когда)\n'
            'и др.\n'
            '\n'
            'Если что то из этого стоит в предложении, то это Future Perfect Continuous')

    await update.message.reply_text(
            '1)Примеры утвердительных предложений:\n'
            'I/He/She/It/We/You/They + will have been + V-ing\n'
            '\n'
            'I will have been eating — Я буду есть\n'
            'She will have been reading — Она будет читать\n'
            'We will have been playing — Они будут играть'
            'следующей недели\n'
            '\n'
            '2)Примеры отрицательных предложений:\n'
            'I/He/She/It/We/You/They + will not have been + V-ing\n'
            '\n'
            'I will not have been eating — Я не буду есть\n'
            'She will not have been reading — Она не будет читать\n'
            'We will not have been playing — Мы не будем играть\n'
            '\n'
            '3)Примеры вопросительных предложений:\n'
            'Will + I/He/She/It/We/You/They + have been + V-ing\n'
            '\n'
            'Will I have been eating? — Я буду есть?\n'
            'Will she have been reading? — Она будет читать?\n'
            'Will we have been playing? — Мы будем играть?\n')

    await update.message.reply_text(
            'Чтобы выйти, нажмите - /start')


async def help_command(update, context):
    await update.message.reply_text('По всем вопросам: @alex11qqq')


async def result(update, context):
    if update.message.text == 'Present Simple':
        await present_simple(update, context)

    if update.message.text == 'Present Continuous':
        await present_continuous(update, context)

    if update.message.text == 'Present Perfect':
        await present_perfect(update, context)

    if update.message.text == 'Present Perfect Continuous':
        await present_perfect_continuous(update, context)

    if update.message.text == 'Past Simple':
        await past_simple(update, context)

    if update.message.text == 'Past Continuous':
        await past_continuous(update, context)

    if update.message.text == 'Past Perfect':
        await past_perfect(update, context)

    if update.message.text == 'Past Perfect Continuous':
        await past_perfect_continuous(update, context)

    if update.message.text == 'Future Simple':
        await future_simple(update, context)

    if update.message.text == 'Future Continuous':
        await future_continuous(update, context)

    if update.message.text == 'Future Perfect':
        await future_perfect(update, context)

    if update.message.text == 'Future Perfect Continuous':
        await future_perfect_continuous(update, context)


async def check_message(update, context):
    if update.message.text == "правильно":
        await update.message.reply_text("Правильно")
    else:
        await update.message.reply_text("Неправильно")


async def words(update, context):
    words1 = session.query(Word).all()
    for word in words1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=word.word)

# Блок с временами закончен


def main():
    # Создаём обработчик сообщений типа filters.TEXT
    # из описанной выше асинхронной функции echo()
    # После регистрации обработчика в приложении
    # эта асинхронная функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help_command)
    application.add_handler(help_handler)

    application.add_handler(CommandHandler("check", check_message))

    time_handler_1 = MessageHandler(filters.Regex('^(Времена)$'), time1)
    application.add_handler(time_handler_1)

    time_handler = MessageHandler(filters.Regex('^(Слова)$'), words)
    application.add_handler(time_handler)

    result_time = MessageHandler(filters.TEXT, result)
    application.add_handler(result_time)

    application.add_handler(CommandHandler("start", start))

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
