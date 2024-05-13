from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from .forms import SignUpForm,Loginform
from django.contrib.auth.forms import UserCreationForm
import requests
import datetime
@login_required(login_url='LOGIN')


def home(request):
    #return HttpResponse("HEY,this is my django project")
   
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = 'Trivandrum'     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4bf10470594b27bb2fe4700d28b3d93d'
    PARAMS = {'units':'metric'}

    API_KEY =  'AIzaSyDbA-qVDj3I6EOOSKmkvVYkJV54IBtfXUw'

    SEARCH_ENGINE_ID = 'b63d37fe6ce884c28'
     
    query = city + " 1920x1080" # image size
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    

    try:
          
          data = requests.get(url,params=PARAMS).json()


          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occurred':False,'image_url':image_url})
    
    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          # city = 'indore'
          # data = requests.get(url,params=PARAMS).json()
          
          # description = data['weather'][0]['description']
          # icon = data['weather'][0]['icon']
          # temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day,'city':'Trivandrum','exception_occurred':exception_occurred})
    
    
def SignupPage(request):
    if request.method=='POST':
        Username=request.POST.get('username')
        Email=request.POST.get('email')
        Password1=request.POST.get('password1')
        Password2=request.POST.get('password2')

        if Password1!=Password2:
            return HttpResponse("Password and Confirm password are not same!!!!")
        else:
            my_user=User.objects.create_user(Username,Email,Password1)
            my_user.save()
            #return HttpResponse("User Account has been created Successfully")
            return redirect('LOGIN')
            # print(Username,Email,Password1,Password2)    
    return render(request,'SignUp.html')


def LoginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=uname,password=password1)
        if user is not None:
            login(request,user)
            return redirect('HOME')
            # print(uname,password1)
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request,'Login.html') 


def LogoutPage(request):
    logout(request)
    return redirect('LOGIN')

  
    