from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField()
    # if i wanna add a new field and
    #featured = models.BooleanField(null=True)  #set to null the old observations or default=False

    featured = models.BooleanField()


    #changes?
