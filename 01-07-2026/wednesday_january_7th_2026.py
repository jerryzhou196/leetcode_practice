from collections import defaultdict

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        ans = []
        r = defaultdict(lambda: defaultdict(set))
        for transaction in transactions: 
            name, time, amount, city = transaction.split(',')
            r[time][name].add(city)

        for transaction in transactions: 
            name, time, amount, city = transaction.split(',')
            amount, time = int(amount), int(time)
            added = False
            for i in range(time - 60, time + 61):
                time_range = str(i)
                if not added and (amount > 1000 or (time_range in r and name in r[time_range] and (len(r[time_range][name]) > 1 or next(iter(r[time_range][name])) != city))): 
                    ans.append(transaction)
                    added = True
            
        return ans
