# Generated by Django 4.1 on 2022-08-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0010_linfoximage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='cargo_status',
            field=models.CharField(choices=[('Cargo Available', 'Cargo Available'), ('Cargo Not Available', 'Cargo Not Available')], default='Cargo Available', max_length=50),
        ),
    ]
