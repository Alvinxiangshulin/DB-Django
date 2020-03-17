from django import forms


class query1_form(forms.Form):
    use_mpg = forms.IntegerField(label = 'use_mpg')
    min_mpg = forms.IntegerField(label = 'min_mpg')
    max_mpg = forms.IntegerField(label = 'max_mpg')
    use_ppg = forms.IntegerField(label = 'use_ppg')
    min_ppg = forms.IntegerField(label = 'min_ppg')
    max_ppg = forms.IntegerField(label = 'max_ppg')
    use_rpg = forms.IntegerField(label = 'use_rpg')
    min_rpg = forms.IntegerField(label = 'min_rpg')
    max_rpg = forms.IntegerField(label = 'max_rpg')
    use_apg = forms.IntegerField(label = 'use_apg')
    min_apg = forms.IntegerField(label = 'min_apg')
    max_apg = forms.IntegerField(label = 'max_apg')
    use_spg = forms.IntegerField(label = 'use_spg')
    min_spg = forms.FloatField(label = 'min_spg')
    max_spg = forms.FloatField(label = 'max_spg')
    use_bpg = forms.IntegerField(label = 'use_bpg')
    min_bpg = forms.FloatField(label = 'min_bpg')
    max_bpg = forms.FloatField(label = 'max_bpg')

class query2_form(forms.Form):
    team_color = forms.CharField(label = 'team_color',required=False)

class query3_form(forms.Form):
    team_name = forms.CharField(label = 'team_name',required=False)

class query4_form(forms.Form):
    team_state = forms.CharField(label = 'team_state',required=False)
    team_color = forms.CharField(label = 'team_color',required=False)

class query5_form(forms.Form):
    num_wins = forms.IntegerField(label = 'num_wins')
