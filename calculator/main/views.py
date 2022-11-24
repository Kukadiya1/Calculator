from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    try:
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        print(num1,num2)
        final=int(num1)+int(num2)
    except:
        return render(request, 'val.html', {'val': 'Addition Page', 'path': 'add/'})
    return render(request,'val.html',{'val':'Addition Page','path':'add/','result':f'Result = {final}'})
def sub(request):
    try:
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        print(num1,num2)
        final=int(num1)-int(num2)
    except:
        return render(request, 'val.html', {'val': 'Subtraction Page', 'path': 'sub/'})
    return render(request,'val.html',{'val':'Subtraction Page','path':'sub/','result':f'Result = {final}'})
def div(request):
    try:
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        print(num1,num2)
        final=int(num1)/int(num2)
    except:
        return render(request, 'val.html', {'val': 'Divison Page', 'path': 'div/'})
    return render(request,'val.html',{'val':'Divison Page','path':'div/','result':f'Result = {final}'})
def mul(request):
    try:
        num1 = request.GET['num1']
        num2 = request.GET['num2']
        print(num1, num2)
        final = int(num1) * int(num2)
    except:
        return render(request, 'val.html', {'val': 'Multiplication Page', 'path': 'mul/'})
    return render(request, 'val.html', {'val': 'Multiplication Page', 'path': 'mul/', 'result': f'Result = {final}'})


