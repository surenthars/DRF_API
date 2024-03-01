from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Client"
