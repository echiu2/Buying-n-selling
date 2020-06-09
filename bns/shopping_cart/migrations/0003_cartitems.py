# Generated by Django 3.0.5 on 2020-06-08 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        ('shopping_cart', '0002_auto_20200601_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.Post')),
            ],
        ),
    ]
