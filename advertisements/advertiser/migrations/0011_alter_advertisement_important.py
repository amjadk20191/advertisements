# Generated by Django 4.2.3 on 2023-08-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0010_alter_advertisement_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='important',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True),
        ),
    ]
