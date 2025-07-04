# Generated by Django 5.2 on 2025-04-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vpn_client', '0002_delete_vpnuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='VPNUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('public_key', models.TextField()),
                ('allowed_ips', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
