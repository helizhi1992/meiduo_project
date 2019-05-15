from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class RegisterView(View):

    def get(self, request):
        '''
        定义一个接口,返回注册页面
        :param request:
        :return:
        '''
        return render(request, 'register.html')

def eat(request):

    return HttpResponse( 'niaho')
