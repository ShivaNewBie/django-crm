# Generated by Django 3.0 on 2022-04-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_remove_client_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='estimated_value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]