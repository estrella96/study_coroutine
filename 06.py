import xml.etree.ElementTree as et

'''
#修改
tree=et.parse(r'05.xml')
root=tree.getroot()
for e in root.iter('name'):
    print(e.text)
for stu in root.iter('Student'):
    name=stu.find('name')

    if name != None:
        name.set('test',name.text*2)
tree.write('05.xml')
'''
#创建
stu=et.Element('Student')

name=et.SubElement(stu,'Name')
name.attrib={'lang','en'}
name.text='wing'

age=et.SubElement(stu,'Age')
age.text=18
et.dump(stu)