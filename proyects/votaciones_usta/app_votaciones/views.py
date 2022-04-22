from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app_votaciones.models import Decano,Estudiante,Facultad
from django.contrib.auth.decorators import login_required

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
    return render(request, 'createStudent.html')

@login_required
def addStudent(request):
    # Obtiene los datos
    names = request.POST['names']
    last_name = request.POST['lastnames']
    cycle = request.POST['cycle']
    email = request.POST['email']
    username = request.POST['document']
    password = request.POST['document']
    faculty = request.POST['faculty']
    # Crea el objeto usuario
    usuario = User.objects.create_user(
        first_name=names,
        last_name=last_name,
        email=email,
        username=username)
    usuario.set_password(password)
    # Guarda el usuario en la base de datos
    usuario.save()

    #Obtiene el objeto de facultad
    facultad = Facultad.objects.get(nombre=faculty)
    #Crea el objecto estudiante
    estudiante = Estudiante(id=usuario,idFacultad=facultad,semestre=cycle)
    #Guarda el estudiante en la base de datos
    estudiante.save()
    return redirect('app:logIn')

@login_required
def createCycleVoting(request):
    return render(request, 'createCycleVoting.html')

@login_required
def changeCycleVotingStatus(request):
    return render(request, 'changeCycleVotingStatus.html')

@login_required
def consultCycleVoting(request):
    return render(request, 'consultCycleVoting.html')

@login_required
def createFacultyVoting(request):
    return render(request, 'createFacultyVoting.html')

@login_required
def placeFacultyStudent(request):
    return render(request, 'placeFacultyStudent.html')

@login_required
def changeFacultyVotingStatus(request):
    return render(request, 'changeFacultyVotingStatus.html')

@login_required
def consultFacultyVoting(request):
    return render(request, 'consultFacultyVoting.html')

@login_required
def consultVotingListDean(request):
    return render(request, 'consultVotingListDean.html')

@login_required
def applyToCycleVoting(request):
    return render(request, 'applyToCycleVoting.html')

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
    return render(request, 'consultFacultyStudentList.html')