# Generated by Django 4.2.2 on 2023-06-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='home_address',
            field=models.TextField(verbose_name='Home Address'),
        ),
    ]