"""monitorias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerSplitView
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from accounts.views import UserViewSet, CurrentUserUpdateView
from core.views import CursoViewSet, DisciplinaViewSet
from forum_amo.views import DuvidaViewSet

router = routers.DefaultRouter()
router.register(r"cursos", CursoViewSet, basename="cursos")
router.register(r"disciplinas", DisciplinaViewSet, basename="disciplinas")
router.register(r"usuario", UserViewSet, basename="usuario")
router.register(r"duvidas", DuvidaViewSet, basename="duvidas")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuario/login/", auth_views.obtain_auth_token, name="obtain-api-token"),
    path(  # precisa incluir antes do router para funcionar
        "usuario/eu/",
        CurrentUserUpdateView.as_view({"patch": "partial_update"}),
        name="usuario_atual",
    ),
    path("", include(router.urls)),
    # documentação/drf_spectacular
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/openapi/",
        SpectacularSwaggerSplitView.as_view(url_name="schema"),
        name="openapi",
    ),
    path("api-auth/", include("rest_framework.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
