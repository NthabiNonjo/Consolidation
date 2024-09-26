from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    A form for user registration that extends Django's built-in UserCreationForm.

    This form allows users to create a new account by providing a username, email, and password.
    It includes additional validation for the email field, which is not present in the default UserCreationForm.
    """

    email = forms.EmailField(required=True)
    """
    An email field for user registration. This field is required and ensures that
    the email address entered is in a valid format. This is an additional field
    not present in the default UserCreationForm.
    """

    class Meta:
        """
        Metadata for the SignUpForm class.

        This nested class defines the model to be used with this form and the fields
        that should be included in the form. In this case, it uses Django's built-in
        User model and includes 'username', 'email', 'password1', and 'password2' fields.
        """

        model = User
        """
        Specifies the model that the form is associated with. Here, it uses the built-in
        User model provided by Django's auth system.
        """

        fields = ('username', 'email', 'password1', 'password2')
        """
        Specifies the fields from the User model to include in the form. 'username' is the
        user's login name, 'email' is their email address, 'password1' is their chosen password,
        and 'password2' is a confirmation of the password.
        """
