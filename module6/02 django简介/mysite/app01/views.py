from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def favicon(request):
    return render(request,'favicon.ico')

def regist(request):
    return render(request,'register.html')

def timer(request):
    import datetime
    ctime = datetime.datetime.now()
    return render(request,'timer.html',{"time":ctime})

def special_case_2019(request):
    return HttpResponse('special_case_2019')

def year_archive(request,year):
    print(year)
    return HttpResponse('special_case_%s'%year)

def month_archive(request,year,month):
    print(year,month)
    return HttpResponse('special_case_%s_%s'%(year,month))

def day_archive(request,year,month,day):
    print(year,month,day)
    return HttpResponse('special_case_%s_%s_%s'%(year,month,day))