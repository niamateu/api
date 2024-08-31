from django.db import models


class Food(models.Model):
    name = models.CharField('品物', max_length=50)
    date = models.DateField('消費期限')
    number = models.PositiveIntegerField('数量', blank=True, default=0)

    def __str__(self):
        return self.name