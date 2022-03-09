
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from youtube_app.views import MijizAPIView, MijozRUD, PlaylistRUD,CommentAPIView,PlaylistAPIView,VideoAPIView,CommentD,VideoD

schema_view = get_schema_view(
   openapi.Info(
      title="Youtube clone API",
      default_version='v1',
      description="Youtube clone versiyasi",
      contact=openapi.Contact("Asrorbek Xursanaliyev <asrorxursanaliyev@gmail.com>, <+998993205707>"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mijoz/', MijizAPIView.as_view()),
    path('mijoz/<int:pk>/', MijozRUD.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:pk>/', CommentD.as_view()),
    path('video/', VideoAPIView.as_view()),
    path('video/<int:pk>/', VideoD.as_view()),
    path('playlist/', PlaylistAPIView.as_view()),
    path('playlist/<int:pk>/', PlaylistRUD.as_view()),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),
    path('doc/', schema_view.with_ui("redoc", cache_timeout=0), name="redoc-doc"),
]
