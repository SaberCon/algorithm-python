import bisect
from collections import defaultdict
from typing import List


class TweetCounts:

    def __init__(self):
        self.tweet_dict = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweet_dict[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunk = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        tweets = self.tweet_dict[tweetName]
        start, end = bisect.bisect_left(tweets, startTime), bisect.bisect_right(tweets, endTime)
        ans = []
        for i in range(startTime, endTime + 1, chunk):
            j = min(i + chunk - 1, endTime)
            k = bisect.bisect_right(tweets, j, start, end)
            ans.append(k - start)
            start = k
        return ans
