# import twitter api package
import twint

#define twitter search function
def twitter_search(hashtag,limit, filename):
    '''
         This function used to search twitter hashtags.
         Inputs:
            hashtag: hashtag, string type
            limit: number of result needed, type integer
            filename: file name ex: data.csv, type string
        Return:
            return csv file contain search result 

    '''
    # start twitter object configure
    c = twint.Config()

    # set the hashtag search
    c.Search = hashtag

    # set result limit 
    c.Limit = limit

    # set option to save result as csv
    c.Store_csv = True

    # set the filename to save the result 
    c.Output = filename

    #Run the search
    twint.run.Search(c)

print("Twitter API --- searching for Hashtags")

# Start loop
while True:
    # ask user for hashrag
    hashtag = input("Enter hashtag name: ")
    
    # ask user for result limit 
    limit = int(input("Enter number of result needed:  "))
    
    # ask user for filename to save result
    filename = input("Enter filname to save data to it ex-> data.csv :")

    # call the search function api
    twitter_search(hashtag=hashtag, limit=limit,filename=filename)

    # ask user if need to another search
    answer = input('Do you need another search [y or N]: ')
    
    # if user choose to end the program 
    if answer.lower() == 'n':
        # break the loop
        break 
    # start new loop