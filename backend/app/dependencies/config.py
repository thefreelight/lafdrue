# config.py
NOTIFY_URL = 'https://localhost/api/v1/payment-notification/'
RETURN_URL = 'http://localhost:3001/payment-success'


# 定义你的 SECRET_KEY, ALGORITHM, 和 ACCESS_TOKEN_EXPIRE_MINUTES
SECRET_KEY = "LAFDRUE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30