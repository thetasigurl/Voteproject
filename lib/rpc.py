import argparse
import chain
parser = argparse.ArgumentParser()
connstr = "http://jenn:password@127.0.0.1:2776"
#print chain.getNewWallet(connstr)
print chain.getVotesFromWallet(connstr,"1A4wnUwbeGrQFfj9pQ9SCUgqAqj7xKfZ6vE1VW")