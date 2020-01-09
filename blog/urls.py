from django.urls import path
from blog.views import AboutView,PostListView,PostDetailView,CreatePostView,PostUpdateView,PostDeleteView,DraftPostView,add_comment_to_post,commnet_approve,commnet_remove,post_publish

app_name='blog'
urlpatterns=[
    path('',PostListView.as_view(),name='post_list'),
    path('about/',AboutView.as_view(),name='about'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',PostDeleteView.as_view(),name='post_remove'),
    path('draft/',DraftPostView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',add_comment_to_post,name='add_comment_to_post'),
    path('post/<int:pk>/approved/',commnet_approve,name='commnet_approve'),
    path('post/<int:pk>/remove/',commnet_remove,name='commnet_remove'),
    path('post/<int:pk>/publish/',post_publish,name='post_publish'),
]
