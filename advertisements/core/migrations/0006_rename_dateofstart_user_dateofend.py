# Generated by Django 4.2.3 on 2023-08-05 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_pending_subscribe_user_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dateOfStart',
            new_name='dateOfEnd',
        ),
    ]