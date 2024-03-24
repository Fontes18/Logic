import sqlite3
from sqlite3 import Error

############ CRIANDO CONEXÃO COM BANCO DE DADOS EXISTENTE #############

def ConexaoBanco():
    caminho = "C:\\Users\\defon\\Desktop\\Lógica de Programação\\sqlite\\teste.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()
############ CRIANDO TABELA #############

vsql = """CREATE TABLE tb_contatos2(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("tabela criada")
    except Error as ex:
        print(ex)

criarTabela(vcon, vsql)
vcon.close()
