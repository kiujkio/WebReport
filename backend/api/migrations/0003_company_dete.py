# Generated by Django 4.0.2 on 2022-02-03 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vulnerability'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='dete',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
