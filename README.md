
# How to Scrape Google reCAPTCHA-Protected Websites with Python
 

### 🎯 Join Scravity Now !
✔ Free credits  
✔ Priority access  
✔ Early features
### 👉 [https://scravity.com/join](https://scravity.com/join)


In this tutorial, you'll learn how to solve **Google reCAPTCHA puzzles** using Python completely free ✅
-   No third-party services.
-   No CAPTCHA-solving services.
-   Just you, your code, and a little help from me. 🤝💻
We will test on this demo [ [https://www.google.com/recaptcha/api2/demo](https://www.google.com/recaptcha/api2/demo) ], so let's get started!


## 📁 Step 1: Create a Project Directory.

First, let's create a new directory to hold all our project files. Open your terminal or command prompt and run:

    mkdir recaptcha-test

Then navigate into the directory:

    cd recaptcha-test

> _📌_ **_Example:_**  `_recaptcha-test_`_ — feel free to name it whatever you like!_


## 🚀 Step 2: Set Up the Project with uv.

We'll use `uv` to manage our project. It's a fast Python package manager that handles virtual environments automatically. 🐍⚡ you can learn more about [here](https://docs.astral.sh/uv/).
First, make sure you're inside the `recaptcha-test` directory we created:

    cd recaptcha-test

Now, initialize a new Python project:

    uv init

This command creates a `pyproject.toml` file and sets up a virtual environment for you .  no extra steps needed! 🎉

> _📝_ **_Note:_** _If you prefer using pip, you can create a virtual environment manually with:_

> `_python -m venv venv_`

> _But I recommend_ `_uv_`_— it's fast and simple. For more details, check out the_ [_uv getting started guide_](https://docs.astral.sh/uv/getting-started/)_._


We'll need a Python package called **SeleniumBase** to interact with the reCAPTCHA puzzle. In your terminal, run:

    uv add seleniumbase

This command installs the package and automatically updates your `pyproject.toml` and `uv.lock` files. ⚡

You'll also need **Playwright** for browser automation:

    uv add playwright


### 🌐 Install Chromium Browser
We'll be using Chromium instead of Chrome for this tutorial. I'll explain why Chromium is preferred later , but trust me, it makes a difference! 🔍

Download and install Chromium from the official source: 👉 [Download Chromium](https://www.chromium.org/getting-involved/download-chromium/)

**Quick download steps:**

1.  Go to the Chromium snapshots directory
2.  Choose your platform: Mac, Win, or Linux 🖥️
3.  Open the `LAST_CHANGE` file to find the latest build number
4.  Download the zip file for that build number

### 🔌 Activate the Virtual Environment

After installation is complete, activate the virtual environment:

**🐧 Linux / macOS:**

    source .venv/bin/activate

**🪟 Windows (Command Prompt):**

    .venv\Scripts\activate

**🪟 Windows (PowerShell):**

    .venv\Scripts\Activate.ps1  

  
You'll know it's working when you see `(.venv)` appear at the beginning of your terminal prompt. 

  
### 📂 Project Structure (After Installation)  
  
Your folder structure should now look like this:  

    drwxr-xr-x    - dxbear 22 Mar 14:29  📁 .  
    drwxr-xr-x    - dxbear 22 Mar 14:28  📁 ..  
    drwxr-xr-x    - dxbear 22 Mar 14:28  📁 .git  
    drwxr-xr-x    - dxbear 22 Mar 14:30  📁 .venv  
    .rw-r--r--  109 dxbear 22 Mar 14:28  📄 .gitignore  
    .rw-r--r--    5 dxbear 22 Mar 14:28  🐍 .python-version  
    .rw-r--r--   92 dxbear 22 Mar 14:28  🐍 main.py  
    .rw-r--r--  256 dxbear 22 Mar 14:30  ⚙️ pyproject.toml      ⬅️ Updated with SeleniumBase  
    .rw-r--r--    0 dxbear 22 Mar 14:28  📖 README.md  
    .rw-r--r-- 115k dxbear 22 Mar 14:30  🔒 uv.lock              ⬅️ Updated with locked versions

✅ SeleniumBase and its dependencies are now ready to use!


## 💻 Step 3: Writing the Code

Let's open `main.py` in our project and start coding step by step. 📝

### 📦 Import Required Packages
First, we need to import the necessary packages from SeleniumBase and Playwright:

    from seleniumbase import cdp_driver  
    from playwright.async_api import async_playwright

We'll also need `asyncio` to run our code asynchronously. This step is optional — you can use synchronous code if you prefer, but async gives us better performance! ⚡

    import asyncio

### 🛡️ Why SeleniumBase's CDP Driver?

The `cdp_driver` from SeleniumBase is a stealth driver that emulates human browser behavior. 🕵️‍♂️
Unlike regular Playwright  where bots are easily detected ,  SeleniumBase patches the Playwright browser to bypass bot detection. This is crucial for solving reCAPTCHA, as Google is very good at identifying automated scripts. It's still **not enough to bypass reCAPTCHA on its own**, but we'll explain how to handle that. What's important first is not triggering bot detection in the first place.

> _🔍_ **_Key Insight:_** _Standard Playwright can be flagged as a bot almost immediately. The_ `cdp_driver` _makes your browser appear as a real human user, giving us a much higher success rate with reCAPTCHA_

### 🔧 Initialize the Drivers
Inside our main function, we'll start by initializing the CDP driver:

    async def main():  
        # Start the stealth CDP driver  
        driver = await cdp_driver.start_async()  
        endpoint_url = driver.get_endpoint_url()

### 🔌 Connect via CDP (Chrome DevTools Protocol)
Now we'll connect to the browser using CDP. This is a powerful protocol for web scraping and browser automation! 🎯

    async def main():  
        # Start the stealth CDP driver  
        driver = await cdp_driver.start_async()  
        endpoint_url = driver.get_endpoint_url()  
      
        # Connect to the browser using CDP (Chrome DevTools Protocol)  
        async with async_playwright() as p:  
            browser = await p.chromium.connect_over_cdp(endpoint_url)  
            context = browser.contexts[0]  # Create browser context  
            page = context.pages[0]        # Create page object  
              
            # Navigate to Google's official reCAPTCHA demo page  
            await page.goto("https://www.google.com/recaptcha/api2/demo")  
              
            # Wait 10 seconds to observe the page before closing  
            await driver.sleep(10)  
      
    if __name__ == "__main__":  
        loop = asyncio.new_event_loop()  
        loop.run_until_complete(main())

### 🌟 Why CDP Instead of Traditional Selenium/WebDriver?

BenefitDetails🥷 **Stealth Mode** CDP interacts directly with the browser at the protocol level, making it much harder for services like reCAPTCHA to detect automation.🎮 **Fine-Grained Control** Intercept network requests, manipulate the DOM, capture performance metrics, and simulate network conditions .  all through a single protocol.📦 **No Extra Dependencies** Unlike Selenium, CDP doesn't require separate browser drivers that need version matching and constant updates.⚡ **Async Support** CDP works beautifully with async/await patterns, making your scraping scripts faster and more efficient.👤 **True Browser Emulation** Since we're connecting to an actual Chromium instance via CDP, we inherit all browser features without the "tells" that give away automation tools.

### 🧪 What This Code Does
1.  **Starts a stealth CDP driver 🕵️‍♂️** — The `cdp_driver` launches a Chromium browser with stealth patches to avoid bot detection.
2.  **Connects via CDP 🔌** — We connect Playwright to the same browser instance using Chrome DevTools Protocol.
3.  **Creates browser context and page 📄** — We access the existing browser context and page (or create new ones if needed).
4.  **Navigates to the reCAPTCHA demo page 🌐** — Google provides an official demo page for testing: 👉 [https://www.google.com/recaptcha/api2/demo](https://www.google.com/recaptcha/api2/demo)
5.  **Waits 10 seconds ⏱️** — This gives us time to see the page and reCAPTCHA widget before the browser closes.

### 📝 Complete Code So Far

    import asyncio  
    from seleniumbase import cdp_driver  
    from playwright.async_api import async_playwright  
      
    async def main():  
        # Start the stealth CDP driver  
        driver = await cdp_driver.start_async()  
        endpoint_url = driver.get_endpoint_url()  
      
        # Connect to the browser using CDP (Chrome DevTools Protocol)  
        async with async_playwright() as p:  
            browser = await p.chromium.connect_over_cdp(endpoint_url)  
            context = browser.contexts[0]  # Create browser context  
            page = context.pages[0]        # Create page object  
              
            # Navigate to Google's official reCAPTCHA demo page  
            await page.goto("https://www.google.com/recaptcha/api2/demo")  
              
            # Wait 10 seconds to observe the page before closing  
            await driver.sleep(10)  
      
    if __name__ == "__main__":  
        loop = asyncio.new_event_loop()  
        loop.run_until_complete(main())

  

### 🧩 Step 4: Solving the CAPTCHA

If you run this code:

    uv run main.py

You'll notice two things:
1.  **It loads and opens Chrome by default 🌐** — > If Chrome is installed, it will use it. If not, it will ask you to install it.
2.  **We haven't solved any CAPTCHA yet ❌** — > The reCAPTCHA puzzle remains untouched; we just opened the page!

### 🎯 The Trick: Using a Chrome Extension
Here's the key insight you must understand: 🧠

> **_SeleniumBase itself has no capability to bypass or solve Google reCAPTCHA._** _So we'll use a Chrome extension that does the heavy lifting for us!_

### 🧩 Why Chromium Instead of Chrome?
To load any extension, you **MUST** use Chromium, not Chrome.
Why? Because Chrome no longer allows loading external extensions in automated environments. Chromium gives us the freedom to load custom extensions without restrictions. This is why I had you install Chromium earlier! 🎯

### 🤖 The reCAPTCHA Solver Extension

We'll load a modified version of a Chrome extension called **reCAPTCHA solver**.

By "modified," I mean I've tweaked it to run automatically as soon as the page loads — so you don't have to click anything to activate it. ✨

**🔬 How It Works:**

The extension uses tiny AI models trained to:

-   Detect image-based CAPTCHA challenges 🔍
-   Identify objects like traffic lights, buses, crosswalks, etc. 🚦🚌🚶
-   Automatically solve the puzzles for you ⚡

### 📁 Create a Folder for Chrome Extensions

First, let's create a folder to hold our Chrome extension:

    mkdir chrome-extensions

Or create it manually in your project directory. 📂

### 🔽 Download the Modified reCAPTCHA Solver Extension

Head over to my GitHub repository to download the extension: 👉 **[ https://github.com/dx-bear/reCAPTCHA-solver ]**
You have two options:

**Option 1 — Download the extension only 📦**

Look for the `recaptcha-solver` folder in the repository and download it directly.

**Option 2 — Clone the entire repository 🌀**

    git clone [your-repo-url]  

  
  
Then copy the extension folder into your `chrome-extensions` directory.  
  
### 📂 Project Structure After Adding the Extension  

    recaptcha-test/  
    ├── .venv/  
    ├── chrome-extensions/              📁 New folder  
    │   └── recaptcha-solver/           📁 Extension files  
    │       ├── manifest.json  
    │       ├── background.js  
    │       └── ... (other extension files)  
    ├── .gitignore  
    ├── .python-version  
    ├── main.py  
    ├── pyproject.toml  
    ├── README.md  
    └── uv.lock

### 🔌 Update the Code to Load the Extension

Now let's modify `main.py` to load the reCAPTCHA solver extension into Chromium. 🎯
First, import `os` to handle file paths:

    import os  
    import asyncio  
    from seleniumbase import cdp_driver  
    from playwright.async_api import async_playwright

Now, set the absolute path to our extension and configure the driver:

    async def main():  
        # Get the absolute path to the extension folder  
        ext = os.path.abspath("./chrome-extensions/recaptcha-solver/0.1.0_0/")  
          
        # Start the stealth CDP driver with Chromium and the extension loaded  
        driver = await cdp_driver.start_async(  
            use_chromium=True,   # Use Chromium instead of Chrome  
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
            await driver.sleep(10)  
      
    if __name__ == "__main__":  
        loop = asyncio.new_event_loop()  
        loop.run_until_complete(main())

### 📝 What's Happening Here?

Parameter Purpose `use_chromium=True`Tells SeleniumBase to launch Chromium instead of Chrome 🧩`extension_dir=ext` Loads our modified reCAPTCHA solver extension into the browser 🔌`os.path.abspath()` Converts the relative path to an absolute path so the browser can find it 📁

### 🚀 What to Expect
When you run the script:

    uv run main.py

Here's what will happen:

1.  **First Run — Downloading Files 📥** — The extension may take a few seconds to download some AI model files. These will be saved in a folder called `downloaded_files` in the same directory. This only happens once!
2.  **Chromium Launches 🌐** — A Chromium browser window will open automatically with our extension pre-loaded.
3.  **Page Loads 📄** — The script navigates to Google's reCAPTCHA demo page.
4.  **Automatic Solving ✨** — Here's the magic — you'll see the reCAPTCHA widget open and solve itself automatically! No clicking, no manual interaction needed.
