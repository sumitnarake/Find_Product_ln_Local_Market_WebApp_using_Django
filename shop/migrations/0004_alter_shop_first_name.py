# Generated by Django 4.1.3 on 2023-04-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_shop_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
    ]