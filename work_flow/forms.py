from django import forms
from .models import Ele_Overview, Detial

class OverviewForm(forms.ModelForm):
    class Meta:
        model = Ele_Overview
        fields = ['name', 'number', 'material', 'flag']
        labels = {'name': '名称', 'number': '数量', 'material': '材质', 'flag': '是否完成'}



class WorkStepForm(forms.ModelForm):
    class Meta:
        model = Detial
        fields = ['name', 'price', 'flag']
        labels = {'name': '工序名称', 'price': '计件价格', 'flag': '是否完成'}