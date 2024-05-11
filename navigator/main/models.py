from django.db import models

class Routes(models.Model):
    car_number = models.CharField(max_length=255, blank=False, default="")
    start_point = models.CharField(max_length=255, blank=False, default="")
    end_point = models.CharField(max_length=255, blank=False, default="")
    start_time = models.CharField(max_length=255, blank=False, default="")
    end_time = models.CharField(max_length=255, blank=False, default="")
    reference_to_video = models.TextField(blank=False, default="")
    reference_to_geo = models.TextField(blank=False, default="")

class Book(models.Model):

    name = models.CharField(max_length=255, blank=False, default="")
    price = models.FloatField()
    available_amount = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name