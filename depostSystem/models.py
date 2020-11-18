from django.db import models


class Client(models.Model):

    '''用户表'''

    SEX = (
        ('m', 'male'),
        ('f', 'female'),
    )

    national_id = models.IntegerField(unique=True, verbose_name='身份证号')

    name = models.CharField(max_length=128)

    sex = models.CharField(max_length=32, choices=SEX, default='male')

    phone = models.IntegerField()

    email = models.CharField(max_length=128)

    home_adress = models.CharField(max_length=128)

    # TODO 这是什么？
    nation = models.CharField(max_length=20)

    # TODO 这是什么？
    open_adress = models.CharField(max_length=256)

    # TODO 这是什么？
    open_bank = models.CharField(max_length=128)

    # TODO 重复？
    adress = models.CharField(max_length=256)

    birth = models.DateField()

    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name

    class Meta:

        ordering = ['c_time']


# TODO 待讨论
class Admin(models.Model):

    '''管理员表'''

    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.id

    class Meta:

        ordering = ['c_time']


class Card(models.Model):

    '''银行卡表'''

    card_id = models.CharField(max_length=128, unique=True, db_index=True)

    password = models.CharField(max_length=256)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    phone = models.IntegerField()

    # 开户地址
    open_adress = models.CharField(max_length=256)

    # 开户银行
    open_bank = models.CharField(max_length=128)

    c_time = models.DateTimeField(auto_now_add=True)

    is_loss = models.BooleanField(default=False)

    def __str__(self):

        return self.card_id

    class Meta:

        ordering = ['c_time']




class Service(models.Model):

    '''服务表'''

    TYPE = (
        ('c', 'current'),   # 定期
        ('f', 'fixed'),     # 活期
    )

    saving_type = models.CharField(max_length=20, choices=TYPE, default='current')

    rate = models.IntegerField()

    # TODO 这啥？
    term = models.CharField(max_length=128)

    def __str__(self):

        return self.id


class Banlance(models.Model):

    '''余额表'''

    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    amount = models.IntegerField(default=0)

    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.id

    class Meta:

        ordering = ['c_time']
