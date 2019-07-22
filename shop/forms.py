from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(label='الإسم', widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"أكتب اسمك هنا ...",
        }
    ))
    email    = forms.EmailField(label='البريد الالكتروني', widget=forms.EmailInput(
        attrs={
            "class":"form-control",
            "placeholder":"البريد الالكتروني",
            "label":"البريد الالكتروني"
        }
    ))
    content  = forms.CharField(label='رسالتك', widget=forms.Textarea(
        attrs={
            "class":"form-control",
            "placeholder":"أكتب رسالتك هنا...",
            "label":"الرسالة",
        }
    ))