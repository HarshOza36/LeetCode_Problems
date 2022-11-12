class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # Time complexity: O(m*n)
        # Space complexity: O(m*n)
        def justify(line, width, max_width):
            total_spaces = max_width - width
            words_cnt = len(line)
            if words_cnt == 1:
                # then we just add all the spaces to end
                return line[0] + ' ' * total_spaces
            else:
                rem_spaces_to_ins = (words_cnt - 1)
                # space_betn_words list tells us to insert i spaces for idx i 
                # after the word on line[i]
                space_betn_words = rem_spaces_to_ins * [total_spaces // rem_spaces_to_ins]
                
                
                # Now distribute spaces via round robin to the left words
                # so left get more spaces than right
                spaces_cnt = total_spaces % rem_spaces_to_ins
                for i in range(spaces_cnt):
                    space_betn_words[i] += 1

                aligned_words_list = []
                for i in range(rem_spaces_to_ins):
                    # add word then spaces
                    aligned_words_list.append(line[i])
                    aligned_words_list.append(space_betn_words[i] * ' ')
                
                # adding last word
                aligned_words_list.append(line[-1])
                return ''.join(aligned_words_list)


        answer = []
        line, width = [], 0
        for word in words:
            if width + len(word) + len(line) <= maxWidth:
                # keep adding words until we can fill out maxWidth
                # width = sum of length of all words without spaces
                # len(line) = number of spaces to insert between words
                line.append(word)
                width += len(word)
            else:
                # cannot add more words so justify
                answer.append(justify(line, width, maxWidth))
                # reset new line and new width
                line, width = [word], len(word)
        
        remaining_spaces = maxWidth - width - len(line)
        answer.append(' '.join(line) + (remaining_spaces + 1) * ' ')
        return answer