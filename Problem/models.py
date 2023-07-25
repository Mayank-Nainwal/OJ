from django.db import models

# Create your models here.

class Problem(models.Model):
    problem_id = models.IntegerField()
    problem_name = models.CharField(max_length=200)
    problem_description = models.TextField()
    problem_output = models.CharField(max_length=200)
    problem_difficulty = models.CharField(max_length=200)

class Test_Case(models.Model):
    p_id = models.ForeignKey(Problem,on_delete=models.CASCADE)
    test_case = models.CharField(max_length=200)
    output = models.CharField(max_length=200)
