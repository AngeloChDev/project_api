# Generated by Django 5.0.2 on 2024-03-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_disponible_alter_car_inmatricolation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_car', models.IntegerField()),
                ('id_user', models.IntegerField()),
            ],
        ),
    ]
