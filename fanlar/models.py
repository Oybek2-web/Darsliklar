from django.db import models

class Fanlar(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fanlar'