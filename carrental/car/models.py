from django.db import models

# Create your models here.


class contactUs(models.Model):
    name =models.CharField(max_length=500)
    email = models.EmailField()
    phone =models.CharField(max_length=50)
    project=models.CharField(max_length=500)
    subject =models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
    



class Homedetails(models.Model):
    car_type =models.CharField(max_length=500)
    pick_up =models.CharField(max_length=500)
    drop_off =models.CharField(max_length=500)
    pick_up_date =models.DateTimeField(auto_now=False, auto_now_add=False)
    drop_off_date =models.DateTimeField(auto_now=False, auto_now_add=False)
 