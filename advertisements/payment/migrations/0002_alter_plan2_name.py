# Generated by Django 4.2.3 on 2023-08-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan2',
            name='name',
            field=models.TextField(),
        ),
    ]