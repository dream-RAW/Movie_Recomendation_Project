from django import forms

class FeedbakcForm(forms.Form):
    rating = forms.IntegerField(label='your rating', )
    review = forms.CharField(widget=forms.Textarea,label='Your review comment',)
