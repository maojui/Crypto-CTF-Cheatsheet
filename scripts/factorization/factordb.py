
import requests
from bs4 import BeautifulSoup
from functools import reduce

def factordb(n):
    
    url = 'http://factordb.com/index.php?query={}'.format(n)
    td = BeautifulSoup(requests.get(url).text,'html.parser').select('td')
    states = list(td[11].strings)[0].strip(" ")
    print({
        'C'    : "[ ] Composite, Still no factors known.",
        "CF"   : "[ ] Composite, factors known, If number is small, You can try it again.",
        'FF'   : "[+] Composite, fully factored",
        "P"    : "[+] Definitely prime",
        "PRP"  : "[ ] Probably prime",
        "U"    : "[-] Factordb Search Failed",
        "Unit" : "[-] 1 is nothing.",
        "N"    : "This number is not in database (and was not added due to your settings)"
    }[states])
    
    if not states in  ['FF','P','PRP','CF'] :
        return None

    factor = ''
    ss = list(td[13].strings)
    for i,s in enumerate(ss):
        if ('.' in s) :
            for a in td[13].select('a') :
                if s == a.string:
                    temp1 = requests.get('http://factordb.com/'+ a['href'])
                    tsoup = BeautifulSoup(temp1.text,'html.parser')
                    temp2 = requests.get('http://factordb.com/'+ tsoup.select('td')[12].a['href'])
                    tsoup2 = BeautifulSoup(temp2.text,'html.parser')
                    for dnum in tsoup2.select('td')[-1].strings:
                        factor += dnum.strip('\n')
                    break

        elif s[0] != '<' :
            factor += s
        else :
            pass
    
    pair = {}

    _, factors = factor.split(' = ')
    if ')^' in factors :
        factors, exp = factors.split('^')
        factors = factors.strip('\(').strip('\)')
        pair = { x:int(exp) for x in list(map(int,factors.split(' · ')))}
    elif '^' in factors :
        for f in factors.split(' · '):
            if '^' in f :
                num,exp = f.split('^')
                pair[int(num)] = int(exp)
            else :
                pair[int(f)] = int(1)
    else :
        pair = { x:1 for x in list(map(int,factors.split(' · ')))}
    
    assert n == reduce( lambda x, y: x*y, [pow(k,v) for k,v in pair.items()],1), 'factordb function failed....'
    return pair

if __name__ == "__main__":
    print(factordb(1983429174039147129347801923749127489127048971930471289374019273491))