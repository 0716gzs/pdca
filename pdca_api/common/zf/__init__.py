from common.zf.wechatpayv3 import WeChatPayType, WeChatPay
import logging
from django.conf import settings
import os

CORP_ID = 'your_corp_id'
CORP_SECRET = 'your_corp_secret'

APPID = 'wxc5b398ecb0435012'
# MCHID = '1651380696'
MCHID = '1651870985'
# 商户证书私钥
with open(f'{settings.BASE_DIR}/common/zf/cert/wx_payv3/apiclient_key.pem') as f:
    PRIVATE_KEY = f.read()
# 商户证书序列号
CERT_SERIAL_NO = '3F376E9D601F0D920676563F174BD74B24045B8C'
# API v3密钥， https://pay.weixin.qq.com/wiki/doc/apiv3/wechatpay/wechatpay3_2.shtml
APIV3_KEY = 'eFtnV2iMIx8SyD7h0PL9l4BcWwH53Cfd'
# 密钥
SECRET = "e5d47cf9155cc30b5cf11ed4a2df341d"
# 回调地址，也可以在调用接口的时候覆盖
NOTIFY_URL = f'{settings.BASE_NOTIFY_URL}/legou/order/pay/payNotify'

# 退款回调地址
REFUND_NOTIFY_URL = f'{settings.BASE_NOTIFY_URL}/legou/order/refund/refundNotify'
# 微信支付平台证书缓存目录，减少证书下载调用次数
# 初始调试时可不设置，调试通过后再设置，示例值：'./cert'
CERT_DIR = f'{settings.BASE_DIR}/common/cert/wx_cert'
# 日志记录器，记录web请求和回调细节
logging.basicConfig(filename=os.path.join(os.getcwd(), 'demo.log'), level=logging.DEBUG, filemode='a', format='%(asctime)s - %(process)s - %(levelname)s: %(message)s')
LOGGER = logging.getLogger("demo")
# 接入模式：False=直连商户模式，True=服务商模式
PARTNER_MODE = True
# 代理设置，None或者{"https": "http://10.10.1.10:1080"}，详细格式参见https://docs.python-requests.org/zh_CN/latest/user/advanced.html
PROXY = None
# 初始化
WXPAY = WeChatPay(
    wechatpay_type=WeChatPayType.MINIPROG,
    mchid=MCHID,
    private_key=PRIVATE_KEY,
    cert_serial_no=CERT_SERIAL_NO,
    apiv3_key=APIV3_KEY,
    appid=APPID,
    notify_url=NOTIFY_URL,
    cert_dir=CERT_DIR,
    logger=LOGGER,
    partner_mode=PARTNER_MODE,
    proxy=PROXY)


# SERVICE_CERT_SERIAL_NO = "137C7B824924970720D6DA1324729B201A53244B"
# SERVICE_API_KEY = "eFtnV2iMIx8SyD7h0PL9l4BcWwH53Cfd"
# SERVICE_CERT_DIR = f'{settings.BASE_DIR}/common/cert/wx_cert'
# SERVICE_SUB_APPID = "wxc5b398ecb0435012"
# SERVICE_APP_ID = "wx9e0939b01def7fa6"
# SERVICE_MCH_ID = "1651380696"

SERVICE_APP_ID = "wx9e0939b01def7fa6"
# SERVICE_MINI_APP_ID = "wxc5b398ecb0435012"

SERVICE_MINI_APP_ID = settings.APPID
SERVICE_MINI_APP_SECRET = settings.APPSECRET



SERVICE_MCH_ID = "1651380696"
SERVICE_API_KEY = "eFtnV2iMIx8SyD7h0PL9l4BcWwH53Cfd"
SERVICE_CERT_SERIAL_NO = "137C7B824924970720D6DA1324729B201A53244B"
SERVICE_PARTNER_MODE = True
SERVICE_CERT_DIR = f'{settings.BASE_DIR}/common/cert/wx_cert/service'
with open(f'{settings.BASE_DIR}/common/cert/wx_payv3/service/apiclient_key.pem') as f:
    SERVICEPRIVATE_KEY = f.read()

# 微信服务商费率
WECHAT_PAY_SERVICE_RATE = 0.006

OTHERS_MCH_ID = 1651870985


ServiceWxPay = WeChatPay(
    wechatpay_type=WeChatPayType.MINIPROG,
    mchid=SERVICE_MCH_ID,
    private_key=SERVICEPRIVATE_KEY,
    cert_serial_no=SERVICE_CERT_SERIAL_NO,
    apiv3_key=SERVICE_API_KEY,
    appid=SERVICE_APP_ID,
    notify_url=NOTIFY_URL,
    refund_notify_url=REFUND_NOTIFY_URL,
    cert_dir=SERVICE_CERT_DIR,
    logger=LOGGER,
    partner_mode=SERVICE_PARTNER_MODE,
    proxy=PROXY)
