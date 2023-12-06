from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("http://localhost:3000/")
    
def after_scenario(context, scenario):
    context.driver.quit()