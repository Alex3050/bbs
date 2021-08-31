from django.db import models

# Create your models here.
class TblUser(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    check_password = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'tbl_user'
