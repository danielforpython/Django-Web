from django import forms

class RegisterForms(forms.Form):
    TOPIC_CHOICES = (
        ('leve1', '好评'),
        ('leve2', '中评'),
        ('leve3', 'cha评'),
    )
    GENDER = (
        ('NAN'),
        ('NV'),
    )

    user_name = forms.CharField(min_length=4,max_length=12,label="用户名",initial="name yourself a cute name"
                                ,widget=forms.TextInput(attrs={'class':'custom-forms'}))
    password = forms.CharField(min_length=4,max_length=12
                               ,widget=forms.PasswordInput(attrs={'class':'custom-forms'}))
    age = forms.IntegerField(min_value=18,max_value=150
                             ,widget=forms.NumberInput(attrs={'class':'custom-forms'}))   #attrs一般只写属性或id，字典形式
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'custom-forms'}))
    phone = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'custom-forms'}))
    gender = forms.CheckboxInput(check_test=GENDER)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'custom-forms'}))
    # cc_myself = forms.BooleanField(required=False,label='订阅该贴')
    # topic=forms.ChoiceField(choices=TOPIC_CHOICES,label='评分')
    # date = forms.DateField()
    # datetime=forms.DateTimeField()
    introdue = forms.CharField(widget= forms.Textarea(attrs={'class':'custom-forms'}))
    xingbie=forms.CheckboxSelectMultiple(choices=TOPIC_CHOICES)
