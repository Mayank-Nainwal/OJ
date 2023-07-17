from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email = models.EmailField(unique=True)

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

class Submission(models.Model):
    problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.TextField()
    verdict = models.CharField(max_length=200)
    date = models.DateTimeField()

# Create your models here.
