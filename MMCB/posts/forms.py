from django import forms
from django.forms.models import inlineformset_factory

from products.models import Product, Detail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from bootstrap3_datetime.widgets import DateTimePicker

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Test: It test for DatePicker but no idea how to work.
        date = forms.DateField(
            widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
        fields = [
            'name',
            'notes',
            'raiser',
            'date',
            'image',
            'is_display',
        ]

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
    parent_model=Product, model=Detail, fields=('color', 'size', 'price'), extra=0,
)
class DetailFormSet(BaseDetailFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.template = 'bootstrap/table_inline_formset.html'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
