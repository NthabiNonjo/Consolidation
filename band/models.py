from django.contrib.auth.models import User
from django.db import models


class BandMember(models.Model):
    """
    Model representing a band member.

    This model stores information about each member of the band, including their name, role,
    a profile image, and a brief biography.
    """

    name = models.CharField(max_length=100)
    """
    The name of the band member. This field is a character field with a maximum length of 100 characters.
    """

    role = models.CharField(max_length=100)
    """
    The role of the band member in the band (e.g., lead singer, guitarist). 
    This field is a character field with a maximum length of 100 characters.
    """

    image = models.ImageField(upload_to='band_members/')
    """
    A profile image of the band member. The image file will be uploaded to the 'band_members/' directory.
    """

    bio = models.TextField()
    """
    A biography of the band member, providing additional details about their background and contributions.
    This field is a text field that can store a large amount of text.
    """

    def __str__(self):
        """
        Return a string representation of the BandMember object.

        This method returns the name of the band member, which is useful for display purposes
        in the Django admin interface and other parts of the application.
        """
        return self.name


class Event(models.Model):
    """
    Model representing an event or concert.

    This model stores details about upcoming events or concerts, including the title, description,
    date and time, and location of the event.
    """

    title = models.CharField(max_length=200)
    """
    The title of the event (e.g., 'Summer Concert'). This field is a character field with a maximum 
    length of 200 characters.
    """

    description = models.TextField()
    """
    A detailed description of the event, including any additional information or special notes. 
    This field is a text field that can store a large amount of text.
    """

    event_date = models.DateTimeField()
    """
    The date and time when the event will take place. This field is a date-time field.
    """

    location = models.CharField(max_length=200)
    """
    The location where the event will be held (e.g., 'City Hall'). This field is a character field with 
    a maximum length of 200 characters.
    """

    image = models.ImageField(upload_to='Events/')
    """
    An event image of the event. The image file will be uploaded to the 'Events/' directory.
    """

    def __str__(self):
        """
        Return a string representation of the Event object.

        This method returns the title of the event, which is useful for display purposes
        in the Django admin interface and other parts of the application.
        """
        return self.title
