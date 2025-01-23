from django.urls import path
from .views import MembroListView, MembroDetailView, MembroCreateView, MembroUpdateView, MembroDeleteView

urlpatterns = [
    path('', MembroListView.as_view(), name='membro_list'),
    path('<int:pk>/', MembroDetailView.as_view(), name='membro_detail'),
    path('novo/', MembroCreateView.as_view(), name='membro_create'),
    path('<int:pk>/editar/', MembroUpdateView.as_view(), name='membro_update'),
    path('<int:pk>/deletar/', MembroDeleteView.as_view(), name='membro_delete'),
]
