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
    The name of the band member.

    :type: CharField (max_length=100)
    """

    role = models.CharField(max_length=100)
    """
    The role of the band member in the band (e.g., lead singer, guitarist).

    :type: CharField (max_length=100)
    """

    image = models.ImageField(upload_to='band_members/')
    """
    A profile image of the band member.

    :type: ImageField (upload_to='band_members/')
    """

    bio = models.TextField()
    """
    A biography of the band member, providing additional details about their background and contributions.

    :type: TextField
    """

    def __str__(self):
        """
        Return a string representation of the BandMember object.

        :return: The name of the band member.
        :rtype: str
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
    The title of the event (e.g., 'Summer Concert').

    :type: CharField (max_length=200)
    """

    description = models.TextField()
    """
    A detailed description of the event, including any additional information or special notes.

    :type: TextField
    """

    event_date = models.DateTimeField()
    """
    The date and time when the event will take place.

    :type: DateTimeField
    """

    location = models.CharField(max_length=200)
    """
    The location where the event will be held (e.g., 'City Hall').

    :type: CharField (max_length=200)
    """

    image = models.ImageField(upload_to='Events/')
    """
    An image representing the event.

    :type: ImageField (upload_to='Events/')
    """

    def __str__(self):
        """
        Return a string representation of the Event object.

        :return: The title of the event.
        :rtype: str
        """
        return self.title
