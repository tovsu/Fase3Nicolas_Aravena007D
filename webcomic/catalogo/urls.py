from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,                                  name='index'),
    path('estante/'      ,views.estante,                  name='estante'),
    path('compra/'       ,views.compra,                   name='compra'), 
    path('vendidos/'     ,views.vendidos,                 name='vendidos'),
    path('comic_lista/'  ,views.comicListView.as_view(),  name='comics'),
    
    
]

#URL COMIC
urlpatterns += [
    path('comic/create/', views.comicCreate.as_view(), name='comic_create'),
    path('comic_lista/',views.comicListView.as_view(),  name='comic_lista'),
    path('comic/<id>/', views.comicUpdate.as_view(), name='comic_update'),
    path('comic/<uuid:pk>', views.comicDelete.as_view(), name='comic_delete'),
    path('comic/<uuid:pk>',views.comicDetailView.as_view(),name='comic_especificacion'),
]