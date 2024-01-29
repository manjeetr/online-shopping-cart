# Generated by Django 3.2.23 on 2024-01-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tax", "0007_auto_20230217_0837"),
    ]

    operations = [
        migrations.AddField(
            model_name="taxconfiguration",
            name="calculated_taxes_required_to_place_order",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="taxconfiguration",
            name="tax_app_id",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="taxconfigurationpercountry",
            name="tax_app_id",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.RunSQL(
            """
            ALTER TABLE tax_taxconfiguration
            ALTER COLUMN calculated_taxes_required_to_place_order
            SET DEFAULT true;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
