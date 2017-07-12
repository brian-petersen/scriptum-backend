from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse_lazy
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet
from wordstudies.views import VerseSearchViewSet, WordStudyViewSet, WordStudyCategoryViewSet, WordStudyNoteViewSet
# from wordstudies.views import search_verses

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'verses', VerseSearchViewSet, base_name='verses')
router.register(r'word-studies', WordStudyViewSet, base_name='wordstudies')
router.register(r'word-studies-categories', WordStudyCategoryViewSet, base_name='wordstudies-categories')
router.register(r'word-studies-notes', WordStudyNoteViewSet, base_name='wordstudies-notes')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^django-rq/', include('django_rq.urls')),

    url(r'^api/v1/', include('authentication.urls')),

    # url(r'^api/v1/verses/search/(?P<query>\w+)/$', search_verses),

    url(r'^api/v1/', include(router.urls)),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    url(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
