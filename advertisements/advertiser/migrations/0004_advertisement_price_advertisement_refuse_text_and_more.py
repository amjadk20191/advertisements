# Generated by Django 4.2.3 on 2023-08-01 13:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertiser', '0003_alter_seen_advertisement_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='refuse_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='cative',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]