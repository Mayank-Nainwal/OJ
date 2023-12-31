# Generated by Django 4.2.3 on 2023-07-17 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Problem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("problem_id", models.IntegerField()),
                ("problem_name", models.CharField(max_length=200)),
                ("problem_description", models.TextField()),
                ("problem_output", models.CharField(max_length=200)),
                ("problem_difficulty", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=200)),
                ("user_password", models.CharField(max_length=200)),
                ("user_email", models.EmailField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Test_Case",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("test_case", models.CharField(max_length=200)),
                ("output", models.CharField(max_length=200)),
                (
                    "p_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="User.problem"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.TextField()),
                ("verdict", models.CharField(max_length=200)),
                ("date", models.DateTimeField()),
                (
                    "problem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="User.problem"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="User.user"
                    ),
                ),
            ],
        ),
    ]
