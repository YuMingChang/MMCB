from django import forms
from django.forms.models import inlineformset_factory

from products.models import Product, Detail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'notes',
            'raiser',
            'date',
            'image',
            'is_display',
        ]
        date = forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            )
        )

    def __init__(self, *args, submit_title='Submit', **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        if submit_title:
            self.helper.add_input(Submit('submit', submit_title))
        self.helper.add_input(Button('delete', '移除商品', css_class='btn btn-danger', onclick='javascript:ProductDelete();'))


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = [
            'product',
            'color',
            'size',
            'price',
        ]

BaseDetailFormSet = inlineformset_factory(
    parent_model=Product, model=Detail, fields=('color', 'size', 'price'), extra=1,
)
class DetailFormSet(BaseDetailFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
