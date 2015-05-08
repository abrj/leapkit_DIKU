from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FieldWithButtons, StrictButton, FormActions, \
    AppendedText
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.layout import Submit, Fieldset, Layout, Field, ButtonHolder, Div
from crispy_forms.helper import FormHelper
import floppyforms as forms

from models import Student, StudentProject
from queries.models import CompanyEmailContact


"""
    ------------------------------------------------------------------------
    Below this section are all the forms used to handle student profiles and
    projects.
    ------------------------------------------------------------------------
"""


class StudentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'image',
                'gender',
                'institution',
                'education_level',
                'country',
                'line_of_study',
                'description',
                'cv'
            ),
            ButtonHolder(
                Submit('submit', 'Update', css_class="col-md-4 col-xs-4 col-xs-offset-4 col-md-offset-4")
            )
        )

    class Meta:
        model = Student
        fields = (
            'image',
            'gender',
            'institution',
            'education_level',
            'country',
            'description',
            'line_of_study',
            'cv'
        )


class StudentProjectForm(forms.ModelForm):
    start_date = forms.DateField(required=False,
                                 help_text="This field is only if there is a specific "
                                           "start date that needs to be taken into account")
    end_date = forms.DateField(required=False, help_text="This field is only there if a specific end date"
                                                         " needs to be taken into account")

    def __init__(self, *args, **kwargs):
        super(StudentProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Fieldset(
                'Basic Information',
                Field('title',),
                Field('contact_phone'),
                PrependedText('students_needed', '<i class="fa fa-users"></i>'),
                Field('job_functions'),
            ),
            Fieldset(
                'Project Description',
                Field('short_description'),
                Field('full_description'),
                Field('project_document'),
            ),
            Fieldset(
                'Project Preferences',
                Field('education_requirements'),
                Field('university_requirements'),
                Field('related_lines_of_study'),
            ),
            Fieldset(
                'Other Information',
                Field('start_date'),
                'end_date'
            ),
            ButtonHolder(
                Submit('_save', 'Make Draft',
                       css_class="col-md-2 col-xs-2 col-xs-offset-3 col-md-offset-3 btn-info btn-fill",
                       css_id="draft_button"),
                Submit('_publish', 'Publish',
                       css_class="col-md-2 col-xs-2 col-xs-offset-2 col-md-offset-2 btn-success btn-fill",
                       css_id="publish_button")
            )
        )


    def clean_students_needed(self):
        students_needed = self.cleaned_data.get('students_needed')
        if students_needed and students_needed < 1:
            raise forms.ValidationError("You cannot choose less than 1 student")
        return students_needed

    def clean_image(self):
        image = self.cleaned_data.get('image')
        ext = image.name.split('.')[-1]
        file_types = ['png', 'jpg', 'jpeg']

        if not any(x in ext for x in file_types):
            raise forms.ValidationError("The uploaded file needs to be an image of the type: 'png', 'jpg' or 'jpeg'")
        return image

    class Meta:
        model = StudentProject
        fields = (
            # Basic Information
            'title',
            'contact_phone',
            'students_needed',
            'job_functions',

            # Project information
            'short_description',
            'full_description',

            # Requirements
            'education_requirements',
            'university_requirements',
            'related_lines_of_study',

            # Other Info
            'project_document',
            'start_date',
            'end_date'
        )


"""
    ------------------------------------------------------------------------
    Below this section are all the forms used to create/login students and
    handle basic user information such as name/password etc.
    ------------------------------------------------------------------------
"""


class StudentCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(StudentCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-StudentCreationForm'
        self.helper.form_method = 'post'
        self.helper.form_action = '/students/sign-up/'
        self.helper.layout = Layout(
            Fieldset(
                '',
                'email',
                'institution',
                'first_name',
                'last_name',
                'password1',
                'password2',
            ),
            Submit('submit',
                   'Get started',
                   css_class=('col-md-4 col-md-offset-4')
            )
        )
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

    class Meta:
        model = Student
        fields = ('institution',
                  'first_name',
                  'last_name')

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
        student = super(StudentCreationForm, self).save(commit=False)
        user = User.objects.create_user(username=email,
                                        email=email,
                                        password=self.cleaned_data.get('password2'))
        if commit:
            # Save and create a profile
            student.user = user
            student.save()

        return user


class StudentLogInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(StudentLogInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/students/login/'
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


class EmailForm(forms.ModelForm):
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False,)

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'subject',
                'body',
                'attachment'
            ),
            Submit('submit',
                   'Contact',
                   css_class='col-md-4 col-md-offset-4')
        )

    class Meta:
        model = CompanyEmailContact
        fields = ('subject',
                  'body')