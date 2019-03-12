from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Contact
from .forms import ContactForm
from blog.views import IndexView


def post_contacts(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            return HttpResponseRedirect('postsucceed')
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})


def get_post_succeed(request):
    return render(request, 'blog/postsucceed.html')


def goback_home(request):
    return HttpResponseRedirect('postsucceed')

