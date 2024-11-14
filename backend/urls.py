from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from backend.views import medico_view, pacientes_view

from .views.admin_dashboad_view import dashboard_admin
from .views.contact_view import contato
from .views.dashboard_handle_view import dashboard

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='sobre'),
    path('contato/', contato, name='contato'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('dashboard/admin/', dashboard_admin, name='dashboard_admin'),
    path('dashboard/', dashboard, name='dashboard'),
    
    path('paciente/list/', pacientes_view.paciente_list, name='paciente_list'),
    path('paciente/create/', pacientes_view.paciente_create, name='paciente_create'),
    
    path('medico/list/', medico_view.medico_list, name='medico_list'),
    path('medico/create/', medico_view.medico_create, name='medico_create'),
 ]
