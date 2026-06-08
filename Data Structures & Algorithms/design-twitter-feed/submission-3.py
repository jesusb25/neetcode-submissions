class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # user : [users]
        self.posts = defaultdict(list) # user 
        self.postOrder = 1 # nth order of post
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # user : posts
        if userId not in self.follows:
            self.follows[userId].add(userId)
        self.posts[userId].append([-self.postOrder, tweetId])
        self.postOrder += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # grab 10 newest from all followed users O(n*log(n * 10))
        # heapify
        # grab top 10 most recent
        followee_posts = []
        result = []
        for followee in self.follows[userId]:
            posts = self.posts[followee][-10:]
            followee_posts += posts

        heapq.heapify(followee_posts)
        while followee_posts and len(result) < 10:
            _, postId = heapq.heappop(followee_posts)
            result.append(postId)
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        # add to follows 
        if followerId not in self.follows:
            self.follows[followerId].add(followerId)
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove from follows
        if followeeId in self.follows[followerId] and followerId != followeeId:
            self.follows[followerId].remove(followeeId)

