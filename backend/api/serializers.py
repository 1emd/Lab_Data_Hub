from rest_framework import serializers
from api.models import (Tests, Scores, IndicatorMetric, Reference,
                        Metrics, Indicators, Labs, ResearchResult,
                        MeasurementResult, User)
from django.shortcuts import get_object_or_404


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')


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
    duration_seconds = serializers.SerializerMethodField()
    # lab_id = serializers.CharField(write_only=True)
    # lab_name = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Tests
        fields = '__all__'

    def get_duration_seconds(self, obj):
        if obj.started_at and obj.completed_at:
            duration = (obj.completed_at - obj.started_at).total_seconds()
            return int(duration)
        return None

    # def create(self, validated_data):
    #     lab_id = validated_data.pop('lab_id', None)
    #     lab_name = validated_data.pop('lab_name', None)

    #     if lab_id is None and lab_name:
    #         try:
    #             lab_id = uuid.UUID(lab_name)
    #         except ValueError:
    #             lab = Labs.objects.filter(name=lab_name).first()
    #             if lab:
    #                 lab_id = lab.id

    #     if lab_id:
    #         validated_data['lab_id'] = lab_id

    #     return Tests.objects.create(**validated_data)


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
    # score = serializers.CharField(source='score.score')
    # indicator_name = serializers.CharField(source='indicator_name.name')
    # metric_name = serializers.CharField(source='metric_name.name')
    # metric_unit = serializers.CharField(source='metric_unit.unit')
    indicator_name = serializers.CharField(
        source='score.indicator_metric_id.indicator_id.name')
    metric_name = serializers.CharField(
        source='score.indicator_metric_id.metric_id.name')
    metric_unit = serializers.CharField(
        source='score.indicator_metric_id.metric_id.unit')
    is_within_normal_range = serializers.SerializerMethodField()

    class Meta:
        model = MeasurementResult
        fields = '__all__'

    # def get_is_within_normal_range(self, obj):
    #     return (obj.score.score >= obj.indicator_name.references.min_score and
    #             obj.score.score <= obj.indicator_name.references.max_score)

    def get_is_within_normal_range(self, obj):
        try:
            reference = obj.indicator_name.indicator_metrics.first().metric_id.references.first()
            if reference:
                min_score = reference.min_score
                max_score = reference.max_score
                return (min_score <= obj.score.score <= max_score)
        except AttributeError:
            pass
        return False


class ResearchResultSerializer(serializers.ModelSerializer):
    lab_id = serializers.UUIDField(source='lab_id.id')
    # duration_seconds = TestSerializer()
    results = MeasurementResultSerializer(
        many=True, read_only=True)

    class Meta:
        model = ResearchResult
        fields = ['id', 'lab_id', 'duration_seconds', 'results']

    def get_lab_id(self, obj):
        return str(obj.lab_id)


class MeasurementResultCreateSerializer(serializers.ModelSerializer):
    lab_id = serializers.UUIDField()

    class Meta:
        model = MeasurementResult
        fields = ['score', 'indicator_name',
                  'metric_name', 'metric_unit', 'lab_id']

    def create(self, validated_data):
        lab_id = validated_data.pop('lab_id')
        lab = get_object_or_404(Labs, id=lab_id)
        measurement_result = MeasurementResult.objects.create(**validated_data)
        lab.measurement_results.add(measurement_result)
        return measurement_result


class ResearchResultCreateSerializer(serializers.ModelSerializer):
    lab_id = serializers.UUIDField()
    results = MeasurementResultCreateSerializer(many=True)

    class Meta:
        model = ResearchResult
        fields = ['lab_id', 'duration_seconds', 'results']

    def create(self, validated_data):
        lab_id = validated_data.pop('lab_id')
        lab = get_object_or_404(Labs, id=lab_id)
        measurement_results_data = validated_data.pop('results')
        research_result = ResearchResult.objects.create(**validated_data)
        for measurement_result_data in measurement_results_data:
            measurement_result_data['lab_id'] = lab_id
            measurement_result = MeasurementResult.objects.create(
                **measurement_result_data)
            research_result.results.add(measurement_result)
        return research_result
