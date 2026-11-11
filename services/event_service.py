from data import conectar

def add_event(nome, data, hora):
    conexao = conectar()

    conexao.execute(
        "INSERT INTO eventos (nome, data, hora) VALUES (?,?,?)",
        (nome, data, hora)
    )   

    conexao.commit()
    conexao.close()

def list_events():
    conexao = conectar()

    cursor = conexao.execute("SELECT * FROM eventos")
    events = cursor.fetchall()

    conexao.close()
    return events

def remove_event(event_id):
    conexao = conectar()

    conexao.execute("DELETE FROM eventos WHERE id = ?", (event_id,))
    conexao.commit()
    conexao.close()

def edit_event(event_id, nome, data, hora):
    conexao = conectar()

    conexao.execute(
        "UPDATE eventos SET nome = ?, data = ?, hora = ? WHERE id = ?",
        (nome, data, hora, event_id)
    )

    conexao.commit()
    conexao.close()