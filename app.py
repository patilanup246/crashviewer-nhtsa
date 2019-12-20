from selenium import webdriver
import urllib.parse as urlparse
from urllib.parse import parse_qs
from selenium.webdriver.chrome.options import Options
import base64
import os
import time

options = Options()

executable_path = "chromedriver"
browser = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
browser.get(
    "https://crashviewer.nhtsa.dot.gov/nass-CIREN/CaseForm.aspx?ViewText&CaseID=153427&xsl=textonly.xsl&websrc=true")

alllinks = browser.find_elements_by_xpath('//table/tbody/tr/td/img')
for e in alllinks:
    try:

        url = e.get_attribute("src")
        parsed = urlparse.urlparse(url)

        imgdata = base64.b64decode(e.screenshot_as_base64)
        # define the name of the directory to be created
        path = os.getcwd() + "/" + parse_qs(parsed.query)['CaseID'][0]
        try:
            os.mkdir(path)
        except OSError:
            m = 0
        filename = parse_qs(parsed.query)['CaseID'][0] + '/' + parse_qs(parsed.query)['CaseID'][0] + '_' + \
                   parse_qs(parsed.query)['ImageID'][0] + '.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
    except:
        pass
