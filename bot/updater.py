from django.utils import timezone
from django.conf import settings
from telegram.ext import Updater, CallbackContext, MessageHandler, \
    Filters, CallbackQueryHandler, Defaults, CommandHandler
from exchange_rate.models import ExchangeRates

import datetime
from django.conf import settings
from django.utils.timezone import make_aware


def start_bot():
    global updater
    updater = Updater(settings.BOT_TOKEN, use_context=True, request_kwargs={})

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
    naive_datetime = datetime.datetime.now()
    aware_datetime = make_aware(naive_datetime)
    data = ExchangeRates.objects.filter(is_expired=False, delivery_time__lte=aware_datetime)
    if data:
        text_message = ''
        for item in data:
            text_message += f'Зака: {item.order}\nСрок обработки заказа истёк истек {item.delivery_time.strftime("%m/%d/%y")}\n\n'
        data.update(is_expired=True)
        context.bot.send_message(chat_id=settings.CHANNEL_ID, text=text_message)
