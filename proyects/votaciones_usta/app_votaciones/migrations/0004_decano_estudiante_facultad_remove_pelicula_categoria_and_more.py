# Generated by Django 4.0.4 on 2022-04-22 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_votaciones', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Pelicula',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='idFacultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estudiantes', to='app_votaciones.facultad'),
        ),
        migrations.AddField(
            model_name='decano',
            name='idFacultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='decanos', to='app_votaciones.facultad'),
        ),
    ]
