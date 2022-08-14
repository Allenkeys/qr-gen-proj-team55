# Generated by Django 4.0.6 on 2022-08-13 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QrcodeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
                ('organizer', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('event_name', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('organizer_email', models.EmailField(max_length=254)),
                ('organizer_phone', models.CharField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QrcodeBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
                ('company', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('opening_hours', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('url', models.URLField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QrcodeAppDownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
                ('app_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('androidApp_link', models.URLField(null=True)),
                ('iosApp_link', models.URLField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
