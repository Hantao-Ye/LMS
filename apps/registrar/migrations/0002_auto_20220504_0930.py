# Generated by Django 2.2 on 2022-05-04 09:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='worth',
            field=models.PositiveSmallIntegerField(choices=[(0, '0 %'), (5, '5 %'), (10, '10 %'), (15, '15 %'), (20, '20 %'), (25, '25 %'), (30, '30 %'), (35, '35 %'), (40, '40 %'), (45, '45 %'), (50, '50 %'), (55, '55 %'), (60, '60 %'), (65, '65 %'), (70, '70 %'), (75, '75 %'), (80, '80 %'), (85, '85 %'), (90, '90 %'), (95, '95 %'), (100, '100 %')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='exam',
            name='worth',
            field=models.PositiveSmallIntegerField(choices=[(0, '0 %'), (5, '5 %'), (10, '10 %'), (15, '15 %'), (20, '20 %'), (25, '25 %'), (30, '30 %'), (35, '35 %'), (40, '40 %'), (45, '45 %'), (50, '50 %'), (55, '55 %'), (60, '60 %'), (65, '65 %'), (70, '70 %'), (75, '75 %'), (80, '80 %'), (85, '85 %'), (90, '90 %'), (95, '95 %'), (100, '100 %')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='worth',
            field=models.PositiveSmallIntegerField(choices=[(0, '0 %'), (5, '5 %'), (10, '10 %'), (15, '15 %'), (20, '20 %'), (25, '25 %'), (30, '30 %'), (35, '35 %'), (40, '40 %'), (45, '45 %'), (50, '50 %'), (55, '55 %'), (60, '60 %'), (65, '65 %'), (70, '70 %'), (75, '75 %'), (80, '80 %'), (85, '85 %'), (90, '90 %'), (95, '95 %'), (100, '100 %')], default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
