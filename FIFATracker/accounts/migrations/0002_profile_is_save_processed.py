# Generated by Django 2.0 on 2018-03-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_save_processed',
            field=models.BooleanField(default=0),
        ),
    ]