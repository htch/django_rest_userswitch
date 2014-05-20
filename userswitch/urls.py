from django.conf.urls import patterns, url
from userswitch.views import LoginAsView

urlpatterns = patterns('',
    url(r'^loginas/(?P<pk>\d+)/$', LoginAsView.as_view(), name='loginas'),
)
