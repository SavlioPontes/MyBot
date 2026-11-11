from .data import conectar

def add_link(nome, url):
    conexao = conectar()

    conexao.execute(
        "INSERT INTO links (nome, url) VALUES (?,?)",
        (nome, url)
    )   

    conexao.commit()
    conexao.close()

def list_links():
    conexao = conectar()

    
    