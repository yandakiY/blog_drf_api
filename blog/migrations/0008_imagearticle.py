# Generated by Django 5.0.1 on 2024-01-04 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='media/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='blog.article')),
            ],
        ),
    ]
