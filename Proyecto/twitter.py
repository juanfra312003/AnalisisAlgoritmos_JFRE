import os
import asyncio
from twscrape import API, gather
from dotenv import load_dotenv

async def fetch_tweets(api, user_login, filename):
    user = await api.user_by_login(user_login)
    tweets = await gather(api.user_tweets(user.id, limit=100))  # Adjust limit as needed

    with open(filename, 'w', encoding='utf-8') as f:
        for tweet in tweets:
            f.write(f"{tweet.id}\t{tweet.rawContent}\n")

async def main():
    load_dotenv()  # load environment variables

    # Get credentials from environment variables
    username = os.getenv('TWITTER_USERNAME')
    password = os.getenv('TWITTER_PASSWORD')
    email = os.getenv('TWITTER_EMAIL')
    email_password = os.getenv('TWITTER_EMAIL_PASSWORD')

    # Delete existing database
    if os.path.exists("accounts.db"):
        os.remove("accounts.db")

    api = API()  # or API("path-to.db") - default is `accounts.db`

    # ADD ACCOUNTS
    await api.pool.add_account(username, password, email, email_password)
    await api.pool.login_all()

    # Fetch tweets for JDOviedoA
    await fetch_tweets(api, "JDOviedoA", "tweets_JDOviedoA.txt")

    # Fetch tweets for GustavoBolivar
    await fetch_tweets(api, "GustavoBolivar", "tweets_GustavoBolivar.txt")

if __name__ == "__main__":
    asyncio.run(main())
