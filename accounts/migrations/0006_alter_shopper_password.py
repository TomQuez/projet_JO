# Generated by Django 5.0 on 2023-12-08 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_shopper_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopper',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(message='le mot de passe doit contenir au moins 8 caractères, une majuscule, une minuscule et un chiffre', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d]{8,}$')]),
        ),
    ]
