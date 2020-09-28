from django.urls import path
from .views import Words4View, Words6View, RankView

urlpatterns = [
    path('word4/', Words4View.as_view()),
    path('word6/', Words6View.as_view()),
    path('word/rankcheck', RankView.as_view())
]
