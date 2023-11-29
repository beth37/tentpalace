import os.path
import uuid

from django.db import models

# Create your models here.

def generate_unique_name(instance, filename):
    name = uuid.uuid4()
    ext = filename.split(".")[-1]
    full_filename = f"{name}.{ext}"
    # full_filename = "%s.%s" % (name, ext)  gives same result as line 11
    return os.path.join("customers", full_filename)


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    profile_pic = models.ImageField(upload_to=generate_unique_name, null=True, default="students/default.png")
    created_at = models.DateTimeField(auto_now_add=True)  # updates time automatically
    updated_at = models.DateTimeField(auto_now=True)  # hapa inaonyesha last time it was updated on the database


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


