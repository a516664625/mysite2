# -*-coding:utf-8-*- 
# 作者：   51666 
# 当前系统日期时间：2019/11/19，10:21
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

POST_FORM = '''<form method='post' action="/login">
    姓名:<input type="text" name="username">
    <input type='submit' value='登陆'>
</form>'''


def sum_view(request):
    if request.method == 'GET':
        try:
            start = request.GET.get('start')
            step = request.GET.get('step')
            stop = request.GET.get('stop')
            if not stop:
                return HttpResponse('pppp')
            html = '结果%s' % (sum(range(int(start), int(stop), int(step))))
            return HttpResponse(html)
        except Exception as e:
            print(e)
            return HttpResponse("pap")
    return HttpResponse('pleser giveme a method')


def login(request):
    if request.method == 'GET':
        # 给页面
        return HttpResponse(POST_FORM)
    elif request.method == 'POST':
        # 用户提交了数据
        # 处理用户数据
        username = request.POST.get('username', 'abcde')
        # return HttpResponse("欢迎:%s"%username)
        print(username)
        return HttpResponseRedirect('/index',username)


def index(request,username):
    return HttpResponse('欢迎%s'%username)


def test_html(request):
    # 加载模板
    # t=loader.get_template('test_html.html')
    # #将t转换成 HTML 字符串
    # html=t.render()
    # return HttpResponse(html)
    username = 'GHI'
    dic = {}
    dic['username'] = username
    dic['int'] = 8
    dic['lst'] = ['北京', '上海', '天津']
    dic['dict'] = {'age': 18}
    dic['sayhi'] = sayhi
    dic['person'] = Person()
    # Django模板层自动对传进来的变量进行转义[防范xss攻击]
    dic['script'] = '<script>alert(11)</script>'

    return render(request, 'test_html.html', dic)


def sayhi():
    return 'hi body'


class Person:
    def sayhi(self):
        return 'hi body'


def test_if(request):
    val = 10
    dic = {'val': val}
    return render(request, 'test_if.html', dic)


def mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        n1 = request.POST.get('x')
        if not n1:
            return HttpResponse('please give me a num ')
        n1 = float(n1)
        op = request.POST.get('op')
        n2 = request.POST.get('y')
        if not n2:
            return HttpResponse('please give me a num ')
        n2 = float(n2)
        if op == 'add':
            result = n1 + n2
        elif op == 'sub':
            result = n1 - n2
        elif op == 'mul':
            result = n1 * n2
        elif op == 'div':
            result = n1 / n2
        dic = {}
        dic['n1'] = n1
        dic['n2'] = n2
        dic['op'] = op
        dic['re'] = result
        return render(request, 'mycal.html', dic)
def test_for(request):
    lst=['北京','上海','天津']

    return render(request,'test_for.html',locals())
# def index(rquest):
#     return render(rquest, 'index.html')
def sports_index(request):

    return render(request, 'sports.html',locals())
def music_index(request):
    return render(request, 'music.html')


