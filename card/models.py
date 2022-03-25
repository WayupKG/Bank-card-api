from django.db import models

from .managers import ActiveManager, NotActiveManager, OverdueManager


class Card(models.Model):
    """Карты"""
    class Meta:
        ordering = ('-release_date',)
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    SERIES = (
        ('ELCARD', 'ЭЛКАРТ'),
        ('VISA', 'VISA'),
        ('MASTERCARD', 'MASTERCARD'),
    )
    STATUS = (
        ('activated', 'Активирована'),
        ('not_activated', 'Не активирована'),
        ('overdue', 'Просрочена'),
    )
    series = models.CharField('Серия карты', max_length=20, choices=SERIES)
    number = models.PositiveBigIntegerField('Номер карты', unique=True, blank=True)
    release_date = models.DateTimeField('Дата выпуска', auto_now=True)
    end_date = models.DateTimeField('Дата окончания активности')
    use_date = models.DateTimeField('Дата использования')
    money = models.DecimalField('Деньги', max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField('Статус', max_length=15, choices=STATUS, default='activated')

    objects = models.Manager()
    active = ActiveManager()
    not_active = NotActiveManager()
    overdue = OverdueManager()

    def __str__(self) -> str:
        return f"{self.series}-{self.number}"