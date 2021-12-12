from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from to_do_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange

def sign_up(request):
	if request.method == "POST":
		fn = request.POST.get("fn")
		ln = request.POST.get("ln")  
		un = request.POST.get("un")
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username=un)
			return render(request,"sign_up.html",{"msg":"Username already registered"})
		except User.DoesNotExist:
			try:
				usr = User.objects.get(email=em)
				return render(request,"sign_up.html",{"msg":"email already registered"})
			except User.DoesNotExist:		
				pw = ""
				text = "123456789"
				for i in range(6):
					pw = pw + text[randrange(len(text))]
				print(pw)
				msg = "Your password is " + pw
				send_mail("Welcome to Ishita's project", msg, EMAIL_HOST_USER, [str(em)])
				usr = User.objects.create_user(username=un, password=pw, email=em, first_name=fn, last_name=ln)
				usr.save()
				return redirect("user_login")
	else:
		return render(request,"sign_up.html")

def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
		if usr is None:
			return render(request,"user_login.html",{"msg":"Login denied"})
		else:
			login(request,usr)
			return redirect("home")
	else:
		return render(request,"user_login.html")

def user_logout(request):
	logout(request)
	return redirect("main")

def main(request):
	return render(request,"main.html")

def forgot_pass(request):
	if request.method=="POST" :
		un = request.POST.get("un")
		em = request.POST.get("em")
		try:
			usr = User.objects.get(username=un) and User.objects.get(email=em)
			pw = ""
			text = "123456789"
			for i in range(6):
				pw = pw + text[randrange(len(text))]
			print(pw)
			msg = "Your new password is " + pw
			send_mail("Hello!! Welcome to Ishita's project",msg,EMAIL_HOST_USER,[str(em)])
			usr.set_password(pw)
			usr.save()
			return redirect("user_login")
		except User.DoesNotExist:
			return render(request,"forgot_pass.html",{"msg":"Invalid Information"})

	else:
		return render(request,'forgot_pass.html')

