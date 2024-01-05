from django.shortcuts import render
from django.http import HttpResponse
from .models import Userinputmodel
from .form import userform
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .form import signupform
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import Userser
#data retrival with the help of ORM query
@login_required
def test1(r):
    obj=Userinputmodel.objects.all()
    return render(r,'base.html',{'obj':obj})
# Create your views here.

def test(r):
    form=userform()
    if r.method=='POST':
        form=userform(r.POST)
        if form.is_valid():
            form.save()
            #print('Name:',obj.cleaned_data['name'])
            return HttpResponseRedirect('/first')
    return render(r,'base1.html',{"form":form})


def base(r):
    return render(r,'baseadv.html')

def logout(r):
    return render(r,'logout.html')
def Signup(r):
    form=signupform()
    if r.method=='POST':
        form=signupform(r.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/')
    return render(r,'signup.html',{'form':form})


def count_view(r):
    if 'count' in r.COOKIES:
        newcount=int(r.COOKIES['count'])+1
    else:
        newcount=1
    response=render(r,'count.html',{'count':newcount})
    response.set_cookie('count',newcount,max_age=60)
    return response

class Userview(APIView):   #for get method
    def get(self,r):

        userobj=Userinputmodel.objects.all()
        ser=Userser(userobj,many=True)
        return Response(ser.data)


    def post(self,r):
        serobj=Userser(data=r.data)
        if serobj.is_valid():
            serobj.save()
        return Response(serobj.data,status=status.HTTP_201_CREATED)
    


class FlightviewUpdateDelete(APIView):
    
    def put(self,r,id):
        obj=Userinputmodel.objects.get(id=id)
        serobj=Userser(obj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,r,id):
        obj=Userinputmodel.objects.get(id=id)
        obj.delete()
        return Response(status=status.HTTP_200_OK)

        
    def patch(self,r,id):
        obj=Userinputmodel.objects.get(id=id)
        serobj=Userser(obj,data=r.data,partial=True)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)

#now lets prepare for the orm queries


def updated(r,id):
    user=Userinputmodel.objects.get(id=id)
    if r.method=='POST':
        form=userform(r.POST,instance=user)
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect('/first')
    return render(r,'update.html',{'user':user})


def delete(r,id):
    user=Userinputmodel.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect('/first')