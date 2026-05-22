import json
import sys
import config
import scraper
import notifier

print("Scraping new data")
new_data = scraper.scrape()

if len(new_data) == 0:
    print("Failed to scrape data, exit")
    sys.exit()

try:
    with open(config.FILE, "r+", encoding="utf-8") as file:
        print("Reading old data")
        old_data = file.read()
except (FileNotFoundError) as error:
    print(f"Failed to read old data from {config.FILE}:", error)
    old_data = None

notifier.check_and_notify(new_data, old_data)

with open(config.FILE, "w", encoding="utf-8") as file:
    print("Writing new data")
    file.write(new_data)
