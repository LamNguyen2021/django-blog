# Generated by Django 4.1.7 on 2023-04-19 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_iamge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='iamge',
            new_name='image',
        ),
    ]