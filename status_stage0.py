import re 
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import mysql.connector
from mysql.connector import errorcode
from time import sleep

con = mysql.connector.connect(user='', password='', host='', database='')


browser = webdriver.Firefox()  
type(browser)

tipo = "?Opc=0"
browser.get('http://comprasnet.gov.br/livre/Pregao/Lista_Pregao_Filtro.asp'+tipo)

wait = WebDriverWait(browser, 5)

codUasg = browser.find_element_by_id("co_uasg")
numprp = browser.find_element_by_id("numprp")
lstSituacao = browser.find_element_by_id("lstSituacao")
ok = browser.find_element_by_id("ok")

#Usasg
teste = '135100'

#N° Pregão
teste2 = '22021'
lstSituacao.send_keys("Todas")
codUasg.send_keys(teste)
numprp.send_keys(teste2)
ok.click()

tag = browser.find_element_by_tag_name('html').text

original_window = browser.current_window_handle


dados = browser.find_element_by_partial_link_text('22021')
esclarecimentos = browser.find_element_by_partial_link_text('Esclarecimentos')

split_tag = tag.split("\n")

pregao = split_tag[6][0:6]
# print(pregao)

uasg = split_tag[6][7:12]
# print(uasg)

orgao = split_tag[6][13:-33]
# print(orgao)

inicio_envio_propostas = split_tag[6][-33:-16]
# print(inicio_envio_propostas)


fim_envio_propostas =  split_tag[6][-16:]
# print(fim_envio_propostas)

dados.click()
popup_window = browser.window_handles
browser.switch_to.window(popup_window[1])
dados_tag = browser.find_element_by_tag_name('html').text
split_dados = dados_tag.split("\n")

objeto = split_dados[6][36:]

descricao = split_dados[7][31:]

modo = split_dados[8][17:]

# 


browser.close
browser.switch_to.window(original_window)
esclarecimentos.click()
sleep(3)
popup_window = browser.window_handles
print(popup_window)
browser.switch_to.window(popup_window[2])
url_esclarecimentos = browser.current_url
sleep(3)
# texto = urlopen(url_esclarecimentos).read()
# print(texto)

def convert(list): 
    return tuple(i for i in list) 

def soupMount(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    return soup

def inseriEsclarecimentos(idPregao):
    texto = str(soupMount(url_esclarecimentos))
    split_texto = texto.split("\n")
    url_avisos1_part1 = 'http://comprasnet.gov.br/livre/Pregao/'+split_texto[94][-39:-13]
    url_avisos1_completa = url_avisos1_part1 + split_texto[94][-9:-3]

    texto2_soup = soupMount(url_avisos1_completa)

    esclarecimentos_data =  texto2_soup.select('.mensagem2')

    cursor.execute("SELECT data_esclarecimento FROM esclarecimentos WHERE id_pregao LIKE('%s')" % (idPregao))
    datas = cursor.fetchall()
    lista = list()
    
    for linha in esclarecimentos_data:

        data = str(linha)
        format_data = data[25:-10]
        # print(idPregao)
        # print(format_data)
        # print(url_avisos1_completa)
        
        if(len(datas) > 0):
            print("velho")
        
            for data in datas:
                for data2 in data:
                    lista.append(data2)

            if(format_data not in tuple(lista)):
            
            
                sql2 = "INSERT INTO esclarecimentos(id_pregao, data_esclarecimento, link ) VALUES(%s,%s,%s)"
                cursor.execute(sql2, (idPregao, format_data, url_avisos1_completa))

                     
        else:
            print("novo")
            print(format_data)
            sql2 = "INSERT INTO esclarecimentos(id_pregao, data_esclarecimento, link ) VALUES(%s,%s,%s)"
            cursor.execute(sql2, (idPregao, format_data, url_avisos1_completa))

    con.commit() 



cursor = con.cursor()

cursor.execute("SELECT pregao, uasg, id FROM pregao WHERE pregao LIKE('%s') AND uasg LIKE (%s)" % (pregao,uasg))
select_pregao_uasg = cursor.fetchall()
if(len(select_pregao_uasg) > 0):
    # prepara_pregao_uasg = select_pregao_uasg[0]

    # valida_pregao = prepara_pregao_uasg[0]
    # valida_uarsg = prepara_pregao_uasg[1]
    # print("registro encontrado")
    tratamento = select_pregao_uasg[0]
    valida_id_pregao = tratamento[2]
    inseriEsclarecimentos(valida_id_pregao)
    
else:

    # print(pregao)
    # print(uarsg)


    sql = "INSERT INTO pregao(orgao, uasg, pregao, objeto, descricao, modo, inicio_envio_propostas, fim_envio_propostas ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (orgao, uasg, pregao, objeto, descricao, modo, inicio_envio_propostas, fim_envio_propostas ))
    con.commit() 

    
    cursor.execute("SELECT id FROM pregao WHERE pregao LIKE('%s') AND uasg LIKE (%s)" % (pregao,uasg))
    select_pregao_id = cursor.fetchone()

    pregao_id = select_pregao_id[0]



    inseriEsclarecimentos(pregao_id)
