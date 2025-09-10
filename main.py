import os

def test_api_key():
    api_key = os.getenv("DASHSCOPE_API_KEY")
    assert api_key is not None, "API Key 未设置"
    assert len(api_key) >= 5, "API Key 长度异常"  # 根据实际Key长度调整
    print(api_key)
    print("✅ 环境变量注入成功")

if __name__ == "__main__":
    test_api_key()
