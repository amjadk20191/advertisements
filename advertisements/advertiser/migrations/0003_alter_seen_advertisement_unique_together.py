# Generated by Django 4.2.3 on 2023-07-30 14:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertiser', '0002_seen_advertisement'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seen_advertisement',
            unique_together={('user', 'advertisement')},
        ),
    ]