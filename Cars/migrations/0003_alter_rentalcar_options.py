# Generated by Django 4.2 on 2025-01-14 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0002_alter_car_car_color_alter_car_car_daily_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rentalcar',
            options={'verbose_name': 'Locadora', 'verbose_name_plural': 'Locadoras'},
        ),
    ]