from django.shortcuts import render
from betask.models import *
import re


def index(request):
	if request.method == "POST":
		username = request.POST.get('username')
		name = request.POST.get('name')
		email = request.POST.get('email')
		pswd = request.POST.get('pswd')
		pswd_rep = request.POST.get('pswd-rep')

		#checking uniqueness of username
		if(betask.objects.filter(username=username).first() is not None):
			return render(request, 'signup.html', {"message":"User already exists with that username!!! Please enter different username."})
		data = betask.objects.filter(username=username).first()
		user=betask(username=username, name=name, email=email, passwd=pswd, conf_passwd=pswd_rep)
		user.save()
		return render(request, 'home.html')
	return render(request, 'signup.html')

def login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		pswd = request.POST.get('pswd')
		data = betask.objects.filter(username=username,passwd=pswd).first()
		if data is not None:
			return render(request, 'home.html')
		return render(request, 'signup.html', {"message":"Invalid credentials!!! If you are not a registered user please register."})
	return render(request, 'login.html')

def home(request):
	if request.method == "POST":
		string = request.POST.get('input')
		choice = request.POST.get('choice')
		if choice == 'ext_num':
			pattern = re.compile(r'(\d*)')
			result = pattern.findall(string)
			return render(request, 'home.html', {"message":result})
		elif choice == 'ext_date':
			pattern = re.compile(r'\d{4}[/-]\d{1,2}[/-]\d{1,2}')
			result = pattern.findall(string)
			return render(request, 'home.html', {"message":result})
		elif choice == 'ext_string':
			pattern = re.compile(r"('.+')*")
			result = pattern.findall(string)
			return render(request, 'home.html', {"message":result})
		elif choice == 'val_email':
			pattern = re.compile(r'(\D\w*([\.-]?\w+)@\w+([\.-]?\w+)*.(com|cc|org}))')
			result = pattern.search(string)
			if result is None:
				return render(request, 'home.html', {"message2":'The entered Email Address is Invalid!!!'})
			return render(request, 'home.html', {"message2":'The entered Email Address is Valid.'})
		elif choice == 'val_ip':
			case=""
			for i in string:
				if i!=".":
					case+=i;
					if case>="0" and case<="127":
						cls="A"
					elif case>="128" and case<="191":
						cls="B"
					elif case>="192" and case<="233":
						cls="C"
					else:
						pass
				else:
					break;

			pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
			result = pattern.search(string)
			if result is None:
				return render(request, 'home.html', {"message2":'The entered IP Address is Invalid!!!'})
			return render(request, 'home.html', {"message2":'The entered IP Address is Valid. It belongs to Class '+cls})
		elif choice == 'val_mac':
			pattern = re.compile(r'(([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2})')
			result = pattern.search(string)
			if result is None:
				return render(request, 'home.html', {"message2":'The entered MAC Address is Invalid!!!'})
			return render(request, 'home.html', {"message2":'The entered MAC Address is Valid.'})
		else:
			pattern = re.compile(r'([A-Z][^A-Z]+)')
			result = pattern.findall(string)
			stn=""
			for i in result:
				stn=stn+i.lower()+"_"
			stn=stn[0:len(stn)-1]
			return render(request, 'home.html', {"message2":stn})
	return render(request, 'home.html')
