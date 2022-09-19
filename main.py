from aiogram import types, Dispatcher, Bot, executor
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

BOT_TOKEN = '5462862139:AAE2pL2t6wCfW74IhdP5FzDud4ZWLAciQZE'

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode = 'HTML')
dp = Dispatcher(bot, loop=loop)

button1 = KeyboardButton('Обо мне 💁🏻‍♂')
button2 = KeyboardButton('Консультации 💻')
button7 = KeyboardButton('Наставничество 💡')
button8 = KeyboardButton('Отзывы 💬')
button9 = KeyboardButton('Мои соцсети | Запись на консультацию 📱')

reply_keyboard = [['Обо мне 💁🏻‍♂', 'Отзывы 💬'],
                  ['Консультации 💻', 'Наставничество 💡'],
                   ['Мои соцсети | Запись на консультацию 📱']]

@dp.message_handler(Command('start'))
async def startjoin(message: types.Message):
    buttonfile = open('button.jpg', 'rb')
    await bot.send_message(message.chat.id, '👋🏻 Здравствуйте! Вы попали в официальный чат-бот психолога Павла Макарова. Здесь вы найдёте всю информацию о консультациях. \nСвязь со мной (запись на консультацию) - @makpsy.\n\nМеню с информацией представлено ниже👇🏻')
    await bot.send_photo(message.chat.id, buttonfile, reply_markup=markup4) 
    
inline_btn_1 = InlineKeyboardButton('Отзывы', url='https://t.me/otzivy_klietov')
inline_btn_2 = InlineKeyboardButton('Базовая',  callback_data='button2')
inline_btn_3 = InlineKeyboardButton('Поддерживающая',  callback_data='button3')
inline_btn_5 = InlineKeyboardButton('Запись на консультацию', url='https://t.me/makpsy')
inline_btn_6 = InlineKeyboardButton('Мои компетенции',  callback_data='button6')
inline_btn_7 = InlineKeyboardButton('Личный кейс',  callback_data='button7')
inline_btn_8 = InlineKeyboardButton('Назад',  callback_data='button8')
inline_btn_9 = InlineKeyboardButton('Назад',  callback_data='button9')
inline_kb_full = InlineKeyboardButton('',  callback_data='button4')
inline_kb_full1 = InlineKeyboardButton('',  callback_data='button6')
inline_kb_full2 = InlineKeyboardButton('',  callback_data='button8')
inline_kb_full3 = InlineKeyboardButton('',  callback_data='button9')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)
inline_kb3 = InlineKeyboardMarkup().add(inline_btn_3)
inline_kb5 = InlineKeyboardMarkup().add(inline_btn_5)
inline_kb6 = InlineKeyboardMarkup().add(inline_btn_6)
inline_kb7 = InlineKeyboardMarkup().add(inline_btn_7)
inline_kb8 = InlineKeyboardMarkup().add(inline_btn_8)
inline_kb9 = InlineKeyboardMarkup().add(inline_btn_9)
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_kb_full)
inline_kb_full.add(inline_btn_2, inline_btn_3)
inline_kb_full1 = InlineKeyboardMarkup(row_width=2).add(inline_kb_full1)
inline_kb_full1.add(inline_btn_6, inline_btn_7)
inline_kb_full2 = InlineKeyboardMarkup(row_width=2).add(inline_kb_full2)
inline_kb_full2.add(inline_btn_2, inline_btn_3, inline_btn_8)
inline_kb_full3 = InlineKeyboardMarkup(row_width=2).add(inline_kb_full3)
inline_kb_full3.add(inline_btn_6, inline_btn_7, inline_btn_9)
markup4 = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(text='<b>Базовая:</b>\n\nДлительность: 1 час 30 минут \n\nЗнакомство, разбор причины, проработка, плавный выход + получение клиентом инструментов, как ему работать с проблемой самостоятельно \n\n<b>Стоимость - 5000р</b>', reply_markup=inline_kb_full2)
    
