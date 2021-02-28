from django.db import models


class Crudex(models.Model):
    username = models.CharField(verbose_name='Username', max_length=150, unique=True,)
    first_name = models.CharField(verbose_name='First name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Last name', max_length=150, blank=True)
    password = models.CharField(verbose_name='Password', max_length=128)
    is_active = models.BooleanField(verbose_name='Active', default=True)

    def __str__(self):
        return self.username
