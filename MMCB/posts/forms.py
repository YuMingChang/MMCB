from django import forms
from django.forms.models import inlineformset_factory

from products.models import Product, Detail, Images
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Layout, Div, HTML, Fieldset, Field
from bootstrap3_datetime.widgets import DateTimePicker


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'notes',
            'date',
            'image',
            'is_display',
        ]
    def __init__(self, *args, submit_title=None, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('name', css_class="col-md-8"),
                Div('date', css_class="col-md-2"),
                Div('is_display', css_class="col-md-2"),
                css_class="row"
            ),
            Div(
                Div('notes', css_class="col-md-8"),
                Div(
                    Div(
                        HTML("""
                            {% if form.image.value %}
                            <img class="img-responsive" src="{{ MEDIA_URL }}{{ form.image.value }}">
                            {% endif %}
                        """, )
                    ),
                    Div('image'),
                    css_class="col-md-4"
                ),
                css_class='row'
            ),
            Div(
                Div(HTML("""

                <h4>商品內容圖片展示：</h4>
                <div class="ui tiny images">
                    {% for item in image_formset %}
                    {% if item.image.value %}
                    <img class="ui small image" src="{{ MEDIA_URL }}{{ item.image.value }}">
                    {% endif %}
                    {% endfor %}
                </div>
                <div class="ui divider"></div>
                """, )),
            )
        )
        if submit_title:
            self.helper.add_input(Submit('submit', submit_title))
            self.helper.add_input(Button(
                'delete', '移除商品',
                css_class='btn btn-danger', onclick='javascript:ProductDelete();'))


class DetailForm(forms.ModelForm):

    class Meta:
        model = Detail
        fields = [
            'product',
            'color',
            'size',
            'price',
            'stock',
            'sold',
            'total_sold',
        ]


BaseDetailFormSet = inlineformset_factory(
    parent_model=Product, model=Detail,
    fields=('color', 'size', 'price', 'stock', 'sold', 'total_sold', ), extra=0,
)


class DetailFormSet(BaseDetailFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.template = 'bootstrap/table_inline_formset.html'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Fieldset(
                Field('color', ),
                Field('size', ),
                Field('price', ),
                Field('stock', ),
                Field('sold', readonly=True),
                Field('total_sold', readonly=True),
            )
        )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = [
            'image',
        ]

BaseImagesFormSet = inlineformset_factory(
    parent_model=Product, model=Images,
    fields=('image', ), extra=4, max_num=4,
)


class ImageFormSet(BaseImagesFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.template = 'bootstrap3/table_inline_formset.html'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
