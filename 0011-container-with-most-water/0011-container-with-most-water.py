class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=height
        i=0
        j=len(a)-1
        maxi=min(a[i],a[j])*(j-i)
        while(i<j):
            maxi_up=min(a[i],a[j])*(j-i)
            if maxi<maxi_up:
                maxi=maxi_up
            if a[i]<a[j]:
                i=i+1
            elif a[j]<a[i]:
                j=j-1
            elif a[j]==a[i]:
                i=i+1
                j=j-1
        return(maxi)
        