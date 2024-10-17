from datetime import datetime
import pytz


def convert_iso_to_normal_time_with_timezone(iso_string):
    # 解析 ISO 8601 时间字符串
    dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))

    # 将时间转为本地时区
    local_tz = pytz.timezone('Asia/Shanghai')  # 替换为所需的时区
    local_dt = dt.astimezone(local_tz)

    # 格式化为所需的时间格式
    normal_time = local_dt.strftime('%Y-%m-%d %H:%M:%S')
    return normal_time
