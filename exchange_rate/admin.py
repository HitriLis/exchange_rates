from django.contrib import admin
from .models import *


class ExchangeRatesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExchangeRates._meta.get_fields() if
                    not isinstance(field, (models.ForeignKey, models.ManyToOneRel, models.ManyToManyField))
                    ]


admin.site.register(ExchangeRates, ExchangeRatesAdmin)
