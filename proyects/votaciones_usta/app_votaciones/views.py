from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logIn(request):
    return render(request, 'logIn.html')

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