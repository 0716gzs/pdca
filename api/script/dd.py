# """
# 请假processCode=PROC-EF6YNNYRN2-CRQI0Q3ZSC7L2TDQEKQO1-25SLJQZI-ST
# 加班processCode=PROC-EF6YNNYRN2-CRQI0Q3ZSC7L2TDQEKQO1-XZRLJQZI-GT
# 补卡processCode=PROC-EF6YNNYRN2-CRQI0Q3ZSC7L2TDQEKQO1-V2SLJQZI-NT
# """
# import json
# import time
#
# import requests
#
#
# # 获取审批信息
# class ProcessInstance:
#     def __init__(self, process_code: str, start_time: int, end_time: int, userid: str):
#         self.process_code = process_code
#         self.start_time = start_time
#         self.end_time = end_time
#         self.userid = userid
#
#     # 获取审批实例id列表
#     def processinstance_list(self):
#         post_url = "https://oapi.dingtalk.com/topapi/processinstance/listids?access_token=%s" % (access_token())
#         data = {
#             "process_code": self.process_code,
#             "start_time": self.start_time - 2678400000,
#             "end_time": self.end_time + 2678400000,
#             "userid_list": self.userid,
#             "size": 20,
#             "cursor": 0,
#         }
#         response = requests.post(post_url, data)
#         str_res = response.text
#         result = (json.loads(str_res)).get('result').get("list")
#         return result
#
#     # 获取审批实例详情
#     def getprocessinstance_details(self):
#         lists = self.processinstance_list()
#         response_list = []
#         for i in lists:
#             post_url = "https://oapi.dingtalk.com/topapi/processinstance/get?access_token=%s" % (access_token())
#             data = {
#                 "process_instance_id": i,
#             }
#             response = requests.post(post_url, data)
#             str_res = response.text
#             result = (json.loads(str_res)).get('process_instance')
#             status = self.status_CN(result.get("status"))
#             form_component_values = result.get("form_component_values")
#             types = [x.get('value') for x in form_component_values if x.get("component_type") == "DDSelectField"][0]
#             s_times = [(json.loads(x.get('value')))
#                        for x in form_component_values if x.get("component_type") == "DDDateRangeField"][0][0]
#             if self.start_time <= self.date_to_UNIX(s_times) <= self.end_time:
#                 e_times = [(json.loads(x.get('value')))
#                            for x in form_component_values if x.get("component_type") == "DDDateRangeField"][0][1]
#                 days = [(json.loads(x.get('value')))
#                         for x in form_component_values if x.get("component_type") == "DDDateRangeField"][0][2]
#                 text = [x.get('value') for x in form_component_values if x.get("component_type") == "TextareaField"][0]
#                 response_list.append(
#                     {"status": status, "types": types, "s_times": s_times, "e_times": e_times, "days": days,
#                      "text": text})
#         print(response_list)
#         return response_list
#
#     # 获取天数
#     def getprocessinstance_days(self):
#         lists = self.processinstance_list()
#         days = 0
#         for i in lists:
#             post_url = "https://oapi.dingtalk.com/topapi/processinstance/get?access_token=%s" % (access_token())
#             data = {
#                 "process_instance_id": i,
#             }
#             response = requests.post(post_url, data)
#             str_res = response.text
#             try:
#                 form_component_values = (json.loads(str_res)).get('process_instance').get("form_component_values")
#                 num = self.date_to_UNIX([(json.loads(x.get('value')))
#                                          for x in form_component_values if
#                                          x.get("component_type") == "DDDateRangeField"][
#                                             0][0])
#                 if self.start_time <= num <= self.end_time:
#                     days += float([(json.loads(x.get('value')))
#                                    for x in form_component_values if x.get("component_type") == "DDDateRangeField"][0][
#                                       2])
#             except AttributeError:
#                 pass
#         return days
#
#     @staticmethod
#     def date_to_UNIX(date: str):
#         return int(time.mktime(time.strptime(date, "%Y-%m-%d"))) * 1000
#
#     @staticmethod
#     def status_CN(status: str):
#         if status == "NEW":
#             return "新创建"
#         elif status == "RUNNING":
#             return "审批中"
#         elif status == "COMPLETED":
#             return "已完成"
#         elif status == "CANCELED":
#             return "已取消"

import requests
import json


class Dd(object):
    def getToken(self):
        '''获取钉钉的token:return: 钉钉token'''
        url = 'https://oapi.dingtalk.com/gettoken?appkey=XXXXXXXXXXXXXXXXX&appsecret=XXXXXXXXXXXXXXXXXXXXXXXXXX'
        req = requests.get(url)
        req = json.loads(req.text)
        return req['access_token']

    def createCallbackDd(self, request):
        '''注册钉钉回调函数:return:'''
        url = 'https://oapi.dingtalk.com/call_back/register_call_back?access_token=' + self.getToken()
        data = {"call_back_tag": ["bpms_task_change",
                                  "bpms_instance_change"]}

        # 这两个回调种类是审批的"token": TOKEN,  #自定义的字符串"aes_key": AES_KEY, #自定义的43位字符串，密钥"url": URL  #回调地址}requests.post(url, data=json.dumps(data))return HttpResponse('OK')

    def create(self, request):
        '''创建钉钉审批:param request::return:'''
        url = 'https://oapi.dingtalk.com/topapi/processinstance/create?access_token=' + self.getToken()
        form_component_value_vo = [{'name': '姓名', 'value': '测试2'}, {'name': '部门', 'value': '测试2'},
                                   {'name': '["开始时间","结束时间"]',
                                    'value': '["2019-06-10 10:32","2019-06-10 10:36"]'},
                                   {'name': '加班事由',
                                    'value': '测试2'}]  # 钉钉后台配置的需要填写的字段（这一段由点到传过来实现，这里只是测试使用）data = {'agent_id': None,'process_code': 'XXXXXXXXXXXXXXXX',  #工单id'originator_user_id': 'manager2606', #创建人的钉钉userid'dept_id': -1,  #创建人的钉钉部门id'form_component_values': str(form_component_value_vo), #钉钉后台配置的需要填写的字段}response = requests.post(url, data=data)print(response.text)return HttpResponse('成功')


dd = Dd()
print(dd.getToken())
