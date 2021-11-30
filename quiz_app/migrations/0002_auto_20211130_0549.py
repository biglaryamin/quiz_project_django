# Generated by Django 3.2.9 on 2021-11-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='Clicked',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='is_right',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='Category',
            field=models.ManyToManyField(blank=True, null=True, to='quiz_app.Category'),
        ),
    ]
