from django.apps import AppConfig


class BandConfig(AppConfig):
    """
    Configuration class for the 'band' app.

    This class is used to configure the application-specific settings for the 'band' app.
    It inherits from Django's AppConfig class and allows customization of application
    settings and behaviors.
    """

    default_auto_field = "django.db.models.BigAutoField"
    """
    Specifies the type of primary key field to use for models that don't explicitly specify a primary key field.
    'BigAutoField' is an auto-incrementing primary key field that is suitable for large datasets.
    """

    name = "band"
    """
    The name of the application as it will be referenced in the Django project. 
    It is used by Django to locate the application and is typically the same as the application directory name.
    """
