from django.urls import path 
from . import views

app_name = 'app' 
urlpatterns = [
    path('', views.logIn, name='logIn'),
    path('logIn/', views.logIn, name='logIn'),
    path('logout/', views.view_logout, name='view_logout'), 
    path('autenticar/', views.autenticar, name='autenticar'), 
    path('index/', views.index, name='index'),
    path('createStudent/', views.createStudent, name='createStudent'),
    path('addStudent/', views.addStudent, name="addStudent"),
    path('createCycleVoting/', views.createCycleVoting, name='createCycleVoting'),
    path('addCycleVoting/', views.addCycleVoting, name="addCycleVoting"),
    path('changeCycleVotingStatus/', views.changeCycleVotingStatus, name='changeCycleVotingStatus'),
    #path('nextStatus/', views.nextStatus, name="nextStatus"),
    path('consultCycleVoting/', views.consultCycleVoting, name='consultCycleVoting'),
    path('createFacultyVoting/', views.createFacultyVoting, name='createFacultyVoting'),
    path('addFacultyVoting/', views.addFacultyVoting, name="addFacultyVoting"),
    path('placeFacultyStudent/', views.placeFacultyStudent, name='placeFacultyStudent'),
    #path('placeStudent/', views.placeStudent, name="placeStudent"),
    path('changeFacultyVotingStatus/', views.changeFacultyVotingStatus, name='changeFacultyVotingStatus'),
    path('consultFacultyVoting/', views.consultFacultyVoting, name='consultFacultyVoting'),
    path('consultVotingListDean/', views.consultVotingListDean, name='consultVotingListDean'),
    #
    path('applyToCycleVoting/', views.applyToCycleVoting, name='applyToCycleVoting'),
    path('voteCycle/', views.voteCycle, name='voteCycle'),
    path('voteFaculty/', views.voteFaculty, name='voteFaculty'),
    path('consultVoteResults/', views.consultVoteResults, name='consultVoteResults'),
    path('consultMyVote/', views.consultMyVote, name='consultMyVote'),
    path('consultVotingListStudent/', views.consultVotingListStudent, name='consultVotingListStudent'),
    #
    path('consultFacultyStudentList/', views.consultFacultyStudentList, name='consultFacultyStudentList'),
    #
]
