# Generated by Django 5.0.1 on 2024-01-12 11:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0005_alter_category_main_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, max_length=500
            ),
        ),
    ]
