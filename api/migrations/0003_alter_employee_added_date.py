# Generated by Django 5.2.4 on 2025-07-25 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='added_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
