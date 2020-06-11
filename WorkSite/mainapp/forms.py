from django import forms
from mainapp.models import Arm


class ArmForm(forms.ModelForm):
    class Meta:
        model = Arm
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
