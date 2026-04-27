from django.contrib import admin
from django.urls import path
from management import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔐 Default page → LOGIN
    path('', views.login_view, name='login'),

    # 🏠 Landing page AFTER login
    path('home/', views.landing_home, name='landing_home'),
    

    # 🚢 Ships page
    path('ships/', views.ships, name='ships'),
    

    # 🔍 Ship detail
    path('ship/<int:ship_id>/', views.ship_detail, name='ship_detail'),

    # ℹ️ About page
    path('about/', views.about, name='about'),

    # Register & logout
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # Serve media files in production using WhiteNoise-compatible approach
    from django.views.static import serve
    from django.urls import re_path
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]