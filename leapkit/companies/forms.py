from datetime import datetime

from crispy_forms.bootstrap import PrependedText
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, ButtonHolder, Fieldset, HTML
from models import CompanyProject, Company

"""
    ------------------------------------------------------------------------
    Below this section are all the views used to handle company profiles and
    projects.
    ------------------------------------------------------------------------
"""


class CompanyForm(forms.ModelForm):
    year_founded = forms.IntegerField(min_value=1800, max_value=datetime.now().year, required=False)
    website = forms.URLField(initial="http://",
                             help_text="Please provide the URL to a relevant website. "
                                       "Make sure the URL begins with 'http://'.",
                             required=False)

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('logo', css_class='logo_section'),
                'industry',
                'address',
                'website',
                'company_size',
                'country',
                Field('year_founded', ),
                'about',
                'overview',
                'mission'
            ),
            ButtonHolder(
                Submit('submit', 'Update', css_class="col-md-4 btn-fill col-xs-4 col-xs-offset-4 col-md-offset-4")
            )
        )

    def clean_company_size(self):
        company_size = self.cleaned_data.get('company_size')
        if company_size is not None:
            if company_size < 1:
                raise forms.ValidationError("You cannot have less than 1 employee")
        return company_size

    class Meta:
        model = Company
        fields = (
            'logo',
            'industry',
            'address',
            'website',
            'company_size',
            'country',
            'year_founded',
            'about',
            'overview',
            'mission',
        )


class CompanyProjectForm(forms.ModelForm):
    web_page = forms.URLField(help_text="Please provide the URL to a relevant website. "
                                        "Make sure the URL begins with 'http://'.",
                              initial="http://",
                              required=False)
    start_date = forms.DateField(help_text="", required=False)
    end_date = forms.DateField(help_text="", required=False)

    def __init__(self, *args, **kwargs):
        super(CompanyProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Fieldset(
                'Basic Information',
                Field('title'),
                Field('contact_person'),
                Field('contact_email'),
                Field('contact_phone'),
                PrependedText('students_needed', '<i class="fa fa-users"></i>'),
                Field('involvement'),
                Field('job_functions'),

            ),
            Fieldset(
                'Project Description',
                Field('short_description'),
                Field('full_description'),
                Field('project_document'),
            ),
            Fieldset(
                'Project Requirements',
                Field('education_requirements'),
                Field('thesis_or_internship_required'),
                Field('university_requirements'),
                Field('related_lines_of_study'),
                Field('resume_required')
            ),
            Fieldset(
                'Other Information',
                PrependedText('web_page',
                              '<i class="fa fa-link"></i>'),
                Field('payment'),
                Field('nda_required'),
                Field('start_date'),
                Field('end_date'),
            ),
            ButtonHolder(
                Submit('_save', 'Save as Draft',
                       css_class="col-md-2 btn-fill col-xs-2 col-xs-offset-3 col-md-offset-3 btn-info",
                       css_id="draft_button"),
                Submit('_publish', 'Publish',
                       css_class="col-md-2 col-xs-2 btn-fill col-xs-offset-2 col-md-offset-2 btn-success",
                       css_id="publish_button")
            )
        )

    def clean_students_needed(self):
        students_needed = self.cleaned_data.get('students_needed')
        if students_needed:
            if students_needed < 1:
                raise forms.ValidationError("You cannot need less than 1 students")
        return students_needed

    def clean_involvement(self):
        involvement = self.cleaned_data.get('involvement')
        if involvement < 1:
            raise forms.ValidationError("You cannot be involved less than 1 hour pr. month")
        return involvement

    class Meta:
        model = CompanyProject
        fields = (
            # Basic Information
            'title',
            'contact_person',
            'contact_email',
            'contact_phone',
            'involvement',
            'job_functions',
            'students_needed',
            'web_page',

            # Project information
            'short_description',
            'full_description',

            # Requirements
            'education_requirements',
            'thesis_or_internship_required',
            'university_requirements',
            #'university_places'
            'related_lines_of_study',
            'resume_required',

            # Other Info
            'payment',
            'nda_required',
            'project_document',
            'start_date',
            'end_date',
        )


class BuyProjectsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BuyProjectsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('projects_available', css_class="hidden", ),
                ButtonHolder(
                    HTML(
                        '<input type="button" class="btn btn-danger col-md-offset-4 col-md-2 col-lg-2"'
                        ' name="cancel" value="Cancel" id="button-id-cancel" '
                        'data-dismiss="modal" aria-hidden="true">'),
                    HTML('<input type="submit" '
                         'name="submit" value="Purchase" '
                         'class="btn btn-primary col-md-2 col-lg-2" id="submit-id-submit" disabled>')
                ),
            )
        )

    class Meta:
        model = Company
        fields = (
            'projects_available',
        )


"""
    ------------------------------------------------------------------------
    Below this section are all the views used to create/login/logout companies
    and handle basic user information such as name/password etc.
    ------------------------------------------------------------------------
"""


class CompanyCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(CompanyCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-CompanyCreationForm'
        self.helper.form_method = 'post'
        self.helper.form_action = '/companies/sign-up/'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'email',
                'name',
                'industry',
                'password1',
                'password2',
            ),
            Submit('submit',
                   'Get started',
                   css_class='col-md-4 col-md-offset-4 btn-fill')
        )
        self.fields['name'].label = 'Company name'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

    class Meta:
        model = Company
        fields = ('name',
                  'industry',
        )

    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        ext = logo.name.split('.')[-1]
        file_types = ['png', 'jpg', 'jpeg']

        if not any(x in ext for x in file_types):
            raise forms.ValidationError("The uploaded file needs to be an image of the type: 'png', 'jpg' or 'jpeg'")
        return logo

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("This email is already in our system")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

    def save(self, commit=True):
        # Clean all data
        email = self.cleaned_data['email']

        # Insert the correct information in Custom User
        company = super(CompanyCreationForm, self).save(commit=False)

        user = User.objects.create_user(username=email,
                                        email=email,
                                        password=self.cleaned_data.get('password2'))

        if commit:
            company.user = user
            company.save()

        return user


class CompanyLogInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CompanyLogInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/companies/login/'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'password',
            ),
            Submit('submit',
                   'Log in',
                   css_class='col-md-4 col-md-offset-4 btn-fill')
        )
        self.fields['username'].label = 'Email'

    class Meta:
        model = User


class ChangeUserPassword(forms.ModelForm):
    old_password = forms.CharField(required=True, widget=forms.PasswordInput())
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(ChangeUserPassword, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('email', css_class='hidden'),
                'old_password',
                'password1',
                'password2',
            ),
            Submit('submit',
                   'Change Password',
                   css_class='col-md-4 col-md-offset-4')
        )
        self.fields['email'].label = ''
        self.fields['old_password'].label = 'Old password'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        email = self.cleaned_data.get('email')

        user = User.objects.get(username=email)

        if not user.check_password(old_password):
            raise forms.ValidationError("The password given was not correct")
        return old_password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

    def save(self, commit=True):
        email = self.cleaned_data.get('email')
        user = User.objects.get(username=email)

        user.set_password(self.cleaned_data.get('password2'))
        user.save()

        return user

    class Meta:
        model = User
        fields = ('email', )