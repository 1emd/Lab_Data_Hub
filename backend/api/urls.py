from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (LabsViewSet, TestsViewSet, IndicatorsViewSet,
                       MetricsViewSet, IndicatorMetricViewSet, ScoresViewSet,
                       ReferenceViewSet, ResearchResultViewSet)

router = DefaultRouter()

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('labs', LabsViewSet, basename='labs')
v1_router.register('tests', TestsViewSet, basename='tests')
v1_router.register('indicators', IndicatorsViewSet, basename='indicators')
v1_router.register('metrics', MetricsViewSet, basename='metrics')
v1_router.register('indicator-metrics', IndicatorMetricViewSet,
                   basename='indicator-metrics')
v1_router.register('scores', ScoresViewSet, basename='scores')
v1_router.register('references', ReferenceViewSet, basename='references')
v1_router.register('test-results', ResearchResultViewSet,
                   basename='test-results')


urlpatterns = [
    path('', include(v1_router.urls)),
    # path('', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
]
