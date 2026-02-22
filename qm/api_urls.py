from django.urls import path
from . import api_views

urlpatterns = [
    path('analytics/', api_views.get_analytics, name='api_analytics'),
    path('analytics/<int:pk>/', api_views.get_analytic, name='api_analytic_detail'),
    path('categories/', api_views.get_categories, name='api_categories'),
    path('categories/<int:pk>/', api_views.get_category, name='api_category_detail'),
    path('tactics/', api_views.get_tactics, name='api_tactics'),
    path('tactics/<int:pk>/', api_views.get_tactic, name='api_tactic_detail'),
    path('techniques/', api_views.get_techniques, name='api_techniques'),
    path('techniques/<int:pk>/', api_views.get_technique, name='api_technique_detail'),
    path('campaigns/', api_views.get_campaigns, name='api_campaigns'),
    path('campaigns/<int:pk>/', api_views.get_campaign_detail, name='api_campaign_detail'),
    path('snapshots/', api_views.get_snapshots, name='api_snapshots'),
    path('snapshots/<int:pk>/', api_views.get_snapshot_detail, name='api_snapshot_detail'),
]
