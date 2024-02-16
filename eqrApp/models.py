from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import qrcode
from PIL import Image


class Member(models.Model):
    employee_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50, choices=(("Male", "Male"), ("Female", "Female")), default="Male")
    profession = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_joining_splm = models.DateField()
    date_of_issue = models.DateField()
    expiry_date = models.DateField()
    avatar = models.ImageField(upload_to="employee-avatars/", null=True, blank=True)
    county = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    payam = models.CharField(max_length=255)
    boma = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.employee_code} - {self.name}"

    def full_name(self):
        return self.name


    def save(self, *args, **kwargs):
        super(Member, self).save(*args, **kwargs)
        print(self.avatar)
        imag = Image.open(self.avatar.path)
        if imag.width > 200 or imag.height> 200:
            output_size = (200, 200)
            imag.thumbnail(output_size)
            imag.save(self.avatar.path)
        
# @receiver(post_save, sender=Employee)
# def create_qr(sender, instance, **kwargs):
#     code = instance.employee_code
#     img = qrcode.make(code)
#     instance.qr_path = img
#     print(img)
#     # instance.save()

