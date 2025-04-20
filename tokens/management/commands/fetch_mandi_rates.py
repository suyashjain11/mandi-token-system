from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from tokens.models import MandiPrice
from datetime import date

class Command(BaseCommand):
    help = 'Fetches grain mandi rates from Napanta'

    def handle(self, *args, **kwargs):
        url = "https://www.napanta.com/market-price/madhya-pradesh/vidisha/ganjbasoda"

        # Chrome Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        # Path to your chromedriver.exe
        service = Service(executable_path="D:\\mandi_token_system\\chromedriver.exe")

        # Launch browser
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        time.sleep(5)  # wait for page to load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        rows = soup.select("table tbody tr")

        count = 0
        for row in rows:
            cells = [c.get_text(strip=True) for c in row.find_all("td")]
            if len(cells) < 6:
                continue

            try:
                crop = cells[0]
                variety = cells[2]
                max_price = int(cells[3].replace("₹", "").replace(",", "").strip())
                avg_price = int(cells[4].replace("₹", "").replace(",", "").strip())
                min_price = int(cells[5].replace("₹", "").replace(",", "").strip())

                MandiPrice.objects.create(
                    crop_name=crop,
                    variety=variety,
                    max_price=max_price,
                    avg_price=avg_price,
                    min_price=min_price,
                    date=date.today()
                )
                count += 1

            except Exception as e:
                print(f"Skipping row due to error: {e}")
                continue

        self.stdout.write(self.style.SUCCESS(f"✅ {count} mandi rates fetched and saved successfully."))
