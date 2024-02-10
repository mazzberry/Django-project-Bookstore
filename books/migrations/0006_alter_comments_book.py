# Generated by Django 5.0 on 2024-02-10 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.books'),
        ),
    ]
