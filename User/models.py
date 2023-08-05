from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email = models.EmailField(unique=True)
    def __str__(self):
        return self.user_name

class Submission(models.Model):
    # problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
    LANGUAGES = (("C++", "C++"), ("C", "C"), ("Python3", "Python3"), ("Python2", "Python2"), ("Java", "Java"))
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.TextField()
    verdict = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    language = models.CharField(
        max_length=10, choices=LANGUAGES, default="C++")

