from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app_votaciones.models import Decano,Estudiante,Facultad, Votacion, EstadoVotacion, TipoVotacion, Candidato, Voto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logIn(request):
    return render(request, 'logIn.html')


@login_required
def view_logout(request):
    # Cierra la sesión del usuario
    logout(request)

    # Redirecciona la página de login
    return redirect('app:logIn')

def autenticar(request):
    # Obtiene los datos del formulario de autenticación
    email = request.POST['email']
    password = request.POST['password']

    # Obtiene el usuario
    usuario = authenticate(username=email, password=password)
    # TODO: authenticate always returning none
    #usuario = User.objects.get(email=email)
    # Verifica si el usuario existe en la base de datos
    if usuario is not None:
        # Inicia la sesión del usuario en el sistema
        login(request, usuario)
        # Verifica si el usuario es decano o estudiante
        try:
            estudiante = Estudiante.objects.get(id=usuario)
        except:
            estudiante = None
        try:
            decano = Decano.objects.get(id=usuario)
        except:
            decano = None

        if(estudiante is not None):
            return redirect('app:voteFaculty')
        if(decano is not None):
            return redirect('app:createStudent')

    else:
        # Retorna un mensaje de error de login no válido
        return HttpResponse(usuario)

@login_required
def createStudent(request):
    if request.user.is_superuser:
        query = Decano.objects.get(id_id=request.user.id)
        query = Facultad.objects.get(id=query.idFacultad_id)
        contexto = {"Facultad":query.nombre}
        return render(request, 'createStudent.html',contexto)
    else:
        redirect('app:logIn')

@login_required
def addStudent(request):
    # Obtiene los datos
    names = request.POST['names']
    last_name = request.POST['lastnames']
    cycle = request.POST['cycle']
    email = request.POST['email']
    password = request.POST['document']
    faculty = request.POST['faculty']
    # Crea el objeto usuario
    usuario = User.objects.create_user(
        first_name=names,
        last_name=last_name,
        email=email,
        username=email)
    usuario.set_password(password)
    # Guarda el usuario en la base de datos
    usuario.save()

    #Obtiene el objeto de facultad
    facultad = Facultad.objects.get(nombre=faculty)
    #Crea el objecto estudiante
    estudiante = Estudiante(id=usuario,idFacultad=facultad,semestre=cycle)
    #Guarda el estudiante en la base de datos
    estudiante.save()
    return redirect('app:consultFacultyStudentList')

@login_required
def createCycleVoting(request):
    query = Decano.objects.get(id_id=request.user.id)
    query = Facultad.objects.get(id=query.idFacultad_id)
    contexto = {"Facultad":query.nombre}
    return render(request, 'createCycleVoting.html',contexto)

@login_required
def addCycleVoting(request):
    # Obtiene datos de la votacion
    name = request.POST['name']
    start_date = request.POST['startdate']
    end_date = request.POST['enddate']
    # TODO: cycle is not in model
    cycle = request.POST['cycle']
    faculty = request.POST['faculty']

    facultad = Facultad.objects.get(nombre=faculty)
    tipo = TipoVotacion.objects.get(nombre="Semestre")
    estado = EstadoVotacion.objects.get(nombre="Postulacion")

    # Crea el objeto de la votacion
    votacion = Votacion(nombre=name,idFacultad=facultad,start_date=start_date,end_date=end_date,idTipo=tipo,idEstado=estado)
    # Guarda la votacion
    votacion.save()

    return redirect('app:consultVotingListDean')


