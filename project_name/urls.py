from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment to redirect the main index to a specific app url
#from django.views.generic import RedirectView
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Login Page
    url(r'^login/$', 'django.contrib.auth.views.login', name = 'login'),
    
    # Logout Link
    url(r'logout/$', 'django.contrib.auth.views.logout', 
        { 'next_page':'/'}, name='login'),

    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Change this to redirect the home view to an app
    #url(regex=r'^$', view= RedirectView.as_view(url='/appname')),
                   
    # change this to include the app you create
    #url(r'^appname/', include('appname.urls')),
                       
    # Admin url at /manage instead of /admin #
    url(r'^manage/', include(admin.site.urls)),
)

# Enables serving of static files on local server
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
