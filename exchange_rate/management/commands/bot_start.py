from django.core.management.base import BaseCommand, CommandError
from bot.updater import start_bot


class Command(BaseCommand):
    help = 'Команда запуска бота'

    def handle(self, *args, **options):
        start_bot()
