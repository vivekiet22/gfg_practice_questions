#User function Template for python3

class Solution:
    def getCount(self, N):
        # code here 
        sum =0
        chain_len = 0
        count = 0
        while sum <N:
            chain_len+=1
            sum+=chain_len
        for L in range(1,chain_len):
            a = (N - L*(L+1)/2)/(L+1)
            if a == int(a):
                count+=1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.getCount(N))
# } Driver Code Ends
