# Generated by Django 2.2 on 2019-06-23 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190621_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]
