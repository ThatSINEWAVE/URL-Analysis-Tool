# twitter_module.py
import os
import tweepy
import json


def load_twitter_config():
    # Load API keys from twitter_config.json
    with open("configs/twitter_config.json", "r") as config_file:
        api_keys = json.load(config_file)

    # Authenticate to Twitter
    client = tweepy.Client(consumer_key=api_keys["consumer_key"],
                           consumer_secret=api_keys["consumer_secret"],
                           access_token=api_keys["access_token"],
                           access_token_secret=api_keys["access_token_secret"])
    return client


def list_output_files():
    output_files = os.listdir("outputs")
    print("Available output files:")
    for i, output_file in enumerate(output_files):
        print(f"{i+1}. {output_file}")
    return output_files


def start_twitter_module():
    client = load_twitter_config()

    while True:
        tweet_option = input("Enter 1 to tweet text, 2 to tweet from an output file, or 3 to quit: ")

        if tweet_option == "1":
            tweet_text = input("Enter the tweet text (max 280 characters): ")
            if len(tweet_text) > 280:
                print("Tweet text exceeds 280 characters. Please try again.")
                continue
            try:
                response = client.create_tweet(text=tweet_text)
                print("Tweet posted successfully!")
                print(f"Tweet ID: {response.data['id']}")
            except tweepy.errors.Forbidden as e:
                print(f"Error posting tweet: {e}")
            except tweepy.errors.TweepyException as e:
                print(f"Error posting tweet: {e}")

        elif tweet_option == "2":
            output_files = list_output_files()
            file_choice = input("Enter the number of the file you want to tweet from: ")
            try:
                file_choice = int(file_choice)
                if 1 <= file_choice <= len(output_files):
                    file_path = os.path.join("outputs", output_files[file_choice - 1])
                    with open(file_path, "r") as chosen_file:
                        tweet_text = chosen_file.read()
                        if len(tweet_text) > 280:
                            print("Content of the selected file exceeds 280 characters. Please try again.")
                            continue
                        try:
                            response = client.create_tweet(text=tweet_text)
                            print("Tweet posted successfully!")
                            print(f"Tweet ID: {response.data['id']}")
                        except tweepy.errors.Forbidden as e:
                            print(f"Error posting tweet: {e}")
                        except tweepy.errors.TweepyException as e:
                            print(f"Error posting tweet: {e}")
                        except tweepy.errors.BadRequest as e:
                            print("Error posting tweet: The Tweet contains an invalid URL.")
                else:
                    print("Invalid file choice. Please enter a valid number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

        elif tweet_option == "3":
            print("Exiting the Twitter module...")
            break

        else:
            print("Invalid option. Please try again.")
            continue

        retry = input("Do you want to tweet again? (y/n) ")
        if retry.lower() != "y":
            break
