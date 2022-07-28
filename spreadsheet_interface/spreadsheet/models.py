from django.db import models

class Orders(models.Model):
    number = models.IntegerField(unique=True)
    order_number = models.IntegerField(unique=True)
    cost_usd = models.FloatField()
    cost_rub = models.FloatField()
    delivery_date = models.DateTimeField()

