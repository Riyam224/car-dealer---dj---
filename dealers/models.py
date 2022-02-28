from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Dealer(models.Model):
    name = models.CharField( max_length=50)
    picture = models.ImageField(upload_to="images")
    description = models.TextField()
    email = models.CharField(max_length=50)

    

    class Meta:
        verbose_name = _("Dealer")
        verbose_name_plural = _("Dealers")

    def __str__(self):
        return self.name

  