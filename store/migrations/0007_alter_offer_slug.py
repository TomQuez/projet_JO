# Generated by Django 5.0 on 2023-12-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_offer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='slug',
            field=models.SlugField(max_length=128),
        ),
    ]
