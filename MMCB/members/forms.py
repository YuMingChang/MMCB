from django import forms
from members.models import PersonalInfo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from bootstrap3_datetime.widgets import DateTimePicker


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        birthday = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
        fields = [
            'user',
            'name',
            'sexual',
            'birthday',
            'phone',
            'email',
            'address',
            'accounts',
        ]
        widgets = {'user': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div('name', css_class="col-md-5"),
                Div('birthday', css_class="col-md-4"),
                Div('sexual', css_class="col-md-3"),
                css_class='row'
            ),
            Div(
                Div('phone', css_class="col-md-6"),
                Div('email', css_class="col-md-6"),
                css_class='row'
            ),
            Div(
                Div('address', css_class="col-md-9"),
                Div('accounts', css_class="col-md-3"),
                css_class='row'
            ),
        )
        self.helper.layout.append(Submit('save', '確定'))
# Layout Sample:
#   https://kuanyui.github.io/2015/04/13/django-crispy-inline-form-layout-with-bootstrap/
