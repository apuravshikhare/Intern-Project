from Data import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.index,name='index'),
    
    path('First/',views.First, name='First'),

    path('upload/',views.upload, name= 'upload'),


    path('analysis/',views.analysis, name='analysis'),

    path('Second/',views.second, name='Second'),

    path('Third/',views.three,  name='three'),

    path('display',views.display, name='display'),

    path('visualizations',views.visualizations,name='visualizations')

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
