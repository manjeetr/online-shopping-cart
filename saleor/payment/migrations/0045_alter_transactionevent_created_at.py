# Generated by Django 3.2.16 on 2022-11-18 08:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0044_transactionevent_cause"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactionevent",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
