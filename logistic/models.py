from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    tg_username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    order_context = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.user, self.order_context)


class OrdersConfig(models.Model):
    title = models.CharField(max_length=255)
    logistic_days = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    max_weight = models.CharField(max_length=255)
    volume_weight = models.CharField(max_length=255)
    max_size = models.CharField(max_length=255)
    traking_link = models.CharField(max_length=255)
    departure_frequency = models.CharField(max_length=255)
    exception = models.TextField()

    def __str__(self):
        return '{}'.format(self.title)


class SocialLinks(models.Model):
    tg_link = models.CharField(max_length=100, null=True, blank=True)
    vk_link = models.CharField(max_length=100, null=True, blank=True)
    inst_link = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)


class OrderStatistics(models.Model):
    sended = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)
    on_market = models.IntegerField(default=1)


class Reviews(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    starts = models.IntegerField(default=3)
    date = models.DateTimeField()

    def __str__(self):
        return '{} - {}'.format(self.name, self.starts)