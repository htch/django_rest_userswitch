django_rest_userswitch
======================

Instant user switching widget for django rest framework browsable API. Adds a handy widget to switch between different users in one click.

**DISCLAIMER: only use it in test environments**

![screenshot](https://raw.github.com/htch/django_rest_userswitch/screenshot.png)

Installation
============

Install with `pip install -e git+https://github.com/htch/django_rest_userswitch.git#egg=django-rest-userswitch`

Add `userswitch` to `INSTALLED_APPS` in your settings.

Add `url(r'^api-auth-userswitch/', include('userswitch.urls', namespace='userswitch')),` to your app's urlpatterns.

Add `USERSWITCH_ENABLE = True` to your settings.


Configuration
=============

So far the app only supports two configuration variables:

`USERSWITCH_ENABLE`: set to `True` to enable user switching widget; comment it out to turn off user switch functionality.

`USERSWITCH_WHITELIST`: set to a tuple of usernames that you want to see in the user switching dropdown; by default displays all available users. You can use this with `USERNAME_FIELD`.