from django.urls import path
# from .views import PostDetail, PostList, UserDetail, UserList
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

# Not using viewsets
# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view())
# ]

# Using view sets

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls
