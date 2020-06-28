from django import forms
from judapp.models import JudSite


class JudSiteForm(forms.ModelForm):
    class Meta:
        model = JudSite
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
