class uraiRajutKata:
    def urai(self, line):
        ans = ''
        for l in range(len(line)+1):
            ans += line[:l]
        return ans
        
    def rajut(self, line):
        ans = ''
        l = len(line)
        for i in range(l):
            ans += line[i]
        #     print(ans)
            line = line[i+1:]
            if len(line) == 0:
                break
        return ans

x = uraiRajutKata()
# print(x.urai('Code'))
# print(x.urai('Python'))
# print(x.urai('Purwadhika'))

# print(x.rajut('CCoCodCode'))
# print(x.rajut('PPyPytPythPythoPython'))
# print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
