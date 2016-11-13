from django import forms
from django.forms.models import inlineformset_factory

from products.models import Product, Item, Images
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Layout, Div, HTML, Fieldset, Field


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'name',
            'notes',
            'onshelf_time',
            'image',
            'is_display',
            'freight_only',
        ]
    def __init__(self, *args, submit_title=None, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('name', css_class="col-md-6"),
                Div('onshelf_time', css_class="col-md-2"),
                Div('is_display', css_class="col-md-2"),
                Div('freight_only', css_class="col-md-2"),
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
            self.helper.add_input(Button(
                'delete', '歸零全選/全取消',
                css_class='btn', onclick='javascript:ResetAllItem();'))


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'product',
            'style',
            'size',
            'price',
            'pre_order',
            'selling',
            'selling_volume',
            'reset_time',
            'is_reset',
            'is_shortage',
        ]


BaseItemFormSet = inlineformset_factory(
    parent_model=Product, model=Item,
    fields=(
        'style',
        'size',
        'price',
        'pre_order',
        'selling',
        'selling_volume',
        'reset_time',
        'is_reset',
        'is_shortage',
    ), extra=0,
)


class ItemFormSet(BaseItemFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.template = 'bootstrap/table_inline_formset.html'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Fieldset(
                Field('style', ),
                Field('size', ),
                Field('price', ),
                Field('pre_order', readonly=True),
                Field('selling', readonly=True),
                Field('selling_volume', readonly=True),
                Field('reset_time', readonly=True),
                Field('is_reset', ),
                Field('is_shortage', ),
            )
        )


class ImagesForm(forms.ModelForm):
    image = forms.ImageField(label='Images')

    class Meta:
        model = Images
        fields = [
            'image',
        ]

BaseImagesFormSet = inlineformset_factory(
    parent_model=Product, model=Images,
    fields=('image', ), extra=4, max_num=4,
)


class ImagesFormSet(BaseImagesFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.template = 'bootstrap3/table_inline_formset.html'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
