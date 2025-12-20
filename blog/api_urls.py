from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .viewsets import AutorViewSet, EditoraViewSet

router = SimpleRouter()
router.register(r'autores', AutorViewSet)
router.register(r'editoras', EditoraViewSet)


#app_name = 'blog.api'

urlpatterns = [
    path('', include(router.urls)),
]