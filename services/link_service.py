from data import conectar

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

    cursor = conexao.execute("SELECT * FROM links")
    links = cursor.fetchall()

    conexao.close()
    return links

def remove_link(nome):
    conexao = conectar()

    conexao.execute(
        "DELETE FROM links WHERE nome = ?",
        (nome,)
    )
    
    conexao.commit()
    conexao.close()

def edit_link(nome, novo_nome=None, nova_url=None):
    conexao = conectar()

    if novo_nome is not None and nova_url is not None:
        conexao.execute(
            "UPDATE links SET nome = ?, url = ? WHERE nome = ?",
            (novo_nome, nova_url, nome)
        )

    elif novo_nome is not None:
        conexao.execute(
            
            "UPDATE links SET nome = ? WHERE nome = ?",
            (novo_nome, nome)
        )

    elif nova_url is not None:
        conexao.execute(
            "UPDATE links SET url = ? WHERE nome = ?",
            (nova_url, nome)
        )

    else:
        conexao.close()
        return False

    alterados = conexao.execute("SELECT changes()").fetchone()[0]
    conexao.commit()
    conexao.close()

    return alterados > 0

    

    
    