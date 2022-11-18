from playwright.sync_api import Playwright, sync_playwright
import time



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    

    context = browser.new_context()
    page = context.new_page()
    page.goto("https://purefast.net/user")
    time.sleep(6)
    page.goto("https://purefast.net/auth/login")
    #此处填入账号
    page.get_by_label("邮箱无需验证码").fill("114514@qq.com")
    #此处填入密码
    page.get_by_label("密码").fill("1919810")
    page.get_by_role("button", name="登录").click()
    page.wait_for_url("https://purefast.net/user")
    time.sleep(2)
    page.get_by_role("button", name="已读").click()
    page.get_by_role("link", name=" 每日签到").click()
    page.wait_for_url("https://purefast.net/user#")
    time.sleep(2)
    page.get_by_role("button", name="OK").click()
    page.reload()
    time.sleep(2)
    page.get_by_role("button", name="已读").click()
    time.sleep(2)
    element_handle = page.query_selector("//section[@class='main-content']")
    element_handle.screenshot(path='result.png')
    page.close()
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


