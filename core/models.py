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

see_choices = [
    ('English','English'),
    ('Nepali','Nepali'),
    ('Math ','Math'),
    ('Science','Science'),
    ('Social','Social'),
    ('Eph','Eph'),
    ('Account','Account'),
    ('Computer','Computer'),

]
plus_two_choices = [
    ('Physics','Physics'),
    ('Chemistry','Chemistry'),
    ('Math','Math'),
    ('English','English'),
    ('Bio','Bio'),
]
bachelor_choices = [
    ('CSIT','CSIT'),
    ('BIM','BIM'),
    ('BHM','BHM'),
    ('BCA', 'BCA'),
    ('BBA','BBA')
]

# class Faculty(models.Model):
#     level = models.CharField(max_length=15,choices=level_choices)
#     faculty = models.CharField(max_length=30, blank=True)
#     def __str__(self):
#        return self.faculty


    
# class YearOrSemester(models.Model):
#     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
#     year = models.CharField(max_length=15, choices=year_choices, blank=True)
#     sem = models.CharField(max_length=30, choices=sem_choices, blank=True, null= True)

#     def __str__(self):
#         return '%s %s' % (self.year, self.sem)





# class Questions(models.Model):
#     questions = models.ForeignKey(YearOrSemester, on_delete=models.CASCADE)
#     sub_name = models.CharField(max_length=125)
#     date_posted = models.DateTimeField(default=timezone.now)
#     file = models.FileField()

#     def __str__(self):
#         return self.sub_name

class Years(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)




class See(models.Model):
    year = models.ForeignKey(Years, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=100, choices=see_choices)
    file = models.FileField()

    def __str__(self):
        return self.subjects

class PlusTwo(models.Model):
    year = models.ForeignKey(Years, on_delete=models.CASCADE)
    level = models.IntegerField()
    subjects = models.CharField(max_length=100, choices=plus_two_choices)
    file = models.FileField()

    def __str__(self):
        return self.subjects


class Bachelors(models.Model):
    bachelors_year = models.CharField(max_length=50, choices=year_choices)
    question_year = models.CharField(max_length=100)
    faculty = models.CharField(max_length=50, choices=bachelor_choices)
    semester = models.CharField(max_length=50,choices=sem_choices)
    subjects = models.CharField(max_length=100)
    file = models.FileField()


    def __str__(self):
        return '%s %s %s' % (self.faculty, self.subjects, self.question_year)
    
