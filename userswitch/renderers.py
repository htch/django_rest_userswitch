from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.renderers import BrowsableAPIRenderer


class BrowsableAPIRenderer(BrowsableAPIRenderer):
    template = 'userswitch/api.html'

    def get_context(self, *args, **kwargs):
        context = super(BrowsableAPIRenderer, self).get_context(*args, **kwargs)
        if not hasattr(settings, 'USERSWITCH_ENABLE') or settings.USERSWITCH_ENABLE == False:
            return context
        if not hasattr(settings, 'USERSWITCH_WHITELIST'):
            if hasattr(settings, 'ANONYMOUS_USER_ID'):      # filtering out django-guardian's AnonymousUser
                context['available_users'] = get_user_model().objects.filter(is_active=True).exclude(pk=settings.ANONYMOUS_USER_ID)
            else:
                context['available_users'] = get_user_model().objects.filter(is_active=True)
        else:
            user = get_user_model()
            if hasattr(user, 'USERNAME_FIELD'):
                context['available_users'] = user.objects.filter(**{user.USERNAME_FIELD + '__in': settings.USERSWITCH_WHITELIST})
            else:
                context['available_users'] = user.objects.filter(username__in=settings.USERSWITCH_WHITELIST)
        return context