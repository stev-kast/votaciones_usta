from django.db import models
# Librería de la clase User
from django.contrib.auth.models import User

class Facultad(models.Model):
    nombre = models.CharField(max_length=45,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'app_votaciones'


class Decano(models.Model):
    id = models.OneToOneField(User,
                related_name='decanos',
                on_delete=models.PROTECT,
                primary_key=True)
    idFacultad = models.ForeignKey(Facultad,
                related_name='decanos',
                null=False,                  
                on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'app_votaciones'

class Estudiante(models.Model):
    id = models.OneToOneField(User,
                related_name='estudiantes',
                on_delete=models.PROTECT,
                primary_key=True)
    idFacultad = models.ForeignKey(Facultad,
                  related_name='estudiantes',
                  null=False,                  
                  on_delete=models.PROTECT)
    semestre = models.IntegerField(null=False)
    
    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'app_votaciones'


class EstadoVotacion(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'app_votaciones'

class TipoVotacion(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'app_votaciones'

class Votacion(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    idTipo = models.ForeignKey(TipoVotacion,
                  related_name='votaciones',
                  null=False,                  
                  on_delete=models.PROTECT)
    idEstado = models.ForeignKey(EstadoVotacion,
                  related_name='votaciones',
                  null=False,                  
                  on_delete=models.PROTECT)
    idFacultad = models.ForeignKey(Facultad,
                  related_name='votaciones',
                  null=False,                  
                  on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'app_votaciones'