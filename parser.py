from re import findall


def strip(string, char='\n'):
    return string.replace(char, '')


def parse(string):
    content_type = r'\s*[a-zA-Z]*\s*:'
    res = {}
    string = strip(strip(string), char='\t')
    for block in string.split('end;'):
        if len(block) < 1:
            continue
        cntt = findall(content_type, block)[0]
        block = block.replace(cntt, '')
        res[cntt[:-1]] = {}
        for param in block.split(';'):
            if len(param) < 1:
                continue
            param = param.split(':')
            res[cntt[:-1]][param[0]] = param[1]

    return res

if __name__ == '__main__':
    c = open('bot/init.bot')
    print(parse(c.read()))
    c.close()
