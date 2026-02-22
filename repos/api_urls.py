from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.get_repos, name='api_repos'),
    path('<int:pk>/', api_views.get_repo, name='api_repo_detail'),
]
