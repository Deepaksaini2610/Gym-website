# Generated by Django 3.1.1 on 2021-06-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_mycontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile_no',
            field=models.IntegerField(default=False),
        ),
    ]