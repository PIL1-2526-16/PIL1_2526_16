from django import forms


class MessageForm(forms.Form):
    contenu = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Écrire un message...',
            'class': 'message-input',
        }),
        max_length=5000,
        label=''
    )