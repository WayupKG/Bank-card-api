from django.contrib import admin

from .models import Card
from .services import generateCardNumber


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'series', 'release_date', 'end_date', 'money', 'status')
    list_filter = ('series', 'status')
    search_fields = ['number', 'series', 'status']
    fieldsets = (
        (None, {
            'fields': (('series', 'number', 'money'),),
            'description': "При создании карты, номер будет сгенерирован автоматически."
        }),
        ('Необходимые данные:', {
            'fields': (('use_date', 'end_date'),)
        }),
        ('Статус:', {
            'fields': ('status',)
        })
    )
    readonly_fields = ('number',)

    def save_model(self, request, obj, form, change):
        if not obj.number:
            obj.number = generateCardNumber(form.data['series'])
        super().save_model(request, obj, form, change)