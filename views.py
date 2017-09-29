from .forms import MemberForm
from .models import Member
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.http import urlquote_plus

def member_list(request):
    members = Member.objects.all()
    context = {
        "title": "Our Team | AMG",
        "breadcrumb":"Home",
        "members":members,
    }
    return render(request,"AMGTeam.html",context)

#Displays the full post
def member_detail(request,slug):
    instance = get_object_or_404(Nominee,slug=slug)
    context = {
        "title": instance.name + ' | ' + instance.position,
        "name": instance.name,
        "instance":instance
    }
    return render(request,"AMGTeam.html",context)
