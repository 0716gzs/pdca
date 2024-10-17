import json
from datetime import datetime
from django.db import transaction
from django.db.models import Q
from rest_framework import status
from rest_framework.fields import CharField, ListField, IntegerField
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.plan.models import Plan
from apps.plan.serials import PlanSerializer
from common import const
from common.exceptions import ParamError
from common.utils.time_conversion import convert_iso_to_normal_time_with_timezone
from common.views import BaseModelViewSet, RowDict, BaseParam, page_query_set, BaseApiView


class PlanViewSet(BaseModelViewSet):
    queryset = Plan.objects.all().select_related('user').order_by('id')
    serializer_class = PlanSerializer
    edit_serializer_class = PlanSerializer

    def create(self, request, *args, **kwargs):
        _data = request.data
        plan_bulk_create_list = []
        user_id = request.user_id
        for data in _data:
            data = RowDict(data)
            start_time = convert_iso_to_normal_time_with_timezone(data.datatime[0])
            end_time = convert_iso_to_normal_time_with_timezone(data.datatime[1])
            plan_bulk = Plan(name=data.name, level=data.level, start_time=start_time, end_time=end_time, user_id=user_id)
            plan_bulk_create_list.append(plan_bulk)
        Plan.objects.bulk_create(plan_bulk_create_list)
        return self.success_response()

    def custom_filter(self, request, queryset):
        """子类可重写"""
        if request.user_id:
            queryset = queryset.filter(user_id=request.user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = self.custom_filter(request, queryset)

        page, page_size = self.get_page_param(request)
        result = page_query_set(queryset, page=page, page_size=page_size, serializer=self.serializer_class)
        if result.get('data'):
            self.fill_result(result.get('data'))
        return Response(result)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_filter_object({'user_id': request.user_id})
        serializer = self.get_serializer(instance)
        return self.success_response(serializer.data)


