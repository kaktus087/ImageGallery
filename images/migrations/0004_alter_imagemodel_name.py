# Generated by Django 4.2.4 on 2023-08-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_imagemodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
