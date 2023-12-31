# Generated by Django 5.0 on 2024-01-07 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0001_initial"),
        ("posts", "0002_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                default=6, on_delete=django.db.models.deletion.CASCADE, to="posts.post"
            ),
            preserve_default=False,
        ),
    ]
