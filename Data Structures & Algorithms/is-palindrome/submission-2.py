class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s)-1
        while front<back:
            while (not self.isalphanum(s[front])) and front<back :
                front = front+1
            while not self.isalphanum(s[back]) and back>front:
                back = back-1

            if s[front].lower()!=s[back].lower():
                return False
            else:
                front = front+1
                back = back-1
        return True


    def isalphanum(self, char):
        if (char>="A"and char<="Z") or  (char>="a"and char<="z") or  (char>="0"and char<="9"):
            return True
        else:
            return False
    
    

            

