# Generated by Django 4.2.3 on 2023-07-20 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0002_alter_user_user_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="test_case", name="p_id",),
        migrations.RemoveField(model_name="submission", name="problem",),
        migrations.DeleteModel(name="Problem",),
        migrations.DeleteModel(name="Test_Case",),
    ]
