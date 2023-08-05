# Generated by Django 4.2.3 on 2023-08-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0003_remove_test_case_p_id_remove_submission_problem_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="language",
            field=models.CharField(
                choices=[
                    ("C++", "C++"),
                    ("C", "C"),
                    ("Python3", "Python3"),
                    ("Python2", "Python2"),
                    ("Java", "Java"),
                ],
                default="C++",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
