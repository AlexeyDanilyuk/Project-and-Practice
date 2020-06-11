from django import forms
from mainapp.models import Account, Currency, Regions


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""


class RegionsForm(forms.ModelForm):
    class Meta:
        model = Regions
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
