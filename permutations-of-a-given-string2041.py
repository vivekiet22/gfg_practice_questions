#User function Template for python3

# def pp(l1):
    

    
class Solution:
    def find_permutation(self, S):
        list1 = []
        s = list(S)
        def print_str(s,l,r):
            if l==r:
                a = "".join(s)
                list1.append(a)
                # print(list1)
        
            else:
                for i in range(l,r):
                    s[l],s[i] = s[i],s[l]
                    print_str(s,l+1,r)
                    s[l],s[i] = s[i],s[l]
            # print("l1:".l1)
        print_str(s,0,len(S))
        # Code here
        
        return sorted(list1)
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        ob = Solution()
        ans = ob.find_permutation(S)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends
