# Generated by Django 4.1 on 2022-10-17 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_alter_ichki_bolim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=300)),
                ('kafolat', models.CharField(max_length=300)),
                ('yetkazish', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('batafsil', models.TextField()),
                ('narx', models.PositiveIntegerField()),
                ('mavjud', models.BooleanField(default=False)),
                ('detal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.detal')),
                ('ichki', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ichki_mahsulotlari', to='asosiy.ichki')),
            ],
        ),
        migrations.CreateModel(
            name='Rasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='mahsulot_rasmlari')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mahsulot_rasmlari', to='asosiy.mahsulot')),
            ],
        ),
    ]
