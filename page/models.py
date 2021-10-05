from django.db import models

# Create your models here.

class TblPosts(models.Model):
    last_time = models.IntegerField()
    tag = models.BinaryField()
    content = models.BinaryField()
    comment = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'tbl_posts'