# Generated by Django 3.0 on 2021-03-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="last_activity",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
