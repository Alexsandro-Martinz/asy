import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required
def dashboard(request):
    user = request.user

    if user.is_superuser:
        return redirect("dashboard_admin")

    return redirect("dashboard_profissional")
