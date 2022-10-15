import imp
from xmlrpc.client import boolean
from django.shortcuts import render
from flask import Blueprint, render_template

auth=Blueprint('auth',__name__)