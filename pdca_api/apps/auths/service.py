import logging
import random

from apps.auths.models import *
from common.services import BaseService
from common.middles.token import AppTokenService
from conf import settings

logger = logging.getLogger(__name__)


class AccountService(BaseService):
    model = User

    @classmethod
    def generate(cls):
        # 生成11位数的账号
        second_spot1 = random.choice([i for i in range(1, 10) if i != 6])
        second_spot = random.choice([3, 4, 5, 7, 8])
        third_spot = {3: random.randint(0, 9),
                      4: random.choice([5, 7, 9]),
                      5: random.choice([i for i in range(10) if i != 4]),
                      7: random.choice([i for i in range(10) if i not in [4, 9]]),
                      8: random.randint(0, 9), }[second_spot]
        remain_spot = random.randint(1, 10000000)
        num = "{}{}{}{}".format(second_spot1, second_spot, third_spot, remain_spot)
        return num

    @classmethod
    def get_account(cls, pk):
        account = User.objects.get_or_none(pk=pk)
        return account

    @classmethod
    def get_login_token(cls, account):
        token = AppTokenService.create_token(account.id)
        return token

    @classmethod
    def get_login_token_payload(cls, token: str, verify: bool = True):
        payload = AppTokenService.get_payload(token, verify=verify)
        return payload

    @classmethod
    def get_login_token_refresh_token(cls, account):
        token = AppTokenService.create_token(account.id, settings.JWT_EXPIRE_IN_REFRESH)
        return token


class RoleService(BaseService):
    @classmethod
    def set_user_role(cls, user_id: int, roles: list):
        UserRole.objects.filter(user_id=user_id).remove()
        bulk = [UserRole(user_id=user_id, role_id=role) for role in roles if Role.objects.get_or_none(pk=role)]
        UserRole.objects.bulk_create(bulk)

    @classmethod
    def user_role_names(cls, user_id):
        return [ur.role.name for ur in UserRole.objects.filter(user_id=user_id)]


# class DepartmentService(BaseService):
#     @classmethod
#     def set_user_department(cls, user_id: int, departments: list):
#         UserDepartment.objects.filter(user_id=user_id).remove()
#         bulk = [UserDepartment(user_id=user_id, department_id=d) for d in departments if
#                 Department.objects.get_or_none(pk=d)]
#         UserDepartment.objects.bulk_create(bulk)

class Tree:
    @classmethod
    def xtree(cls, data):
        data_list = []
        for d in data:
            if d['parent_id'] is None:
                d.setdefault('children', [])
                data_list.append(d)
            for dd in data:
                if dd['parent_id'] == d['id']:
                    d.setdefault('children', []).append(dd)
        return data_list
    # def xtree(cls, data):
    #     if not data:
    #         return data
    #     tree = {}
    #     list = []
    #     for i in data:
    #         tree[i['id']] = i
    #     for j in data:
    #         tree_level = j['tree_level']
    #         if tree_level == 0:
    #             list.append(j)
    #         else:
    #             if 'children' not in tree[tree_level]:
    #                 tree[tree_level]['children'] = []
    #             tree[tree_level]['children'].append(j)
    #     return list
