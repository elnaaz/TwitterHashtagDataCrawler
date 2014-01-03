#simple file-writer class
class Storage:

    #app simple - we can use file as data-storage
    storageFile = 'db.txt'

    def save(self, tweet):
        databaseFile = open(self.storageFile, 'a+')
        databaseFile.write('@' + tweet.author.screen_name + ':')
        databaseFile.write(tweet.text.encode('utf8') + '\n')
        databaseFile.write('-----------------------' + '\n')
        databaseFile.close()

