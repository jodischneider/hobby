###############################################################################
# Gets definitions for a list of words and adds them to a user's wordnik list.
#
# Internal variables:
# FILENAME: text file with a list of words, one per line
# LISTPERMALINK: string identifying the wordnik list 
#                (delete https://www.wordnik.com/lists/ from the URL)
#
# Requires secret.py with user information:
# APIKEY (wordnik API key) set in secret.py
# USERNAME (wordnik username) set in secret.py
# PASSWORD (wordnik password) set in secret.py
#
# Writing personal lists via the Wordnik API requires their API Hobby Plan
# since February 28, 2019
###############################################################################


from wordnik import * #see https://github.com/wordnik/wordnik-python3
import secret

FILENAME = "words.txt"
LISTPERMALINK='phrases-and-words-i-didnt-know'


apiUrl = 'http://api.wordnik.com/v4'
apiKey = secret.APIKEY
client = swagger.ApiClient(apiKey, apiUrl)

account = AccountApi.AccountApi(client)
response = account.authenticate(secret.USER, secret.PW)
token = response.token


wordniklist= WordListApi.WordListApi(client)

wordApi = WordApi.WordApi(client)
file = open(FILENAME, "r")

wordlist = file.readlines()
words = []
definitions = []
print("------------------------")
print("Definitions")
print("------------------------")
for word in wordlist:
	word = word.lower().rstrip()
	words.append(word)
	textdefinition = (wordApi.getDefinitions(word, limit=1))[0].text
	definitions.append(textdefinition)
	print(word+":", textdefinition)
file.close()

wordniklist.addWordsToWordList(LISTPERMALINK, token, body=words)
print("------------------------")
print("Added", len(words), "words to the list https://www.wordnik.com/lists/"+LISTPERMALINK)
print("------------------------------------------------------------------------")
