# Generated by Django 3.1.6 on 2021-02-04 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('immoapp', '0002_auto_20210204_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appartement',
            old_name='characteristiques',
            new_name='caracteristiques',
        ),
    ]
