from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page_view(request):
    return render(request,'SpritleApp/home.html')
def logout_view(request):
    return render(request,'SpritleApp/logout.html')
from SpritleApp.forms import SignUpForm
from django.http import HttpResponseRedirect
def signup_view(request):
    formobj=SignUpForm()
    if request.method=="POST":
        formobj=SignUpForm(request.POST)
        user=formobj.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'SpritleApp/signup.html', {'formobj':formobj})


@login_required
#  1 st Method
def Caluculation(reqeust):
    result='';
    try:
        if reqeust.method == 'POST':
            n1 = int(reqeust.POST.get('num1'))
            n2 = int(reqeust.POST.get('num2'))
            opr = reqeust.POST.get('opr')
            if opr == '+':
                result= n1+n2;
            elif opr == '-':
                result=n1-n2;
            elif opr == '*':
                result=n1*n2;
            elif opr == '/':
                result=int(n1/n2);
    except:
      resut= "Invalid opration.."

    return render(reqeust,'SpritleApp/student.html',{'result':result}) ;


#  2 nd method
#def Caluculation(reqeust):
#    return render(reqeust,'SPRITLEApp/form.html') ;
def Add(reqeust):
    num1 = int(reqeust.GET['num1'])
    num2 = int(reqeust.GET['num2'])
    res= num1+num2
    return render(reqeust,'SpritleApp/result.html',{'result': res});

def Subfraction(reqeust):
    num1 = int(reqeust.GET['num1'])
    num2 = int(reqeust.GET['num2'])
    res= num1-num2
    return render(reqeust,'SpritleApp/result.html',{'result': res});

def Multplication(reqeust):
    num1 = int(reqeust.GET['num1'])
    num2 = int(reqeust.GET['num2'])
    res= num1*num2
    return render(reqeust,'SpritleApp/result.html',{'result': res});

def Division(reqeust):
    num1 = int(reqeust.GET['num1'])
    num2 = int(reqeust.GET['num2'])
    res= int(num1/num2)
    return render(reqeust,'SpritleApp/result.html',{'result': res});


