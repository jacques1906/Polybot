"""
Tests for Polybot Twitter bot
"""

import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

# Add parent directory to path to import polybot
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from polybot import Polybot


class TestPolybot(unittest.TestCase):
    """Test cases for Polybot"""
    
    @patch.dict(os.environ, {}, clear=True)
    def test_missing_credentials_raises_error(self):
        """Test that missing credentials raise ValueError"""
        with self.assertRaises(ValueError) as context:
            bot = Polybot()
        self.assertIn("Missing required Twitter API credentials", str(context.exception))
    
    @patch('polybot.tweepy.Client')
    @patch('polybot.tweepy.API')
    @patch('polybot.tweepy.OAuth1UserHandler')
    @patch.dict(os.environ, {
        'TWITTER_API_KEY': 'test_key',
        'TWITTER_API_SECRET': 'test_secret',
        'TWITTER_ACCESS_TOKEN': 'test_token',
        'TWITTER_ACCESS_TOKEN_SECRET': 'test_token_secret',
        'TWITTER_BEARER_TOKEN': 'test_bearer'
    })
    def test_initialization_with_credentials(self, mock_auth, mock_api, mock_client):
        """Test that bot initializes with valid credentials"""
        bot = Polybot()
        self.assertIsNotNone(bot.client)
        self.assertIsNotNone(bot.api)
        mock_client.assert_called_once()
    
    @patch('polybot.tweepy.Client')
    @patch('polybot.tweepy.API')
    @patch('polybot.tweepy.OAuth1UserHandler')
    @patch.dict(os.environ, {
        'TWITTER_API_KEY': 'test_key',
        'TWITTER_API_SECRET': 'test_secret',
        'TWITTER_ACCESS_TOKEN': 'test_token',
        'TWITTER_ACCESS_TOKEN_SECRET': 'test_token_secret',
        'TWITTER_BEARER_TOKEN': 'test_bearer'
    })
    def test_follow_user_success(self, mock_auth, mock_api, mock_client):
        """Test successful user follow"""
        # Setup mocks
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance
        
        mock_user_data = Mock()
        mock_user_data.id = 123456
        mock_user_response = Mock()
        mock_user_response.data = mock_user_data
        mock_client_instance.get_user.return_value = mock_user_response
        
        # Test
        bot = Polybot()
        result = bot.follow_user('testuser')
        
        self.assertTrue(result)
        mock_client_instance.get_user.assert_called_with(username='testuser')
        mock_client_instance.follow_user.assert_called_with(123456)
    
    @patch('polybot.tweepy.Client')
    @patch('polybot.tweepy.API')
    @patch('polybot.tweepy.OAuth1UserHandler')
    @patch.dict(os.environ, {
        'TWITTER_API_KEY': 'test_key',
        'TWITTER_API_SECRET': 'test_secret',
        'TWITTER_ACCESS_TOKEN': 'test_token',
        'TWITTER_ACCESS_TOKEN_SECRET': 'test_token_secret',
        'TWITTER_BEARER_TOKEN': 'test_bearer'
    })
    def test_follow_user_not_found(self, mock_auth, mock_api, mock_client):
        """Test following non-existent user"""
        # Setup mocks
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance
        
        mock_user_response = Mock()
        mock_user_response.data = None
        mock_client_instance.get_user.return_value = mock_user_response
        
        # Test
        bot = Polybot()
        result = bot.follow_user('nonexistent')
        
        self.assertFalse(result)
        mock_client_instance.follow_user.assert_not_called()
    
    @patch('polybot.tweepy.Client')
    @patch('polybot.tweepy.API')
    @patch('polybot.tweepy.OAuth1UserHandler')
    @patch.dict(os.environ, {
        'TWITTER_API_KEY': 'test_key',
        'TWITTER_API_SECRET': 'test_secret',
        'TWITTER_ACCESS_TOKEN': 'test_token',
        'TWITTER_ACCESS_TOKEN_SECRET': 'test_token_secret',
        'TWITTER_BEARER_TOKEN': 'test_bearer'
    })
    def test_follow_user_by_id(self, mock_auth, mock_api, mock_client):
        """Test following user by ID"""
        # Setup mocks
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance
        
        # Test
        bot = Polybot()
        result = bot.follow_user_by_id(123456)
        
        self.assertTrue(result)
        mock_client_instance.follow_user.assert_called_with(123456)
    
    @patch('polybot.tweepy.Client')
    @patch('polybot.tweepy.API')
    @patch('polybot.tweepy.OAuth1UserHandler')
    @patch.dict(os.environ, {
        'TWITTER_API_KEY': 'test_key',
        'TWITTER_API_SECRET': 'test_secret',
        'TWITTER_ACCESS_TOKEN': 'test_token',
        'TWITTER_ACCESS_TOKEN_SECRET': 'test_token_secret',
        'TWITTER_BEARER_TOKEN': 'test_bearer'
    })
    def test_unfollow_user(self, mock_auth, mock_api, mock_client):
        """Test unfollowing a user"""
        # Setup mocks
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance
        
        mock_user_data = Mock()
        mock_user_data.id = 123456
        mock_user_response = Mock()
        mock_user_response.data = mock_user_data
        mock_client_instance.get_user.return_value = mock_user_response
        
        # Test
        bot = Polybot()
        result = bot.unfollow_user('testuser')
        
        self.assertTrue(result)
        mock_client_instance.unfollow_user.assert_called_with(123456)
    
    @patch('polybot.tweepy.Client')
    @patch('polybot.tweepy.API')
    @patch('polybot.tweepy.OAuth1UserHandler')
    @patch.dict(os.environ, {
        'TWITTER_API_KEY': 'test_key',
        'TWITTER_API_SECRET': 'test_secret',
        'TWITTER_ACCESS_TOKEN': 'test_token',
        'TWITTER_ACCESS_TOKEN_SECRET': 'test_token_secret',
        'TWITTER_BEARER_TOKEN': 'test_bearer'
    })
    def test_get_following(self, mock_auth, mock_api, mock_client):
        """Test getting following list"""
        # Setup mocks
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance
        
        mock_me_data = Mock()
        mock_me_data.id = 999999
        mock_me_response = Mock()
        mock_me_response.data = mock_me_data
        mock_client_instance.get_me.return_value = mock_me_response
        
        mock_user1 = Mock()
        mock_user1.username = 'user1'
        mock_user2 = Mock()
        mock_user2.username = 'user2'
        
        mock_following_response = Mock()
        mock_following_response.data = [mock_user1, mock_user2]
        mock_client_instance.get_users_following.return_value = mock_following_response
        
        # Test
        bot = Polybot()
        following = bot.get_following()
        
        self.assertEqual(len(following), 2)
        self.assertIn('user1', following)
        self.assertIn('user2', following)


if __name__ == '__main__':
    unittest.main()
