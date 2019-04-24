from django.contrib import admin
from django.urls import path
from bst.views import *
from search.views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bst/',BinarySearchTreeView),
    path('sort/',SortingView),
    path('', TemplateView.as_view(template_name='bst/home.html'))
]
