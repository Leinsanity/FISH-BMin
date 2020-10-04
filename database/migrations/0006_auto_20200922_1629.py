# Generated by Django 3.0.8 on 2020-09-22 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_delete_historicalspecimen'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Identifiers',
            },
        ),
        migrations.CreateModel(
            name='Tissue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tissue', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tissue',
            },
        ),
        migrations.RemoveField(
            model_name='specimen',
            name='collector',
        ),
        migrations.AddField(
            model_name='specimen',
            name='collector',
            field=models.ManyToManyField(to='database.Collector'),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='final_ID',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='initial_ID',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='specimen',
            name='initialIdentifer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='database.InitialIdentifier'),
        ),
        migrations.AddField(
            model_name='specimen',
            name='tissue',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='database.Tissue'),
        ),
    ]