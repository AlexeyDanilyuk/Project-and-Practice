from django import forms
from userapp.models import WorkUser


class WorkUserForm(forms.ModelForm):
    class Meta:
        model = WorkUser
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
