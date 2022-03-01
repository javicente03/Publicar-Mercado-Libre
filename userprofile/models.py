from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    created_at = models.DateTimeField(default="2022-02-28")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(UserProfile, self).save(*args, **kwargs)