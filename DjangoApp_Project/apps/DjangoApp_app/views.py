# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect 

def index(request):
	response = "This is my first response"
	return HttpResponse(response)

def new(request):
	response = "This is the new page"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def show(request, number):
	response = "This is a placeholder to display blog ", number
	return HttpResponse(response)

def edit(request, number):
	response = "placeholder to edit blog ", number
	return HttpResponse(response)

def destroy(request, number):
	return redirect('/')
# Create your views here.
