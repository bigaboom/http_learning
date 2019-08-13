from xml.etree import ElementTree

slov = {'red' : 0, 'green' : 0, 'blue' : 0}

def childs(mom, points):
    slov[mom.attrib['color']] = slov[mom.attrib['color']] + points
    for i in mom:
        childs(i, points + 1)
    return

tree = input()
root = ElementTree.fromstring(tree)
childs(root, 1)
print(slov['red'], slov['green'], slov['blue'])