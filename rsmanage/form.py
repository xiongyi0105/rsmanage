from django import forms
from rsmanage.models import RFConfig


class ResourceEdit(forms.Form):
    which_to_edit = forms.CharField(widget=forms.RadioSelect(choices=[(0, "port"), (1, "password"), (2, "rsa")]),
                                    label="选择需要批量修改的选项:")
    edit_rsa = forms.CharField(widget=forms.Textarea, label="rsa:")
    edit_passwd = forms.CharField(widget=forms.PasswordInput, label="password:")
    edit_port = forms.CharField(max_length=5, label="port:")


class RFConfigChangeView(forms.ModelForm):
    class Meta:
        model = RFConfig
        fields = ['orchestrator_name', 'json_info']

        widgets = {
            'json_info': forms.Textarea(attrs={
                'style': 'height: 500px;width:500px'}),
        }
