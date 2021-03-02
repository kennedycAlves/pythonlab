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























# print('Informe os caracteres solicitados: ')
# caracteres = input()

# insericaracteres = browser.find_element_by_id('idLetra')
# confirmar = browser.find_element_by_id('idSubmit')
# insericaracteres.send_keys(caracteres)
# confirmar.click()

# tag = browser.find_element_by_tag_name('html').text



# compItem = re.compile(r'(\d+)\sServiço', re.IGNORECASE)
# itens = compItem.findall(tag)

# #print(item)


# tag = re.sub(r'Tratamento Diferenciado Tipo.+', '', tag)

# listaTag = tag.split('\n')
# #print(listaTag)

# orgao = ' '.join(listaTag[0:2])
# print(orgao)

# pregao = ''.join(listaTag[4])
# print (pregao)

# objeto = ''.join(listaTag[6])
# print(objeto)

# descricao  = ''.join(listaTag[7])
# print(descricao)

# modo  = ''.join(listaTag[8])
# print(modo)

# data_realizacao  = ''.join(listaTag[9][41:])
# print(data_realizacao)

# data_abertura  = ''.join(listaTag[10][28:])
# print(data_abertura)

# cursor = con.cursor()
# sql = "INSERT INTO pregao(orgao, pregao, objeto, descricao, modo, data_realizacao, data_abertura) VALUES(%s,%s,%s,%s,%s,%s,%s)"
# cursor.execute(sql, (orgao, pregao, objeto, descricao, modo, data_realizacao, data_abertura))
# con.commit()  


# select_idpregao = ("SELECT id FROM pregao WHERE pregao like('%s')" % (pregao))
# cursor.execute("SELECT id FROM pregao WHERE pregao like('%s')" % (pregao))

# select_pregao_id = cursor.fetchone()

# pregao_id = select_pregao_id[0]



# #pregao_id = 0
# #for id in select_pregao_id:
# #
# #    pregao_id = int(id[0])
# #   
# #print(pregao_id)   




# original_window = browser.current_window_handle
# lista_itens = (listaTag[17:-3])
# browser.find_element_by_partial_link_text(itens[0]).click()
# popup_window = browser.current_window_handle
# i = 0
# inicio = 0


# for linha in lista_itens: 


    

#     if ("Qtde" not in linha):

#         split_linha = linha.split()
#         print(split_linha)

#         item = ''.join(split_linha[0])
#         print(item)
#         descricao = ' '.join(split_linha[1:5])
#         #print(descricao)
#         tratamento_diferenciado = ''.join(split_linha[6])
#         #print(tratamento_diferenciado)
#         aplicabilidade = ''.join(split_linha[7])
#         #print(aplicabilidade)
#         aplic_margem = ''.join(split_linha[8])
#         #print(aplic_margem)
        
#         if(len(split_linha) == 11):
#             situacao = ''.join(split_linha[9])
#             recurso = ''.join(split_linha[-1])
#             #print(situacao + " " + recurso)
#         else:
#             situacao = ' '.join(split_linha[9:13])
#             recurso = ''.join(split_linha[-1])
#             #print(situacao + " " + recurso)

    
#         sql2 = "INSERT INTO lista_itens(pregao_id, item, descricao, tratamento_diferenciado, aplicabilidade, aplic_margem, situacao, recurso  ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
#         cursor.execute(sql2, (pregao_id, item, descricao, tratamento_diferenciado, aplicabilidade, aplic_margem, situacao, recurso))
#         con.commit() 
    
    
#         janelas = browser.window_handles
#         browser.switch_to.window(janelas[1])
        
#         urllista = browser.current_url
#         # print(urllista)

#         # inicio = urllista[59:]
#         # print(inicio)
#         if(inicio == 0):
#             inicio = int(urllista[59:])
#             #print(inicio)
#             #inicio = int(inicio)
#         else:
#             inicio+=1
        
#         getUrl = urllista[:59]

#         # print(getUrl)
        
        
       
#         while (i < int(item)):
        
        
#             print('tratando:',getUrl+str(inicio))
#             #print(i)
        
#             browser.get(getUrl+str(inicio))
#             i+=1
#             sleep(3)
#             propostas = browser.find_element_by_tag_name('html').text  
#             texto_split = propostas.split('\n')
#             #print(texto_split)


#             for ind,linha in enumerate(texto_split):
#                 #print(ind,linha.strip())
#                 if('Descrição Detalhada' in linha.strip()):

#                 #   print('primeiro IF')
#                     cnpj_cpf = str(texto_split[ind - 1]).split()[0]
#                     fornecedor = ' '.join((texto_split[ind - 1]).split()[1:-2])
#                     qtde_ofertada = str(texto_split[ind - 1]).split()[-2]
#                     valor_total = str(texto_split[ind - 1]).split()[-1]
#                     descricao_detalhada = ' '.join(texto_split[ind].split()[5:-1])
#                     porte_ME_EPP = str(texto_split[ind + 1]).split()[2]
#                     declaracao_ME_EPP_COOP = str(texto_split[ind + 1]).split()[-1]
#                     declaracao7174 = str(texto_split[ind + 2]).split()[-1]
                    
                    
#                     cursor.execute("SELECT id FROM lista_itens WHERE pregao_id = %s AND item = %s " % (pregao_id, item))
#                     select_lista_itens_id = cursor.fetchone()
#                     lista_itens_id = select_lista_itens_id[0]



#                     sql3 = "INSERT INTO propostas(lista_itens_id,cnpj_cpf_fornecedor,fornecedor,qtde,valor_total,descricao_detalhada,porte_ME_EPP,declaracao_ME_EPP_COOP,declaração7174) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#                     cursor.execute(sql3, (lista_itens_id,str(cnpj_cpf),str(fornecedor),str(qtde_ofertada),str(valor_total),str(descricao_detalhada),str(porte_ME_EPP),str(declaracao_ME_EPP_COOP),str(declaracao7174))) 
#                                                  #print(lista_itens_id,cnpj_cpf_fornecedor,fornecedor,qtde,valor_total,descricao_detalhada,porte_ME_EPP,declaracao_ME_EPP_COOP,declaração7174)
#             con.commit()
#     else:
       
       
#         browser.switch_to.window(original_window)
#         proxima_pagina = browser.find_element_by_id("proximas")
#         proxima_pagina.click()
#         idLetra = browser.find_element_by_id('idLetra')
#         idSubmit = browser.find_element_by_id('idSubmit')
#         print('Informe os caracteres solicitados: ')
#         caracteres = input()
#         idLetra.send_keys(caracteres)
#         idSubmit.click()
#         tag2 = browser.find_element_by_tag_name('html').text
#         listaTag2 = tag2.split('\n')
#         # print(listaTag2[17:-4])
#         lista_itens.extend(listaTag2[17:-4])
#         # print(lista_itens)

    
        
