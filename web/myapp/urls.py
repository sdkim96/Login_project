from django.urls import path, include
from .views.home_views import home
from .views.about_views import about
from .views.progress_views import progressing
from .views.visualization_views import visualization
from .views.progress_write_views import progress_view
from .views.register_login import login_view, register
from django.conf import settings
from django.conf.urls.static import static
from django_plotly_dash.views import add_to_session
from django.views.generic import TemplateView
from .views.visualization_views import map


#  앱의 URL 패턴을 정의하는 파일, URL 요청을 뷰 함수와 연결하는 역할을 함

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('progress/', progressing, name='progress'),
    path('progress/write', progress_view, name='progress_write'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('visualization/', visualization, name='visualization'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('map/', map, name='map'),
    # path('BusStations/_dash-update-component', add_to_session, name='session_state'),
    # path('BusStations/', TemplateView.as_view(template_name='BusStations.html'), name="BusStations"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)