# Create your models here.
import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating 'created' and 'modified' fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class FAQuestion(TimeStampedModel):
    """
    Question is used to store all the frequently asked questions.
    It contains the question, an answer to that question along with the section to which the question belongs.
    The subject can be either Students, Companies or Universities, and are stored as S, C & U.
    """
    GENERAL = "G"
    STUDENTS = 'S'
    COMPANIES = 'C'
    UNIVERSITIES = 'U'

    QUESTION_SUBJECT_AREA = (
        (GENERAL, 'General'),
        (STUDENTS, 'Students'),
        (COMPANIES, 'Companies'),
        (UNIVERSITIES, 'Universities'),
    )

    question = models.CharField(max_length=200)
    answer = models.TextField()
    subject = models.CharField(max_length=1,
                               choices=QUESTION_SUBJECT_AREA,
                               default=STUDENTS)

    def __unicode__(self):
        return self.question

    class Meta:
        ordering = ["subject", "question"]
        verbose_name_plural = "Frequently Asked Questions"


class UserQuestion(TimeStampedModel):
    """
    UserQuery is used to store the questions users ask Leapkit.
    It contains the name and email of the user along with the message.
    It has two fields keeping track of whether the question has been answered, as well as the actual answer.
    """
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    body = models.TextField()
    has_been_answered = models.BooleanField(default=False)
    answer = models.TextField(default='')

    def __unicode__(self):
        return self.name

    def was_asked_recently(self):
        """
        Checks if the query has been created less than 24 hours ago
        :return: Boolean
        """
        now = timezone.now()

        return now - datetime.timedelta(days=1) <= self.created < now

    was_asked_recently.admin_order_field = 'created'
    was_asked_recently.boolean = True
    was_asked_recently.short_description = 'Question asked recently?'

    class Meta:
        ordering = ["created"]
        verbose_name_plural = "User Queries"


class CompanyEmailContact(TimeStampedModel):
    sender = models.ForeignKey(User, related_name="email_sender")
    receiver = models.ForeignKey(User, related_name="email_receiver")
    contact_email = models.EmailField(blank=True)
    subject = models.CharField(max_length=100)
    body = models.TextField()
