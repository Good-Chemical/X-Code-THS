import imp
from xmlrpc.client import boolean
from django.shortcuts import render
from flask import Blueprint,render_template

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("SC.html",boolean=True)