from django.conf import settings
import os
import time


# test_conf = {
# 	"business_code": "1900013511_10000",
# 	"contact_info": {
# 		"contact_email": "laixiumei@gome.email",
# 		"contact_name": "赖秀美",
# 		"contact_type": "SUPER",
# 		"mobile_phone": "15913154004",
# 	},
# 	"subject_info": {
# 		"subject_type": "SUBJECT_TYPE_ENTERPRISE",
# 		"business_license_info": {
# 			"legal_person": "张三",
# 			"license_address": "",
# 			"license_copy": "营业执照照片",
# 			"license_number": "注册号/统一社会信用代码",
# 			"merchant_name": "商户名称",
# 			"period_begin": "",
# 			"period_end": ""
# 		},
# 		"certificate_letter_copy": "",
# 		"finance_institution_info": {
# 			"finance_license_pics": ["0P3ng6KTIW4-Q_l2FjmFJBZR9FwczhJehHhAZN6BKXQPcs-VvdSo"],
# 			"finance_type": "BANK_AGENT"
# 		},
# 		"identity_info": {
# 			"authorize_letter_copy": "",
# 			"id_card_info": {
# 				"card_period_begin": "2026-06-06",
# 				"card_period_end": "2026-06-06",
# 				"id_card_address": "北京朝阳区",
# 				"id_card_copy": "身份证人像面照片",
# 				"id_card_name": "身份证姓名",
# 				"id_card_national": "身份证国徽面照片",
# 				"id_card_number": "身份证号码	"
# 			},
# 			"id_doc_type": "IDENTIFICATION_TYPE_IDCARD",
# 			"id_holder_type": "LEGAL",
# 			"owner": True
# 		},
# 		"ubo_info_list": [{
# 			"ubo_id_doc_address": "广东省深圳市南山区xx路xx号xx室",
# 			"ubo_id_doc_copy": "证件正面照片	",
# 			"ubo_id_doc_copy_back": "证件反面照片	",
# 			"ubo_id_doc_name": "证件姓名	",
# 			"ubo_id_doc_number": "证件号码	",
# 			"ubo_id_doc_type": "IDENTIFICATION_TYPE_OVERSEA_PASSPORT",
# 			"ubo_period_begin": "2019-06-06",
# 			"ubo_period_end": "2026-06-06"
# 		}]
# 	},
# 	"business_info": {
# 		"merchant_shortname": "张三餐饮店",
# 		"sales_info": {
# 		"sales_scenes_type": [
# 				# "SALES_SCENES_STORE",
# 				# "SALES_SCENES_MP",
# 				"SALES_SCENES_MINI_PROGRAM",
# 				# "SALES_SCENES_WEB",
# 				# "SALES_SCENES_APP",
# 				# "SALES_SCENES_WEWORK"
# 			],
# 			"app_info": {
# 				"app_appid": "wx1234567890123456",
# 				"app_pics": ["app截图"]
# 			},
# 			"biz_store_info": {
# 				"biz_address_code": "线下场所省市编码",
# 				"biz_store_address": "线下场所地址",
# 				"biz_store_name": "线下场所名称",
# 				"biz_sub_appid": "",
# 				"线下场所内部照片": ["线下场所内部照片"],
# 				"store_entrance_pic": ["线下场所门头照片"]
# 			},
# 			"mini_program_info": {
# 				"mini_program_appid": "wx1234567890123456",
# 				"mini_program_pics": ["小程序截图	"]
# 			},
# 			"mp_info": {
# 				"mp_appid": "wx1234567890123456",
# 				"mp_pics": ["公众号页面截图"]
# 			},
# 			"web_info": {
# 				"domain": "互联网网站域名",
# 				"web_appid": "",
# 				"web_authorisation": ""
# 			},
# 			"wework_info": {
# 				"corp_id": "wx1234567890123456",
# 				"sub_corp_id": "wx1234567890123456",
# 				"wework_pics": ["0P3ng6KTIW4-Q_l2FjmFJBZR9FwczhJehHhAZN6BKXQPcs-VvdSo"]
# 			}
# 		},
# 		"service_phone": "0758XXXXX"
# 	},
# 	"settlement_info": {
# 		"activities_id": "",
# 		"activities_rate": "",
# 		"debit_activities_rate ": "",
# 		"credit_activities_rate ": "",
# 		"qualification_type": "餐饮",
# 		"settlement_id": "719"
# 	},
# 	"bank_account_info": {
# 		"account_bank": "招商银行",
# 		"account_name": "北京西二旗招商",
# 		"account_number": "1829817291028172628991",
# 		"bank_account_type": "BANK_ACCOUNT_TYPE_PERSONAL",
# 		"bank_address_code": "110000",
# 		"bank_branch_id": "402713354941"
# 	}
# }



