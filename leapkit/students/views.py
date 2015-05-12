from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import DetailView, CreateView, FormView, UpdateView, ListView, TemplateView
from braces.views import LoginRequiredMixin

from forms import StudentCreationForm, StudentLogInForm, ChangeUserPassword, StudentForm, StudentProjectForm, EmailForm
from models import Student, StudentProject, insertLinkedInProfile, LinkedInProfile, Skill, Language, Education, Course, Position
from companies.models import CompanyProject
from queries.models import FAQuestion, UserQuestion
from queries.forms import ContactForm
from projects.models import Project
from institutions.models import Institution, FieldOfStudy

import logging
import linkedin_connector
from matchmaking import compareSkillsFullString


"""
    ------------------------------------------------------------------------
    Below this section are all the views used to handle student profiles and
    projects.
    ------------------------------------------------------------------------
"""


class StudentView(LoginRequiredMixin, DetailView):
    template_name = "student_profile.html"
    login_url = "/students/login/"
    model = Student

    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        try:
            request.session['profile_views'] += 1
        except:
            request.session['profile_views'] = 0

        # call the view
        return super(StudentView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['profile'] = Student.objects.get(user=self.request.user)
        project_list = StudentProject.objects.get_own_projects(self.request.user.student)

        logger = logging.getLogger("debug_logger")
        logger.debug("STUDENTVIEW: Assigning project list in context.")

        context['project_list'] = project_list
        logger.debug(project_list)
        context['published_projects'] = project_list.filter(published=True)
        if LinkedInProfile.objects.filter(leapkituser=self.request.user):
            linked = LinkedInProfile.objects.get(leapkituser=self.request.user)
            context['linked'] = linked
            context['skills'] = Skill.objects.filter(profile=linked)
            context['educations'] = Education.objects.filter(profile=linked)
            context['languages'] = Language.objects.filter(profile=linked)
            context['courses'] = Course.objects.filter(profile=linked)
            context['positions'] = Position.objects.filter(profile=linked)

        return context

class UpdateStudentProfileView(LoginRequiredMixin, UpdateView):
    template_name = "update_student_profile.html"
    login_url = "/students/login/"
    model = Student
    form_class = StudentForm

    def form_valid(self, form):
        form.save()

        messages.add_message(self.request, messages.SUCCESS, "Your profile was updated!", extra_tags="alert-success")
        return redirect(reverse("students:profile", args=(self.object.slug, )))

    def form_invalid(self, form):
        messages.add_message(self.request,
                             messages.ERROR,
                             "There was some problems with the provided information",
                             extra_tags="alert-error")
        return super(UpdateStudentProfileView, self).form_invalid(form)


class StudentOwnProjectListView(LoginRequiredMixin, ListView):
    template_name = "student_own_project_list_view.html"
    login_url = "/students/login/"
    model = StudentProject

    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        try:
            request.session['own_projects_views'] += 1
        except:
            request.session['own_projects_views'] = 0

        # call the view
        return super(StudentOwnProjectListView, self).dispatch(request, *args, **kwargs)


    def get_queryset(self, **kwargs):
        logger = logging.getLogger("debug_logger")
        logger.debug("STUDENTOWNPROJECTLISTVIEW: Assigning project list in context.")
        project_list = StudentProject.objects.get_own_published_queryset(self.request.user.student)
        return project_list

    def get_context_data(self, **kwargs):
        context = super(StudentOwnProjectListView, self).get_context_data(**kwargs)
        context['student'] = self.request.user.student
        context['published_projects'] = StudentProject.objects.get_own_published_queryset(self.request.user.student)
        context['drafts'] = StudentProject.objects.get_own_drafts_queryset(self.request.user.student)
        return context


class StudentProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "student_project_update_view.html"
    login_url = "/students/login/"
    model = StudentProject
    form_class = StudentProjectForm

    def form_valid(self, form):
        project = form.save(commit=False)

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
        return redirect(reverse("students:own_student_projects"))


class StudentProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "student_own_project_detail_view.html"
    login_url = "/students/login/"
    model = Project

    def get_queryset(self):
        project = Project.objects.filter(slug=self.kwargs['slug'])
        return project


class StudentProjectCreationView(LoginRequiredMixin, CreateView):
    template_name = "student_project_creation_view.html"
    login_url = "/students/login/"
    model = StudentProject
    form_class = StudentProjectForm

    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        try:
            request.session['create_project_views'] += 1
        except:
            request.session['create_project_views'] = 0

        # call the view
        return super(StudentProjectCreationView, self).dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        project = form.save(commit=False)
        project.project_owner = self.request.user.student
        project.contact_email = self.request.user.email
        project.contact_person = self.request.user.get_full_name()

        message = ""
        if '_publish' in self.request.POST:
            project.published = True
            message = "The project has been created"

        if '_save' in self.request.POST:
            project.published = False
            message = "The draft has been created"

        project.save()
        form.save_m2m()

        messages.add_message(self.request, messages.SUCCESS, message, extra_tags="alert-success")
        return redirect(reverse("students:profile", args=(self.request.user.student.slug, )))


class ListAllProjectsView(LoginRequiredMixin, ListView):
    template_name = "list_all_projects.html"
    login_url = "/students/login/"
    model = Project
    paginate_by = 20
    allow_empty = True

    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        try:
            request.session['all_projects_views'] += 1
        except:
            request.session['all_projects_views'] = 0

        # call the view
        return super(ListAllProjectsView, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        projects = Project.objects.get_published_queryset()

        for project in projects.iterator():
            project.views += 1
            project.save()

        return projects

    def get_context_data(self, **kwargs):
        """
        Builds the context that is needed for the project list to display the
        relevant projects.
        """
        context = super(ListAllProjectsView, self).get_context_data(**kwargs)

        all_projects = Project.objects.filter(is_active=True, published=True)

        # Retrieve the skills from the relevant linkedin profile.
        linkedin_profile = LinkedInProfile.objects.filter(leapkituser=self.request.user)
        skills = Skill.objects.filter(profile=linkedin_profile)
        skillstrings = []
        for skill in skills:
            skillstrings.append(skill.name)

        # Create a list of tubles on the form:
        # [project ID, [project Description (split by spaces)], Project Description.]
        project_tuples = []
        for project in all_projects:
            project_tuples.append([project.id, project.full_description.split(), project.full_description])

        # Call the matchmaking functions (from the module matchmaking.py) to
        # generate a list of project ID's and their respective match rating.
        compare_result = compareSkillsFullString(skillstrings, project_tuples)


        # Go through the results one by one and add the full project object for
        # any project that had a higher score than 0.
        recommended_projects = []
        for tup in compare_result:
            pid = tup[0]
            score = tup[1]
            if score > 0:
                recommended_projects.append(Project.objects.get(id=pid))

        context['recommended_projects'] = recommended_projects

        nr_of_projects_count = Project.objects.filter(is_active=True, published=True).count()
        nr_of_company_projects = CompanyProject.objects.filter(is_active=True, published=True).count()
        nr_of_student_projects = StudentProject.objects.filter(is_active=True, published=True).count()
        context['all_projects_count'] = nr_of_projects_count
        context['company_projects_count'] = nr_of_company_projects
        context['student_projects_count'] = nr_of_student_projects

        # Get and add list of universities to context
        institutions = Institution.objects.get_queryset()
        institutionsList = [];
        for institution in institutions:
            institutionsList.append(str(institution));

        context['institutionsList'] = institutionsList

        # Get and add list of lines_of_study to context
        lines_of_study = FieldOfStudy.objects.get_queryset()
        lines_of_studyList = [];
        for line_of_study in lines_of_study:
            lines_of_studyList.append(str(line_of_study));

        context['lines_of_studyList'] = lines_of_studyList


        return context



# @register.assignment_tag
# def filterFunction(value):
#     for p in value:
#         print p.title
#     studProjects = StudentProject.objects.all()
#     return studProjects


class AllProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = "all_project_detail_view.html"
    login_url = "/students/login/"
    model = Project

    def dispatch(self, request, *args, **kwargs):
        # parse the request here ie.
        try:
            request.session['project_detail'] += 1
        except:
            request.session['project_detail'] = 0

        # call the view
        return super(AllProjectDetailView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        project = Project.objects.get(slug=self.kwargs['slug'])
        project.detail_views += 1
        project.save()

        return project

    def get_context_data(self, **kwargs):
        context = super(AllProjectDetailView, self).get_context_data(**kwargs)
        context['form'] = EmailForm
        context['user_name'] = self.request.user.student.get_full_name()
        context['user_email'] = self.request.user.email
        return context


class StudentFAQView(LoginRequiredMixin, ListView):
    template_name = "students_FAQ_view.html"
    login_url = "/students/login/"
    model = FAQuestion

    def get_queryset(self):
        return FAQuestion.objects.filter(subject="S")


class StudentFeedBack(LoginRequiredMixin, FormView):
    template_name = "student_feedback.html"
    login_url = "/students/login/"
    model = UserQuestion
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        messages.add_message(self.request, messages.SUCCESS,
                             "Thank you for your feedback! We will get back to you shortly!",
                             extra_tags="alert-success")
        return redirect(reverse("students:student_feedback"))

    def form_invalid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "There was a problem with the information provided",
                             extra_tags="alert-danger")

        return super(StudentFeedBack, self).form_invalid(form)


class StudentTermsOfUsage(LoginRequiredMixin, TemplateView):
    template_name = "student_terms_of_usage.html"


class SendMailView(FormView):
    template_name = "send_email.html"
    form_class = EmailForm

    def get_context_data(self, **kwargs):
        context = super(SendMailView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(slug=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        slug = self.kwargs['slug']
        email_query = form.save(commit=False)
        email_query.sender = self.request.user

        project = ""
        if CompanyProject.objects.filter(slug=self.kwargs['slug']).exists():
            project = CompanyProject.objects.get(slug=self.kwargs['slug'])
        elif StudentProject.objects.filter(slug=self.kwargs['slug']).exists():
            project = StudentProject.objects.get(slug=self.kwargs['slug'])

        project_owner = project.project_owner
        email_query.receiver = project_owner.user
        email_query.contact_email = project.contact_email
        email_query.save()

        student = Student.objects.get(user=self.request.user)
        student_name = student.get_full_name()
        student_email = student.user.email
        student_school = student.institution.name

        subject = email_query.subject
        body = email_query.body

        email = "From: %s \n Institution: %s \n Reply to email: %s \n\n Message: \n %s" % (student_name,
                                                                                           student_school,
                                                                                           student_email,
                                                                                           body)
        email = EmailMessage(subject=subject,
                             body=email,
                             from_email=settings.DEFAULT_FROM_EMAIL,
                             to=[email_query.contact_email, ])
        try:
            attachment = self.request.FILES['attachment']
        except MultiValueDictKeyError:
            attachment = None

        if attachment is not None:
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        email.send(fail_silently=False)

        message = "An email has been sent to %s" % project_owner.get_full_name()
        messages.add_message(self.request, messages.SUCCESS, message, extra_tags="alert-success")

        return redirect(reverse("students:all_projects_detail", args=(slug, )))


def all_projects_filter(request):
    value = request.POST.get('filter_dropdown')
    print value
    job_functions = Project.objects.get_published_queryset()
    return render(request, "list_all_projects.html", {'job_functions' : job_functions})



def student_project_delete_view(request, slug):
    project = Project.objects.get(slug=slug)
    project.is_active = False

    student_project = project.studentproject
    student_project.is_active = False
    student_project.save()
    project.save()

    return redirect(reverse("students:own_student_projects"))


def student_project_alter_contact_view(request, slug):
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
    return redirect(reverse("students:student_project_details", args=(slug, )))


"""
    ------------------------------------------------------------------------
    Below this section are all the views used to create/login/logout students
    and handle basic user information such as name/password etc.
    ------------------------------------------------------------------------
"""


class StudentSignUpView(CreateView):
    template_name = "student_signup.html"
    form_class = StudentCreationForm
    model = Student

    def form_valid(self, form):
        form.save()
        user = authenticate(username=self.request.POST['email'],
                            password=self.request.POST['password2'])
        if user is not None:
            student = Student.objects.get(user=user)
            login(self.request, user)

            self.request.session['user_name'] = student.get_full_name()
            self.request.session['user_slug'] = student.slug
            self.request.session['user_id'] = user.id

            try:
                student.send_activation_email()
            except:
                pass
            # Add a student to the student counter in the university part
            student.institution.add_one_student()

            return redirect(reverse("students:sign_up_success", args=(student.slug, )))
        else:
            return redirect("students:sign_up")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "There seems to be an error",
                             extra_tags="alert-danger")
        return super(StudentSignUpView, self).form_invalid(form)


class StudentLogInView(FormView):
    template_name = "student_log_in.html"
    form_class = StudentLogInForm
    model = User


    def form_valid(self, form):
        user = authenticate(username=self.request.POST['username'],
                            password=self.request.POST['password'])
        if user is not None and Student.objects.filter(user=user).exists():
            login(self.request, user)
            student = Student.objects.get(user=user)
            self.request.session['user_name'] = student.get_full_name()
            self.request.session['user_slug'] = student.slug
            self.request.session['user_id'] = user.id

            student.times_logged_in += 1
            student.save()

            return redirect(reverse("students:profile", args=(student.slug, )))
        else:
            messages.add_message(self.request, messages.ERROR, "There is no student with this email",
                                 extra_tags="alert-danger")
            return redirect("students:log_in")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "There seems to be an error",
                             extra_tags="alert-danger")
        return super(StudentLogInView, self).form_invalid(form)


class ChangePasswordView(UpdateView):
    template_name = "change_student_password.html"
    model = User
    form_class = ChangeUserPassword

    def form_valid(self, form):
        profile = Student.objects.get(user=self.request.user)

        form.save()

        messages.add_message(self.request, messages.SUCCESS, "Your password have been changed",
                             extra_tags="alert-success")
        return redirect(reverse("students:profile", args=(profile.slug, )))


def sign_out_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_check(request):
    user = request.user

    if user.is_authenticated() and Student.objects.filter(user=user).exists():
        student = Student.objects.get(user=user)
        request.session['user_name'] = student.get_full_name()
        request.session['user_slug'] = student.slug
        request.session['user_id'] = user.id
        student.times_logged_in += 1
        student.save()
        return redirect(reverse("students:profile", args=(student.slug, )))
    else:
        return redirect(reverse("students:log_in"))


def student_sign_up_success(request, slug):
    return redirect(reverse("students:profile", args=(slug, )))


"""
    -------------------------------------------------------------------------
    Below this section are all the views used to handle contact with LinkedIn
    -------------------------------------------------------------------------
"""

def linkedin_redirect(request):
    """
    Redirects the user to a login form in LinkedIn to retrieve a sign in code.
    """
    #logging.error(request)
    #logging.error("\nrequest.user = " + str(request.user))
    try:
        #path = request.META['HTTP_REFERER']
        slug = Student.objects.get(user=request.user).slug
        #path = 'http://www.leapkit.com?u=' + slug
        path = 'http://' + request.META['HTTP_HOST'] + '/students/stage?u=' + slug
        #logging.error("\nurl:" + path)
        linkedin_url = linkedin_connector.linkedin_get_url(path)
    except:
        return redirect(reverse("students:log_in"))


    return HttpResponseRedirect(linkedin_url)

def stage(request):
    """
    Creates a connection to LinkedIn and retrieves the users LinkedIn profile
    information in a JSON format and then parses the information and saves it in
    the local database before returning to the students profile pages.
    """
    #logging.error(request)
    slug = request.GET['u']
    code = request.GET['code']
    return_url = 'http://' + request.META['HTTP_HOST'] + request.path + '?u=' + slug
    data = linkedin_connector.linkedin_extract(code, return_url)
    if len(data) <= 1:
        pass
        #TODO in no success cases - inform user???
    logging.error(data)

    LeapkitUsername = request.user
    # TODO: Redo the insert function to work with a dict instead of the data string. It's much more fun and secure.
    if insertLinkedInProfile(str(data), LeapkitUsername):
        messages.add_message(request, messages.SUCCESS,
                "Successfully extracted data from LinkedIn",
                extra_tags="alert-success")
    else:
        messages.add_message(request, messages.ERROR,
            ("Failed to extract data from LinkedIn"), extra_tags="alert-danger")



    return redirect(reverse("students:profile", args=(slug, )))
