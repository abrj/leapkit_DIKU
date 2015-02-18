from django.test import TestCase

from ..models import StudentProfile
from custom_users.models import CustomUser


class StudentProfileTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email="test@test.dk",
                                                   name="test test",
                                                   password="test")

    def create_profile(self,
                       first_name="test",
                       last_name="test",
                       sex="M",
                       university="ITU"):
        return StudentProfile.objects.create(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            university=university,
            user=self.user
        )

    def test_student_profile_creation(self):
        profile = self.create_profile()

        self.assertTrue(isinstance(profile, StudentProfile))
        self.assertEquals(profile.__unicode__(), "%s %s" % (profile.first_name, profile.last_name))
        self.assertTrue(profile.is_active)