from playwright.async_api import async_playwright
import asyncio
import os

async def run(usr,pwd):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width":1300,"height":1440})
        page = await context.new_page()
        await page.goto("https://purefast.net/auth/login")
        #此处填入账号
        await page.get_by_label("邮箱无需验证码").fill(usr)
        #此处填入密码
        await page.get_by_label("密码").fill(pwd)
        await page.get_by_role("button", name="登录").click()
        await page.wait_for_url("https://purefast.net/user")
        await page.get_by_role("button", name="已读").click()
        await page.get_by_role("link", name=" 每日签到").click()
        await page.wait_for_url("https://purefast.net/user#")
        await page.get_by_role("button", name="OK").click()
        # await page.reload()
        # await page.get_by_role("button", name="已读").click()
        # await asyncio.sleep(2)
        # element_handle = await page.query_selector("//section[@class='section']")
        # await element_handle.screenshot(path='result'+usr[0:3]+'.png')
        await page.close()
        await context.close()
        await browser.close()

async def main(users,pwds):
    tasks =[]
    #此处修改为你要签到的账号和密码，顺序要对应
    for user,pwd in zip(users,pwds):
        task = asyncio.ensure_future(run(user,pwd))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    USERS = os.environ["USERS"]
    PWDS = os.environ["PWDS"]
    users = USERS.split(";")
    pwds = PWDS.split(";")
    asyncio.run(main(users,pwds))
