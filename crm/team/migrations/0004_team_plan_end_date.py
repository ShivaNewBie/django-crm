# Generated by Django 3.0 on 2022-05-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20220505_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]