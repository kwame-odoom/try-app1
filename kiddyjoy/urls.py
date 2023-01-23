from django.urls import path
from .views import index, upcoming_projects,ongoing_projects,past_projects,join_team, team,donate,contact, all_projects, about

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),
    path('join-team/', join_team, name='join-team'),
    path('donate/', donate, name='donate'),
    path('upcomimg-projects/',upcoming_projects, name='upcoming-projects'),
    path('all-projects/', all_projects, name='all-projects'),
    path('ongoing-projects/', ongoing_projects, name='ongoing-projects'),
    path('past-projects/', past_projects, name='past-projects')
]