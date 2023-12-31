# Generated by Django 3.2 on 2023-10-26 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generales', '0006_empresa_institucioneducativa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUsuario',
            fields=[
                ('IdInfoUsuario', models.AutoField(db_column='IdInfoUsuario', primary_key=True, serialize=False)),
                ('CorreoInstitucional', models.CharField(max_length=250)),
                ('Agnio', models.IntegerField()),
                ('Telefono', models.CharField(max_length=20)),
                ('FechaNacimiento', models.DateField()),
                ('Carnet', models.CharField(blank=True, max_length=100, null=True)),
                ('FotoPerfil', models.ImageField(blank=True, null=True, upload_to='fotos-perfil/')),
                ('IdDepartamento', models.ForeignKey(db_column='IdDepartamento', on_delete=django.db.models.deletion.CASCADE, to='generales.departamento')),
                ('IdEmpresa', models.ForeignKey(db_column='IdEmpresa', default=1, on_delete=django.db.models.deletion.CASCADE, to='generales.empresa')),
                ('IdInstitucionEducativa', models.ForeignKey(db_column='IdInstitucionEducativa', default=1, on_delete=django.db.models.deletion.CASCADE, to='generales.institucioneducativa')),
                ('IdMunicipio', models.ForeignKey(db_column='IdMunicipio', on_delete=django.db.models.deletion.CASCADE, to='generales.municipio')),
                ('IdPais', models.ForeignKey(db_column='IdPais', on_delete=django.db.models.deletion.CASCADE, to='generales.pais')),
                ('IdTipoUsuario', models.ForeignKey(db_column='IdTipoUsuario', on_delete=django.db.models.deletion.CASCADE, to='generales.tipousuario')),
                ('IdUsuario', models.OneToOneField(db_column='IdUsuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'InfoUsuario',
            },
        ),
    ]
