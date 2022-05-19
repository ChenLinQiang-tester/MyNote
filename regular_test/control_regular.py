# https://www.cnblogs.com/shenjianping/p/11647473.html

import re


def re_search():
    pattern = 'this'
    text = 'Does this text match the pattern?'

    match = re.search(pattern, text)

    s = match.start()
    e = match.end()

    print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
        match.re.pattern, match.string, s, e, text[s:e]))
    print("match.re.pattern:", match.re.pattern)
    print("match.string:", match.string)


def a():
    # Precompile the patterns
    regexes = [
        re.compile(p)
        for p in ['this', 'that']
    ]
    print(regexes)
    print([type(i) for i in regexes])
    print([i.pattern for i in regexes])
    text = 'Does this text match the pattern?'
    #
    # print('Text: {!r}\n'.format(text))
    #
    for regex in regexes:
        print('Seeking "{}" ->'.format(regex.pattern),
              end=' ')
    #
    #     if regex.search(text):
    #         print('match!')
    #     else:
    #         print('no match')


def aa():
    pattern = "test vv"
    print(re.compile(pattern=pattern))
    print(re.compile(pattern=pattern).pattern)
    print(re.compile(pattern=pattern).search('vv'))

# import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))


if __name__ == '__main__':
    aa()
