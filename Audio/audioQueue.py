from Audio.youtube import load_from_url, parse_url

class SongQueue:

    def __init__(self) -> None:
        self.queue = []

    def Add(self, elem: str):
        self.queue.append({ "content": elem, "isLoaded": False})

    def Find(self, elem: str):
        for qelem in self.queue:
            if (qelem["content"] == elem):
                return qelem
        return None
    
    def SetIsLoaded(self, elem) -> None:
        self.Find(elem)["isLoaded"] = True
    
    def Take(self):
        return self.queue.pop()

    def Clear(self):
        self.queue = []

    def IsEmpty(self):
        return len(self.queue) == 0

async def add_song_from_url(sgqueue: SongQueue, url: str):
    if (sgqueue == None):
        sgqueue = SongQueue()

    sgqueue.Add(parse_url(url))
    await load_from_url(url)
    sgqueue.SetIsLoaded(parse_url(url))