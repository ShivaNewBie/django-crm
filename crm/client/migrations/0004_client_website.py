# Generated by Django 3.0 on 2022-04-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_estimated_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
