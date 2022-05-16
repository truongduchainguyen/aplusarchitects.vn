from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password/reset/', views.password_reset, name='password-reset'),
    path('password/reset/done/', views.password_reset_done,
         name='password-reset-done'),
    re_path(
        'password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.password_reset_confirm, name='password-reset-confirm'
    ),
    path('password/reset/complete/', views.password_reset_complete,
         name='password-reset-complete'),
    path('site-setting/', include(('app.dashboard.sitesetting.urls',
                                   'sitesetting'), namespace='sitesetting')),
    path('account/', include(('app.dashboard.account.urls',
                              'account'), namespace='account')),
    path('blog/', include(('app.dashboard.blog.urls',
                           'blog'), namespace='blog')),
    path('service/', include(('app.dashboard.service.urls',
                              'service'), namespace='service')),
    path('portfolio/', include(('app.dashboard.portfolio.urls',
                                'portfolio'), namespace='portfolio')),
]
