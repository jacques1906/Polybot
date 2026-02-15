"""
Polybot - A Twitter bot with follow functionality
"""

import os
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Polybot:
    """Twitter bot with follow functionality"""
    
    def __init__(self):
        """Initialize the bot with Twitter API credentials"""
        # Get credentials from environment variables
        api_key = os.getenv('TWITTER_API_KEY')
        api_secret = os.getenv('TWITTER_API_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        
        if not all([api_key, api_secret, access_token, access_token_secret]):
            raise ValueError("Missing required Twitter API credentials. Please check your .env file.")
        
        # Authenticate with Twitter API v2
        self.client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True
        )
        
        # Also initialize API v1.1 for additional functionality
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)
        
        print("Polybot initialized successfully!")
    
    def follow_user(self, username):
        """
        Follow a user by username
        
        Args:
            username (str): The username to follow (without @)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Get user ID from username
            user = self.client.get_user(username=username)
            if user.data:
                user_id = user.data.id
                # Follow the user
                self.client.follow_user(user_id)
                print(f"Successfully followed @{username}!")
                return True
            else:
                print(f"User @{username} not found.")
                return False
        except tweepy.TweepyException as e:
            print(f"Error following @{username}: {e}")
            return False
    
    def follow_user_by_id(self, user_id):
        """
        Follow a user by their ID
        
        Args:
            user_id (int): The user ID to follow
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.client.follow_user(user_id)
            print(f"Successfully followed user ID {user_id}!")
            return True
        except tweepy.TweepyException as e:
            print(f"Error following user ID {user_id}: {e}")
            return False
    
    def unfollow_user(self, username):
        """
        Unfollow a user by username
        
        Args:
            username (str): The username to unfollow (without @)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Get user ID from username
            user = self.client.get_user(username=username)
            if user.data:
                user_id = user.data.id
                # Unfollow the user
                self.client.unfollow_user(user_id)
                print(f"Successfully unfollowed @{username}!")
                return True
            else:
                print(f"User @{username} not found.")
                return False
        except tweepy.TweepyException as e:
            print(f"Error unfollowing @{username}: {e}")
            return False
    
    def get_following(self, max_results=10):
        """
        Get list of users that the bot is following
        
        Args:
            max_results (int): Maximum number of results to return (default 10, max 1000)
        
        Returns:
            list: List of usernames the bot is following
        """
        try:
            # Get the authenticated user's ID
            me = self.client.get_me()
            if me.data:
                my_id = me.data.id
                following = self.client.get_users_following(
                    id=my_id,
                    max_results=min(max_results, 1000)
                )
                
                if following.data:
                    usernames = [user.username for user in following.data]
                    print(f"Following {len(usernames)} users:")
                    for username in usernames:
                        print(f"  @{username}")
                    return usernames
                else:
                    print("Not following anyone yet.")
                    return []
        except tweepy.TweepyException as e:
            print(f"Error getting following list: {e}")
            return []
    
    def get_followers(self, max_results=10):
        """
        Get list of followers
        
        Args:
            max_results (int): Maximum number of results to return (default 10, max 1000)
        
        Returns:
            list: List of follower usernames
        """
        try:
            # Get the authenticated user's ID
            me = self.client.get_me()
            if me.data:
                my_id = me.data.id
                followers = self.client.get_users_followers(
                    id=my_id,
                    max_results=min(max_results, 1000)
                )
                
                if followers.data:
                    usernames = [user.username for user in followers.data]
                    print(f"Have {len(usernames)} followers:")
                    for username in usernames:
                        print(f"  @{username}")
                    return usernames
                else:
                    print("No followers yet.")
                    return []
        except tweepy.TweepyException as e:
            print(f"Error getting followers list: {e}")
            return []


def main():
    """Main function to demonstrate bot functionality"""
    try:
        # Initialize the bot
        bot = Polybot()
        
        # Example usage - follow a user
        print("\nExample: Following a user")
        print("To follow a user, call: bot.follow_user('username')")
        
        # Get current following list
        print("\nGetting current following list...")
        bot.get_following()
        
    except ValueError as e:
        print(f"Error: {e}")
        print("\nPlease create a .env file with your Twitter API credentials.")
        print("See .env.example for the required format.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
