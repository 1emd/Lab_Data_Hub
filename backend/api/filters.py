from django_filters.rest_framework import (FilterSet, UUIDFilter)
from api.models import ResearchResult


class ResearchResultFilter(FilterSet):
    lab_id = UUIDFilter(field_name='lab_id__id')

    class Meta:
        model = ResearchResult
        fields = ['lab_id']
