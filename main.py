import os  
import asyncio  
from seleniumbase import cdp_driver  
from playwright.async_api import async_playwright

async def main():  
    # Get the absolute path to the extension folder  
    ext = os.path.abspath("./chrome-extensions/bbdhfoclddncoaomddgkaaphcnddbpdh/0.1.0_0/")  
      
    # Start the stealth CDP driver with Chromium and the extension loaded  
    driver = await cdp_driver.start_async(  
        # use_chromium=True,   # Use Chromium instead of Chrome  
        extension_dir=ext,   # Load our custom extension  
    )  
      
    endpoint_url = driver.get_endpoint_url()  
  
    # Connect to the browser using CDP  
    async with async_playwright() as p:  
        browser = await p.chromium.connect_over_cdp(endpoint_url)  
        context = browser.contexts[0]  
        page = context.pages[0]  
          
        # Navigate to Google's reCAPTCHA demo page  
        await page.goto("https://www.google.com/recaptcha/api2/demo")  
          
        # Wait for the extension to do its magic! ✨  
        await driver.sleep(20)  
  
if __name__ == "__main__":  
    loop = asyncio.new_event_loop()  
    loop.run_until_complete(main())