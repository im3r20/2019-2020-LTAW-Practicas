from django.urls import path

# -- Importar todas las vistas de mi_tienda
from . import views

# -- Aquí se definen las URLs de nuestra tienda
# -- Metemos de momento sólo la principal (índice)

urlpatterns = [
    # -- Vista pricipal (índice)
    path('', views.index, name='index'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test3, name='test2'),
    path('test3/', views.test3, name='test3'),
    path('test4/', views.test4, name='test4'),
    path('test5/', views.test5, name='test5'),
    path('list/', views.list, name='list'),
    path('p_<personaje>/', views.personajes, name='personajes'),
    path('recepcion1', views.recepcion1, name='recepcion1'),
]
