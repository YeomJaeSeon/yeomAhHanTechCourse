from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)

    class Meta:
        db_table = 'board'

    def __str__(self):
        return self.title
