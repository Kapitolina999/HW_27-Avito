# Generated by Django 4.1.1 on 2022-09-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ad",
            name="created",
        ),
        migrations.AlterField(
            model_name="ad",
            name="is_published",
            field=models.BooleanField(blank=True, default=True),
        ),
    ]