from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://comprasnet.gov.br/ConsultaLicitacoes/ConsLicitacaoDia.asp")
soup = BeautifulSoup(html, "html.parser")


'''
lista = soup.find_all("b","br")
for i in lista:
    print(i)
'''


#print(soup.prettify())
paginas = str(soup.center.string)

limpa =re.sub(r'\s+', '',paginas)
limpa = re.sub(r'Licitações', '', limpa)
limpa = re.sub(r'[()]', '', limpa)
limpa = re.sub(r'[-|de]', ' ', limpa)


print(limpa)


processa = re.sub(r'&nbsp', ' ', tres)
    processa2 = re.sub(r'\s+', ' ', processa)
    processa3 = re.sub(r'<..>', ' ', processa2)
    processa4 = re.sub(r'<b>', '\n', processa3)
    processa5 = re.sub(r';Objeto:', '', processa4)
    processa5 = re.sub(r';Objeto:', '', processa4)
    processa6 = re.sub(r'  ;', ' ', processa5)
    processa7 = re.sub(r'xx', '', processa6)
    processa8 = re.sub(r'</td>', '', processa7)
    tres2 = processa8