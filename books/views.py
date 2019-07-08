from datetime import date

from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from books.forms import RegisterForms
from books.models import BookInfo, PersonInfo, NewsInfo, AreaInfo


def shirley(request):
    return render(request, 'Shirley.html')

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')

class IndexForms(View):
    def get(self,request):
        forms = RegisterForms()
        context = {
            'forms':forms
        }
        return render(request, 'register.html', context=context)

    def post(self,request):
        post_data = RegisterForms(request.POST)

        if post_data.is_valid():  #验证通过，才会有clean data
            user_name = post_data.cleaned_data.get('user_name')
            password = post_data.cleaned_data['password']

            context = {
                'user_name': user_name,
                'password':password,
            }

            return render(request,'homepage.html',context=context)

        else:
            return HttpResponse('<h1>no pass</h1>')



def base(request):
    return render(request,'base.html')

def book_list(request):
    bl=BookInfo.objects.all()
    context ={
        'bl':bl
    }
    return render(request,'book_list.html',context=context)

def person_list(request):
    pl=PersonInfo.objects.all()
    context ={
        'pl':pl
    }
    return render(request,'person_list.html',context=context)

def q_duixiang(request):
    q_list = BookInfo.objects.filter(Q(bread__gt=20) | Q(bcomment__gt=50))
    context ={
        'q':q_list
    }
    return render(request,'q_duixiang.html',context=context)


def f_duixiang(request):    #如果是两个属性比较，可以通过F对象进行
    f_list = BookInfo.objects.filter(bread__gt=F('bcomment'))
    context ={
        'f':f_list
    }
    return render(request,'f_duixiang.html',context=context)

# 由一到多查询：一类模型类对象名.小写多类模型类类名_set.查询函数()
# 通过对象查询分成2步，先查到某本图书，再通过该图书对象查询该图书中的人物对象
# 实例演练： 查询id为1的图书中，所有人物的信息
def query_mutitable(request):
    book = BookInfo.objects.get(id=1)
    persons = book.personinfo_set.all()

    result = ''
    for p in persons:
        result += str(p.id) + ", " + p.pname + ", " + str(p.pgender) \
               + ", " + p.pcomment + ", " + str(p.fbook_id)
        result += '<br>'
        # result2 += str(p.id)+","+p.pname+","+str(p.pgender)+\
        #            ","+p.pcomment+","+str(p.fbook_id)

    return HttpResponse(result)

# 语法格式：模型类名.objects.raw('SQL语句', params=None, translations=None)
def raw_sql(request):
    book = BookInfo.objects.raw('select * from books_bookinfo where id>2')
    context = {
        'books':book
    }
    return render(request,'raw_sql.html',context=context)

def raw_sql_m_m(request):   #注意当输入查询字段的时候，不要漏了主键(id)，否则会出错：InvalidQuery: Raw query must include the primary key
    news = NewsInfo.objects.raw('''select n.`id`, n.`ntitle`,n.`ncontent`,t.`tname`
                                    from books_newsinfo n,books_typeinfo t,books_newsinfo_typeinfo nt
                                    where n.`id`=nt.`newsinfo_id` and t.`id`=nt.`typeinfo_id` order by n.`id`;''')
    context = {
        'context':news
    }
    return render(request,'raw_sql_m_m.html',context=context)


def self_table(request):
    prov = AreaInfo.objects.get(pk=210000)  #'QuerySet' object has no attribute 'areainfo_set' 所以不可以用filter，只可以用get
    city = prov.areainfo_set.all()

    cities={
        'cities':city
    }
    return render(request,'self_table.html',context=cities)


def cud_c(request):
    book = BookInfo()
    book.btitle = '天龙八部'
    book.bpub_date = date.today()
    book.save()

    return redirect('book_list',permanent=True)


def cud_u(request):
    book = BookInfo.objects.get(btitle__exact='西游记')
    book.isDelete= True
    book.save()

    return redirect('book_list', permanent=True)

def area_list(request):
    areas=AreaInfo.objects.all()
    context ={
        'areas':areas
    }
    return render(request,'area_list.html',context=context)

def view_request(request):

    path = request.path
    method = request.method
    GET = request.GET
    host = request.headers
    scheme = request.scheme
    cookies = request.COOKIES
    body = request.body
    reslover = request.resolver_match

    contexts={
        'path':path,
        'method':method,
        'GET':GET,
        'host':host,
        'scheme':scheme,
        'cookies':cookies,
        'body':body,
        'reslover':request
    }

    return render(request,'view_request.html',context=contexts)

def cookie(request):

    ret = ''
    if 'ck1' in request.COOKIES:
        ret = request.COOKIES.get('ck1')
        num = request.COOKIES.get('num')


        num = int(num)
        num = num + 1
        num = str(num)

        ret += num

        res = HttpResponse('Welcome old Timer: ' + ret + 'log in for:   ' + num + 'times')
        res.set_cookie('ck1',ret)
        res.set_cookie('num',num)

        # res = HttpResponse('Welcome old Timer: ' + ret + '  log in for: ' + num + 'times')
        return res
    else:
        res = HttpResponse('First Time Log In, Welcome')
        res.set_cookie('ck1','zhang3')
        res.set_cookie('num',0)
        return res


def sessionrequest(request):

    s1 = request.session.get('s1','')
    request.session['s1'] = 'li4'

    return HttpResponse('session; ' + s1)

def glowing(request):
    return render(request,'Glowing Border.html')

def responsive(request):
    return render(request,'Responsive.html')

def galley(request):
    return render(request,'gallery.html')

