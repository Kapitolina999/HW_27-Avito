# Generated by Django 4.1.1 on 2022-10-29 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="slug",
        ),
    ]
