# Generated by Django 3.0.8 on 2020-09-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimen',
            name='dna_barcode',
            field=models.TextField(max_length=700),
        ),
    ]
