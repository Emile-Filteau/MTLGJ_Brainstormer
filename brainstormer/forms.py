from django import forms


class AddIdeaForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
