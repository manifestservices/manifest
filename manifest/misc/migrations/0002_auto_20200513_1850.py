# Generated by Django 2.0.6 on 2020-05-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]