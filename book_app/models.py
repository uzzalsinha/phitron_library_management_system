from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=80)

    def __str__(self):
        return str(self.name)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=12)
    branch = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=5, blank=True)
    phone = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return str(self.user)


def expiry():
    return datetime.today() + timedelta(days=14)
class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)