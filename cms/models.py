from django.db import models
from django.contrib.auth.models import User
# pillow not working in django 3.9 use other version
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField()
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.title

from django.db import models

class Docter(models.Model):
    user = models.OneToOneField(User, null=True ,related_name="docteruser", on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False, blank=False)
    position = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(null=True, blank=False)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # docter = models.ForeignKey(User, on_delete=models.CASCADE)
    docters = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Dignocis(models.Model):
    name = models.CharField(max_length=20, null=False)
    symptoms = models.TextField(null=True)
    medcines = models.TextField(null=True)
    docter = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,null=False, on_delete=models.CASCADE)
    # patient = models.CharField(max_length=20, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


