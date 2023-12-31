from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from exam_project_web.FashionForEveryone.forms import CommentForm
from exam_project_web.FashionForEveryone.models import News, Comment, Profile, HomeDescription


# Create your views here.


def home(request):
    description = HomeDescription.objects.all().first()
    context = {
        "description": description,
    }
    return render(request, 'FashionForEveryone/home.html', context=context)


class NewsListView(views.ListView):
    model = News
    template_name = 'FashionForEveryone/news.html'
    paginate_by = 3


class NewsDetailView(views.DetailView):
    model = News
    template_name = 'FashionForEveryone/news_detail.html'


def add_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = News.objects.get(id=pk)
            comment.to_user = Profile.objects.get(user=request.user)
            comment.save()
            return redirect('news')
    else:
        form = CommentForm()
    return render(request, 'FashionForEveryone/comments.html', {'form': form})


class AboutUsView(views.TemplateView):
    template_name = 'FashionForEveryone/about_us.html'


