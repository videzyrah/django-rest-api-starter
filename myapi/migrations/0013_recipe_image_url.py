# Generated by Django 4.1.2 on 2022-11-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0012_auto_20210824_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