@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button1(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(text='<b>Поддерживающая:</b>\n\nДлительность: 1 час\n\nПодходит тем, кто уже был на базовой консультации и хорошо знает свои особенности, поэтому одного часа хватит для качественной работы с проблемой. \n\nТакже в этом формате может состояться коуч-сессия (работа с состоянием здесь и сейчас). \n\n<b>Стоимость - 3500р</b>', reply_markup=inline_kb_full2)
    
@dp.callback_query_handler(lambda c: c.data == 'button6')
async def process_callback_button1(call: types.CallbackQuery):
    workfile = open('work.jpg', 'rb')
    await call.answer()
    await call.message.delete()
    await call.bot.send_photo(call.from_user.id, workfile, 'За 8 лет изучения психологии и практики я приобрел большое количество знаний. Выше представлены темы запросов, с которыми я смогу вам помочь.\n\n*Это примерный список компетенций. О своем запросе можно уточнить в личных сообщениях @makpsy', reply_markup=inline_kb_full3)

@dp.callback_query_handler(text='button7')
async def process_callback_button1(call: types.CallbackQuery):
    await call.answer()
    await call.message.delete()
    await call.bot.send_message(call.from_user.id, text='Знакомство с психологией у меня началось в период моего пребывания в депрессии (об этом я узнал уже позже). Жизнь казалась адом, негативные мысли переполняли мою голову, начались панические атаки и сильное бессилие. О причинах я уже писал посты в канале. Я ненавидел и не любил себя за все мои травмы и комплексы, потому что они очень мешали жить. В какой-то момент я начал искать ответ на вопрос: «А что со мной не так?» и «Какого черта я вообще такой ущербный?» Так и начался мой путь к самопознанию и осознанности. Я увлекся психологией, даже понял, что я нормальный (просто есть пара особенностей и нужно их учитывать). Потом поступил на психолога и начал путь по проработке травм, постановке личностных границ, развитию внутреннего стержня.  \n\n<b>Точка «А»</b> - застенчивый (стыдливый, трусливый, неуверенный) человек в депрессии, который боится позвонить по телефону родственнику, потому что считает себя недостойным этого диалога. Что было в отношениях с незнакомцами даже не буду говорить. Мечтаю о зарплате 30 тыс. в месяц, съемной однушке и компьютере, чтобы проваливаться в онлайн-игры из этого ужасного мира. \n*выход из депрессии длился год, с постоянными откатами обратно. \n\nПрошло 3 года. Я проработал десятки проблем, перепробовал себя в разных сферах деятельности. Кто меня видел давно, говорили, что я стал другим человеком. \n\nРаботаю на хорошей должности, меня устраивает все, но случается, что меня несправедливо понижают с администратора до официанта. Причем зарплату даже немного повысили, но это не спасло мою психику. Я не смирился и начал думать, куда мне уйти, тк уже отвергал профессию официанта из-за понижения (даже имя на бейдже писал другое). \n\nНа ум пришла профессия ведущего мероприятий. На ведущих в банкетном зале молились. Они много зарабатывали и вообще выглядели круто. <b>Но была проблема:</b> какой из меня ведущий, если я даже доклад на паре без дрожания голоса не могу прочитать при одногруппниках?  Начался анализ и наблюдение за ведущими. В какой-то момент я понял, что я от них отличаюсь <b>психологическим развитием.</b> И я решаю сам себе заложить то, что нужно для профессии ведущего. Мне стало интересно, чего я смогу достичь. Началась ярая психологическая работа над собой. \n\nЧерез полгода я заработал свои первые 150 тыс. за месяц и понял, что реальность поменялась. В провинциальном городе в 21 год такие деньги благодаря смене мышления и психотерапии. А еще я из бедной семьи, в которой мама тянула все на себе адским трудом, поэтому упал в чувство стыда за то, что смог заработать такие большие деньги. Вот так бывает)\nЧерез год мне снова сказали, что я другой человек. Только теперь это было еще и с восхищением.  <b>Благодаря психологии я смог улучшить уровень своей жизни и стать намного счастливее. Если вы тоже стремитесь к этому, то я с удовольствием поделюсь с вами своим опытом и знаниями.</b>  \n\n*Это <b>очень краткая</b> история, не отражающая очень многие моменты моей жизни. Но я уверен, что смог вам показать, как психология способна менять жизнь человека. Даже прослезился, пока писал.', reply_markup=inline_kb_full3)

@dp.callback_query_handler(lambda c: c.data == 'button8')
async def process_callback_button1(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(text='Краткая информация о консультациях со мной👇 \n\nhttps://youtu.be/IAyok3yZDKE', reply_markup=inline_kb_full)
    
@dp.callback_query_handler(lambda c: c.data == 'button9')
async def process_callback_button1(call: types.CallbackQuery):
    await call.answer()
    await call.message.delete()
    await call.bot.send_message(call.from_user.id, text='В этом видео кратко рассказываю о себе и о принципах моей работы. Также обратите внимание на кнопки, по которым можно увидеть дополнительную информацию.\n\nhttps://youtu.be/PgQ4ZSg_Nw0', reply_markup=inline_kb_full1)

@dp.message_handler()
async def all_msg_handler(message: types.Message):
    
    button_text = message.text 

    if button_text == 'Обо мне 💁🏻‍♂':
        await bot.send_message(message.chat.id, "В этом видео кратко рассказываю о себе и о принципах моей работы. Также обратите внимание на кнопки, по которым можно увидеть дополнительную информацию.\n\nhttps://youtu.be/PgQ4ZSg_Nw0", reply_markup=inline_kb_full1)
    if button_text == 'Консультации 💻':
        await bot.send_message(message.chat.id, "Краткая информация о консультациях со мной👇 \n\nhttps://youtu.be/IAyok3yZDKE", reply_markup=inline_kb_full)
    if button_text == 'Наставничество 💡':
        await bot.send_message(message.chat.id, "<b>Наставничество:</b>\n\nБудет интересно вам, если вы хотите получить:\n\n1. Серьезную и длительную работу с психологом (которая включает ежедневную поддержку) для достижения определенных целей.\n2. Психотерапию по вашей проблеме или ситуации с ежедневной поддержкой психолога. \n\nВключает 4 базовые консультации 1 раз в неделю.\n\n<b>Длительность - 4 недели</b>\n<b>Стоимость - 30 000р</b>\n\nВопросы, по которым ко мне приходят в наставничество:\n- принятие себя (в т.ч. выход в сторис)\n- выход из зависимых / абьюзивных отношений\n- поиск себя\n- проработка травм, критично мешающих качеству жизни\n- ведение мероприятий и развитие харизмы\nи др. \nЕсли вы подписаны и следите за мной, то уже знаете, сколько ценной информации и навыков я могу передать. ")
    if button_text == 'Отзывы 💬':
        await bot.send_message(message.chat.id, "👇Отзывы находятся здесь👇\n⠀⠀https://t.me/otzivy_klietov", reply_markup=inline_kb1)
    if button_text == 'Мои соцсети | Запись на консультацию 📱':
        await bot.send_message(message.chat.id, "<a href='https://t.me/+BOR-XsozYz4wNTFi'>Основной телеграм-канал</a> \n<a href='https://t.me/+AXZLBCgGSgNiNTMy'>Лайв телеграм-канал</a> \n<a href='https://instagram.com/makarov_psy'>Inst-m (запрещена в РФ)</a> \n<a href='https://www.youtube.com/channel/UCjGqZIkig_Hz1dS8VDg-n6Q'>YouTube</a> \n<a href ='https://vk.com/pv_makarov1'>ВКонтакте</a>", disable_web_page_preview = True, reply_markup=inline_kb5)
        
executor.start_polling(dp)