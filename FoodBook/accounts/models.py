from django.contrib.auth.models import User
from django.db import models

def profile_path_name(instens:'Profile', filename:str) -> str:
    return "profile/profile_{pk}/avatar/{filename}".format(
        pk=instens.pk,
        filename=filename,
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    argumet_acsepted = models.BooleanField(default=False)
    avatar  = models.ImageField(null=True, blank=True, upload_to=profile_path_name)