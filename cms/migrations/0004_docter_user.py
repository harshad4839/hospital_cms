# Generated by Django 3.1.4 on 2021-01-19 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0003_docter_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='docter',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='docteruser', to=settings.AUTH_USER_MODEL),
        ),
    ]
