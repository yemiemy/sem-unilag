from django.db import models
from phone_field import PhoneField
# Create your models here.
class TeamMemberInfo(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    image = models.ImageField(upload_to='member_img/%Y/%m/%d/', max_length=255, null=True, blank=True)
    phone = PhoneField(help_text='Contact phone number')
    email = models.EmailField(max_length=254)
    sub_team = models.CharField(max_length=120)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    linkedIn = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()


class Contact(models.Model):
    fname = models.CharField(max_length=120)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname