from django.db import models

# Create your models here.
from django.db import models

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    next_of_kin = models.CharField(max_length=100)
    NIN = models.CharField(max_length=20)
    recommender_name = models.CharField(max_length=100)
    religion = models.CharField(max_length=50, blank=True, null=True)
    education_level = models.CharField(max_length=100)
    sitter_number = models.CharField(max_length=20)
    contacts = models.CharField(max_length=100)
    active = models.BooleanField(default=True)  # Indicates if the sitter is on duty

    def __str__(self):
        return self.name

class Baby(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    brought_by = models.CharField(max_length=100)
    time_of_arrival = models.DateTimeField(auto_now_add=True)
    parent_names = models.CharField(max_length=200)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    period_of_stay = models.CharField(max_length=100)
    baby_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class BabyDeparture(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    departed_by = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

class Payment(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class ProcuredItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ResoldDoll(models.Model):
    doll = models.ForeignKey(ProcuredItem, on_delete=models.CASCADE, related_name='resold_dolls')
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doll.name} for {self.baby.name}"
