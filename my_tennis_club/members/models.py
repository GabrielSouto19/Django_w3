from django.db import models

#user e senha do django dmin é : user : Gabriel , senha : gabriel123
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname}  {self.lastname}"
    
