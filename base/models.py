from django.db import models
from django.contrib.auth.models import User



class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    imageReason = models.ImageField(default="", null=True, blank=True)
    documentReason = models.FileField(default="",null=True,blank=True)
    is_Approved = models.BooleanField(default=False)
    created_At = models.DateField(auto_now=True)
    def __str__(self):
        return self.reason