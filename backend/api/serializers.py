from rest_framework import serializers
from api.models import (Tests, Scores, IndicatorMetric, Reference,
                        Metrics, Indicators, Labs,)


class LabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labs
        fields = '__all__'


class IndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicators
        fields = '__all__'


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tests
        fields = '__all__'


class IndicatorMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorMetric
        fields = '__all__'


class ScoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scores
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reference
        fields = '__all__'


class ResultSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    score = serializers.DecimalField(max_digits=10, decimal_places=5)
    indicator_name = serializers.CharField()
    metric_name = serializers.CharField()
    metric_unit = serializers.CharField()
    is_within_normal_range = serializers.BooleanField()


class ResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    lab_id = serializers.UUIDField()
    duration_seconds = serializers.SerializerMethodField()
    # duration_seconds = serializers.IntegerField()
    # results = ResultSerializer(many=True)
    results = ResultSerializer(many=True, source='result_set')

    def get_duration_seconds(self, obj):
        # Получаем время начала и завершения исследования
        started_at = obj.started_at
        completed_at = obj.completed_at

        time_difference = completed_at - started_at
        duration_seconds = time_difference.total_seconds()
        return duration_seconds


# class TestResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TestResult
#         fields = '__all__'


# class TestSerializer(serializers.ModelSerializer):
#     scores = ScoresSerializer(many=True, read_only=True)

#     class Meta:
#         model = Tests
#         fields = '__all__'

#     def get_lab_results(self, obj):
#         scores = Scores.objects.filter(test_id=obj.id, is_active=True)
#         results = []

#         for score in scores:
#             indicator_metric = IndicatorMetric.objects.get(
#                 id=score.indicator_metric_id_id)
#             indicator = Indicators.objects.get(
#                 id=indicator_metric.indicator_id_id)
#             metric = Metrics.objects.get(id=indicator_metric.metric_id_id)

#             results.append({
#                 "id": score.id,
#                 "score": str(score.score),
#                 "indicator_name": indicator.name,
#                 "metric_name": metric.name,
#                 "metric_unit": metric.unit,
#                 "is_within_normal_range": score.is_within_normal_range,
#             })

#         return {
#             "id": obj.id,
#             "lab_id": obj.lab_id.id,
#             "duration_seconds": (obj.completed_at - obj.started_at).seconds,
#             "results": results,
#         }
