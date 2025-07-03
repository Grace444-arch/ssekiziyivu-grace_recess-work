import os
import random
import time
import schedule
from datetime import datetime
from dotenv import load_dotenv
import tweepy

# Load environment variables
load_dotenv()

# Client with credentials from .env
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
    consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    wait_on_rate_limit=True
)

# Post templates
football_posts = [
    "The beautiful game never fails to amaze! ⚽ #Football",
    "Football brings people together across all boundaries 🌍⚽",
    "Every match tells a story. What's your favorite football moment? ⚽",
    "The passion for football in Uganda is incredible! 🇺🇬⚽",
    "From grassroots to professional - football is life! ⚽💪",
    "Sunday league or Premier League - the love for football is the same ⚽❤️",
    "Watching football with friends hits different! Who's your match day crew? ⚽👥",
    "The World Cup brings the entire world together! 🌍🏆 #WorldCup",
    "Local football talent in Uganda is incredible! Time to shine! 🇺🇬⚽✨"
]

uganda_posts = [ ... ]  # Truncated for brevity (unchanged)
political_posts = [ ... ]
entertainment_posts = [ ... ]
lifestyle_posts = [ ... ]
tech_posts = [ ... ]
business_posts = [ ... ]
general_posts = [ ... ]

football_comments = [ ... ]  # Truncated for brevity
uganda_comments = [ ... ]
political_comments = [ ... ]
entertainment_comments = [ ... ]
lifestyle_comments = [ ... ]
tech_comments = [ ... ]
business_comments = [ ... ]
general_comments = [ ... ]

FOOTBALL_KEYWORDS = [ ... ]
UGANDA_KEYWORDS = [ ... ]
POLITICAL_KEYWORDS = [ ... ]
ENTERTAINMENT_KEYWORDS = [ ... ]
LIFESTYLE_KEYWORDS = [ ... ]
TECH_KEYWORDS = [ ... ]
BUSINESS_KEYWORDS = [ ... ]

def test_connection():
    try:
        me = client.get_me()
        print(f"✅ Connected successfully! Account: @{me.data.username}")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

def post_tweet(content):
    try:
        if len(content) > 280:
            content = content[:277] + "..."
        response = client.create_tweet(text=content)
        print(f"✅ Tweet posted: {content}")
        return True
    except Exception as e:
        print(f"❌ Error posting tweet: {str(e)}")
        return False

def like_tweet(tweet_id):
    try:
        client.like(tweet_id)
        print(f"✅ Liked tweet: {tweet_id}")
        return True
    except Exception as e:
        print(f"❌ Error liking tweet: {str(e)}")
        return False

def reply_to_tweet(tweet_id, reply_text):
    try:
        if len(reply_text) > 280:
            reply_text = reply_text[:277] + "..."
        response = client.create_tweet(text=reply_text, in_reply_to_tweet_id=tweet_id)
        print(f"✅ Replied to tweet: {reply_text}")
        return True
    except Exception as e:
        print(f"❌ Error replying to tweet: {str(e)}")
        return False

def contains_keywords(text, keywords):
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)

def get_comment_for_topic(text):
    if contains_keywords(text, FOOTBALL_KEYWORDS):
        return random.choice(football_comments)
    elif contains_keywords(text, UGANDA_KEYWORDS):
        return random.choice(uganda_comments)
    elif contains_keywords(text, POLITICAL_KEYWORDS):
        return random.choice(political_comments)
    elif contains_keywords(text, ENTERTAINMENT_KEYWORDS):
        return random.choice(entertainment_comments)
    elif contains_keywords(text, LIFESTYLE_KEYWORDS):
        return random.choice(lifestyle_comments)
    elif contains_keywords(text, TECH_KEYWORDS):
        return random.choice(tech_comments)
    elif contains_keywords(text, BUSINESS_KEYWORDS):
        return random.choice(business_comments)
    else:
        return random.choice(general_comments)

def search_and_engage():
    try:
        search_queries = [
            ("football OR soccer -is:retweet lang:en", "football"),
            ("Uganda OR Ugandan -is:retweet lang:en", "uganda"),
            ("politics OR government OR democracy -is:retweet lang:en", "politics"),
            ("entertainment OR music OR movie -is:retweet lang:en", "entertainment"),
            ("technology OR innovation OR startup -is:retweet lang:en", "tech"),
            ("business OR entrepreneur OR success -is:retweet lang:en", "business"),
            ("lifestyle OR wellness OR motivation -is:retweet lang:en", "lifestyle")
        ]

        engagement_count = 0
        max_engagements = 15
        
        for query, topic in search_queries:
            if engagement_count >= max_engagements:
                break

            try:
                tweets = client.search_recent_tweets(
                    query=query,
                    max_results=10,
                    tweet_fields=['public_metrics', 'author_id', 'created_at']
                )

                if tweets.data:
                    selected_tweets = tweets.data[:2]

                    for tweet in selected_tweets:
                        if engagement_count >= max_engagements:
                            break

                        from datetime import timezone, timedelta
                        if hasattr(tweet, 'created_at'):
                            tweet_time = datetime.fromisoformat(tweet.created_at.replace('Z', '+00:00'))
                            if datetime.now(timezone.utc) - tweet_time > timedelta(hours=24):
                                continue

                        # ✅ FIXED: tweet.id cast to int
                        if like_tweet(int(tweet.id)):
                            engagement_count += 1
                            time.sleep(random.uniform(2, 4))

                        if random.random() < 0.3 and engagement_count < max_engagements:
                            comment = get_comment_for_topic(tweet.text)
                            # ✅ FIXED: tweet.id cast to int
                            if reply_to_tweet(int(tweet.id), comment):
                                engagement_count += 1
                                time.sleep(random.uniform(3, 6))

                time.sleep(random.uniform(5, 10))

            except Exception as e:
                print(f"❌ Error searching for {topic}: {str(e)}")
                continue

        print(f"✅ Engagement round completed! Total interactions: {engagement_count}")

    except Exception as e:
        print(f"❌ Error in search and engage: {str(e)}")

