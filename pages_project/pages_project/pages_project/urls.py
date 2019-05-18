"""
Definition of urls for pages_project.
"""

from django.contrib import admin
from django.urls import path, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    # url(r'^$', pages_project.views.home, name='home'),
    # url(r'^pages_project/', include('pages_project.pages_project.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
