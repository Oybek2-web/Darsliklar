from django.db import models
from django.contrib.auth.models import User

class Fanlar(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fanlar'

class SotibOlinganFan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sotib_olgan_fanlar')
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE, related_name='sotib_olganlar')
    sotib_olingan_sana = models.DateTimeField(auto_now_add=True)
    tolov_holati = models.BooleanField(default=True)

    class Meta:
        db_table = 'sotib_olingan_fanlar'
        unique_together = ('user', 'fan')