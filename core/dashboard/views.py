from django.shortcuts import render
from django.views.generic import View, TemplateView
from accounts.models import UserType
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import RedirectView

class DashboardHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy("accounts:login")
        if self.request.user.type == UserType.customer.value:
            return reverse_lazy("dashboard:customer:home")
        if self.request.user.type == UserType.admin.value:
            return reverse_lazy("dashboard:admin:home")
        return reverse_lazy("accounts:login")  # fallback
    