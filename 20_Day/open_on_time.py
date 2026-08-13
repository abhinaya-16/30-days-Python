import webbrowser
import time
from datetime import datetime, timedelta

# Time to open the websites
target_hour = 18
target_minute = 30

# List of URLs
url_lists = [
    "http://www.python.org",
    "https://www.linkedin.com/in/asabeneh/",
    "https://github.com/Asabeneh",
    "https://twitter.com/Asabeneh",
]

# Current time
now = datetime.now()

# Create target datetime
target = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)

# If the time has already passed today, schedule for tomorrow
if target <= now:
    target += timedelta(days=1)

# Calculate wait time
wait_seconds = (target - now).total_seconds()

print(f"Waiting {wait_seconds:.0f} seconds until {target.strftime('%Y-%m-%d %H:%M:%S')}")

# Wait until the target time
time.sleep(wait_seconds)

# Open all websites
for url in url_lists:
    webbrowser.open_new_tab(url)
    time.sleep(1)  # Optional delay between tabs