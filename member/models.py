from django.db import models


class Member(models.Model):
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.email
