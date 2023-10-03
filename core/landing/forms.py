from django import forms

from .models import *

class RequestCallForm(forms.ModelForm):
  services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), required=False,
                                               widget=forms.CheckboxSelectMultiple)
  day = forms.ModelChoiceField(queryset=CallDayRequest.objects.all(), required=True, initial=0)
  time = forms.ModelChoiceField(queryset=CallTimeRequest.objects.all(), required=True, initial=0)
  way = forms.ModelChoiceField(queryset=CallWayRequest.objects.all(), required=True, initial=0)

  def __init__(self, *args, **kwargs):
    super(RequestCallForm, self).__init__(*args, **kwargs)
    self.fields['day'].label = "День"
    self.fields['time'].label = "Время"
    self.fields['way'].label = "Способ связи"
    self.fields['contact'].widget.attrs['placeholder'] = "Номер телефона/Почта"

  class Meta:
    model = CallRequest
    exclude = ['status',]
    # fields = "__all__"
