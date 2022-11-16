import re
import requests
import yaml
from bs4 import BeautifulSoup

SETTINGS = "_data/settings.yml"
PATTERN = "\"campaignTotalAmountRaised\":\".*\""

with open(SETTINGS, 'r') as f:
    settings = yaml.safe_load(f)
paypal_url = settings["donations"]["paypal_url"]
html_r = requests.get(paypal_url, auth=('user', 'pass'))
soup = BeautifulSoup(html_r.text, features="html.parser")
re_str = re.findall(re.compile(PATTERN), str(soup.body))[0]
donation_str = re_str.split(",")[0].split(":")[1].replace("\"", "")
donation = float(donation_str)
print(f"Current donation on PayPal: {donation}")
