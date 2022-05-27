from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Posteo (models.Model):
    fechaPosteo = models.DateField()
    tituloPosteo = models.CharField(max_length=130)
    autorPosteo = models.ForeignKey(User, on_delete=models.CASCADE)
    bodyPosteo = RichTextField(blank=True, null=True)
    class Meta:
        verbose_name = "Posteo"
        verbose_name_plural = "Posteos"
    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.tituloPosteo, self.autorPosteo)

class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
    