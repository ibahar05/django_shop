from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import ContactForm, NewsLetterForm
from django.http import JsonResponse


class IndexView(TemplateView):
    template_name = "website/index.html"


class AboutView(TemplateView):
    template_name = "website/about.html"


class ContactView(TemplateView):
    template_name = "website/contact.html"

class ContactUsFormView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "پیام شما ارسال شد"})
        return JsonResponse({"success": False, "errors": form.errors}, status=400)
    

class NewsLetterFormView(View):
    def post(self, request):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "پیام شما ارسال شد"})
        return JsonResponse({"success": False, "errors": form.errors}, status=400)




