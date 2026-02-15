# Polybot

A Twitter bot with follow functionality built using Python and Tweepy.

## Features

- Follow users by username or user ID
- Unfollow users
- Get list of users you're following
- Get list of your followers
- Built-in rate limit handling

## Prerequisites

- Python 3.7 or higher
- Twitter Developer Account with API credentials

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jacques1906/Polybot.git
   cd Polybot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Twitter API credentials**
   
   a. Create a Twitter Developer account at https://developer.twitter.com/
   
   b. Create a new app and generate API keys and tokens
   
   c. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   
   d. Edit `.env` and add your Twitter API credentials:
   ```
   TWITTER_API_KEY=your_api_key_here
   TWITTER_API_SECRET=your_api_secret_here
   TWITTER_ACCESS_TOKEN=your_access_token_here
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here
   TWITTER_BEARER_TOKEN=your_bearer_token_here
   ```

## Usage

### Basic Usage

Run the bot:
```bash
python polybot.py
```

### Using as a Module

```python
from polybot import Polybot

# Initialize the bot
bot = Polybot()

# Follow a user by username
bot.follow_user('username')

# Follow a user by ID
bot.follow_user_by_id(123456789)

# Unfollow a user
bot.unfollow_user('username')

# Get list of users you're following
following = bot.get_following(max_results=100)

# Get list of your followers
followers = bot.get_followers(max_results=100)
```

## API Methods

### `follow_user(username)`
Follow a user by their username (without @).

**Parameters:**
- `username` (str): The username to follow

**Returns:**
- `bool`: True if successful, False otherwise

### `follow_user_by_id(user_id)`
Follow a user by their user ID.

**Parameters:**
- `user_id` (int): The user ID to follow

**Returns:**
- `bool`: True if successful, False otherwise

### `unfollow_user(username)`
Unfollow a user by their username.

**Parameters:**
- `username` (str): The username to unfollow

**Returns:**
- `bool`: True if successful, False otherwise

### `get_following(max_results=10)`
Get list of users that the bot is following.

**Parameters:**
- `max_results` (int): Maximum number of results (default: 10, max: 1000)

**Returns:**
- `list`: List of usernames

### `get_followers(max_results=10)`
Get list of followers.

**Parameters:**
- `max_results` (int): Maximum number of results (default: 10, max: 1000)

**Returns:**
- `list`: List of follower usernames

## Security Notes

- Never commit your `.env` file to version control
- Keep your API credentials secure
- Be aware of Twitter's rate limits and automation rules
- Follow Twitter's Developer Agreement and Policy

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
