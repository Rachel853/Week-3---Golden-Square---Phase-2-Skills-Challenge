class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string

        self.title = title
        self.contents = contents
        self.contents_words = contents.split()

    def format(self):
        # Returns:
        #   a formatted diary entry, e.g.:
        #   "My Title": These are the contents"

        return f"{self.title.title()}: {self.contents}"

    def count_words(self):
        # Returns"
        #   int: the number of words in the diary entey

        self.words = self.contents.split()
        self.number_words = len(self.words)
        return self.number_words

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing words the user can read per minute
        # Returns:
        #   Int: an estimate of how long it will take the user to read the contents based on the wpm they can read
        
        self.time = round(self.number_words / wpm)
        return self.time


    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an int representing the number of words the user can read in a minute
        #   minutes: an int representing the number of minutes the user has to read
        # Returns: 
        #   string: a chunk of the contents that the user could read in the given number of minutes

        # If called again, this function should return the next chunk of appropriate length. 
        #  This should continue until the contents is finished, after which, if the function is called  
        #again, the contents should be restarted from the beginning.
        
        if self.contents_words == []:
            self.contents_words = self.contents.split()
        
        chunk_num_words = wpm * minutes

        chunk = " ".join(self.contents_words[:chunk_num_words])

        self.contents_words = self.contents_recorder[chunk_num_words + 1:]

        return chunk
        