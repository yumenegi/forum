# Generated by Django 3.1.6 on 2021-05-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='thread',
            name='title',
            field=models.TextField(max_length=3),
        ),
    ]
