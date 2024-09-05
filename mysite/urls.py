
from django.contrib import admin
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap,TagSitemap
from django.views.generic.base import RedirectView
sitemaps = {
    
    'posts':PostSitemap,
    'tags': TagSitemap,
}


urlpatterns = [
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls',namespace='blog')         ),
    path(
        'sitemap.xml', 
        sitemap, 
        {'sitemaps': sitemaps}, 
        name='django.contrib.sitemaps.views.sitemap'
        ),
]
