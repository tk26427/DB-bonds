from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Book ,BookUser  , Trade , Security,  Counterparty
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import  AuthenticationForm , UserCreationForm



class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


def main(request) :
    

    '''

    try:
        tag=request.GET['status']
    except:
        tag = None

    if tag == None :
        try:
            tag2=request.GET['type']
        except:
            tag2 = None

        if tag2 == None :

            try:
                tag3=request.GET['price']
            except:
                tag3 = None

            if tag3 == None :


                rest =Security.objects.all()
                

                return render(request, 'front/restaurant-found2.html' , { 'rests' : rest})
            else:
                study2=[]

                for q in  Security.objects.all():
                    if q.FaceValue >= int(tag3)-200 and q.FaceValue <= int(tag3) +200 :
                        study2.append(q)

        else:
            study2=[]
            print(tag2)

            for q in  Security.objects.all():
                print(q.sector , tag2)
                if str(q.type) == tag2:
                    study2.append(q)

    else :
        study2=[]
        print(tag)

        for q in  Restaurant.objects.all():
            if q.name.lower().startswith(tag.lower()):
                study2.append(q)
    
    if len(study2)==0:
        return render(request, 'front/notfound.html' , {}) '''
    rest =Security.objects.all()

    return render(request, 'bond/main.html' , { 'rests' : rest})



def sign(request):

    if request.method == 'GET':
        form1 = AuthenticationForm()
        form2 = UserCreationForm()
        return render(request, 'bond/sign.html', {'form1' : form1 , 'form2' : form2 })

    if request.method == 'POST':

        if request.POST['action'] == 'login':
        	form1 = AuthenticationForm(request=request, data=request.POST)
        	form2 = UserCreationForm()
        	if form1.is_valid():
        	    username = form1.cleaned_data.get('username')
        	    password = form1.cleaned_data.get('password')
        	    user = authenticate(username=username, password=password)
        	    if user is not None:
        	        login(request, user)
        	        return redirect('mainpage')
        	    else:
        	        form1.error_messages['nouser']= _('No such user found')
        	        raise forms.ValidationError(
        	        form1.error_messages['nouser'],
        	        code='nouser',)
        	        return render(request, 'bond/sign.html', {'form1' : form1 , 'form2' : form2 })
        	else:
        	    
        	    return render(request, 'bond/sign.html', {'form1' : form1 , 'form2' : form2 }) 


        if request.POST['action'] == 'signup':
        	form1 = AuthenticationForm()
        	form2 = UserCreationForm(request.POST)
        	if form2.is_valid():
        	    form2.save()
        	    return redirect('signpage')

        	else:
        	    return render(request, 'bond/sign.html', {'form1' : form1 , 'form2' : form2 }) 

def security(request) :
    try:
        ids=request.GET['id']
        rest = Security.objects.filter(id = ids)[0]
    except:
        return HttpResponse('<h1>No such restaurant found </h1>')
            
    


    return render(request, 'bond/security-detail.html' , {'rest' : rest})

def trademain(request) :
    

    '''

    try:
        tag=request.GET['status']
    except:
        tag = None

    if tag == None :
        try:
            tag2=request.GET['type']
        except:
            tag2 = None

        if tag2 == None :

            try:
                tag3=request.GET['price']
            except:
                tag3 = None

            if tag3 == None :


                rest =Security.objects.all()
                

                return render(request, 'front/restaurant-found2.html' , { 'rests' : rest})
            else:
                study2=[]

                for q in  Security.objects.all():
                    if q.FaceValue >= int(tag3)-200 and q.FaceValue <= int(tag3) +200 :
                        study2.append(q)

        else:
            study2=[]
            print(tag2)

            for q in  Security.objects.all():
                print(q.sector , tag2)
                if str(q.type) == tag2:
                    study2.append(q)

    else :
        study2=[]
        print(tag)

        for q in  Restaurant.objects.all():
            if q.name.lower().startswith(tag.lower()):
                study2.append(q)
    
    if len(study2)==0:
        return render(request, 'front/notfound.html' , {}) '''
    rest =Trade.objects.all()

    return render(request, 'bond/trademain.html' , { 'rests' : rest})



def trade(request) :
    try:
        ids=request.GET['id']
        rest = Trade.objects.filter(id = ids)[0]
    except:
        return HttpResponse('<h1>No such restaurant found </h1>')
            
    


    return render(request, 'bond/trade-detail.html' , {'rest' : rest})




@login_required
def logout_view(request):
    logout(request)
    return redirect('signpage')


def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def about(request):

    


    return render(request, 'bond/about-us.html' , {})
