# coding=utf-8
from django.test import TestCase

from ..forms import ContactForm


class ContactFormTests(TestCase):
    def test_form_international(self):
        # TODO This test returns an error when it should not
        contact_query_us = {"name": "Test Case",
                            "email": "Test_Case@email.com",
                            "body": "This is a question I would like to have answered!"}

        us_form = ContactForm(data=contact_query_us)
        self.assertTrue(us_form.is_valid())

        contact_query_dk = {"name": "Test Åase",
                            "email": "Tæst_Case@ømail.dk",
                            "body": "This is a questiøn I would like to have answered!"}

        dk_form = ContactForm(data=contact_query_dk)
        self.assertTrue(dk_form.is_valid())

        contact_query_fr = {"name": "Test éase",
                            "email": "Test_çase@email.fr",
                            "body": "This is a çuestion I would like to have answered!"}

        fr_form = ContactForm(data=contact_query_fr)
        self.assertTrue(fr_form.is_valid())

    def test_form_numbers(self):
        # TODO make sure that numbers are allowed in email, since this occurs regularly
        contact_query_num_true = {"name": "Test Åase",
                                  "email": "TesttCase99@mail.dk",
                                  "body": "This is a question I would like to have answered!"}

        num_true_form = ContactForm(data=contact_query_num_true)
        self.assertTrue(num_true_form.is_valid())

        contact_query_num_false = {"name": "T231est Åase",
                                   "email": "TætCase@mail.dk",
                                   "body": "This is a question I would like to have answered!"}

        num_false_form = ContactForm(data=contact_query_num_false)
        self.assertFalse(num_false_form.is_valid())

    def test_form_signs(self):
        # TODO Make sure all these signs are available in the body
        contact_query_sign_body = {"name": "Test Åase",
                                   "email": "Tæ2t_Case@ø21mail.dk",
                                   "body": "All these signs should be available! !#€%&/()<=?+$§!'^¨*@>-_.:,;"}

        signs_body_form = ContactForm(data=contact_query_sign_body)
        self.assertTrue(signs_body_form.is_valid())

        contact_query_sign_name = {"name": "T@est Åase",
                                   "email": "Tæ2t_Case@ø21mail.dk",
                                   "body": "This is a questio312n I would like to have answered!"}

        signs_name_form = ContactForm(data=contact_query_sign_name)
        self.assertFalse(signs_name_form.is_valid())

    def test_form_empty(self):
        contact_query_empty_name = {"name": "",
                                    "email": "Tæ2t_Case@ø21mail.dk",
                                    "body": "This is a questio312n I would like to have answered!"}

        empty_name_form = ContactForm(data=contact_query_empty_name)
        self.assertFalse(empty_name_form.is_valid())

        contact_query_empty_email = {"name": "Test Åase",
                                     "email": "",
                                     "body": "This is a questio312n I would like to have answered!"}

        empty_email_form = ContactForm(data=contact_query_empty_email)
        self.assertFalse(empty_email_form.is_valid())

        contact_query_empty_body = {"name": "Test Åase",
                                    "email": "Tæ2t_Case@ø21mail.dk",
                                    "body": ""}

        empty_body_form = ContactForm(data=contact_query_empty_body)
        self.assertFalse(empty_body_form.is_valid())

    def test_form_with_scripts(self):
        contact_query_script_name = {"name": "<script> alert('this is a hack') </script>",
                                     "email": "Tæ2t_Case@ø21mail.dk",
                                     "body": "This is a questio312n I would like to have answered!"}

        script_name_form = ContactForm(data=contact_query_script_name)
        self.assertFalse(script_name_form.is_valid())

        contact_query_script_email = {"name": "Test Åase",
                                      "email": "<script> alert('this is a hack') </script>",
                                      "body": "This is a questio312n I would like to have answered!"}

        script_email_form = ContactForm(data=contact_query_script_email)
        self.assertFalse(script_email_form.is_valid())

        contact_query_script_body = {"name": "Test Åase",
                                     "email": "Tæ2t_Case@ø21mail.dk",
                                     "body": "<script> alert('this is a hack') </script>"}

        script_body_form = ContactForm(data=contact_query_script_body)
        self.assertFalse(script_body_form.is_valid())