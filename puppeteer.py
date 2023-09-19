import asyncio
from pyppeteer import launch

async def main():
    # Запускаем браузер
    browser = await launch(headless=False, args=['--no-sandbox'])
    page = await browser.newPage()

    # Устанавливаем размер viewport
    await page.setViewport({'width': 1800, 'height': 900})

    # Переходим на сайт google.com
    await page.goto('https://www.google.com')

    # Вводим текст "qa engineering" в поле поиска и нажимаем Enter
    await page.type('input[name=q]', 'qa engineering')
    await page.keyboard.press('Enter')

    # Ждем, чтобы результаты поиска загрузились
    await page.waitForSelector('h3')

    # Создаем скриншот открывшейся страницы
    await page.screenshot({'path': 'screenshot.png'})

    # Закрываем браузер
    await browser.close()

# Запускаем асинхронный код
asyncio.get_event_loop().run_until_complete(main())
