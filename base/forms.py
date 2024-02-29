from django import forms
from .models import  Permission

class PermissionForm(forms.ModelForm):
    empty_permitted =True
    class Meta:
        model = Permission
        fields = [
            'reason',
            'imageReason',
            'documentReason'
        ]
        widgets = {
            "reason": forms.Textarea(
                attrs={
                    
                        "class": "textarea",
                })
        }
    
    
