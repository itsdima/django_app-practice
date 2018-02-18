# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def users(request):
	return HttpResponse('placeholder to display all users')

def register(request):
	return HttpResponse('placeholder to add a new user')

def login(request):
	return HttpResponse('placeholder for users to login')



# Create your views here.
