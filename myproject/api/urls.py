from django.urls import path
from . import views

urlpatterns = [
    path('components/', views.component_list),
    path('components/<int:id>/', views.component_detail),
    path('category/', admin.site.urls),
]
