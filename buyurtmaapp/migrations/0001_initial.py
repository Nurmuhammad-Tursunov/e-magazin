# Generated by Django 4.1 on 2022-10-19 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
        ('asosiy', '0003_detal_mahsulot_rasm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tanlangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
    ]