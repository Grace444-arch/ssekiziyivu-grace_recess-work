import tweepy
import datetime
import os
import socket
import time

# Step 1: Wait for internet connection (try for up to 2 minutes)
def is_connected():
    try:
        socket.create_connection(("api.twitter.com", 443), timeout=5)
        return True
    except OSError:
        return False

for _ in range(120):  # wait max 2 mins (120 seconds)
    if is_connected():
        break
    time.sleep(1)
else:
    print("❌ Internet not available. Tweet not sent.")
    exit()

# Step 2: Check if already posted today
today = datetime.datetime.now().strftime("%Y-%m-%d")
weekday = datetime.datetime.now().strftime("%A")

log_file = "last_posted.txt"
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        last_date = f.read().strip()
    if last_date == today:
        print("✅ Already posted today. Skipping.")
        exit()

# Step 3: Tweet today's quote
quotes = {
    "Monday": "Believe you can and you're halfway there.",
    "Tuesday": "Push yourself, because no one else will do it for you.",
    "Wednesday": "Success is not for the lazy.",
    "Thursday": "Stay positive, work hard, make it happen.",
    "Friday": "It always seems impossible until it's done.",
    "Saturday": "Don't stop until you're proud.",
    "Sunday": "Take time to make your soul happy."
}
quote = quotes.get(weekday, "Stay inspired.")

# Twitter credentials
API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''


# Step 4: Post the tweet
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

try:
    response = client.create_tweet(text=quote)
    print(f"✅ Posted: {quote}")
    with open(log_file, "w") as f:
        f.write(today)
except Exception as e:
    print(f"❌ Failed to post tweet: {e}")
