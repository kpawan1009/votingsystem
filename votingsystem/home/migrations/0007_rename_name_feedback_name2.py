# Generated by Django 4.0.4 on 2022-04-27 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='name',
            new_name='name2',
        ),
    ]
