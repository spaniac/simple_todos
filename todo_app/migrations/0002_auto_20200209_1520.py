# Generated by Django 3.0.3 on 2020-02-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Datetime when todo is completed'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='image_url',
            field=models.TextField(blank=True, default='', verbose_name='Image that will be uploaded'),
        ),
    ]
