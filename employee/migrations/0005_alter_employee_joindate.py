# Generated by Django 4.1.5 on 2023-01-14 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_joindate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joinDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 14, 8, 53, 51, 748331, tzinfo=datetime.timezone.utc)),
        ),
    ]
