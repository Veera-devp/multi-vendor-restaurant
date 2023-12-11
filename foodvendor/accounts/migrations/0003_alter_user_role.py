# Generated by Django 4.2.7 on 2023-12-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.PositiveSmallIntegerField(
                blank=True, choices=[(1, "Vendor"), (2, "Customer")], null=True
            ),
        ),
    ]
