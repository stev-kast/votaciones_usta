from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app_votaciones.models import Decano,Estudiante,Facultad

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logIn(request):
    return render(request, 'logIn.html')

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
        #estudiante = Estudiante.objects.get(id=usuario)
        decano = Decano.objects.get(id=usuario)

        #if(estudiante is not None):
        #    return HttpResponse("Es estudiante")
        if(decano is not None):
            return render(request, 'createStudent.html')
        # Redirecciona a una página de éxito
        return HttpResponse("Logged")
    else:
        # Retorna un mensaje de error de login no válido
        return HttpResponse(usuario)

def createStudent(request):
    return render(request, 'createStudent.html')

def createCycleVoting(request):
    return render(request, 'createCycleVoting.html')

def changeCycleVotingStatus(request):
    return render(request, 'changeCycleVotingStatus.html')

def consultCycleVoting(request):
    return render(request, 'consultCycleVoting.html')

def createFacultyVoting(request):
    return render(request, 'createFacultyVoting.html')

def placeFacultyStudent(request):
    return render(request, 'placeFacultyStudent.html')

def changeFacultyVotingStatus(request):
    return render(request, 'changeFacultyVotingStatus.html')

def consultFacultyVoting(request):
    return render(request, 'consultFacultyVoting.html')

def consultVotingListDean(request):
    return render(request, 'consultVotingListDean.html')

def applyToCycleVoting(request):
    return render(request, 'applyToCycleVoting.html')

def voteCycle(request):
    return render(request, 'voteCycle.html')

def voteFaculty(request):
    return render(request, 'voteFaculty.html')

def consultVoteResults(request):
    return render(request, 'consultVoteResults.html')

def consultMyVote(request):
    return render(request, 'consultMyVote.html')

def consultVotingListStudent(request):
    return render(request, 'consultVotingListStudent.html')

def consultFacultyStudentList(request):
    return render(request, 'consultFacultyStudentList.html')