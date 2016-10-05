from django import forms
from members.models import PersonalInfo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', '確定'))
