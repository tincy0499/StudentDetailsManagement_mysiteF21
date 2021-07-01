from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField(default=12)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Student(User):
    LVL_CHOICES = [ ('HS', 'High School'), ('UG', 'Undergraduate'),
                    ('PG', 'Postgraduate'), ('ND', 'No Degree'), ]
    level = models.CharField(choices=LVL_CHOICES, max_length=2, default='HS')
    address = models.CharField(max_length=300, blank=True)
    province=models.CharField(max_length=2, default='ON')
    registered_courses = models.ManyToManyField(Course, blank=True)
    interested_in = models.ManyToManyField(Topic)

    def __str__(self):
        return self.first_name

class Order(models.Model):
    courses = models.ManyToManyField(Course)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ORDER_CHOICES = [(0,'Cancelled'), (1, 'Confirmed'), (2, 'On Hold')]
    order_status = models.IntegerField(choices=ORDER_CHOICES, default=1)
    order_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.student.first_name + ' ' +str(self.total_cost())

    def total_cost(self):
        total = 0
        for course in self.courses.all():
            total += course.price
        print(f'Total Cost is {total}')
        return total
