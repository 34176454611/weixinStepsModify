import sys
import requests

def main():
    if len(sys.argv) != 4:
        print("Usage: python weixinSteps.py <username> <password> <steps>")
        sys.exit(1)

    phone = sys.argv[1]
    password = sys.argv[2]
    step = sys.argv[3]

    # 登录获取 token
    login_url = "https://api.yunyoujun.cn/step/login"
    data = {
        "phone": phone,
        "password": password
    }

    try:
        login_resp = requests.post(login_url, json=data).json()
        if login_resp.get("code") != 1:
            print("登录失败:", login_resp.get("msg", "未知错误"))
            sys.exit(1)

        token = login_resp.get("data", {}).get("token")
        if not token:
            print("未获取到 token")
            sys.exit(1)

        # 提交步数
        step_url = "https://api.yunyoujun.cn/step/update"
        headers = {
            "Authorization": token
        }
        step_data = {
            "step": step
        }

        step_resp = requests.post(step_url, headers=headers, json=step_data).json()
        if step_resp.get("code") == 1:
            print(1)
        else:
            print("提交失败:", step_resp.get("msg", "未知错误"))
            sys.exit(1)

    except Exception as e:
        print("运行异常:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
