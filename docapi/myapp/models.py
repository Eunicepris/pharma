from django.db import models
from tinymce import HTMLField

# Create your models here.

class Medoc(models.Model):
    product_name = models.CharField(max_length=250)
    manufacturing_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    tracking_code = models.CharField(max_length=250)
    producer = models.CharField(max_length=250)
    notice = HTMLField()
            
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name