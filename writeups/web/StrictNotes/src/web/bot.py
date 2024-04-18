from pyppeteer import launch
import os

async def visit(noteId):
    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False,
        executablePath="/usr/bin/chromium-browser",
        args=[
		        "--no-sandbox",
		        "--disable-setuid-sandbox",
		        "--js-flags=--noexpose_wasm,--jitless"
        ]
    )
    page = await browser.newPage()
    
    cookies = {'name': 'flag', 'value': os.getenv("FLAG"), 'url': 'http://127.0.0.1:1234'}
    await page.setCookie(cookies)
    
    await page.goto(f'http://127.0.0.1:1234/public-notes?id={noteId}')

    await page.close()

    await browser.close()
    return
