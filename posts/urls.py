from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, UserPostAPIView, UpvoteAPIView, CommentAPIView


urlpatterns = [
    path('', PostListAPIView.as_view()),
    path('<int:pk>/', PostDetailAPIView.as_view()),
    path('<int:pk>/upvote/', UpvoteAPIView.as_view()),
    path('<int:pk>/comment/', CommentAPIView.as_view()),
    path('<username>/', UserPostAPIView.as_view())
]