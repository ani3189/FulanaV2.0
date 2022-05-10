from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posteo (models.Model):
    fechaPosteo = models.DateField()
    tituloPosteo = models.CharField(max_length=130)
    autorPosteo = models.ForeignKey(User, on_delete=models.CASCADE)
    bodyPosteo = models.TextField()
    class Meta:
        verbose_name = "Posteo"
        verbose_name_plural = "Posteos"
    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.tituloPosteo, self.autorPosteo)