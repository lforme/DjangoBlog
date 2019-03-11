from django.shortcuts import render, get_object_or_404
from .models import AboutmeInfo


def get_aboutme_info(request):
    my_obj = get_object_or_404(AboutmeInfo)

    contents = {'text': my_obj.text,
                'weibo': my_obj.weibo,
                'github': my_obj.github,
                'twitter': my_obj.twitter,
                }

    return render(request, 'blog/aboutme.html', {'info': contents})
