from django.urls import path, include
from .views.views import home, about, progress, visualization
from .views.write_progress import progress_view
from .views.register_login import login_view, register
from django.conf import settings
from django.conf.urls.static import static

#  앱의 URL 패턴을 정의하는 파일, URL 요청을 뷰 함수와 연결하는 역할을 함

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('progress/', progress, name='progress'),
    path('progress/write', progress_view, name='progress_write'),
    path('visualization/', visualization, name='visualization'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('django_plotly_dash/', include('django_plotly_dash.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)