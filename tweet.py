
from logging import exception
import requests
import json



class tweetcont:
    def __init__(self, user):
        self.userID = user
        

    def get_tweet(self):
        response = requests.get("")
        #GET /2/users/:id/tweets

    def processtweet(self):
        return self


def create_url():
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=pmarca"
    user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()
    

def main():
    reader = open('/Users/matt/Desktop/VCTrendy/globals.txt', 'r')
    credslist = reader.read().splitlines()
    API_key=credslist[0]
    API_key_secret=credslist[1]
    global bearer_token
    bearer_token = credslist[2]

    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    #test = tweetcont('/Users/matt/Desktop/VCTrendy/list.txt')
    print("Completed!")

if __name__== "__main__":
    main()
    
