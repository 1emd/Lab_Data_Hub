from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import (Tests, Scores, IndicatorMetric, Metrics,
                        Indicators, Labs, Reference,)
from api.serializers import (TestSerializer, LabsSerializer,
                             IndicatorsSerializer, MetricsSerializer,
                             IndicatorMetricSerializer, ScoresSerializer,
                             ReferenceSerializer, ResponseSerializer)


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

    # @action(detail=False, methods=['GET'])
    # def lab_results(self, request):
    #     lab_id = request.query_params.get('lab_id')

    #     if not lab_id:
    #         return Response({"error": "lab_id query parameter is required."},
    #                         status=400)

    #     lab = Labs.objects.filter(id=lab_id).first()
    #     if not lab:
    #         return Response({"error": "Lab not found."}, status=404)

    #     tests = Tests.objects.filter(lab_id=lab_id, is_active=True)
    #     serializer = TestSerializer(tests, many=True)

    #     return Response(serializer.data)


class TestResultListView(ModelViewSet):
    queryset = Tests.objects.all()
    serializer_class = ResponseSerializer


# class TestResultViewSet(ModelViewSet):
#     queryset = TestResult.objects.all()
#     serializer_class = TestResultSerializer

#     def perform_create(self, serializer):
#         instance = serializer.save()
#         instance.calculate_average_score()
#         instance.save()
