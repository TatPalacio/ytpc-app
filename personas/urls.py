from rest_framework import routers
from .api import PersonaViewSet
from django.urls import path, include
from . import views
from .views import MedicoViewSet, authenticate_user

router=routers.DefaultRouter()
router.register('api/personas', PersonaViewSet, 'personas')
urlpatterns = [
    path('', views.index, name="index"),   
    path('api/', include(router.urls)),    
]
medico_list = MedicoViewSet.as_view({
    "get": "list",
    "post": "create",
    "put": "update",
    "delete": "destroy"
})

medico_detail = MedicoViewSet.as_view({
    "get": "retrieve"
})

urlpatterns = [
    path("clinica/api/authenticate", authenticate_user, name="authenticate"),
    path("clinica/api/medico", medico_list, name="medico-list"),
    path("clinica/api/medico/<str:tipo_documento>/<str:numero_documento>", medico_detail, name="medico-detail")
]