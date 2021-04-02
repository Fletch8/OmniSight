from django.db import models
from django.urls import reverse
from datetime import date
# thank you Django for this user :-)
from django.contrib.auth.models import User

# Create your models here.
# class Cat(models.Model):
#     age = models.IntegerField()
#     breed = models.CharField(max_length=100)
#     description = models.CharField(max_length=250)
#     name = models.CharField(max_length=100)
#     # this is associated with a user
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# # garfield = Cat('Garfield', 'Tabby', 'I have never heard of Tabby', 9)
# # print(garfield)

# # tuples (value1, value2, value3) immutable pop() no changing of the values
# MEALS = (
#     ('B', 'Breakfast'),
#     ('L', 'Lunch'),
#     ('D', 'Dinner')
# )
# start = datetime.datetime.now()
# class Feeding(models.Model):
#     date = models.DateField('when are we getting fed')
#     meal = models.CharField(
#         max_length=1,
#         # possible choices are the MEALS
#         choices = MEALS,
#         default = MEALS[0][0]
#     )
#     # make association to Cat Model, when cat is deleted, delete assoc. feedings
#     cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.get_meal_display()} on {self.date}"

class Currency(models.Model):
    symbol = models.CharField(max_length=12)
    price = models.FloatField()

    def __str__(self):
        info = f"{self.symbol} : {self.price}"
        return info

class FavCurrencies(models.Model):
    symbol = models.CharField(max_length=12)
    alert_price = models.FloatField()

    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
