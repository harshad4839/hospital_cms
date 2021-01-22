from django.db import models

class Docter1(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    position = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

class Patient2(models.Model):
    name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Dignosis(models.Model):
    name = models.CharField(max_length=20, null=False)
    symptoms = models.TextField(null=True)
    medcines = models.TextField(null=True)
    docter = models.ForeignKey(Docter1, null=False, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient2,null=False, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


