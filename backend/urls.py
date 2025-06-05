# from django.conf import settings
# from django.conf.urls.static import static  # 👈 This is the missing import

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('accounts.urls')),
    path('', include('aife.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)