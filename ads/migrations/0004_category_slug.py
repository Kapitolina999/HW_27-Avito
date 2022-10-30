# Generated by Django 4.1.1 on 2022-10-29 21:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_remove_category_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                default="slug_1",
                max_length=10,
                validators=[django.core.validators.MinLengthValidator(5)],
            ),
            preserve_default=False,
        ),
    ]