# Generated by Django 3.2.7 on 2021-10-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
