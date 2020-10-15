# Generated by Django 3.0.3 on 2020-04-01 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Desarrollo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=255)),
                ('Estado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=255)),
                ('prioridad', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('observacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Desarrollo',
        ),
    ]
