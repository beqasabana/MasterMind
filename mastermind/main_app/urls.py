from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('play', views.play),
    path('play/<int:code_length>/<int:duplicates>/<int:range_start>/<int:range_end>/<int:tries>', views.play),
    path('check', views.check),
    path('victory', views.victory),
    path('lost', views.lost),
    path('customize', views.customize_display),
    path('customize/play', views.customize_play),
    path('giveHint', views.give_hint)
]