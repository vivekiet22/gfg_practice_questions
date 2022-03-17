#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

class Solution:
    def ValidPair(self, a, n): 
        # Your code goes here
        a.sort(reverse = True)
    #     print(a)
        c = 0
        l = 0
        h = len(a)-1
        while(h>l):
            s = a[l]+a[h]
            if s <=0:
                h-=1
            if s >0:
                c+=h-l
                l+=1
            
        return c
        
        
        
        
        
    #     for i in range(0,len(a)):
    #         k = len(a)-1
    #         while i<k:
                
    #             if a[i]+a[k] >0:
    #                 c+=k-i
    #                 break
    #                # print(k,i)
    #             k-=1
    #     return c
            
           
                
        

#{ 
#Driver Code Starts.

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.ValidPair(array, n)
        print(ans) 



#} Driver Code Ends
