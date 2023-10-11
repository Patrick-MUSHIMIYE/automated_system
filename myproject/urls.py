"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from student_inquiries import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from facilitators import views as fac_views
import debug_toolbar

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
    re_path(r'^$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^home2/$', fac_views.home2, name='home2'),
    re_path(r'^board/$', views.board, name='board'),
    re_path(r'form/$', views.reply, name='reply'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^post/$', views.post_request, name='post_request'),
    re_path(r'^fac_post/$', fac_views.fac_post, name='fac_post'),
    re_path(r'^reply/$', views.reply_to_post, name='reply_to_post'),
    
    # re_path(r'^reply_to_post/$', views.reply_to_post, name='reply_to post'),
    
    # re_path(r'reply/$', reply_views.reply_form, name='post_reply'),
    # re_path(r'^replies/$', reply_views.post_reply, name='replies'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)