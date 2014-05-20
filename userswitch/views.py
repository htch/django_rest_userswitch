from django.core.exceptions import PermissionDenied
from django.views.generic import RedirectView
from django.utils.module_loading import import_by_path
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth import login


class LoginAsView(RedirectView):
    permanent = False

    def get_redirect_url(self, pk):
        if not hasattr(settings, 'USERSWITCH_ENABLE') or settings.USERSWITCH_ENABLE == False:
            raise PermissionDenied()
        user = get_user_model().objects.get(pk=pk)
        backend = import_by_path(settings.AUTHENTICATION_BACKENDS[0])()
        user.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
        login(self.request, user)
        return self.request.GET['redirect_to']