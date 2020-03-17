from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import query1_form, query2_form,query3_form,query4_form,query5_form
from .models import Player, Team, Color, State
import os
# Create your views here.
def createColor(request):
    #create Color
    color_file = open('data/color.txt', "r")
    color_lines = color_file.readlines()
    for line in color_lines: 
       color_id, name =line.split(' ')
       addcolor(name = name[:-1])
    color_file.close()
    return HttpResponse("create Color success")

def createState(request):
    #create State 
    state_file = open('data/state.txt', "r")
    state_lines = state_file.readlines()
    for line in state_lines: 
       state_id, name =line.split(' ')
       addstate(name = name[:-1])
    state_file.close()
    return HttpResponse("create State success")

def createTeam(request):
    team_file = open('data/team.txt', "r")
    team_lines = team_file.readlines()
    for line in team_lines: 
       team_id, name, state_id, color_id, wins, losses =line.split(' ')
       addteam(name = name, state_id = state_id, color_id = color_id, wins = wins , losses = losses[:-1])
    team_file.close()
    return HttpResponse("create Color success")

def createPlayer(request):
    player_file = open('data/player.txt', "r")
    player_lines = player_file.readlines()
    for line in player_lines: 
       player_id, team_id, uniform_num, first_name, last_name, mpg, ppg, rpg, apg, spg, bpg =line.split(' ')
       addplayer(team_id = team_id, uniform_num = uniform_num, first_name = first_name, last_name = last_name, mpg = mpg, ppg = ppg, rpg = rpg, apg = apg, spg = spg, bpg = bpg[:-1])
    player_file.close()
    return HttpResponse("create Player success") 

def addcolor(name):
    color = Color.objects.create(name = name)
    color.save()
    return

def addstate(name):
    state = State.objects.create(name = name)
    state.save()
    return

def addteam(name, state_id, color_id, wins, losses):
    team = Team.objects.create(name = name, state_id = State.objects.get(state_id = state_id), color_id = Color.objects.get(color_id = color_id), wins = wins,losses = losses)
    team.save()
    return

def addplayer(team_id, uniform_num, first_name, last_name, mpg, ppg, rpg, apg, spg, bpg):
    player = Player.objects.create(team_id = Team.objects.get(team_id = team_id), uniform_num = uniform_num, first_name = first_name, last_name = last_name, mpg = mpg, ppg = ppg, rpg = rpg, apg = apg, spg = spg, bpg = bpg)
    player.save()
    return 

def query1(request):
    #players = query1_func(0, 35, 40, 1, 1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if request.method == "POST":
        form = query1_form(request.POST)
#        print("post")
        if form.is_valid():
 #           print("isvalid")
            #form = query1_form()    
            use_mpg = form.cleaned_data['use_mpg']
            min_mpg = form.cleaned_data['min_mpg']
            max_mpg = form.cleaned_data['max_mpg']
            use_ppg = form.cleaned_data['use_ppg']
            min_ppg = form.cleaned_data['min_ppg']
            max_ppg = form.cleaned_data['max_ppg']
            use_rpg = form.cleaned_data['use_rpg']
            min_rpg = form.cleaned_data['min_rpg']
            max_rpg = form.cleaned_data['max_rpg']
            use_apg = form.cleaned_data['use_apg']
            min_apg = form.cleaned_data['min_apg']
            max_apg = form.cleaned_data['max_apg']
            use_spg = form.cleaned_data['use_spg']
            min_spg = form.cleaned_data['min_spg']
            max_spg = form.cleaned_data['max_spg']
            use_bpg = form.cleaned_data['use_bpg']
            min_bpg = form.cleaned_data['min_bpg']
            max_bpg = form.cleaned_data['max_bpg']
            players = query1_func(use_mpg, min_mpg, max_mpg, use_ppg, min_ppg,max_ppg, use_rpg, min_rpg, max_rpg, use_apg, min_apg, max_apg, use_spg, min_spg, max_spg, use_bpg, min_bpg, max_bpg)
  #          print(players)
            context = {
                "players":  players
            }
            return render(request,'player_list.html', context=context)
    else:
        form = query1_form()
    
    return render(request, 'query1_form.html', {'form':query1_form})
   

def query1_func(use_mpg, min_mpg, max_mpg,use_ppg, min_ppg, max_ppg,use_rpg, min_rpg, max_rpg,use_apg, min_apg,  max_apg,use_spg, min_spg,  max_spg,use_bpg, min_bpg,  max_bpg):
    players = Player.objects.all()
    if use_mpg:
        players = players.filter(mpg__lte = max_mpg).filter(mpg__gte = min_mpg)
    if use_ppg:
        players = players.filter(ppg__lte = max_ppg).filter(ppg__gte = min_ppg)
    if use_rpg:
        players = players.filter(rpg__lte = max_rpg).filter(rpg__gte = min_rpg)
    if use_apg:
        players = players.filter(apg__lte = max_apg).filter(apg__gte = min_apg)
    if use_spg:
        players = players.filter(spg__lte = max_spg).filter(spg__gte = min_spg)
    if use_bpg:
        players = players.filter(bpg__lte = max_bpg).filter(bpg__gte = min_bpg)
    #print(players)
    return players

def query2(request):
    #query2 = query2_func("Red")
    if request.method == "POST":
        form = query2_form(request.POST)
        if form.is_valid():            
            team_color = form.cleaned_data['team_color']
            query2 = query2_func(team_color)
            context = {
                "query2":  query2
            }
            return render(request,'query2_list.html', context=context)
        else:
            form = query2_form()
    
    return render(request, 'query2_form.html', {'form':query2_form})

def query2_func(name):
    teams = Team.objects.all()
    teams  = teams.filter(color_id__name = name)
    return teams

def query3(request):
    # query3 = query3_func("Duke")
    if request.method == "POST":
        form = query3_form(request.POST)
        if form.is_valid():   
            team_name = form.cleaned_data['team_name']
            query3 = query3_func(team_name)
            context = {
                "query3":  query3
            }
            return render(request,'query3_list.html', context=context)
        else:
            form = query3_form()
    
    return render(request, 'query3_form.html', {'form':query3_form})
    

def query3_func(team_name):
    players = Player.objects.all()
    players = players.filter(team_id__name = team_name).order_by('-ppg')
    return players

def query4(request):
    #query4 = query4_func("NC","DarkBlue")
    if request.method == "POST":
        form = query4_form(request.POST)
        if form.is_valid():
            
            team_state = form.cleaned_data['team_state']
            team_color = form.cleaned_data['team_color']
            query4 = query4_func(team_state,team_color)
            context = {
                "query4":  query4
            }
            return render(request,'query4_list.html', context=context)
        else:
            form = query4_form()
    
    return render(request, 'query4_form.html', {'form':query4_form})
    

def query4_func(team_state, team_color):
    players = Player.objects.all()
    players = players.filter(team_id__state_id__name = team_state).filter(team_id__color_id__name = team_color)
    return players


def query5(request):
    #query5 = query5_func(10)
    if request.method == "POST":
        form = query5_form(request.POST)
        if form.is_valid():
            print("isvalid")
            num_wins = form.cleaned_data['num_wins']
            query5 = query5_func(num_wins)
            context = {
                "query5":  query5
            }
            return render(request,'query5_list.html', context=context)
        else:
            form = query5_form()
    
    return render(request, 'query5_form.html', {'form':query5_form})
    

def query5_func(num_wins):
    players = Player.objects.all()
    players = players.filter(team_id__wins__gt = num_wins)
    return players
