# Generated by Django 3.2 on 2023-10-23 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('IdDepartamento', models.AutoField(db_column='IdDepartamento', primary_key=True, serialize=False)),
                ('NombreCorto', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'Departamento',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('IdPais', models.AutoField(db_column='IdPais', primary_key=True, serialize=False)),
                ('NombreCorto', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'Pais',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('IdMunicipio', models.AutoField(db_column='IdMunicipio', primary_key=True, serialize=False)),
                ('NombreCorto', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=250)),
                ('IdDepartamento', models.ForeignKey(db_column='IdDepartamento', on_delete=django.db.models.deletion.CASCADE, to='generales.departamento')),
            ],
            options={
                'db_table': 'Municipio',
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='IdPais',
            field=models.ForeignKey(db_column='IdPais', on_delete=django.db.models.deletion.CASCADE, to='generales.pais'),
        ),
    ]
