# Generated by Django 5.1.4 on 2024-12-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aiservice',
            name='url',
        ),
        migrations.AddField(
            model_name='aiservice',
            name='path',
            field=models.CharField(default='default-path', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aiservice',
            name='tagid',
            field=models.CharField(default='default-path', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aiservice',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icons/'),
        ),
    ]