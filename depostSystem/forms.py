from django import forms

class DepositForm(forms.Form):
    typeList = (
        ('current', "活期"),
        ('regular', "定期"),
        ('fix', "定活期"),
    )
    timeList = (
        ('')
    )

    cardPassword = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    money = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    types = forms.CharField(choices=typeList)
    time = forms.CharField(choices=timeList)


#获取银行卡列表
class SearchForm(forms.Form):
    national_id = forms.CharField(max_length=18)


#开户
class AddUserForm(forms.Form):
    SEX = (
        "男",
        "女",
    )
    NATION = (
        "汉族",
        "壮族",
        "藏族",
        "满族",
        "蒙古族",
        "回族",
        "藏族",
        "维吾尔族",
        "苗族",
        "彝族",
        "布依族",
        "侗族",
        "瑶族",
        "白族"
    )
    name = forms.CharField(
        label='姓名',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入姓名'}),
        error_messages={"required": "该字段不能为空", 'invalid': "请填入正确的身份证号!"},
        max_length=100
    )
    sex = forms.CharField(
        label='性别',
        category=forms.ModelChoiceField(queryset=SEX, empty_label=''),
        default='男'
    )
    birth = forms.DateField(
        label='出生年月',
        error_messages={"required": "该字段不能为空"}
    )
    nation = forms.CharField(
        label='民族',
        max_length=20,
        category=forms.ModelChoiceField(queryset=NATION, empty_label=''),
        default='汉族'
        # widget = forms.Select(choices=NATION),
    )
    client_national_id = forms.IntegerField(
        label='身份证号',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入身份证号'}),
        error_messages={"required": "该字段不能为空", 'invalid': "请填入正确的身份证号"}
    )
    address = forms.CharField(
        label='籍贯',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入籍贯'}),
        error_messages={"required": "该字段不能为空"},
        max_length=256
    )
    home_address = forms.CharField(
        label='详细住址',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入详细住址'}),
        error_messages={"required": "该字段不能为空"},
        max_length=128
    )
    phone = forms.IntegerField(
        label='手机号',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入手机号'}),
        error_messages={"required": "该字段不能为空", 'invalid': "请填入正确的手机号"}
    )
    open_address = forms.CharField(
        label='开户地',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入开户地'}),
        error_messages={"required": "该字段不能为空"},
        max_length=256
    )
    open_bank = forms.CharField(
        label='开户银行',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入开户银行'}),
        max_length=128
    )
    email = forms.EmailField(
        label='邮箱号',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱号'}),
        error_messages={"required": "该字段不能为空", 'invalid': "请填入正确的邮箱号"},
        max_length=128
    )


class ChangeInformation(forms.Form):
    phone = forms.IntegerField(
        max_length=11
    )



