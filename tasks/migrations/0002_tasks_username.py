# Generated by Django 4.0 on 2021-12-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='username',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
