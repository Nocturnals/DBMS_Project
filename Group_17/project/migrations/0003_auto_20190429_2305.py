# Generated by Django 2.1.3 on 2019-04-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190414_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='money',
            field=models.IntegerField(null='True'),
        ),
        migrations.AlterField(
            model_name='package',
            name='no_of_days',
            field=models.IntegerField(null='True'),
        ),
    ]