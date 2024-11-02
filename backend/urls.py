from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from .views import medico_view, profile_view
from .views.admin_dashboad_view import dashboard_admin
from .views.contact_view import contato
from .views.dashboard_handle_view import dashboard
from .views.medico_dashboad_view import medico_dashboard

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='sobre'),
    path('contato/', contato, name='contato'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('dashboard/profissional/', medico_dashboard, name='dashboard_profissional'),
    path('dashboard/admin/', dashboard_admin, name='dashboard_admin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('medicos/', medico_view.medico_list, name='medico_list'),
    path('medicos/novo/', medico_view.medico_create, name='medico_create'),
    path('medicos/<int:pk>/editar/', medico_view.medico_update, name='medico_update'),
    path('medicos/<int:pk>/excluir/', medico_view.medico_delete, name='medico_delete'),
    path('profiles/new/', profile_view.profile_create, name='profile_create'),
    path('profiles/<int:pk>/edit/', profile_view.profile_update, name='profile_update'),
    path('profiles/', profile_view.profile_list, name='profile_list'),
    path('profiles/<int:pk>/delete/', profile_view.profile_delete, name='profile_delete')]
