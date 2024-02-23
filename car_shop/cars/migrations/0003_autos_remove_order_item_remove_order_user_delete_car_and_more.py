# Generated by Django 5.0.2 on 2024-02-22 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('inmatricolation', models.DateField(help_text="Date as 'Year/month'")),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
