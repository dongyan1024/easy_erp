from django import forms
from .models import Inventory, Element

class TypeForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['inventory_type']
        labels = {'inventory_type': '添加合适的类别，如抽油泵零件、数控刀具等'}

class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['name', 'number', 'material']
        labels = {'name': '零件名称', 'number': '零件数量', 'material': '零件材质'}