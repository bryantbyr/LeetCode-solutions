#804. Unique Morse Code Words

#Created by bryantbyr on 20180712
#Time:O(n)
#Space:O(n)
#set + dict + list

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        r = set()
        for word in words:
            transform = ""
            for letter in word:
                transform = transform + d[letter]
            r.add(transform)
        return r.__len__()


s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
