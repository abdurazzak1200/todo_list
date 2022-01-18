from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField('Заголовок', max_length=200, null=True, blank=True)
    description = models.CharField('Описание', max_length=250, null=True, blank=True)
    complete = models.BooleanField('Сделано', default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Задачу'
        verbose_name_plural = 'Задачи'
        ordering = ['complete']