# Generated by Django 3.1.4 on 2021-08-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_plant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]