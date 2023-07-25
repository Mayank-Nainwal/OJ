from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email = models.EmailField(unique=True)

class Submission(models.Model):
    # problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.TextField()
    verdict = models.CharField(max_length=200)
    date = models.DateTimeField()

# Create your models here.
