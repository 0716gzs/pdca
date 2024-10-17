from apps.plan.models import *
from common.serials import BaseSerializer


class PlanSerializer(BaseSerializer):
    class Meta:
        model = Plan
        fields = ('id', 'name', 'start_time', 'end_time', 'level', 'user')
