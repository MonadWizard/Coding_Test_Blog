from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Posts, Tags
from .forms import NewTagsForm , NewPostForm
# Create your views here.

def createPost(request):
    posts = Posts.objects.all()
    tags = Tags.objects.all()
    post_form = NewPostForm(request.POST or None)
    tag_form = NewTagsForm(request.POST or None)

    if post_form.is_valid():
        if request.method == 'POST':
            tag_data = (request.POST.get('tags')).split(',')
            tag_data = list(map(int, tag_data))
            title = post_form.cleaned_data['title']
            detail = post_form.cleaned_data['detail']

            posts_add = Posts.objects.create(
                title = title,
                detail = detail,
            )
            for x in tag_data:
                posts_add.tags.add(Tags.objects.get(id=x))

        # post_form.save()
        return HttpResponseRedirect(request.path_info)

    if tag_form.is_valid():
        tag_form.save()
        return HttpResponseRedirect(request.path_info)

    context = {'post_form': post_form,'tags': tags}
    template = 'pages/create_blog.html'
    return render(request, template, context)



def updatePost(request):

    context = {}
    template = 'pages/update_blog.html'
    return render(request, template, context)

