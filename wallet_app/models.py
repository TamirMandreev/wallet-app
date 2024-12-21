from django.db import models

# Create your models here.

# Создать модель для кошелька
class Wallet(models.Model):
    # uuid - универсально уникальный идентификатор
    uuid = models.UUIDField(primary_key=True)
    # Баланс
    balance = models.DecimalField(max_digit=20, decimal_places=2, default=0)
