import regex as re

class TextileCode:

    def __init__(self, code, i, j, k):
        self.code = code
        self.HorizontalNum = j
        self.VerticalNum = k
        self.CrossingNum = i

    def BasicValidation(self):
        code = self.code
        new_code = code.replace(" ", "")
        # print(new_code)
        basic_pattern = '(([hv][[:digit:]](\\+|-))(\\,)?)+([[:digit:]](\\+|-)?)+'
        val = False
        if len(code) == 0:
            print('Error: No words entered before pressing Return Key.')
            return val
        elif code.endswith(',') == True:
            print('Error: The Gauss paragraph end with a comma.')
            return val
        else:
            if re.match(basic_pattern, new_code) == None:
                print('Error: The basic format is not valid.')
                return val
            else:
                val = True
                print('The basic format is valid.')
                return val

    def getEdgepair(self):
        code = self.code
        j = self.HorizontalNum
        k = self.VerticalNum

        word_set = code.split(",")
        Edgepair_Set = []
        for i in range(len(word_set)):

            symbol_set = word_set[i].split(" ")

            for i in range(len(symbol_set)):
                if i < len(symbol_set) - 1:
                    Edgepair1 = [symbol_set[i], symbol_set[i + 1], '+']
                    Edgepair2 = [symbol_set[i + 1], symbol_set[i], '-']
                    Edgepair_Set.append(Edgepair1)
                    Edgepair_Set.append(Edgepair2)
                else:
                    Edgepair1 = [symbol_set[i], symbol_set[0], '+']
                    Edgepair2 = [symbol_set[0], symbol_set[i], '-']
                    Edgepair_Set.append(Edgepair1)
                    Edgepair_Set.append(Edgepair2)

        # symbol_set = code.split(" ")

        h_set = []
        for i in range(j):
            h_set.append('h%s' % (i + 1))
        # print(h_set)
        if j == 1:
            Edgepair1 = ['c', h_set[0], '+']
            Edgepair2 = [h_set[0], 'c', '-']
            Edgepair3 = ['c', h_set[0], '-']
            Edgepair4 = [h_set[0], 'c', '+']
            Edgepair_Set.append(Edgepair1)
            Edgepair_Set.append(Edgepair2)
            Edgepair_Set.append(Edgepair3)
            Edgepair_Set.append(Edgepair4)
        else:
            for i in range(j + 1):
                if i == 0:
                    Edgepair1 = ['c', h_set[i], '+']
                    Edgepair2 = [h_set[i], 'c', '-']
                    Edgepair_Set.append(Edgepair1)
                    Edgepair_Set.append(Edgepair2)
                elif i == j:
                    Edgepair1 = [h_set[i - 1], 'c', '+']
                    Edgepair2 = ['c', h_set[i - 1], '-']
                    Edgepair_Set.append(Edgepair1)
                    Edgepair_Set.append(Edgepair2)
                else:
                    Edgepair1 = [h_set[i - 1], h_set[i], '+']
                    Edgepair2 = [h_set[i], h_set[i - 1], '-']
                    Edgepair_Set.append(Edgepair1)
                    Edgepair_Set.append(Edgepair2)

        v_set = []
        for i in range(k):
            v_set.append('v%s' % (i + 1))
        # print(v_set)
        if k == 1:
            Edgepair1 = ['c', v_set[0], '+']
            Edgepair2 = [v_set[0], 'c', '-']
            Edgepair3 = ['c', v_set[0], '-']
            Edgepair4 = [v_set[0], 'c', '+']
            Edgepair_Set.append(Edgepair1)
            Edgepair_Set.append(Edgepair2)
            Edgepair_Set.append(Edgepair3)
            Edgepair_Set.append(Edgepair4)
        else:
            for i in range(k + 1):
                if i == 0:
                    Edgepair1 = ['c', v_set[i], '+']
                    Edgepair2 = [v_set[i], 'c', '-']
                    Edgepair_Set.append(Edgepair1)
                    Edgepair_Set.append(Edgepair2)
                elif i == k:
                    Edgepair1 = [v_set[i - 1], 'c', '+']
                    Edgepair2 = ['c', v_set[i - 1], '-']
                    Edgepair_Set.append(Edgepair1)
                    Edgepair_Set.append(Edgepair2)
                else:
                    Edgepair1 = [v_set[i - 1], v_set[i], '+']
                    Edgepair2 = [v_set[i], v_set[i - 1], '-']
                    Edgepair_Set.append(Edgepair1)
                    Edgepair_Set.append(Edgepair2)

        # print(Edgepair_Set)
        # print(len(Edgepair_Set))
        return Edgepair_Set


