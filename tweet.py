
from logging import exception
from urllib import response
import requests
import json


class tweetlists:
    def __init__(self, username):
        self.user= username
        self.ID = get_userid(username)
        self.tweets = get_tweets(self.ID, username)


def get_userid(user):
        usernames = "usernames={}".format(user)
        user_fields = "user.fields=name,description,created_at"
        try:
            url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
            json_response = connect_to_endpoint(url)
            return json_response["data"][0]["id"]
        except Exception as e:
            print("{} doesn't exist".format(user))
            exit

def get_tweets(ID, username):
        exclusions = "exclude=retweets"
        max_results = "max_results=50"
        url = "https://api.twitter.com/2/users/{}/tweets?{}&{}".format(ID,exclusions, max_results)
        tweet_list = connect_to_endpoint(url)
        if tweet_list:
            try:
                return tweet_list["data"]
            except Exception as e:
                print("missing tweets data from {}".format(username))
                exit
        else: 
            return {"none"}
        #print(self.tweets)

def processtweets(dict, data, exclusion_list):
    #if dict is not {}:
    #    return Exception
    
    # split all the word of the string.
    lst = data.split()
   
    # take each word from lst and pass it to the method count.
    for elements in lst:
        count(elements,dict, exclusion_list)

    return dict

def count(elements,dict,exclusion_list):
    
    if elements[-1] == '.':
        elements = elements[0:len(elements) - 1]
   
    # if there exists a key as "elements" then simply
    # increase its value.
    #
    if elements in dict:
        dict[elements] += 1
   
    # if the dictionary does not have the key as "elements" 
    # then create a key "elements" and assign its value to 1.
    else:
        if elements not in exclusion_list:
            dict.update({elements: 1})
    
    return dict
    
   

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    reader = open('/Users/matt/Desktop/VCTrendy/globals.txt', 'r')
    credslist = reader.read().splitlines()
    bearer_token = credslist[2]

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()
    

def main():
    #reader = open('/Users/matt/Desktop/VCTrendy/globals.txt', 'r')
    #credslist = reader.read().splitlines()
    #API_key=credslist[0]
    #API_key_secret=credslist[1]
    #global bearer_token
    #bearer_token = credslist[2]

    test = tweetlists('pmarca')

    #url = create_url()
    #json_response = connect_to_endpoint(url)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    #test = tweetcont('/Users/matt/Desktop/VCTrendy/list.txt')
    print("Completed!")

if __name__== "__main__":
    main()
    
