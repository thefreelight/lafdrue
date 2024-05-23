import hashlib
import requests
import re
from urllib.parse import urlencode
from ...dependencies.config import NOTIFY_URL,RETURN_URL

class YiPayProcessor:
    def __init__(self, merchant_id, secret_key, api_url):
        self.merchant_id = merchant_id
        self.secret_key = secret_key
        self.api_url = api_url

    def generate_md5_sign(self, params):
        """
        生成 MD5 签名
        :param params: 包含所有待签名参数的字典
        :return: 签名字符串
        """

        # 移除不参与签名的参数
        filtered_params = {k: v for k, v in params.items() if k not in ["sign", "sign_type"] and v is not None}

        # 参数按 ASCII 码从小到大排序
        sorted_params = sorted(filtered_params.items())

        # 拼接参数字符串
        concatenated_params = "&".join([f"{k}={v}" for k, v in sorted_params])

        # 拼接商户密钥
        sign_str = f"{concatenated_params}{self.secret_key}"

        # 生成 MD5 签名并转换为小写
        sign = hashlib.md5(sign_str.encode()).hexdigest()

        return sign

    def create_payment_url(self, order_info):
        # 基础参数
        base_params = {
            'pid': self.merchant_id,
            'type': order_info.get('payment_method'),
            'out_trade_no': order_info.get('order_number'),
            'notify_url': NOTIFY_URL,
            'return_url': RETURN_URL,
            'name': order_info.get('items')[0].get('product_name'),  # 获取商品名称
            'money': order_info.get('total_amount'),
            'sitename': order_info.get('order_number')
        }

        # 生成签名
        sign = self.generate_md5_sign(base_params)
        base_params['sign'] = sign
        base_params['sign_type'] = 'MD5'

        # 构建POST请求的完整URL
        request_url = f"{self.api_url}/submit.php"

        # 发送POST请求
        response = requests.post(request_url, data=base_params)

        # 检查请求是否成功
        if response.status_code == 200:
            try:
                # 使用正则表达式提取出支付链接
                match = re.search(r"window.location.href='(.*?)';", response.text)
                if match:
                    # 获取匹配到的第一个分组，即相对URL
                    relative_url = match.group(1)
                    # 拼接成完整的URL
                    payment_url = self.api_url + relative_url
                    return payment_url
                else:
                    return None
            except Exception as e:
                # 处理任何正则表达式解析错误
                print(f"Error extracting payment URL: {e}")
                return None
        else:
            # 处理错误情况
            return None


