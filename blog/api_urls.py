from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .viewsets import AutorViewSet, EditoraViewSet, UserViewSet

router = SimpleRouter()
router.register(r'autores', AutorViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'users', UserViewSet)

#app_name = 'blog.api'

urlpatterns = [
    path('', include(router.urls)),
]