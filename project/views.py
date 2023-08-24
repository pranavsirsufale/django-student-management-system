# Views.py
# I have created this file - Pranav
from django.http import HttpResponse
from django.shortcuts import render,redirect
import qrcode
from django.contrib.auth import authenticate,logout,login
from app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user !=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request,''' Email or Password is wrong !
                                           please enter valid Credential ''')
                return redirect('login')
        else:
            messages.error(request, ''' Email or Password is wrong !
                                                       please enter valid Credential ''')
            return redirect('login')




# profile edits
@login_required(login_url="/")
def PROFILE(request):
    user = CustomUser.objects.get( id = request.user.id)

    context = {
        'user':user
    }
    return render(request,'profile.html',context)

@login_required(login_url="/")
def PROFILE_UPDATE(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            # print(profile_pic)
            if profile_pic != None and profile_pic != '':
                customuser.profile_pic = profile_pic
            if password != None and password != '':
                customuser.set_password(password)
            customuser.save()
            messages.success(request,'Your Profile Updated successfully !')
            redirect('profile')


        except:
            messages.error(request, ' Failed to update Your profile !')

    return render(request,'profile.html')


# user logout
def LogOut(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    # get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    textcaptal = request.GET.get('captaltext','off')

    if removepunc =='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

    elif textcaptal == "on":
        capital = ""
        for char in djtext:
            capital = djtext.upper()
        params = {'purpose':'make capitalize', 'analyzed_text':capital}
    else:
        analyzed = djtext
    return render(request, 'analyze.html', params)








def qrredire(request):
    return render(request,'qrmaker.html')


def qrmaker(request):


    link = request.GET.get('link')
    object_name = request.GET.get('object_name')
    created_qr = qrcode.make(f"{link}")
    created_qr.save(f"media/profile_pic/{object_name}.png")
    print('saved ')
    print(object_name)
    param = {'object':object_name}
    return render(request,'qrmaker.html',param)
    # return HttpResponse(f'''
    # qr created successfully
    #
    #  {{% load static %}}
    #     <img src="{{% static 'images/{object_name}.png' %}}">
    #
    #
    #
    #
    # ''')


def showqr(request,):
    if request.method == 'POST':
        name = request.POST.get('object_name')
        imname = (f"{name}.png")
        link = request.POST.get('link')
        created_qr = qrcode.make('link')
        created_qr.save(f"media/profile_pic/{name}.png")
        print('saved ')


        try:
            pass

            # if


        except:
            messages.error(request, ' Failed to Create qr')

    return render(request, 'showqr.html')




# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")


# Get the text

"""
djtext = request.GET.get('text', 'default')

# Check checkbox values
removepunc = request.GET.get('removepunc', 'off')
fullcaps = request.GET.get('fullcaps', 'off')
newlineremover = request.GET.get('newlineremover', 'off')
extraspaceremover = request.GET.get('extraspaceremover', 'off')

# Check which checkbox is on
if removepunc == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
    params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

else:
    return HttpResponse("Error")

"""