# Generated by Django 2.0.7 on 2018-07-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='con_password',
            field=models.CharField(default='conpassword', max_length=10),
        ),
    ]
