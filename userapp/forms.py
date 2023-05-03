from django import forms
from buyurtma.models import Manzil


class ManzilForm(forms.ModelForm):
    class Meta:
        model = Manzil
        fields = "__all__"
