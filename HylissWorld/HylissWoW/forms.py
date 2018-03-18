from django import forms

class CharacterForm(forms.Form):
    pseudo = forms.CharField(max_length=100)
    serveur = forms.CharField(max_length=100)

    regions = (('eu', 'eu'), ('us', 'us'))
    locs_eu = (('fr_FR', 'fr_FR'), ('en_GB', 'en_GB',), ('de_DE', 'de_DE'), ('es_ES', 'es_ES'), ('it_IT', 'it_IT'), ('pl_PL', 'pl_PL'), ('pt_PT', 'pt_PT'), ('ru', 'ru_RU'))
    locs_us = (('en_US', 'en_US'), ('pt_BR', 'pt_BR',), ('es_MX', 'es_MX',))

    region = forms.ChoiceField(widget=forms.Select, choices=regions, initial = regions)
    local = forms.ChoiceField(widget=forms.Select, initial=locs_eu, choices = locs_eu+locs_us)

