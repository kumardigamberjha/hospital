from email.policy import default
from django.db import models

# Create your models here.
class User_Data(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    phn = models.IntegerField()
    disease = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Check_In_Model(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User_Data, on_delete=models.CASCADE)
    chkin = models.BooleanField()
    chkin_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name

class Check_Out_Model(models.Model):
    chkins = models.OneToOneField(Check_In_Model, on_delete=models.CASCADE)
    chkout = models.BooleanField()
    chkout_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.user.name