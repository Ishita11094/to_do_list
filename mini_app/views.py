from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
import urllib.request
from .models import TodoModel
from .forms import TodoForm
from django.contrib.auth import authenticate , login as loginUser , logout

def home(request):
	if request.user.is_authenticated:
		return render(request,"home.html")
	else:
		return redirect("main")

def about_us(request):
	if request.user.is_authenticated:
		return render(request,"about_us.html")
	else:
		return redirect("main")

def weather(request):
	if request.user.is_authenticated:
		if request.GET.get("city"):
			try:
				city=request.GET.get("city")
				a1=" "
				a2=" " + city
				a3=" "
				wa=a1+a2+a3
				res=requests.get(wa)
				data=res.json()
				city_weather = {
					'temp':data['main']['temp'],
					'desc':data['weather'][0]['description'],
					'icon':data['weather'][0]['icon'],
				}
				print(data)
				context = {'msg' : city_weather}
				return render(request, "weather.html", context)
			except Exception:
				return render(request, "weather.html",{"msg":"city name not found"})
		return render(request,"weather.html")
	else:
		return redirect("main")


def news(request):
	src = "the-hindu"
	try:
		a1 = " "
		a2 = " " + src
		a3 = " "
		wa = a1 + a2 + a3
		res = requests.get(wa)
		data = res.json()
		info = data['articles']
		return render(request,"news.html",{"msg":info,"src":src})
	except Exception as e:
		return render(request,"news.html",{"msg":e})
	return render(request,"news.html")

def createtask(request):
	if request.user.is_authenticated:
		user = request.user
		print(user)
		if request.method == "POST":
			f = TodoForm(request.POST)
			if f.is_valid():
				todo = f.save(commit=False)
				todo.user = user
				todo.save()
				fm = TodoForm()
				return render(request,"createtask.html",{"fm":fm,"msg":'Task added'})
			else:
				return render(request,"createtask.html",{"fm":f,"msg":'Error in adding task'})
		else:
			fm = TodoForm()
			return render(request,"createtask.html",{"fm":fm})
	else:
		return redirect("main")

def to_do(request):
	if request.user.is_authenticated:
		data = TodoModel.objects.filter(user=request.user)
		return render(request,"to_do.html",{"data":data})
	else:
		return redirect("main")

def delete(request,t):
	ds = TodoModel.objects.get(task=t)
	ds.delete()
	return redirect("to_do")






