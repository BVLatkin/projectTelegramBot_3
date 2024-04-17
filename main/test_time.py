from telegram import ReplyKeyboardMarkup
from reply_key import reply_keyboard_selection_test_1, reply_keyboard_selection_test_2, \
    reply_keyboard_selection_test_3, reply_keyboard_selection_test_4, reply_keyboard_selection_test_5, \
    reply_keyboard_selection_test_6, reply_keyboard_selection_test_7, reply_keyboard_selection_test_8, \
    reply_keyboard_selection_test_9, reply_keyboard_selection_test_10, reply_keyboard_selection_test_11, \
    reply_keyboard_selection_test_12


async def check_tense_1(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    await update.message.reply_text('Вам дано предложение, поймите какое это время, выберите из списка\n'
                                    'Если после нажатия кнопки ничего не выводится, то ответ не правильный. Продолжайте'
                                    ' попытки')
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_1)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='He always eats a healthy breakfast before going to work', reply_markup=markup)


async def check_tense_present_simple(update, context):
    if update.message.text == '1) Present Simple':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Он всегда завтракает здоровой пищей перед тем '
                                        'как идти на работу.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next1\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_2(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_2)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='I traveled to Europe two years ago and I fell in love with Paris.',
                                   reply_markup=markup)


async def check_tense_past_simple(update, context):
    if update.message.text == '5) Past Simple.':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Два года назад я путешествовал по Европе и влюбился в Париж.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next2\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_3(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_3)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='He had been working at the company for five years before he decided '
                                        'to quit and pursue a new career.',
                                   reply_markup=markup)


async def check_tense_past_perfect_continuous(update, context):
    if update.message.text == '8)Past Perfect Continuous':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Он проработал в компании пять лет, прежде чем решил уволиться '
                                        'и начать новую карьеру.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next3\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_4(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_4)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='She will graduate from university next year and then she plans '
                                        'to travel the world.',
                                   reply_markup=markup)


async def check_tense_future_simple(update, context):
    if update.message.text == '9)  Future Simple':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (В следующем году она закончит университет и планирует '
                                        'отправиться путешествовать по миру.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next4\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_5(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_5)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='She was studying for her final exams while her friends were '
                                        'out enjoying the summer.',
                                   reply_markup=markup)


async def check_tense_past_continuous(update, context):
    if update.message.text == '6. Past Continuous':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Она готовилась к выпускным экзаменам, '
                                        'пока ее друзья наслаждались летом.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next5\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_6(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_6)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='She had finished her work before the deadline, '
                                        'so she could relax and enjoy her weekend',
                                   reply_markup=markup)


async def check_tense_past_perfect(update, context):
    if update.message.text == '7.  Past Perfect':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Она закончила свою работу раньше установленного срока, '
                                        'так что могла расслабиться и насладиться выходными.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next6\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_7(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_7)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='They will have saved enough money to buy a house by the time they turn 30.',
                                   reply_markup=markup)


async def check_tense_future_perfect(update, context):
    if update.message.text == 'Future Perfect.':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (К тому времени, когда им исполнится 30 лет, '
                                        'они накопят достаточно денег, чтобы купить дом.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next7\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_8(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_8)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='Why will they have been waiting for the bus for so long?',
                                   reply_markup=markup)


async def check_tense_future_perfect_continuous(update, context):
    if update.message.text == 'Future Perfect Continuous ㅤ':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Почему они так долго будут ждать автобус?)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next8\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_9(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_9)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="He hasn't been working on the assignment.",
                                   reply_markup=markup)


async def check_tense_present_perfect_continuous(update, context):
    if update.message.text == '4)  Present Perfect Continuous.':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Он не работал над заданием.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next9\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_10(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_10)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="He hasn't received a promotion.",
                                   reply_markup=markup)


async def check_tense_present_perfect(update, context):
    if update.message.text == '3)ㅤPresent Perfect.':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Он не получил повышение.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next10\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_11(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_11)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="I will be studying for my exams all week, "
                                        "so I won't have time to go out with friends.",
                                   reply_markup=markup)


async def check_tense_future_continuous(update, context):
    if update.message.text == '10)ㅤFuture Continuous.ㅤ':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Я буду готовиться к экзаменам всю неделю, '
                                        'поэтому у меня не будет времени встретиться с друзьями.)\n'
                                        '\n'
                                        'Если хотите продолжить - нажмите /next11\n'
                                        'Если хотите выйти - нажмите /start')


async def check_tense_12(update, context):
    global hope_executed
    hope_executed = True
    # Получаем время, выбранное пользователем
    markup = ReplyKeyboardMarkup(reply_keyboard_selection_test_12)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Why are they running late for the meeting?",
                                   reply_markup=markup)


async def check_tense_present_continuous(update, context):
    if update.message.text == '2)Present Continuous.ㅤ':
        await update.message.reply_text('Верно!\n'
                                        'Перевод - (Почему они опаздывают на встречу?)\n'
                                        '\n'
                                        'Конец! Поздравляем!\n'
                                        'Чтобы выйти - нажмите /start')


async def test_next1(update, context):
    await update.message.reply_text('Тесты по временам\n'
                                    'Нажмите /next для продолжения')


hope_executed = False
