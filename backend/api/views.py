from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
# from rest_framework.generics import RetrieveAPIView
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from api.models import (Tests, Scores, IndicatorMetric, Metrics,
                        Indicators, Labs, Reference,)
from api.serializers import (TestSerializer, LabsSerializer,
                             IndicatorsSerializer, MetricsSerializer,
                             IndicatorMetricSerializer,
                             ReferenceSerializer, ScoreSerializer)
from api.filters import TestFilter


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
    serializer_class = ScoreSerializer


class ReferenceViewSet(ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class TestsViewSet(ModelViewSet):
    queryset = Tests.objects.all()
    serializer_class = TestSerializer


class StudyAPIView(ModelViewSet):
    queryset = Tests.objects.all()
    serializer_class = TestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TestFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['test_id'] = self.kwargs.get('pk')
        return context

    def get_object(self):
        test_id = self.kwargs.get('pk')
        try:
            return Tests.objects.get(id=test_id)
        except Tests.DoesNotExist:
            return None

# class ResearchResultViewSet(ModelViewSet):
#     queryset = ResearchResult.objects.all()
#     serializer_class = ResearchResultWithResultsSerializer

#     def get_queryset(self):
#         # Изменяем запрос для включения связанных данных о лаборатории
#         queryset = super().get_queryset().select_related('lab_id')
#         return queryset
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ResearchResultFilter

    # def get_queryset(self):
    #     lab_id = self.kwargs.get('lab_id')
    #     return ResearchResult.objects.filter(lab_id=lab_id)

    # def perform_create(self, serializer):
    #     # Получите данные из запроса
    #     data = self.request.data

    #     # Извлеките ID измерений из запроса
    #     measurement_result_ids = data.get('measurement_results', [])

    #     # Создайте тест
    #     test = serializer.save()

    #     # Проверьте, что есть ID измерений
    #     if measurement_result_ids:
    #         measurement_results = []

    #         # Получите объекты MeasurementResult по ID
    #         for measurement_result_id in measurement_result_ids:
    #             try:
    #                 measurement_result = MeasurementResult.objects.get(
    #                     id=measurement_result_id)
    #                 measurement_results.append(measurement_result)
    #             except MeasurementResult.DoesNotExist:
    #                 # Если ID измерения не существует, верните ошибку
    #                 return Response({"error": f"MeasurementResult with ID {measurement_result_id} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    #         # Свяжите измерения с тестом
    #         test.measurement_results.set(measurement_results)
    #         test.save()

    #     return test


# class ResearchResultViewSet(ModelViewSet):
#     queryset = ResearchResult.objects.all()
#     serializer_class = ResearchResultSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = ResearchResultCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ResearchResultViewSet(ModelViewSet):
#     queryset = ResearchResult.objects.all()
#     serializer_class = ResearchResultSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = ResearchResultFilter

#     def retrieve(self, request, pk=None):
#         lab_id = pk
#         queryset = ResearchResult.objects.filter(lab_id=lab_id)
#         serializer = ResearchResultSerializer(queryset, many=True)
#         return Response(serializer.data)

#     # def list(self, request):
#     #     lab_id = self.request.query_params.get('lab_id')
#     #     if lab_id:
#     #         research_results = ResearchResult.objects.filter(lab_id=lab_id)
#     #         serializer = ResearchResultSerializer(research_results, many=True)
#     #         return Response(serializer.data)
#     #     else:
#     #         return Response({'error': 'lab_id parameter is required'},
#     #                         status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request):
#         lab_id = self.request.query_params.get('lab_id')
#         if lab_id:
#             lab = Labs.objects.get(id=lab_id)
#             lab_results = lab.results.all()
#             serializer = ResearchResultSerializer(lab_results, many=True)
#             return Response(serializer.data)
#         else:
#             return Response({'error': 'lab_id parameter is required'},
#                             status=status.HTTP_400_BAD_REQUEST)
