# Generated by Django 3.2.9 on 2021-11-15 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoqueitens',
            old_name='quntidade',
            new_name='quantidade',
        ),
    ]
