# Generated by Django 5.0.6 on 2024-07-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0004_alter_mithilamodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mithilamodel',
            name='descriptions',
            field=models.TextField(default=''),
        ),
    ]