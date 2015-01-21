from django import forms


class AddIdeaForm(forms.Form):
    name = forms.CharField(required=True)