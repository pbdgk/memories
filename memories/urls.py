from django.urls import path
from . import views

app_name = "memories"

urlpatterns = [
    path('', views.Index.as_view(), name='main'),
    path('<str:username>/', views.MemoryListView.as_view(), name="list"),
    path('<str:username>/create/', views.MemoryCreateView.as_view(), name="create"),
    path('<str:username>/create-embed/', views.MemoryEmbedView.as_view(), name="embed"),
    path('<str:username>/<int:pk>/', views.MemoryDetailView.as_view(), name='detail'),
    path('<str:username>/<int:pk>/edit/', views.MemoryEditView.as_view(), name='edit'),
    path('<str:username>/<int:pk>/delete/', views.MemoryDeleteView.as_view(), name='delete'),

]