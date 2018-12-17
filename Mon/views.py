from django.shortcuts import render

def detail(request, question_id):
	return Httpresponse("You're looking at question %s." % question_id)
	
# Create your views here.
