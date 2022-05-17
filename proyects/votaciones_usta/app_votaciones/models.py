from django.db import models
# Librería de la clase User
from django.contrib.auth.models import User
from datetime import datetime 

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
        return self.id

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
    start_date = models.DateField(
                                auto_now=False, 
	                            auto_now_add=False,
    )
    end_date = models.DateField(auto_now=False, 
	                            auto_now_add=False,
                                )
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

class Candidato(models.Model):
    idEstudiante = models.ForeignKey(Estudiante,
        related_name='candidatos',
        null=False,                  
        on_delete=models.PROTECT
    )
    idVotacion = models.ForeignKey(Votacion,
        related_name='candidatos',
        null=False,
        on_delete=models.PROTECT
    )
    semestre = models.IntegerField(null=False)
    propuesta = models.CharField(max_length=200)
    def __int__(self):
        return self.id

    class Meta:
        app_label = 'app_votaciones'

class Voto(models.Model):
    idVotante = models.ForeignKey(Estudiante,
        related_name='votos',
        null=False,                  
        on_delete=models.PROTECT
    )
    idCandidato = models.ForeignKey(Candidato,
        related_name='votos',
        null=False,
        on_delete=models.PROTECT
    )
    fechaHora = models.DateTimeField(auto_now=False, 
        auto_now_add=False,
    )


    def __int__(self):
        return self.id

    class Meta:
        app_label = 'app_votaciones'
