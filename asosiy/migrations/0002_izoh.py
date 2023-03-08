# Generated by Django 4.1.3 on 2023-03-07 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baho', models.PositiveSmallIntegerField()),
                ('matn', models.CharField(max_length=500)),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
    ]
