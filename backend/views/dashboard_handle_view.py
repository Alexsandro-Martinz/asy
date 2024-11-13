from django.shortcuts import redirect, render


def dashboard(request):
    """View rendering the dashboard for the user type."""
    user = request.user

    if user.is_authenticated:
        if user.is_superuser:
            return redirect('dashboard_admin')
        else:
            return redirect('dashboard_profissional')
    else:
        return redirect('login')