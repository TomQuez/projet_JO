# Generated by Django 5.0 on 2023-12-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_shopper_tickets'),
        ('store', '0008_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopper',
            name='tickets',
            field=models.ManyToManyField(blank=True, to='store.ticket'),
        ),
    ]