from datetime import datetime
from django.utils.timezone import make_aware


def google_values_to_tuple(google_values: list) -> tuple:
    return tuple(tuple(i) for i in google_values)


def str_to_datetime(date_str: str = None, format_str: str = '%d.%m.%Y'):
    naive_datetime = datetime.strptime(date_str, format_str)
    return make_aware(naive_datetime)
