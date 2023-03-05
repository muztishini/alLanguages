from django.urls import path, include

# from word.views import QueryListView, QueryDetailView, WordListView, QueryCreateView, update_progress

'''urlpatterns = [
    path('create/', QueryCreateView.as_view(), name='query-create'),
    path('queries/', QueryListView.as_view(), name='query-list'),
    path('query/<pk>/', QueryDetailView.as_view(), name='query-detail'),
    path('query/<pk>/words/', WordListView.as_view(), name='word-list'),

    path('progress', update_progress),
]'''

from rest_framework.routers import DefaultRouter
from word.views import WordViewSet, QueryList, Translates, update_progress

router = DefaultRouter()
router.register(r'', WordViewSet, basename='words')


urlpatterns = [
    path('w/progress/', update_progress),
    path('translates/<pk>/', Translates.as_view(), name='translates'),
    path('query/', QueryList.as_view(), name='queries'),
    path('', include(router.urls))
]
