# Generated by Django 4.2.3 on 2023-08-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser', '0007_rename_cative_to_see_advertisement_active_to_see'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='date_of_start',
            field=models.DateField(default='2222-1-1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='date_of_end',
            field=models.DateField(default='2222-1-1'),
            preserve_default=False,
        ),
    ]
