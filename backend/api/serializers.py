from rest_framework import serializers
from api.models import (Tests, Scores, IndicatorMetric, Reference,
                        Metrics, Indicators, Labs, ResearchResult,
                        MeasurementResult)


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
    # duration_seconds = serializers.IntegerField()

    class Meta:
        model = Tests
        fields = '__all__'

    # def get_duration_seconds(self, obj):
    #     duration = (obj.completed_at - obj.started_at).total_seconds()
    #     return duration


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


class MeasurementResultSerializer(serializers.ModelSerializer):
    score = serializers.CharField(source='score.score')
    indicator_name = serializers.CharField(source='indicator_name.name')
    metric_name = serializers.CharField(source='metric_name.name')
    metric_unit = serializers.CharField(source='metric_unit.unit')

    class Meta:
        model = MeasurementResult
        fields = '__all__'


class ResearchResultSerializer(serializers.ModelSerializer):
    lab_id = serializers.UUIDField(source='lab_id.id')
    measurement_results = MeasurementResultSerializer(
        many=True, read_only=True)

    class Meta:
        model = ResearchResult
        fields = ['id', 'lab_id', 'duration_seconds', 'measurement_results']

    def get_lab_id(self, obj):
        return str(obj.lab_id)
