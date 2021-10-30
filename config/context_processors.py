from django.contrib.auth import get_user_model


User = get_user_model()


def project_context(request):
    context = {"me": User.objects.first()}
    return context
