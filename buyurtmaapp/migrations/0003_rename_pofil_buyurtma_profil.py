# Generated by Django 4.1 on 2022-10-19 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtmaapp', '0002_savat_buyurtma'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyurtma',
            old_name='pofil',
            new_name='profil',
        ),
    ]
