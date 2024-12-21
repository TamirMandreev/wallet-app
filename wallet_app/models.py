from django.db import models

# Create your models here.

# Создать модель для кошелька
class Wallet(models.Model):
    # uuid - универсально уникальный идентификатор
    uuid = models.UUIDField(primary_key=True)
    # Баланс
    balance = models.DecimalField(max_digit=20, decimal_places=2, default=0)

    # Переопределить метод __str__, чтобы он возвращал удобочитаемую информацию
    # об объекте класса
    def __str__(self):
        return f'Кошелек {self.uuid}: Баланс {self.balance}'