# Generated by Django 3.0.5 on 2020-05-27 22:59

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='state',
            new_name='country',
        ),
        migrations.AddField(
            model_name='profile',
            name='states',
            field=localflavor.us.models.USStateField(max_length=2, null=True),
        ),
    ]