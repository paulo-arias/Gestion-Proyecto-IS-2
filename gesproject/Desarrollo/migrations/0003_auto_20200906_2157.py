# Generated by Django 2.2.11 on 2020-09-06 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Desarrollo', '0002_auto_20200906_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='linea_base',
            field=models.ForeignKey(blank=True, help_text='Linea Base a la que pertence', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Configuracion.LineaBase'),
        ),
        migrations.DeleteModel(
            name='LineaBase',
        ),
    ]