# super
SERVICE_MERCHANT_NUMBER = "1651380696"

business_code = f"GOMELINK_{SERVICE_MERCHANT_NUMBER}_{time.time()}"
contact_info = {'contact_name':'张三','contact_id_number':'320311770706001','mobile_phone':'13900000000','contact_email':'admin@demo.com'}

subject_info = {'subject_type':'SUBJECT_TYPE_ENTERPRISE',
				'business_license_info':{
					'license_copy':'demo-media-id','license_number':'123456789012345678','merchant_name':'腾讯科技有限公司','legal_person':'张三'
				},
				'identity_info':{
					'id_doc_type':'IDENTIFICATION_TYPE_IDCARD',
					'id_card_info': {
						"card_period_begin": "2026-06-06",
						"card_period_end": "2026-06-06",
						# "id_card_address": "北京朝阳区",
						"id_card_copy": "身份证人像面照片",
						"id_card_name": "身份证姓名",
						"id_card_national": "身份证国徽面照片",
						"id_card_number": "身份证号码	"
					}
				}
				}

business_info = {'merchant_shortname':'张三餐饮店','service_phone':'0758xxxxxx',
				 'sales_info':{'sales_scenes_type':['SALES_SCENES_STORE','SALES_SCENES_MP']}}

settlement_info = {'settlement_id':'719','qualification_type':'餐饮'}

bank_account_info = {'bank_account_type':'BANK_ACCOUNT_TYPE_CORPORATE','account_name':'xx公司',
					 'account_bank':'工商银行','bank_address_code':'110000','account_number':'1234567890'}

addition_info = {'legal_person_commitment':'demo-media-id'}



"""
            business_code: 业务申请编号 string[1, 124]
            1、只能由数字、字母或下划线组成，建议前缀为服务商商户号；
            2、服务商自定义的唯一编号；
            3、每个编号对应一个申请单，每个申请单审核通过后会生成一个微信支付商户号。
            示例值：1900013511_10000
        """


"""
            contact_info: 超级管理员信息  object
            超级管理员需在开户后进行签约，并可接收日常重要管理信息和进行资金操作，请确定其为商户法定代表人或负责人。
"""

# contact_info = {
#     'contact_type': 'SUPER',
#     'contact_name':'赖秀美',
#     'contact_id_number':'440229199203022223',
#     'mobile_phone':'15913154004',
#     'contact_email':'laixiumei@gome.email'}

# cp_contact_info = {
#     "contact_type": "SUPER",
#     "contact_name": "赖秀美",
#     "contact_id_doc_type": "IDENTIFICATION_TYPE_IDCARD",
#     "contact_id_number": "440229199203022223",
#     "contact_id_doc_copy": settings.WXPAY.image_upload(
#         os.path.join(settings.MEDIA_ROOT, "zf", "wechatpayv3", "super_admin_info", "正.jpg")),
#     "contact_id_doc_copy_back": settings.WXPAY.image_upload(
#         os.path.join(settings.MEDIA_ROOT, "zf", "wechatpayv3", "super_admin_info", "反.jpg")),
#
#     "contact_period_begin": "2023.04.24",
#     "contact_period_end": "2043.04.24",
#     "business_authorization_letter": settings.WXPAY.image_upload(
#         os.path.join(settings.MEDIA_ROOT, "zf", "wechatpayv3", "super_admin_info", "授权函.jpg")),
#     "openid": "",
#     "mobile_phone": "15913154004",
#     "contact_email": "laixiumei@gome.email"
# }