def multiplication(symbol1, symbol2):
    if symbol1 == symbol2:
        return '+'
    else:
        return '-'
def negative(symbol):
    if symbol == '+':
        return '-'
    else:
        return '+'


def algorithm(Edgepair_Set, i, j, k):

    # start cycle count
    cycle = 0
    # initiate the first cycle
    CYC = []
    UsedPair = []

    while len(Edgepair_Set) != len(UsedPair):

        for pair in Edgepair_Set:
            while pair not in UsedPair:
                # print('-------------new cycle--------------')
                inputpair = pair
                # print('input: ')
                # print(inputpair)

                # runs while the next input pair is not already part of the cycle.
                # returns FALSE if a cycle contains both oriented passes of a graph edge

                while inputpair not in CYC:

                    # print('input not in CYC')
                    # print(inputpair)

                    basic_pattern1 = '[[:digit:]](\\+|-)'  # eg: '1+'
                    basic_pattern2 = '[h][[:digit:]]'  # eg: 'h1'
                    basic_pattern3 = '[h][[:digit:]](\\+|-)'  # eg: 'h1+'
                    basic_pattern4 = '[v][[:digit:]]'  # eg: 'v1'
                    basic_pattern5 = '[v][[:digit:]](\\+|-)'  # eg: 'v1+'

                    # select edge next to input pair

                    # case: b = i
                    if inputpair[1].isdigit() == True:
                        # print('case: b = i')
                        for str in Edgepair_Set:
                            if str[0] == inputpair[1] + '+' or str[0] == inputpair[1] + '-':
                                if str[2] == multiplication(str[0][1], inputpair[2]):
                                    # print('out: [i+,...]')
                                    outputpair = str
                                    if outputpair[2] == '+':
                                        outputpair_ = [outputpair[1], outputpair[0], '-']
                                    elif outputpair[2] == '-':
                                        outputpair_ = [outputpair[1], outputpair[0], '+']

                                    if outputpair_ in CYC:
                                        break
                                        return False
                                    break

                    # case: b = i+/-
                    elif inputpair[1][0].isdigit() == True and inputpair[1].isdigit() == False:
                        # print('case: b = i+')
                        for str in Edgepair_Set:
                            if str[0] == inputpair[1][0] and str[2] == negative(multiplication(inputpair[2],inputpair[1][1])):
                                outputpair = str
                                if outputpair[2] == '+':
                                    outputpair_ = [outputpair[1], outputpair[0], '-']
                                elif outputpair[2] == '-':
                                    outputpair_ = [outputpair[1], outputpair[0], '+']

                                if outputpair_ in CYC:
                                    break
                                    return False
                                break

                    # case: b = hj
                    elif inputpair[1][0] == 'h' and inputpair[1][1].isdigit() == True and len(inputpair[1]) == 2:
                        # print('case: b = hj')
                        for str in Edgepair_Set:

                            if str[0] == inputpair[1] + '+' or str[0] == inputpair[1] + '-':
                                if str[2] == multiplication(inputpair[2],str[0][2]):
                                    outputpair = str
                                    if outputpair[2] == '+':
                                        outputpair_ = [outputpair[1], outputpair[0], '-']
                                    elif outputpair[2] == '-':
                                        outputpair_ = [outputpair[1], outputpair[0], '+']

                                    if outputpair_ in CYC:
                                        break
                                        return False
                                    break

                    # case: b = hj+/-
                    elif inputpair[1][0] == 'h' and inputpair[1][1].isdigit() == True and len(inputpair[1]) == 3:
                        # print('case: b = hj+')
                        for str in Edgepair_Set:

                            if str[0] == inputpair[1][:-1] and str[2] == negative(multiplication(inputpair[2],inputpair[1][2])):
                                # print('output: [hi,...]')
                                outputpair = str
                                if outputpair[2] == '+':
                                    outputpair_ = [outputpair[1], outputpair[0], '-']
                                elif outputpair[2] == '-':
                                    outputpair_ = [outputpair[1], outputpair[0], '+']

                                # print('find output')
                                # print(outputpair)
                                if outputpair_ in CYC:
                                    break
                                    return False
                                break

                    # case: b = vk
                    elif inputpair[1][0] == 'v' and inputpair[1][1].isdigit() == True and len(inputpair[1]) == 2:
                        # print('case: b = vk')
                        for str in Edgepair_Set:

                            if str[0] == inputpair[1] + '+' or str[0] == inputpair[1] + '-':
                                if str[2] == negative(multiplication(inputpair[2],str[0][2])):
                                    outputpair = str
                                    if outputpair[2] == '+':
                                        outputpair_ = [outputpair[1], outputpair[0], '-']
                                    elif outputpair[2] == '-':
                                        outputpair_ = [outputpair[1], outputpair[0], '+']

                                    if outputpair_ in CYC:
                                        break
                                        return False
                                    break

                    # case: b = vk+/-
                    elif inputpair[1][0] == 'v' and inputpair[1][1].isdigit() == True and len(inputpair[1]) == 3:
                        # print('case: b = vk+')
                        for str in Edgepair_Set:
                            if str[0] == inputpair[1][:-1] and str[2] == multiplication(inputpair[2], inputpair[1][2]):
                                # print('find output [vi,..]')
                                outputpair = str
                                if outputpair[2] == '+':
                                    outputpair_ = [outputpair[1], outputpair[0], '-']
                                elif outputpair[2] == '-':
                                    outputpair_ = [outputpair[1], outputpair[0], '+']

                                if outputpair_ in CYC:
                                    break
                                    return False
                                break

                    # case: b = c & a = hi
                    elif inputpair[1] == 'c' and re.match(basic_pattern2, inputpair[0]) != None:
                        for str in Edgepair_Set:

                            if str[0] == 'c' and re.match(basic_pattern4, str[1]) != None and str[2] == inputpair[2]:
                                outputpair = str
                                if outputpair[2] == '+':
                                    outputpair_ = [outputpair[1], outputpair[0], '-']
                                elif outputpair[2] == '-':
                                    outputpair_ = [outputpair[1], outputpair[0], '+']

                                if outputpair_ in CYC:
                                    break
                                    return False
                                break

                    # case: b = c & a = vk
                    elif inputpair[1] == 'c' and re.match(basic_pattern4, inputpair[0]) != None:
                        for str in Edgepair_Set:

                            if str[0] == 'c' and re.match(basic_pattern2, str[1]) != None and str[2] == negative(inputpair[2]):
                                outputpair = str
                                if outputpair[2] == '+':
                                    outputpair_ = [outputpair[1], outputpair[0], '-']
                                elif outputpair[2] == '-':
                                    outputpair_ = [outputpair[1], outputpair[0], '+']

                                if outputpair_ in CYC:
                                    break
                                    return False
                                break

                    '''
                    print('output')
                    print(outputpair)
                    '''
                    # adds pair to current cycle
                    CYC.append(inputpair)
                    # continues with selected pair as input pair
                    inputpair = outputpair

                    # print('new input')
                    # print(inputpair)

                # Increments count when cycle complete
                if len(CYC) > 1:
                    cycle = cycle + 1
                    # tracks which edges have been used in a cycle
                    UsedPair.extend(CYC)
                    '''
                    print('CYC')
                    print(CYC)
                    print('cycleNum')
                    print(cycle)
                    '''
                    CYC = []



        return cycle == i+j+k+1



print('Input the textile code \nseparate each symbol by a space，'
      'and separate each word by a comma \nfor example: h1+ 1+ 2 v1+ 1 2+')
code = input('textile code is:')
i = int(input('Input the number of crossings: '))
j = int(input('Input the number of horizontal arcs: '))
k = int(input('Input the number of vertical arcs: '))

textile = TextileCode(code, i, j, k)
Edgepair_Set = textile.getEdgepair()
# print(Edgepair_Set)
# print(len(Edgepair_Set))



if textile.BasicValidation() == True:
    print(algorithm(Edgepair_Set, i, j, k))












        




