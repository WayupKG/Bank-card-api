from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='activated')


class NotActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='not_activated')


class OverdueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='overdue')