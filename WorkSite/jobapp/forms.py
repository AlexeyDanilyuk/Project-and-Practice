from django import forms
from jobapp.models import JobTitle


class JobTitleForm(forms.ModelForm):
    class Meta:
        model = JobTitle
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
