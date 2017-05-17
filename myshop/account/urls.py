from django.conf.urls import url
from . import views
from shop import views as sviews
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', sviews.logout_page, name='logout'),
    url(r'^password_edit/$', views.password_edit, name='password_edit'),
    url(r'^user/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    # restore password urls
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    
]
