# Generated by Django 4.1 on 2022-10-19 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0003_detal_mahsulot_rasm'),
        ('userapp', '0001_initial'),
        ('buyurtmaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.SmallIntegerField(default=1)),
                ('chegirma', models.SmallIntegerField(default=1)),
                ('umumiy', models.SmallIntegerField()),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('summa', models.PositiveIntegerField()),
                ('yetkazish', models.PositiveIntegerField(default=0)),
                ('yakuniy', models.PositiveIntegerField()),
                ('pofil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
                ('savat', models.ManyToManyField(to='buyurtmaapp.savat')),
            ],
        ),
    ]
