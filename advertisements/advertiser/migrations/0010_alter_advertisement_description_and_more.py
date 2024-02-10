# Generated by Django 4.2.3 on 2023-08-04 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0009_alter_advertisement_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(default='aaaa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='name',
            field=models.CharField(default='aaaaaa', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]