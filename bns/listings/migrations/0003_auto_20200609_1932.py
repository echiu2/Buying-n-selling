# Generated by Django 3.0.5 on 2020-06-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'slug')},
        ),
    ]