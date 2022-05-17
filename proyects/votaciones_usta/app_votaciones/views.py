from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app_votaciones.models import Decano,Estudiante,Facultad, Votacion, EstadoVotacion, TipoVotacion, Candidato, Voto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

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
    #usuario = authenticate(email=email, password=password)
    # TODO: authenticate always returning none
    usuario = User.objects.get(email=email)
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
    return render(request, 'voteCycle.html')

@login_required
def voteFaculty(request):
    return render(request, 'voteFaculty.html')

@login_required
def consultVoteResults(request):
    return render(request, 'consultVoteResults.html')

@login_required
def consultMyVote(request):
    return render(request, 'consultMyVote.html')

@login_required
def consultVotingListStudent(request):
    return render(request, 'consultVotingListStudent.html')

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
