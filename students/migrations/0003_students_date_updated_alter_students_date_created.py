# Generated by Django 4.1.1 on 2022-10-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_students_regnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
