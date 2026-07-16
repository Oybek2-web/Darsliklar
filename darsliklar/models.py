from django.db import models
from fanlar.models import Fanlar

class Darsliklar(models.Model):
    image = models.ImageField(upload_to='image/')
    video = models.FileField(upload_to='video/', null=True, blank=True)
    pdf = models.FileField(upload_to='pdf/', null=True, blank=True)
    mavzu = models.CharField(max_length=50)
    malumotlar = models.TextField()
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE, related_name='darsliklar', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mavzu

    class Meta:
        db_table = 'darslik'

