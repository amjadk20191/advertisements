# Generated by Django 4.2.3 on 2023-08-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_opinion_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='connect_with_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='complaints',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='phone',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]