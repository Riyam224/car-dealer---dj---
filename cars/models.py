from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
# Create your models here.

from dealers.models import Dealer
from django.urls import reverse


class Car(models.Model):
    dealer = models.ForeignKey(Dealer, verbose_name=_("dealer"), on_delete=models.DO_NOTHING )

    brand = models.CharField( max_length=100)
    CATEGORY = (
        ('New' , 'New') ,
        ('Used' , 'Used')
    )
    category = models.CharField(max_length=100 , choices=CATEGORY)
    image_main = models.ImageField(upload_to="images")
    image1 = models.ImageField(upload_to="images" , blank=True, null=True)
    image2 = models.ImageField(upload_to="images" , blank=True, null=True)
    image3 = models.ImageField(upload_to="images" , blank=True, null=True)
    image4 = models.ImageField(upload_to="images" , blank=True, null=True)
    image5 = models.ImageField(upload_to="images" , blank=True, null=True)

    miles = models.IntegerField(blank=True, null=True)
    TRANSISSION = (
        ('Manual' , 'Manual'),
        ('Automatic' , 'Automatic')
    )
    transission = models.CharField(max_length=100 , choices=TRANSISSION)
    YEAR_CHOICES = [(r,r) for r in range(2010 , datetime.date.today().year+1)]
    year = models.IntegerField(('year') , choices = YEAR_CHOICES , default=datetime.datetime.now().year)
    power = models.IntegerField()
    fuel = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    date = models.DateField()



    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'car_id': self.id})

    