@login_required
def changeCycleVotingStatus(request):
    query = Votacion.objects.all()
    lista = list(query.values())
    fac = Facultad.objects.get(id=Decano.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":lista, "facultad":fac, "facultad_id":fac.id }
    return render(request, 'changeCycleVotingStatus.html',contexto)

@login_required
def nextStatus(request):
    idVotacion = request.POST['id']
    votacion = Votacion.objects.get(id=idVotacion)
    if votacion.idEstado_id < 3:
        votacion.idEstado = EstadoVotacion.objects.get(id=votacion.idEstado_id+1)
        votacion.save()
    return redirect('app:changeCycleVotingStatus')

@login_required
def consultCycleVoting(request):
    query = Votacion.objects.all()
    lista = list(query.values())
    fac = Facultad.objects.get(id=Decano.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":lista, "facultad":fac, "facultad_id":fac.id }
    return render(request, 'consultCycleVoting.html', contexto)


@login_required
def createFacultyVoting(request):
    query = Decano.objects.get(id_id=request.user.id)
    query = Facultad.objects.get(id=query.idFacultad_id)
    contexto = {"Facultad":query.nombre}
    return render(request, 'createFacultyVoting.html',contexto)

@login_required
def addFacultyVoting(request):
    # Obtiene datos de la votacion
    name = request.POST['name']
    start_date = request.POST['startdate']
    end_date = request.POST['enddate']
    # TODO: cycle is not in model
    cycle = request.POST['cycle']
    faculty = request.POST['faculty']

    facultad = Facultad.objects.get(nombre=faculty)
    tipo = TipoVotacion.objects.get(nombre="Facultad")
    estado = EstadoVotacion.objects.get(nombre="Postulacion")

    # Crea el objeto de la votacion
    votacion = Votacion(nombre=name,idFacultad=facultad,start_date=start_date,end_date=end_date,idTipo=tipo,idEstado=estado)
    # Guarda la votacion
    votacion.save()

    return redirect('app:consultVotingListDean')

@login_required
def placeFacultyStudent(request):
    return render(request, 'placeFacultyStudent.html')

@login_required
def changeFacultyVotingStatus(request):
    query = Votacion.objects.all()
    lista = list(query.values())
    fac = Facultad.objects.get(id=Decano.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":lista, "facultad":fac, "facultad_id":fac.id }
    return render(request, 'changeFacultyVotingStatus.html',contexto)

@login_required
def consultFacultyVoting(request):
    return render(request, 'consultFacultyVoting.html')

@login_required
def consultVotingListDean(request):
    query = Votacion.objects.all()
    lista = list(query.values())
    fac = Facultad.objects.get(id=Decano.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":lista, "facultad":fac, "facultad_id":fac.id }
    return render(request, 'consultVotingListDean.html',contexto)

@login_required
def applyToCycleVoting(request):
    votaciones = Votacion.objects.filter(idFacultad=Estudiante.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":votaciones}
    return render(request, 'applyToCycleVoting.html',contexto)

@login_required
def applyToVoting(request):
    propuesta = request.POST['proposal']
    votacion = request.POST['voting']
    candidato = Candidato(idEstudiante=Estudiante.objects.get(id=request.user.id),idVotacion=Votacion.objects.get(id=votacion),propuesta=propuesta,semestre=Estudiante.objects.get(id=request.user.id).semestre)
    print(propuesta,votacion)
    candidato.save()
    return redirect('app:applyToCycleVoting')

@login_required
def voteCycle(request):
    votaciones = Votacion.objects.filter(idFacultad=Estudiante.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":votaciones}
    return render(request, 'voteCycle.html', contexto)

@login_required
def vote(request):
    candidato = request.POST['id']
    votante = request.user.id
    voto = Voto(idCandidato=Candidato.objects.get(id=candidato),
                idVotante=Estudiante.objects.get(id=votante),
                fechaHora=datetime.now())
    voto.save()
    return render(request, 'consultMyVote.html')

@login_required
def listCandidates(request):
    # Se obtienen los votos de el usuario actual en todas las votaciones en las que ha participado
    misVotos = list(Voto.objects.filter(idVotante=request.user.id).values())
    # Se crea el candidatoVotado en caso de que el usuario autenticado ya haya votado en esta votacion 
    candidatoVotado = None
    # Se verifica si alguno de los candidatos por los que el usuario ha votado tiene que ver con la votacion que se esta consultando actualmente
    for voto in misVotos:
        candidato = list(Candidato.objects.filter(id=voto["idCandidato_id"]).values())[0]
        votacion = list(Votacion.objects.filter(id=candidato["idVotacion_id"]).values())[0]
        # En caso de que alguna de las votaciones en las que el usuario ha participado sea la misma que se esta consultando se guarda el candidato por el cual voto
        if votacion['id'] == int(request.POST['id']):
            candidatoVotado = candidato

    # Se obtienen los candidatos de la votacion que se esta consultando actualmente
    candidatos = list(Candidato.objects.filter(idVotacion=request.POST['id']))
    # Se obtienen los usuarios que son candidatos a la votacion
    estudiantes = []
    for i in candidatos:
        estudiantes.append({"nombre":list(User.objects.filter(id=i.idEstudiante_id).values())[0].get("first_name"),
                            "apellido":list(User.objects.filter(id=i.idEstudiante_id).values())[0].get("last_name"), 
                            "propuesta":i.propuesta, "idCandidato":i.id})
    # Se construye el objeto a enviar al template
    contexto = {'estudiantes': estudiantes}
    # Si ya hay un candidato por el cual el usuario actual voto entonces se anexa a la informacion enviada al template
    if candidato is not None:
        contexto = {'estudiantes':estudiantes,'candidatoVotado':candidatoVotado}
    return render(request, 'listCandidates.html', contexto)


@login_required
def voteFaculty(request):
    votaciones = Votacion.objects.filter(idFacultad=Estudiante.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":votaciones}
    return render(request, 'voteFaculty.html',contexto)

@login_required
def consultVoteResults(request):
    fac = Facultad.objects.get(id=Estudiante.objects.get(id=request.user.id).idFacultad_id)
    votaciones = Votacion.objects.filter(idFacultad=Estudiante.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":votaciones, "facultad":fac, "facultad_id":fac.id }
    return render(request, 'consultVoteResults.html', contexto)

@login_required
def listResults(request):
    # Se obtienen los candidatos de la votacion que se esta consultando actualmente
    candidatos = list(Candidato.objects.filter(idVotacion=request.POST['id']))
    # Se obtienen los usuarios que son candidatos a la votacion
    estudiantes = []
    for i in candidatos:
        conteoVotos = len(list(Voto.objects.filter(idCandidato=i).values()))
        estudiantes.append({"nombre":list(User.objects.filter(id=i.idEstudiante_id).values())[0].get("first_name"),
                            "apellido":list(User.objects.filter(id=i.idEstudiante_id).values())[0].get("last_name"), 
                            "propuesta":i.propuesta, "idCandidato":i.id,
                            "conteoVotos":conteoVotos})
    # Se construye el objeto a enviar al template
    contexto = {'estudiantes': estudiantes}
    return render(request, 'listResults.html', contexto)


@login_required
def consultMyVote(request):
    misVotos = list(Voto.objects.filter(idVotante=request.user.id).values())
    votaciones = []
    for voto in misVotos:
        candidato = list(Candidato.objects.filter(id=voto["idCandidato_id"]).values())[0]
        votaciones.append(list(Votacion.objects.filter(id=candidato["idVotacion_id"]).values())[0])
    contexto = {"votaciones":votaciones}
    return render(request, 'consultMyVote.html',contexto)

@login_required
def consultVotingListStudent(request):
    query = Votacion.objects.all()
    lista = list(query.values())
    fac = Facultad.objects.get(id=Estudiante.objects.get(id=request.user.id).idFacultad_id)
    contexto = {"votaciones":lista, "facultad":fac, "facultad_id":fac.id }
    return render(request, 'consultVotingListStudent.html',contexto)

@login_required
def consultFacultyStudentList(request):
    # Obtiene la facultad del decano
    fac = Facultad.objects.get(id=Decano.objects.get(id=request.user.id).idFacultad_id)
    # Obtiene los estudiantes de la facultad del decano
    query = Estudiante.objects.filter(idFacultad=fac)
    # Se obtienen los usuarios que son estudiantes de la facultad del decano
    estudiantes = []
    for i in query:
        estudiantes.append(list(User.objects.filter(id=i.id_id).values())[0])
    # Se configura el objeto para enviar al template
    contexto = {"estudiantes":estudiantes, "facultad":fac, "facultad_id":fac.id }
    return render(request, 'consultFacultyStudentList.html', contexto)
