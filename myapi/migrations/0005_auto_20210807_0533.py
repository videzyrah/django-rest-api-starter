# Generated by Django 3.1.4 on 2021-08-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20210807_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cook_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='prep_time',
        ),
    ]