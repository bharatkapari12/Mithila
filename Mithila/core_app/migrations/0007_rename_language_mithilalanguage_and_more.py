# Generated by Django 5.0.6 on 2024-07-19 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0006_language_mithilacertificate_mithilafood'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Language',
            new_name='MithilaLanguage',
        ),
        migrations.RenameField(
            model_name='mithilacertificate',
            old_name='ceritificate_no',
            new_name='certificate_no',
        ),
    ]
