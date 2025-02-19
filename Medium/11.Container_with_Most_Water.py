return self.using_max(height)
    
    def using_max(self,height):
        max_h=max(height)
        l=0
        r=len(height)-1
        area=0

        while True:
            w = r-l
            
            if height[r]>height[l]:
                new_area = w*height[l]
                l+=1
            else:
                new_area = w*height[r]
                r-=1

            if new_area>area:
                area = new_area
            if w*max_h < area:
                break

        return area

    def two_pointers(self,height):
        result=0
        n=len(height)
        l=0
        r=1
        
        h=0
        w = n-r-l
        while l+r<n:
            L = height[l]
            R = height[-r]
            h1=min(L,R)
            if h1>=h+1:
                h=h1
                area=w*h
                if area > result:
                    result=area
            if L<R:
                l+=1
            else:
                r+=1
            w-=1
        return result    
