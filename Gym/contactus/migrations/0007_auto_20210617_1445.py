# Generated by Django 3.1.1 on 2021-06-17 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0006_auto_20210617_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mobile_no',
            new_name='n',
        ),
    ]
