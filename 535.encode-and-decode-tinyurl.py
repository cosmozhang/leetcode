#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (74.38%)
# Total Accepted:    53.9K
# Total Submissions: 72.4K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
# 
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.
# 
# Design the encode and decode methods for the TinyURL service. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.
# 
#
class Codec(object):

    def __init__(self):
        self.l2s_dic = {}
        self.s2l_dic = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.l2s_dic:
            self.l2s_dic[longUrl] = str(len(self.l2s_dic))
            self.s2l_dic[self.l2s_dic[longUrl]] = longUrl
            
        return 'http://tinyurl.com/'+str(self.l2s_dic[longUrl])
            

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        s = shortUrl.replace('http://tinyurl.com/', '')
        return self.s2l_dic[s]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
