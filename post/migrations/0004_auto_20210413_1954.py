# Generated by Django 3.1.6 on 2021-04-13 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210413_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userPosted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.thread'),
        ),
    ]
