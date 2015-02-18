from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.datetime_safe import date
from django.views.generic import DetailView, ListView, UpdateView, CreateView, FormView, TemplateView
from django.contrib import messages

from braces.views import LoginRequiredMixin, FormMessagesMixin

from institutions.models import Course
from queries.models import FAQuestion, UserQuestion
from queries.forms import ContactForm

from models import Company, CompanyProject, ProjectPackage
from projects.models import Project
from forms import CompanyProjectForm, BuyProjectsForm, CompanyCreationForm, CompanyForm, CompanyLogInForm, \
    ChangeUserPassword


class CompanyView(LoginRequiredMixin, UpdateView):
    """
    This view is used to display the company profile.
    It contains the data of both the user of the type "COM" and the company profile.
    It also collects all the projects the user has created.

    If the user is not logged in, he will be redirected to the login page
    """
    template_name = "company_profile.html"
    login_url = "/companies/login/"
    model = Company

    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        try:
            request.session['profile_views'] += 1
        except:
            request.session['profile_views'] = 0

        # call the view
        return super(CompanyView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['profile'] = Company.objects.get(user=self.request.user)
        context['project_list'] = CompanyProject.objects.get_own_projects(self.request.user.company)
        context['published_projects'] = CompanyProject.objects.get_own_published_queryset(self.request.user.company)

        return context


class UpdateCompanyView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    """
    This view is used to update the company profile.
    This should be changed to be done inline, but for the moment, a separate view is used.
    It uses a custom form, which is created via the Crispy forms plugin
    When the profile is updated, the user is redirected back to the home page
    """
    template_name = "update_company_profile.html"
    login_url = "/companies/login/"
    model = Company
    form_class = CompanyForm
    form_invalid_message = "Please correct the field(s) indicated with red"

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Your profile was updated!", extra_tags="alert-success")
        return redirect(reverse("companies:profile", args=(self.object.slug, )))

    def form_invalid(self, form):

        messages.add_message(self.request,
                             messages.ERROR,
                             "Please correct the field(s) indicated with red",
                             extra_tags="alert-error")
        return super(UpdateCompanyView, self).form_invalid(form)


class HandBookView(LoginRequiredMixin, ListView):
    """
    This view is used to see all the courses that are in direct contact with leapkit

    If the user is not logged in, he will be redirected to the login page
    """
    template_name = "general_guideline.html"
    login_url = "/companies/login/"
    model = Course


class CompanyProjectCreationView(LoginRequiredMixin, CreateView):
    template_name = "company_project_creation_view.html"
    login_url = "/companies/login/"
    model = CompanyProject
    form_class = CompanyProjectForm

    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        try:
            request.session['create_project_views'] += 1
        except:
            request.session['create_project_views'] = 0

        # call the view
        return super(CompanyProjectCreationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        project = form.save(commit=False)
        project.project_owner = self.request.user.company

        message = ""
        if '_publish' in self.request.POST:
            project.published = True
            message = "The project has been updated"
        if '_save' in self.request.POST:
            project.published = False
            message = "The draft has been updated"

        messages.add_message(self.request, messages.SUCCESS, message, extra_tags="alert-success")
        project.save()
        form.save_m2m()
        return redirect(reverse("companies:profile", args=(self.request.user.company.slug, )))

    def form_invalid(self, form):
        messages.add_message(self.request,
                             messages.ERROR,
                             "Please correct the field(s) indicated with red",
                             extra_tags="alert-error")
        return super(CompanyProjectCreationView, self).form_invalid(form)


class CompanyProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "company_project_detail_view.html"
    login_url = "/companies/login/"
    model = Project

    def get_queryset(self):
        project = Project.objects.filter(slug=self.kwargs['slug'])
        return project


class CompanyProjectListView(LoginRequiredMixin, ListView):
    template_name = "company_project_list_view.html"
    login_url = "/companies/login/"
    model = CompanyProject

    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        try:
            request.session['all_projects_views'] += 1
        except:
            request.session['all_projects_views'] = 0

        # call the view
        return super(CompanyProjectListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        project_list = CompanyProject.objects.get_own_published_queryset(self.request.user.company)
        return project_list

    def get_context_data(self, **kwargs):
        context = super(CompanyProjectListView, self).get_context_data(**kwargs)
        context['company'] = self.request.user.company
        context['published_projects'] = CompanyProject.objects.get_own_published_queryset(self.request.user.company)

        context['drafts'] = CompanyProject.objects.get_own_drafts_queryset(self.request.user.company)
        return context


class CompanyProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "company_project_update_view.html"
    login_url = "/companies/login/"
    model = CompanyProject
    form_class = CompanyProjectForm

    def form_valid(self, form):
        project = form.save(commit=False)
        message = ""
        if '_publish' in self.request.POST:
            project.published = True
            message = "The project has been updated"
        if '_save' in self.request.POST:
            project.published = False
            message = "The draft has been updated"

        project.save()
        form.save_m2m()

        messages.add_message(self.request, messages.SUCCESS, message, extra_tags="alert-success")

        return redirect(reverse("companies:list_projects"))

    def form_invalid(self, form):
        messages.add_message(self.request,
                             messages.ERROR,
                             "Please correct the field(s) indicated with red",
                             extra_tags="alert-error")
        return super(CompanyProjectUpdateView, self).form_invalid(form)


class ProjectPricingView(LoginRequiredMixin, UpdateView):
    template_name = "project_sales_view.html"
    login_url = "/companies/login/"
    form_class = BuyProjectsForm
    model = Company

    def form_valid(self, form):
        profile = Company.objects.get(id=self.object.pk)
        nr_of_projects = form.cleaned_data.get('projects_available')
        profile.projects_available += form.cleaned_data.get('projects_available')

        if profile.projects_latest_buying_date:
            profile.projects_former_buying_date = profile.projects_latest_buying_date
        else:
            profile.projects_latest_buying_date = date.today()

        package_type = ""
        if nr_of_projects == 1:
            package_type = "SU"
        elif nr_of_projects == 3:
            package_type = "ST"
        elif nr_of_projects == 10:
            package_type = "EN"

        ProjectPackage.objects.create(company_name=profile.name,
                                      email=profile.user.email,
                                      type=package_type)

        profile.save()

        messages.add_message(self.request, messages.SUCCESS, "The amount of projects available have been updated",
                             extra_tags="alert-success")
        return redirect(reverse("companies:profile", args=(self.object.slug, )))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "There seems to be an error",
                             extra_tags="alert-danger")
        return super(ProjectPricingView, self).form_invalid(form)


class ChangePasswordView(LoginRequiredMixin, UpdateView):
    template_name = "change_password.html"
    model = User
    login_url = "/companies/login/"
    form_class = ChangeUserPassword

    def form_valid(self, form):
        profile = Company.objects.get(user=self.request.user)

        form.save()

        messages.add_message(self.request, messages.SUCCESS, "Your password have been changed",
                             extra_tags="alert-success")
        return redirect(reverse("companies:profile", args=(profile.slug, )))


class CompanyFAQView(LoginRequiredMixin, ListView):
    template_name = "company_FAQ_view.html"
    login_url = "/companies/login/"
    model = FAQuestion

    def get_queryset(self):
        return FAQuestion.objects.filter(subject="C")


class CompanyFeedback(LoginRequiredMixin, FormView):
    template_name = "company_feedback.html"
    login_url = "/companies/login/"
    model = UserQuestion
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        messages.add_message(self.request, messages.SUCCESS,
                             "Thank you for your feedback! We will get back to you shortly!",
                             extra_tags="alert-success")

        return redirect(reverse("companies:company_feedback"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "There was a problem with the information provided",
                             extra_tags="alert-danger")

        return super(CompanyFeedback, self).form_invalid(form)


class CompanyTermsOfUsage(LoginRequiredMixin, TemplateView):
    template_name = "company_terms_of_usage.html"


def company_project_delete_view(request, slug):
    project = Project.objects.get(slug=slug)
    project.is_active = False

    company_project = project.companyproject
    company_project.is_active = False
    company_project.save()
    project.save()

    return redirect(reverse("companies:list_projects"))


def company_project_alter_contact_view(request, slug):
    project = Project.objects.get(slug=slug)

    message = ""
    if project.open_for_applications:
        project.open_for_applications = False
        message = "Students can no longer contact you for collaboration on this project"
    else:
        project.open_for_applications = True
        message = "Students are now able to contact you for collaboration on this project"

    project.save()
    messages.add_message(request, messages.SUCCESS, message, extra_tags="alert-success")
    return redirect(reverse("companies:project_details", args=(slug, )))


class CompanySignUpView(CreateView):
    template_name = "company_signup.html"
    form_class = CompanyCreationForm
    model = Company

    def form_valid(self, form):
        form.save()
        user = authenticate(username=self.request.POST['email'],
                            password=self.request.POST['password1'])
        if user is not None:
            login(self.request, user)
            company = Company.objects.get(user=user)

            try:
                company.send_activation_email()
            except:
                pass
            self.request.session['user_name'] = company.name
            self.request.session['user_slug'] = company.slug
            self.request.session['user_id'] = user.id
            return redirect(reverse("companies:sign_up_success", args=(company.slug, )))
        else:
            return redirect("/companies/login/")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "There seems to be an error",
                             extra_tags="alert-danger")
        return super(CompanySignUpView, self).form_invalid(form)


class CompanyLogInView(FormView):
    template_name = "company_log_in.html"
    form_class = CompanyLogInForm
    model = User

    def form_valid(self, form):
        user = authenticate(username=self.request.POST['username'],
                            password=self.request.POST['password'])

        if user is not None and Company.objects.filter(user=user).exists():
            login(self.request, user)
            company = Company.objects.get(user=user)
            self.request.session['user_name'] = company.name
            self.request.session['user_slug'] = company.slug
            self.request.session['user_id'] = user.id
            company.times_logged_in += 1
            company.save()
            return redirect(reverse("companies:profile", args=(company.slug, )))
        else:
            messages.add_message(self.request, messages.ERROR, "There is no company with this email", extra_tags="alert-danger")
            return redirect("/companies/login/")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "There seems to be an error",
                             extra_tags="alert-danger")
        return super(CompanyLogInView, self).form_invalid(form)


def sign_out_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_check(request):
    user = request.user

    if user.is_authenticated() and Company.objects.filter(user=user).exists():
        company = Company.objects.get(user=user)
        request.session['user_name'] = company.get_full_name()
        request.session['user_slug'] = company.slug
        request.session['user_id'] = user.id
        company.times_logged_in += 1
        company.save()
        return redirect(reverse("companies:profile", args=(company.slug, )))
    else:
        return redirect(reverse("companies:log_in"))


def company_sign_up_success_view(request, slug):
    return redirect(reverse("companies:profile", args=(slug, )))