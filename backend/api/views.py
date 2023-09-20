from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from api.models import (Tests, Scores, IndicatorMetric, Metrics,
                        Indicators, Labs, Reference, ResearchResult)
from api.serializers import (TestSerializer, LabsSerializer,
                             IndicatorsSerializer, MetricsSerializer,
                             IndicatorMetricSerializer, ScoresSerializer,
                             ReferenceSerializer, ResearchResultSerializer,
                             MeasurementResult)


class LabsViewSet(ModelViewSet):
    queryset = Labs.objects.all()
    serializer_class = LabsSerializer


class IndicatorsViewSet(ModelViewSet):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer


class MetricsViewSet(ModelViewSet):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer


class IndicatorMetricViewSet(ModelViewSet):
    queryset = IndicatorMetric.objects.all()
    serializer_class = IndicatorMetricSerializer


class ScoresViewSet(ModelViewSet):
    queryset = Scores.objects.all()
    serializer_class = ScoresSerializer


class ReferenceViewSet(ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class TestsViewSet(ModelViewSet):
    queryset = Tests.objects.all()
    serializer_class = TestSerializer


class ResearchResultViewSet(ModelViewSet):
    queryset = ResearchResult.objects.all()
    serializer_class = ResearchResultSerializer

    def list(self, request):
        lab_id = self.request.query_params.get('lab_id')
        if lab_id:
            research_results = ResearchResult.objects.filter(lab_id=lab_id)
            serializer = ResearchResultSerializer(research_results, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'lab_id parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
