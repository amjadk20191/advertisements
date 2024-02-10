# Generated by Django 4.2.3 on 2023-08-04 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_paln_plan'),
        ('core', '0004_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pending_subscribe',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.plan'),
        ),
    ]
