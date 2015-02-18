import datetime

from django.test import TestCase
from django.utils import timezone
from root.models import Question, UserQuery
from custom_users.models import CustomUser


class FAQTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email="test@test.dk",
                                                   password="test")

    def create_question(self,
                        question="What is the meaning of life?",
                        answer="42",
                        subject="S"):
        return Question.objects.create(
            question=question,
            answer=answer,
            subject=subject
        )

    def test_frequently_asked_question_creation(self):
        question = self.create_question()

        self.assertTrue(isinstance(question, Question))
        self.assertEquals(question.__unicode__(), question.question)


class ContactQueryTests(TestCase):
    def create_user_query(self,
                          name="Test User",
                          email="test@test.dk",
                          body="This is a test question"):
        return UserQuery.objects.create(
            name=name,
            email=email,
            body=body
        )

    def test_contact_query_creation(self):
        question = self.create_user_query()

        self.assertTrue(isinstance(question, UserQuery))
        self.assertEquals(question.__unicode__(), question.name)
        self.assertFalse(question.has_been_answered)

    def test_was_published_recently_with_recent_poll(self):
        """
        was_asked_recently() should return True for polls whose pub_date is within the last day
        """

        recent_question = UserQuery(created=timezone.now() - datetime.timedelta(hours=1))

        self.assertTrue(recent_question.was_asked_recently())

    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently() should return False for polls whose pub_date is older than 1 day
        """

        old_question = UserQuery(created=timezone.now() - datetime.timedelta(days=30))

        self.assertFalse(old_question.was_asked_recently())

