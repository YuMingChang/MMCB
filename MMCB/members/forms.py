from django import forms
from django.forms.models import inlineformset_factory
from members.models import PersonalInfo, Addresses, Accounts, FamilyNumber
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = [
            'user',
            'name',
            'gender',
            'birthday',
            'phone',
            'email',
        ]
        widgets = {'user': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(PersonalInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('name', css_class="col-md-5"),
                Div('birthday', css_class="col-md-4"),
                Div('gender', css_class="col-md-3"),
                css_class='row'
            ),
            Div(
                Div('phone', css_class="col-md-6"),
                Div('email', css_class="col-md-6"),
                css_class='row'
            ),
        )
        self.helper.layout.append(Submit('save', '確定'))
# Layout Sample:
#   https://kuanyui.github.io/2015/04/13/django-crispy-inline-form-layout-with-bootstrap/


# AddressesFormSet
class AddressesForm(forms.ModelForm):
    address = forms.CharField(label='AddressesFC')

    class Meta:
        model = Addresses
        fields = [
            'address',
        ]
BaseAddressesFormSet = inlineformset_factory(
    parent_model=PersonalInfo, model=Addresses,
    fields=('address', ), extra=2, max_num=2,
)


class AddressesFormSet(BaseAddressesFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Div('address', )


# AccountsFormSet
class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = [
            'account',
        ]
BaseAccountsFormSet = inlineformset_factory(
    parent_model=PersonalInfo, model=Accounts,
    fields=('account', ), extra=2, max_num=2,
)


class AccountsFormSet(BaseAccountsFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Div('account', css_class="col-md-6")


# FamilyNumberFormSet
class FamilyNumberForm(forms.ModelForm):
    class Meta:
        model = FamilyNumber
        fields = [
            'number',
        ]
BaseFamilyNumberFormSet = inlineformset_factory(
    parent_model=PersonalInfo, model=FamilyNumber,
    fields=('number', ), extra=2, max_num=2,
)


class FamilyNumberFormSet(BaseFamilyNumberFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Div('number', css_class="col-md-6")
