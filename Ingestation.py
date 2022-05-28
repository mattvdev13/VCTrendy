import listquery
import tweet

exclusion_list = ["the", "be", "and", "a", "of", "to", "in", "i", "you", "it", "have", "to", "that", "for", "do", "he", "with", "on", "this", "we", "that", "not", "but", "they", "say", "at", "what", "his", "from", "go", "or", "by", "get", "she", "my", "can", "as", "know", "if", "me", "your", "all", "who", "about", "their", "will", "so", "would", "make", "just", "up", "think", "time", "there", "see", "her", "as", "out", "one", "come", "people", "take", "year", "him", "them", "some", "want", "how", "when", "which", "now", "like", "other", "could", "our", "into", "here", "then", "than", "look", "way", "more", "these", "no", "thing", "well", "because", "also", "two", "use", "tell", "good", "first", "man", "day", "find", "give", "more", "new", "one", "us", "any", "those", "very", "her", "need"]

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

def main():
    reader = open('/Users/matt/Desktop/VCTrendy/globals.txt', 'r')
    credslist = reader.read().splitlines()
    #API_key=credslist[0]
    #API_key_secret=credslist[1]
    global bearer_token
    bearer_token = credslist[2]

    VCIDs = listquery.VClist('/Users/matt/Desktop/VCTrendy/list.txt')

    print("Started!")

    topics_of_interest = {}

    for user in VCIDs.namedList:
        output = tweet.tweetlists(user)
        for data in output.tweets:
            tweet.processtweets(topics_of_interest, data["text"], exclusion_list)
    
    results = sorted(topics_of_interest.items(),key=lambda x: x[1], reverse=True)
    print(len(results))
    
    writer2 = open('/Users/matt/Desktop/VCTrendy/results.txt', 'w')

    for x in results:
        writer2.write(convertTuple(x))
        writer2.write("\n")
      
    writer2.close()
    print("Completed!")  


if __name__== "__main__":
    main()