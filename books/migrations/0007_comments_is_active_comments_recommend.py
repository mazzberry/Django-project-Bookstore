# Generated by Django 5.0 on 2024-02-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_comments_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
    ]
