# Generated by Django 4.1.1 on 2022-09-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_remove_ad_created_alter_ad_is_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="is_published",
            field=models.BooleanField(
                choices=[(True, "Открыто"), (False, "Закрыто")], default=True
            ),
        ),
    ]
