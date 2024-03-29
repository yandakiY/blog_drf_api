# Generated by Django 5.0.1 on 2024-01-09 12:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_dislikearticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='dislikearticle',
            name='dislike_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='likearticle',
            name='like_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='user_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='my_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dislikearticle',
            name='user_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likearticle',
            name='user_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
