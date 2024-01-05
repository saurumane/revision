from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Userinputmodel(models.Model):
    area_type=models.CharField(max_length=100)
    availiability=models.DateField(max_length=10)
    Total_sqft=models.IntegerField()
    Bhk=models.IntegerField()
    location=models.CharField(max_length=100)
    phone_no=PhoneNumberField()

