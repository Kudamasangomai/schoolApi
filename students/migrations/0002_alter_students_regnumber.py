# Generated by Django 4.1.1 on 2022-10-04 03:42

from django.db import migrations, models
import students.models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='regnumber',
            field=models.IntegerField(default=students.models.random_reg_number),
        ),
    ]
