from datetime import date
from django.conf import settings
from telegram.ext import Updater, CallbackContext, MessageHandler, \
    Filters, CallbackQueryHandler, Defaults, CommandHandler
from exchange_rate.models import ExchangeRates


def start_bot():
    global updater
    updater = Updater(settings['BOT_TOKEN'], use_context=True, request_kwargs={})

    dispatcher = updater.dispatcher
    j = updater.job_queue
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    text_handler = MessageHandler(Filters.all, handle_text)
    dispatcher.add_handler(text_handler)
    start_job(bot=dispatcher.bot, j=j)

    updater.start_polling(timeout=10)
    updater.idle()


global updater


def shutdown():
    updater.stop()
    updater.is_idle = False


def handle_text(update, context):
    if update['channel_post'] is None or update['channel_post']['chat'] is None:
        return True

    channel_id = update['channel_post']['chat']['id']
    if channel_id is not None and len(update['channel_post']['new_chat_photo']) > 0:
        context.bot.delete_message(chat_id=channel_id, message_id=update['channel_post']['message_id'])


def start(*args, **kwargs):
    pass


def start_job(bot, j):
    job_minute = j.run_repeating(callback_repeating, interval=15, first=0)


def callback_repeating(context):
    data = ExchangeRates.objects.filter(delivery_time__lte=date.today())
    print(data)
    # context.bot.send_message(chat_id=settings['CHANNEL_ID'], text='Загрузка статистики...')