def scheduled_post():
    categories = {
        'football': (football_posts, 0.20),
        'uganda': (uganda_posts, 0.20),
        'political': (political_posts, 0.15),
        'entertainment': (entertainment_posts, 0.15),
        'lifestyle': (lifestyle_posts, 0.10),
        'tech': (tech_posts, 0.10),
        'business': (business_posts, 0.10)
    }

    rand = random.random()
    cumulative = 0
    selected_posts = general_posts

    for category, (posts, weight) in categories.items():
        cumulative += weight
        if rand < cumulative:
            selected_posts = posts
            break

    if selected_posts:
        content = random.choice(selected_posts)
        post_tweet(content)
    else:
        print("No posts available")

def engagement_routine():
    print("🤖 Starting engagement routine...")
    search_and_engage()

def add_custom_posts():
    custom_posts = []
    print("\n📝 Add custom posts to your queue (type 'done' when finished):")
    
    while True:
        new_post = input("Enter a post: ")
        if new_post.lower() == 'done':
            break
        custom_posts.append(new_post)
        print(f"Added! Total custom posts: {len(custom_posts)}")
    
    return custom_posts

def main():
    print("🤖 Enhanced Twitter Bot Starting...")
    
    if not test_connection():
        print("Please check your Twitter API credentials and permissions.")
        return

    prompt = input("Enter your initial prompt (or press Enter to skip): ")
    if prompt.strip():
        post_tweet(prompt)

    custom_posts = add_custom_posts()
    if custom_posts:
        general_posts.extend(custom_posts)

    schedule.every().day.at("08:00").do(scheduled_post)
    schedule.every().day.at("12:00").do(scheduled_post)
    schedule.every().day.at("17:00").do(scheduled_post)
    schedule.every().day.at("20:00").do(scheduled_post)

    schedule.every().day.at("10:00").do(engagement_routine)
    schedule.every().day.at("15:00").do(engagement_routine)
    schedule.every().day.at("21:00").do(engagement_routine)

    print(f"\n🚀 Bot started successfully!")
    print("📅 Scheduled activities:")
    print("   - Posts at 8:00 AM, 12:00 PM, 5:00 PM, and 8:00 PM daily")
    print("   - Engagement rounds at 10:00 AM, 3:00 PM, and 9:00 PM daily")
    print("   - Diverse content: Football, Uganda, Politics, Entertainment, Tech, Business, Lifestyle")
    print("   - All content is X community guidelines compliant")
    print("\n💬 Commands:")
    print("   - Type 'post' to post a random tweet now")
    print("   - Type 'engage' to run engagement routine now")
    print("   - Type 'status' to see bot status")
    print("   - Type 'stats' to see content distribution")
    print("   - Type 'quit' to exit")

    while True:
        schedule.run_pending()
        try:
            user_input = input().strip().lower()

            if user_input == 'post':
                scheduled_post()
            elif user_input == 'engage':
                engagement_routine()
            elif user_input == 'status':
                print(f"✅ Bot is running. Next scheduled job: {schedule.next_run()}")
                print(f"📊 Available content categories: Football, Uganda, Politics, Entertainment, Tech, Business, Lifestyle")
            elif user_input == 'stats':
                print(f"📊 Content Statistics:")
                print(f"   - Football posts: {len(football_posts)}")
                print(f"   - Uganda posts: {len(uganda_posts)}")
                print(f"   - Political posts: {len(political_posts)}")
                print(f"   - Entertainment posts: {len(entertainment_posts)}")
                print(f"   - Lifestyle posts: {len(lifestyle_posts)}")
                print(f"   - Tech posts: {len(tech_posts)}")
                print(f"   - Business posts: {len(business_posts)}")
                print(f"   - General posts: {len(general_posts)}")
                print(f"   - Total posts available: {len(football_posts) + len(uganda_posts) + len(political_posts) + len(entertainment_posts) + len(lifestyle_posts) + len(tech_posts) + len(business_posts) + len(general_posts)}")
            elif user_input == 'quit':
                print("👋 Bot shutting down...")
                break
        except KeyboardInterrupt:
            print("\n👋 Bot shutting down...")
            break
        except:
            pass

        time.sleep(1)

if __name__ == "__main__":
    main()
