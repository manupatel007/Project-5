from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Year(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    year = models.IntegerField()

class Subjects(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    description = models.TextField()

class RtuPapers(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150, null=True, blank=True)

class Sub_Notes(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150, null=True, blank=True)