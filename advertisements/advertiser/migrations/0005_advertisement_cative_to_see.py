# Generated by Django 4.2.3 on 2023-08-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0004_advertisement_price_advertisement_refuse_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='cative_to_see',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
