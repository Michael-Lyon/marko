from django.test import TestCase
from django.contrib.auth.models import User

from core.forms import CustomSignupForm


class TestForm(TestCase):

    # Test if form is valid
    def test_form_valid(self):
        form = CustomSignupForm({
            'first_name': 'Mike',
            'last_name': 'Mike',
            'username': 'MIKEMIKE',
            'email': 'mickiasomg@gmail.com',
            'password1': 'michaellyon',
            'password2': 'michaellyon'
        })
        # user = User.objects.create_user("MIKEMIKE", "mike@marko.com")
        # session = self.client.session
        request = self.client.request(session)
        # Check if form is valid
        self.assertTrue(form.is_valid(), "Form is not valid")
        # Check if the form actually save
        # self.assertTrue(form.save(self.client.request))
        # to test the signup function in the form.py
        person = form.save(request)
        self.assertEquals(person, CustomSignupForm.signup())

        # check in values input.

        self.assertEqual(person.first_name, "Mike")
        self.assertEqual(person.last_name, "Mike")
        self.assertEqual(person.username, "Mike")
        self.assertEqual(person.email, "mickiasomg@gmail.com")
        self.assertEqual(person.password1, "michaellyon")
        self.assertEqual(person.password1, "michaellyon")
