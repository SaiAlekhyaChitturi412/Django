from .import views
from django.urls import URLPattern, path

urlpatterns =[
    path('index_view',views.index,name='index'),
    path('simple_view',views.simple_view,name='simpleView')
]