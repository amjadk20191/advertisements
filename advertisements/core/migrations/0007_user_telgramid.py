# Generated by Django 4.2.3 on 2023-09-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_dateofstart_user_dateofend'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telgramID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
