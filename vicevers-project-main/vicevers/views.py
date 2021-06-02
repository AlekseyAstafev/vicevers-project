from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	reverse_text = user_text[::-1]
	original_text = len(user_text.split())
	print(original_text)
	return render(request, 'reverse.html', {'usertext': user_text, 'reversetext': reverse_text, 'originaltext': original_text})
