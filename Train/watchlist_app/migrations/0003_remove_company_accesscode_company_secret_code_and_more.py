# Generated by Django 4.0.5 on 2023-07-28 10:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_company_remove_watchlist_platform_delete_review_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='accessCode',
        ),
        migrations.AddField(
            model_name='company',
            name='secret_code',
            field=models.CharField(default=123, max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
