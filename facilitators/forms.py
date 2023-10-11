# from django import forms
# from facilitators.models import get_message

# class RepliesForm(forms.Form):
#      reply = forms.CharField(widget=forms.Textarea)
     
#      class Meta:
#           model = get_message
#           fields = ['reply']

from django import forms
from facilitators.models import FacilitatorReply

class RepliesForm(forms.ModelForm):
    class Meta:
        model = FacilitatorReply
        fields = ['reply']
        widgets = {
            'reply': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }