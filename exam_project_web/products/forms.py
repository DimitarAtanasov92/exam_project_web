from django import forms

from exam_project_web.products.models import BayRequest


class BuyProductForm(forms.ModelForm):

    class Meta:
        model = BayRequest
        fields = ['email', "phone", "address"]
