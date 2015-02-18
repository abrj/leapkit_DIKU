from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView

from queries.forms import ContactForm

from queries.models import FAQuestion

class HomepageView(TemplateView):
    template_name = "index.html"


class AboutLeapkitView(TemplateView):
    template_name = "about.html"

class ProjectPricingView(TemplateView):
    template_name = "pricing.html"

class FAQView(ListView):
    model = FAQuestion
    template_name = "FAQ.html"

class TermsOfUsageView(TemplateView):
    template_name = "terms_of_usage.html"

class ContactLeapkitView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "success"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        messages.add_message(self.request, messages.SUCCESS,
                             "Your query has been registered, We will get back to you shortly",
                             extra_tags="alert-success")
        return super(ContactLeapkitView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "There was a problem with the information provided",
                             extra_tags="alert-danger")

        return super(ContactLeapkitView, self).form_invalid(form)


def contact_success_redirect(request):
    return redirect(reverse("contact_leapkit"))


"""
Custom error handling views
"""


class PageNotFoundView(TemplateView):
    template_name = "errors/404.html"


class ErrorView(TemplateView):
    template_name = "errors/500.html"


class PermissionDeniedView(TemplateView):
    template_name = "errors/403.html"


class BadRequestView(TemplateView):
    template_name = "errors/400.html"


