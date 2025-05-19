# On Twitter, the algorithmic timeline is sorted such that the tweet ranked higher has a higher likelihood of getting user engagement so as to maximize overall engagement in the app.
# The authors of tweets provide one of the key signals in determining users' likelihood of engaging with a particular tweet. For example, Jack Dorsey tends to generally like tweets authored by Biz Stone -- so serving Biz's tweets to Jack would ensure higher engagement. At the same time, we also have to make sure we are serving a more "diverse" timeline -- showing tweets for different authors -- to improve user experience..
# The question is:
# Given a list of tweets sorted by scores descending with their corresponding scores and authors, transform the list such that consecutive tweets cannot be from the same author whenever possible. Always prefer the author whose tweets have the highest score if there are multiple possible authors to be considered.
# Conditions:
# 0.0 ‹ Score <= 1.0
# Example IO
# Each tuple (score, authorId) represents a tweet. Input is a list of tweets with authors ranked in some initial ordering. The output is a list of
# tweets such that tweets by the same author are not together.
# Example 1
# Input: rankedTweetList = [(6, "A"), (.5, "A"), (.4, "B"), (.3, "B"), (.2, "C"), (.1, "C")]
# Output: rankedTweetListAfterDiversity = [(.6, "A"), (.4, "B"), (.5, "A"), (.3, "B"), (.2, "C"'), (.1,

def transform_timeline(ranked_tweet_list):

    # (6, "A"), (.5, "A")
    # (4, "B"), (3, "B")
    # (2, "C") , (1, "C")



