class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        freq = {}
        word_len = len(words[0])
        ans = []
        
        for w in words:
            if w not in freq:
                freq[w] = 1
            else:
                freq[w] += 1
        
        
        def slideWindow(l):
            found_freq = {}
            total_matched = 0
            
            for r in range(l, len(s), word_len):
                if r + word_len > n:
                    break
                new_word = s[r: r + word_len]
                if new_word not in freq:
                    found_freq = {}
                    total_matched = 0
                    l = r + word_len
                else:
                    found_freq[new_word] = found_freq.get(new_word, 0) + 1
                    if found_freq[new_word] > freq[new_word]:
                        while found_freq[new_word] > freq[new_word]:
                            left_most = s[l : l+word_len]
                            found_freq[left_most] -= 1
                            l += word_len
                            if left_most != new_word:
                                total_matched -= 1
                    else:
                        total_matched += 1
                if total_matched == len(words):
                    ans.append(l)
                

        for i in range(word_len):
            slideWindow(i)

        return ans