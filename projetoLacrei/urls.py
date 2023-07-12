from django.urls import include, path
from rest_framework.routers import DefaultRouter
from LacreiApp import views

router = DefaultRouter()
router.register(r'pessoas-profissionais', views.PessoaProfissionalViewSet)
router.register(r'consultas', views.ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
