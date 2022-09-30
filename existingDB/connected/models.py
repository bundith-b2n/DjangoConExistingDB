from django.db import models

# Create your models here.


class Accounts(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=255)
    created_on = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'