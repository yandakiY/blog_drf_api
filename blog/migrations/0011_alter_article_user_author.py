# Generated by Django 5.0.1 on 2024-01-05 13:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_article_user_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='user_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
