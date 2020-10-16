from datetime import timedelta


def validate_email(email):
    import re
    p = re.compile(r"^[A-Za-z0-9]+([_\.][A-Za-z0-9]+)*@([A-Za-z0-9\-]+\.)+[A-Za-z]{2,6}$")
    return p.match(email)


def validate_phone(phone):
    import re
    p = re.compile(r"^1[3-9]\d{9}$")
    return p.match(phone)


def datetime_to_str(dt, date_separator='-', only_date=False) -> str:
    """将datetime对象转换为形如 '2020-01-01 12:00:00'的字符串,可指定only_date只包含日期

    如果指定date_separator则按指定分隔符格式化日期部分，如 '2020.01.01 12:00:00'

    dt 为 UTC 时间，在该函数中应转换为东八区时间

    Args:
        dt: datetime对象
        date_separator: 日期间隔符
        only_date: 是否只返回日期字符串

    Returns:
        datetime字符串
    """
    dt = dt + timedelta(hours=8)
    if not dt:
        return ''
    if only_date:
        return dt.strftime("%%Y%s%%m%s%%d" % (date_separator, date_separator))
    else:
        return dt.strftime("%%Y%s%%m%s%%d %%H:%%M:%%S" % (date_separator, date_separator))
