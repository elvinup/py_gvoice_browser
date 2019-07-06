from selenium import webdriver

def seleniumOptions():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')


    # Help with headless performance
    options.add_argument('--no-proxy-server') 
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")

    # Pass the argument 1 to allow and 2 to block
    options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 2
    })
    # Set download directory
    #prefs = {"download.default_directory" : "./ahs_logs"}
    #options.add_experimental_option("prefs", prefs)

    return options

