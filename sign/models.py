from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfoForm(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional
    portpolio_site = models.URLField(blank=True)
    profile_img = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username