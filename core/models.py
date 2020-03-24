from django.db import models
from django.utils import timezone

# Create your models here.

sem_choices = [
        ('First', 'I'),
        ('Second', 'II'),
        ('Third', 'III'),
        ('Fourth', 'IV'),
        ('Fifth', 'V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII')]

year_choices = [
        ('First', 'I'),
        ('Second', 'II'),
        ('Third', 'III'),
        ('Fourth', 'IV'),
        ]

level_choices = [
    ('SEE','SEE'),
    ('Plus2','Plus2'),
    ('Bachelor','Bachelor'),
    ('Master','Master'),
]
class Faculty(models.Model):
    level = models.CharField(max_length=15,choices=level_choices)
    faculty = models.CharField(max_length=30, blank=True)
    def __str__(self):
       return self.faculty
class YearOrSemester(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    year = models.CharField(max_length=15, choices=year_choices, blank=True)
    sem = models.CharField(max_length=30, choices=sem_choices, blank=True, null= True)

    def __str__(self):
        return '%s %s' % (self.year, self.sem)





class Questions(models.Model):
    questions = models.ForeignKey(YearOrSemester, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=125)
    date_posted = models.DateTimeField(default=timezone.now)
    file = models.FileField()

    def __str__(self):
        return self.sub_name