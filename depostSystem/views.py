from django.contrib.auth import authenticate, login
from django.http import HttpResponse, Http404
from django.shortcuts import render
from forms import SearchForm, AddUserForm, ChangeInformation
from django.contrib import messages, auth


# Create your views here.
from .models import Card
from .models import Client

CARD = 'card_id'
CLIENT = 'client_national_id'


#管理首页
def index(request):
    return render(request, 'index.html')


#管理员登录
def operator_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user_obj = authenticate(username=username, password=password)
    if user_obj:
        login(request, user_obj)


#银行卡查询
def card(request):
    if request.method == 'POST':
        client_national_id = request.POST["client_national_id"]
        form = SearchForm(request.POST)

        if form.is_valid():
            userobj = Client.objects.filter(client_national_id=client_national_id)
            if userobj.client_national_id == client_national_id:
                request.session[CLIENT] = client_national_id

                filter_dict = dict()
                filter_dict['client_national_id'] = client_national_id
                filter_dict['is_loss'] = False

                obj = Card.objects.filter(**filter_dict)

                return render(request, 'card.html', {'userobj':userobj, 'obj': obj})
            else:
                messages.add_message(request, messages.ERROR, "用户不存在")
            messages.add_message(request, messages.ERROR, "用户不存在")
        else:
            messages.add_message(request, messages.ERROR, "身份证格式错误")
    return render(request, 'index.html')


# 用户开户
def client_open(request):
    if request.method == 'POST':

        form = AddUserForm(request.POST)
        if form.is_valid():
            obj, created = Client.objects.get_or_create(
                name=request.POST["name"],
                sex=request.POST["sex"],
                birth=request.POST["birth"],
                nation=request.POST["nation"],
                client_national_id=request.POST["client_national_id"],
                address=request.POST["address"],
                home_address=request.POST["home_address"],
                phone=request.POST["phone"],
                open_address=request.POST["open_address"],
                open_bank=request.POST["open_bank"],
                email=request.POST["email"],
                is_cancel=False
            )
            if created is True:
                messages.add_message(request, messages.success, '开户成功')
            else:
                messages.add_message(request, messages.warning, '用户已存在')
    return render(request, 'openning.html')


# 银行卡信息(首页)
def card_index(request):
    if request.method == 'POST':
        request.session[CARD]=request.POST[CARD]
        messages.add_message(request, messages.success, '查看详情')
        return render(request, 'cardInformation.html')
    return render(request, 'card.html')


#挂失
def report_loss(request):
    if request.method == 'POST':
        card_id = request.session[CARD]
        Card.objects.filter(card_id=card_id).update(is_loss=True)
        messages.add_message(request, messages.success, '挂失成功')
        return render(request, 'loss.html')
    return render(request, 'card.html')


#修改信息
def information_change(request):
    if request.method == 'POST':
        card_id = request.session[CARD]
        form = ChangeInformation(request.POST)
        if form.is_valid():
            obj=Card.objects.filter(card_id=card_id)
            return render(request, 'informationChange.html', {'obj': obj})
    return render(request, 'cardInformation.html')


