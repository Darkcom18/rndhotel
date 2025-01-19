import requests

# Đây là token bạn đã cung cấp - chú ý bảo mật, không để lộ trên GitHub công khai
TOKEN = "pat_CidyQ5GvfEM8EC7OZcA4aN8bgkjnxPqlZYxDKJGAZYM7gjoNID1GUEM907beYrOB"

# Ví dụ bot_id và user_id. Bạn cần thay bằng giá trị thật (nếu đã có) hoặc
# test tạm. Hoặc nếu Coze cho phép user_id tùy ý, bạn có thể để tuỳ thích:
BOT_ID = "7400714764970311681"    # Lấy từ URL Develop page agent
USER_ID = "Test khach hang"

# Endpoint Coze (v3)
url = "https://api.coze.com/v3/chat"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "bot_id": BOT_ID,
    "user_id": USER_ID,
    # Nếu muốn streaming, đặt = True (nếu Coze support).
    "stream": False,
    "auto_save_history": True,
    "additional_messages": [
        {
            "role": "user",
            "content": "ocany uống lúc nào",
            "content_type": "text"
        }
    ]
}

try:
    response = requests.post(url, headers=headers, json=payload)
    print("Status code:", response.status_code)
    print("Response body:", response.text)

    if response.ok:
        data = response.json()
        # Tuỳ Coze trả về định dạng ra sao. Có thể là:
        # { "choices": [ { "delta": ... } ], ... } 
        # hoặc { ... "result": ... }
        # Bạn có thể in chi tiết, hoặc parse.
        print("Parsed JSON:", data)
    else:
        print("Coze API trả về lỗi:", response.status_code, response.text)

except Exception as e:
    print("Lỗi khi gọi API Coze:", str(e))
