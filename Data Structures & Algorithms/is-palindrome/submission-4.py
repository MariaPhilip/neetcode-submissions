class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = "".join(c.lower() for c in s if self.isalphanum(c))
        front = 0
        back = len(clean)-1
        while front<back:
            if clean[front]!=clean[back]:
                return False
            front +=1
            back-=1
        return True

        

        # front = 0
        # back = len(s)-1
        # while front<back:
        #     while (not self.isalphanum(s[front])) and front<back :
        #         front = front+1
        #     while not self.isalphanum(s[back]) and back>front:
        #         back = back-1

        #     if s[front].lower()!=s[back].lower():
        #         return False
            
        #     front = front+1
        #     back = back-1
        # return True


    def isalphanum(self, char):
        return(
            (char>="A"and char<="Z") or  
            (char>="a"and char<="z") or  
            (char>="0"and char<="9"))
            
    
    

            

