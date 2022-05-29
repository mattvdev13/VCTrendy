import listquery
import tweet

#exclusion_list = ["the", "be", "and", "a", "of", "to", "in", "i", "you", "it", "have", "to", "that", "for", "do", "he", "with", "on", "this", "we", "that", "not", "but", "they", "say", "at", "what", "his", "from", "go", "or", "by", "get", "she", "my", "can", "as", "know", "if", "me", "your", "all", "who", "about", "their", "will", "so", "would", "make", "just", "up", "think", "time", "there", "see", "her", "as", "out", "one", "come", "people", "take", "year", "him", "them", "some", "want", "how", "when", "which", "now", "like", "other", "could", "our", "into", "here", "then", "than", "look", "way", "more", "these", "no", "thing", "well", "because", "also", "two", "use", "tell", "good", "first", "man", "day", "find", "give", "more", "new", "one", "us", "any", "those", "very", "her", "need","is", "are", "-","been","team","thanks","company","companies","has","great","was","an", "post","opportunity","friend","key","said","learn","money","live","part","made","fun","around","enough","ever","top","done","life","does","without","TRUE","portfolio","entire","keep","point","forward","startups","off","build","own","believe","having","before","/","high","social","hope","super","ago","free","value","share","series","please","another","early","congratulations","experience","may","things","while","startup","hard","through","important","yes","feel","sure","lot","data","week","something","public","making","real","check","got","news","investors","few","both","open","its",")","long","book","where","same","building","—","were","don't","fund","happy","looking","+","support","working","change","being","tech","every","--","am","going","never","down","vc","right","proud","today","business","world","read","big","join","don’t","thank","doing","over","help","always","too","did","really","after","last","still","i'm","amazing","even","had","better","only","back","many","via","i’m","it's","next","founders","most","work","should","love","why","best","congrats","excited","years","much"]

def convertTuple(tup):
        # initialize an empty string
    return "{}:{}".format(tup[0], tup[1])

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

    #Test Case for one instance
    #output = tweet.tweetlists("pmarca")
    #for data in output.tweets:
    #    tweet.processtweets(topics_of_interest, data["text"], exclusion_list)

    for user in VCIDs.namedList:
        output = tweet.tweetlists(user)
        for data in output.tweets:
            tweet.processtweets(topics_of_interest, data["text"]) #, exclusion_list
    
    results = sorted(topics_of_interest.items(),key=lambda x: x[1], reverse=True)
    print(len(results))
    
    writer2 = open('/Users/matt/Desktop/VCTrendy/results.txt', 'w')
    writer2.truncate(0)

    for x in results:
        writer2.write(convertTuple(x))
        writer2.write("\n")
      
    writer2.close()
    print("Completed!")  


if __name__== "__main__":
    main()