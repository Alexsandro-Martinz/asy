from django.shortcuts import redirect


def dashboard(request):
    """View rendering the dashboard for the user type."""

    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('dashboard_admin')
        else:
            return redirect('dashboard_profissional')
    else:
        return redirect('login')

