class OrderBookEntry:
    def __init__(self, price=None, amount=None, updateId=None):
        # implement properties
        self.price = price
        self.amount = amount
        self.updateId = updateId

    def __lt__(self, other):
        if isinstance(other, OrderBookEntry):
            return self.price < other.price
        return NotImplemented


def truncateOverlapEntries(bidBook, askBook, dex):
    if dex != 0:
        truncateOverlapEntriesDex(bidBook, askBook)
    else:
        truncateOverlapEntriesCentralised(bidBook, askBook)

def truncateOverlapEntriesDex(bidBook, askBook):
    bidIterator = reversed(bidBook)
    askIterator = iter(askBook)
    while bidIterator and askIterator:
        topBid = bidIterator[-1]
        topAsk = askIterator[0]
        if topBid.price >= topAsk.price:
            if topBid.amount*topBid.price > topAsk.amount*topAsk.price:
                askBook.remove(askIterator[0])
            else:
                bidBook.remove(bidIterator[-1])
        else:
            break

def truncateOverlapEntriesCentralised(bidBook, askBook):
    
    n = len(bidBook)
    bidIterator = n-1
    askIterator = 0
    

    while bidIterator >= 0 and askIterator < len(askBook):

        topBid = bidBook[bidIterator]
        topAsk = askBook[askIterator]
        if topBid.price >= topAsk.price:
            if topBid.updateId > topAsk.updateId:
                askIterator += 1
            else:
                bidIterator -= 1
        else:
            break
            
    
    bidBook[:] = bidBook[:(bidIterator+1)]
    askBook[:] = askBook[askIterator:]
