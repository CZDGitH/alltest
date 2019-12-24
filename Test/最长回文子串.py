#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        newS = '#'

        for i in range(len(s)):
            newS += (s[i]+'#')

        r = 0
        lenNews = len(newS)
        iLeft = lenNews // 2
        words = s[0]
        while iLeft > r:
            if iLeft % 2 == 0:
                tempWords = ''
                for j in range(1,iLeft,2):
                    if not newS[iLeft - j] == newS[iLeft + j]:
                        if r < j - 1:
                            r = j - 1
                            words = tempWords
                        break
                    else:
                        tempWords = newS[iLeft - j] + tempWords + newS[iLeft + j]
                        if j + 1 == iLeft:
                            r = j
                            words = tempWords
            else:
                tempWords = newS[iLeft]
                for j in range(2,iLeft,2):
                    if not newS[iLeft - j] == newS[iLeft + j]:
                        if r < j - 1:
                            r = j - 1
                            words = tempWords
                        break
                    else:
                        tempWords = newS[iLeft - j] + tempWords + newS[iLeft + j]
                        if j + 1 == iLeft:
                            r = j
                            words = tempWords
            iLeft -= 1
        iRight = lenNews//2 + 1
        while iRight < lenNews - r - 1:
            if iRight % 2 == 0:
                tempWords = ''
                for j in range(1,lenNews - 1 - iRight,2):
                    if not newS[iRight - j] == newS[iRight + j]:
                        if r < j - 1:
                            r = j - 1
                            words = tempWords
                        break
                    else:
                        tempWords = newS[iRight - j] + tempWords + newS[iRight + j]
                        if j == lenNews - iRight - 2:
                            r = j + 1
                            words = tempWords
            else:
                tempWords = newS[iRight]
                for j in range(2, lenNews - 1 - iRight, 2):
                    if not newS[iRight - j] == newS[iRight + j]:
                        if r < j - 1:
                            r = j - 1
                            words = tempWords
                        break
                    else:
                        tempWords = newS[iRight - j] + tempWords + newS[iRight + j]
                        if j == lenNews - iRight - 2:
                            r = j + 1
                            words = tempWords
            iRight += 1

        return words

t = Solution()
print(t.longestPalindrome("djriirtzdlsinaifnsfklkfks"))

"ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"