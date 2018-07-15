

from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_home),
    path('create/',views.post_create),
    path('detail/',views.post_detail),
    path('delete/',views.post_delete),
    path('update/',views.post_update),
]
