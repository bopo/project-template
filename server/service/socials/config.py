from django.apps import AppConfig


class PythonSocialAuthConfig(AppConfig):
    # Full Python path to the application eg. 'django.contrib.admin'.
    name = 'service.socials'
    # Last component of the Python path to the application eg. 'admin'.
    label = 'socials'
    # Human-readable name for the application eg. "Admin".
    verbose_name = 'Python Social Auth'
