# Generated by Django 4.2.3 on 2023-07-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]