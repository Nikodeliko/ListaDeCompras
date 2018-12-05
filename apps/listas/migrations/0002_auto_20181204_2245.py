# Generated by Django 2.1.2 on 2018-12-05 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listacompras',
            name='costo_total_presupuestado',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listacompras',
            name='costo_total_real',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listacompras',
            name='total_productos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listacompras',
            name='total_productos_comprados',
            field=models.PositiveIntegerField(default=0),
        ),
    ]