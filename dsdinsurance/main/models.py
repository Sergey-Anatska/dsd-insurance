from django.db import models


class Customers(models.Model):
    login = models.CharField("Логин", max_length=50)
    password = models.CharField("Пароль", max_length=50)
    about_customer = models.TextField("О клиенте")

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'