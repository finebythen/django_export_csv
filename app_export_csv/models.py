from django.db import models


list_a = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Forms_Example(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField(blank=True)
    age = models.IntegerField(default=0)
    birth_date = models.DateField()
    list_one = models.CharField(max_length=50, choices=list_a, blank=True, null=True)
    list_two = models.CharField(max_length=50, choices=list_a, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
