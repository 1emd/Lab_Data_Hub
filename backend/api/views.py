from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from api.models import (Tests, Scores, IndicatorMetric, Metrics,
                        Indicators, Labs, Reference, ResearchResult)
from api.serializers import (TestSerializer, LabsSerializer,
                             IndicatorsSerializer, MetricsSerializer,
                             IndicatorMetricSerializer, ScoresSerializer,
                             ReferenceSerializer, ResearchResultSerializer,
                             ResearchResultCreateSerializer)
from api.filters import ResearchResultFilter


# class UserCreateViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = CustomUserCreateSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response(
#                 {"message": "User created successfully", "user_id": user.id},
#                 status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def create(self, request, *args, **kwargs):
        serializer = ResearchResultCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

#     def list(self, request):
#         lab_id = self.request.query_params.get('lab_id')
#         if lab_id:
#             research_results = ResearchResult.objects.filter(lab_id=lab_id)
#             serializer = ResearchResultSerializer(research_results, many=True)
#             return Response(serializer.data)
#         else:
#             return Response({'error': 'lab_id parameter is required'},
#                             status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=False, methods=['GET'])
    # def lab_results(self, request):
    #     lab_id = request.query_params.get('lab_id')
    #     if lab_id:
    #         research_results = ResearchResult.objects.filter(lab_id=lab_id)
    #         serializer = ResearchResultSerializer(research_results, many=True)
    #         return Response(serializer.data)
    #     else:
    #         return Response({'error': 'lab_id parameter is required'},
    #                         status=status.HTTP_400_BAD_REQUEST)
