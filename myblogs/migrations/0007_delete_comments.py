# Generated by Django 4.2.11 on 2024-05-25 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0006_remove_blog_comments_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
