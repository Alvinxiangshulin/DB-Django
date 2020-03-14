from django.db import models

# Create your models here.
class Color(models.Model):
    color_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'Color'
        
    def __str__(self):
        return self.name
    
class State(models.Model):
    state_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'State'
    def __str__(self):
        return self.name

class Team(models.Model):
    team_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    wins = models.IntegerField()
    losses = models.IntegerField()
    class Meta:
        db_table = 'Team'
    def __str__(self):
        return self.name
    
class Player(models.Model):
    player_id = models.AutoField(primary_key = True)
    team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
    uniform_num = models.IntegerField(null =True)
    first_name =  models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    mpg = models.IntegerField()
    ppg = models.IntegerField()
    rpg = models.IntegerField()
    apg = models.IntegerField()
    spg = models.DecimalField(max_digits=4, decimal_places=1)
    bpg = models.DecimalField(max_digits=4, decimal_places=1)
    class Meta:
        db_table = 'Player'
    def __str__(self):
        return self.first_name + self.last_name
