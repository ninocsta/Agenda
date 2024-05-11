from django.contrib import admin
from django.urls import path
from agenda import views
from accounts import views as accounts_views
from django.urls import include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('ajax/load-funcoes', views.load_funcoes_servicos_profissional, name='ajax_load_funcoes'),
    path('ajax/load-dados', views.load_funcoes_dados_servicos, name='ajax_load_dados'),
    path('all_events/', views.all_events, name='all_events'),
    path('all_resources/', views.all_resources, name='all_resources'), 
    path('add_event/', views.add_event, name='add_event'), 
    path('update/', views.update, name='update'),
    path('move/', views.move, name='move'),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),    
]
