# Generated by Django 2.0.6 on 2018-06-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_flow', '0003_auto_20180620_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detial',
            name='flag',
            field=models.NullBooleanField(),
        ),
    ]