"""
常量
"""
import os

class DefaultRole:
    ALL = 'ALL'
    ADMIN = 'ADMIN *'
    DC = 'DC'
    GM = 'GM'
    DGM = 'DGM'
    PM = 'PM'
    MG = 'MG'
    BD = 'BD'
    FD = 'FD'
    TEST = 'TEST'
    OAM = 'OAM'
    HR = 'HR'

    CHOICES = (
        (ADMIN, '管理员'),
        (DC, '董事'),
        (GM, '总经理'),
        (DGM, '副总经理'),
        (PM, '项目经理'),
        (MG, '主管'),
        (BD, '后端开发'),
        (FD, '前端开发'),
        (TEST, '测试'),
        (OAM, '运维'),
        (HR, '人事'),

    )


class ProjectType:
    INTERIOR = 0
    OUTSOURCING = 1
    PARTNER = 2
    CHOICES = (

        (INTERIOR, '内部项目'),
        (OUTSOURCING, '外包项目'),
        (PARTNER, '合作方项目'),
    )


class ProjectStatus:
    NOT_YET_STARTED = 0
    UNDER_WAY = 1
    COMPLETE = 2
    CHOICES = (
        (NOT_YET_STARTED, '未开始'),
        (UNDER_WAY, '进行中'),
        (COMPLETE, '已完成'),
    )


class PlanLevel:
    EASY = 1
    NORMAL = 2
    HARD = 3
    CHOICES = (
        (EASY, '简单'),
        (NORMAL, '一般'),
        (HARD, '困难'),
    )


class FileType:
    DEFAULT = 0
    SYSTEM = 1
    UPLOAD = 2
    CHOICES = (
        (DEFAULT, '默认'),
        (SYSTEM, '系统'),
        (UPLOAD, '用户上传'),
    )

# class ALIPAY:
#     ALI_GATEWAY = "https://openapi.alipaydev.com/gateway.do"
#     ALI_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'files/应用私钥RSA2048-敏感数据，请妥善保管.txt')
#     ALI_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'files/支付宝公钥.text')
#     ALI_NOTIFY_URL = "http://127.0.0.1:8000/order/pay/notify/--这里是你自己路径"
#     ALI_RETURN_URL = "http://127.0.0.1:8000/order/pay/notify/--这里是你自己路径"
#     ALI_APPID = "这里是你自己支付宝沙箱账号的APPID"
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#     CHOICES = (
#         (ALI_GATEWAY, 'GATEWAY'),
#         (ALI_PRIVATE_KEY_PATH, 'PRIVATE_KEY_PATH'),
#         (ALI_PUBLIC_KEY_PATH, 'PUBLIC_KEY_PATH'),
#         (ALI_NOTIFY_URL, 'NOTIFY_URL'),
#         (ALI_RETURN_URL, 'RETURN_URL'),
#         (ALI_APPID, 'APPID'),
#         (BASE_DIR, 'DIR'),
#     )
