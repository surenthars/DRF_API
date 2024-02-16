from django.db import models


class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30, null=True)
    lastName = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30)
    createdDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Users"

    @property
    def username(self):
        return str(self.username)
