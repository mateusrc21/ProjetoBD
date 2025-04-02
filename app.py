import psycopg2
from psycopg2.extras import RealDictCursor

# Configuração da conexão com o banco de dados
def get_connection():
    return psycopg2.connect(
        dbname="Projetobd",  # Substitua pelo nome do seu banco
        user="postgres",   # Substitua pelo seu usuário
        password="ma2189", # Substitua pela sua senha
        host="localhost",
        port="5432"
    )

# Funções CRUD para Titulo
def create_titulo(isbn, titulo_obra, data_publicacao, idioma, numero_pagina):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Titulo (ISBN, titulo_obra, data_publicacao, idioma, numero_pagina) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
            (isbn, titulo_obra, data_publicacao, idioma, numero_pagina)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print(f"Erro ao criar título: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_titulo(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM Titulo WHERE id = %s;", (id,))
        return dict(cur.fetchone()) if cur.rowcount > 0 else None
    except Exception as e:
        print(f"Erro ao ler título: {e}")
    finally:
        cur.close()
        conn.close()

def update_titulo(id, isbn=None, titulo_obra=None, data_publicacao=None, idioma=None, numero_pagina=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        query = "UPDATE Titulo SET "
        params = []
        if isbn: query += "ISBN = %s, "; params.append(isbn)
        if titulo_obra: query += "titulo_obra = %s, "; params.append(titulo_obra)
        if data_publicacao: query += "data_publicacao = %s, "; params.append(data_publicacao)
        if idioma: query += "idioma = %s, "; params.append(idioma)
        if numero_pagina: query += "numero_pagina = %s, "; params.append(numero_pagina)
        query = query.rstrip(", ") + " WHERE id = %s;"
        params.append(id)
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar título: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_titulo(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Titulo WHERE id = %s;", (id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar título: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# Funções CRUD para Usuario
def create_usuario(cpf, primeiro_nome, sobrenome, data_nascimento, email, telefone):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Usuario (CPF, primeiro_nome, sobrenome, data_nascimento, email, telefone) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;",
            (cpf, primeiro_nome, sobrenome, data_nascimento, email, telefone)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_usuario(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM Usuario WHERE id = %s;", (id,))
        return dict(cur.fetchone()) if cur.rowcount > 0 else None
    except Exception as e:
        print(f"Erro ao ler usuário: {e}")
    finally:
        cur.close()
        conn.close()

def update_usuario(id, cpf=None, primeiro_nome=None, sobrenome=None, data_nascimento=None, email=None, telefone=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        query = "UPDATE Usuario SET "
        params = []
        if cpf: query += "CPF = %s, "; params.append(cpf)
        if primeiro_nome: query += "primeiro_nome = %s, "; params.append(primeiro_nome)
        if sobrenome: query += "sobrenome = %s, "; params.append(sobrenome)
        if data_nascimento: query += "data_nascimento = %s, "; params.append(data_nascimento)
        if email: query += "email = %s, "; params.append(email)
        if telefone: query += "telefone = %s, "; params.append(telefone)
        query = query.rstrip(", ") + " WHERE id = %s;"
        params.append(id)
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_usuario(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Usuario WHERE id = %s;", (id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# Funções CRUD para Cliente
def create_cliente(id_usuario, limite_emprestimo):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Cliente (id_usuario, limite_emprestimo) VALUES (%s, %s) RETURNING id;",
            (id_usuario, limite_emprestimo)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print(f"Erro ao criar cliente: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_cliente(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM Cliente WHERE id = %s;", (id,))
        return dict(cur.fetchone()) if cur.rowcount > 0 else None
    except Exception as e:
        print(f"Erro ao ler cliente: {e}")
    finally:
        cur.close()
        conn.close()

def update_cliente(id, id_usuario=None, limite_emprestimo=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        query = "UPDATE Cliente SET "
        params = []
        if id_usuario: query += "id_usuario = %s, "; params.append(id_usuario)
        if limite_emprestimo: query += "limite_emprestimo = %s, "; params.append(limite_emprestimo)
        query = query.rstrip(", ") + " WHERE id = %s;"
        params.append(id)
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_cliente(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Cliente WHERE id = %s;", (id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar cliente: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# Funções CRUD para Bibliotecario
def create_bibliotecario(id_usuario):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Bibliotecario (id_usuario) VALUES (%s) RETURNING id;",
            (id_usuario,)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print(f"Erro ao criar bibliotecário: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_bibliotecario(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM Bibliotecario WHERE id = %s;", (id,))
        return dict(cur.fetchone()) if cur.rowcount > 0 else None
    except Exception as e:
        print(f"Erro ao ler bibliotecário: {e}")
    finally:
        cur.close()
        conn.close()

def update_bibliotecario(id, id_usuario=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        if id_usuario:
            cur.execute("UPDATE Bibliotecario SET id_usuario = %s WHERE id = %s;", (id_usuario, id))
            conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar bibliotecário: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_bibliotecario(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Bibliotecario WHERE id = %s;", (id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar bibliotecário: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# Funções CRUD para Emprestimo
def create_emprestimo(data_validade, data_emprestimo):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Emprestimo (data_validade, data_emprestimo) VALUES (%s, %s) RETURNING id;",
            (data_validade, data_emprestimo)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print(f"Erro ao criar empréstimo: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_emprestimo(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM Emprestimo WHERE id = %s;", (id,))
        return dict(cur.fetchone()) if cur.rowcount > 0 else None
    except Exception as e:
        print(f"Erro ao ler empréstimo: {e}")
    finally:
        cur.close()
        conn.close()

def update_emprestimo(id, data_validade=None, data_emprestimo=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        query = "UPDATE Emprestimo SET "
        params = []
        if data_validade: query += "data_validade = %s, "; params.append(data_validade)
        if data_emprestimo: query += "data_emprestimo = %s, "; params.append(data_emprestimo)
        query = query.rstrip(", ") + " WHERE id = %s;"
        params.append(id)
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar empréstimo: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_emprestimo(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Emprestimo WHERE id = %s;", (id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar empréstimo: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# Funções CRUD para Devolucao
def create_devolucao(status, data_devolucao):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Devolucao (status, data_devolucao) VALUES (%s, %s) RETURNING id;",
            (status, data_devolucao)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print(f"Erro ao criar devolução: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_devolucao(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM Devolucao WHERE id = %s;", (id,))
        return dict(cur.fetchone()) if cur.rowcount > 0 else None
    except Exception as e:
        print(f"Erro ao ler devolução: {e}")
    finally:
        cur.close()
        conn.close()

def update_devolucao(id, status=None, data_devolucao=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        query = "UPDATE Devolucao SET "
        params = []
        if status: query += "status = %s, "; params.append(status)
        if data_devolucao: query += "data_devolucao = %s, "; params.append(data_devolucao)
        query = query.rstrip(", ") + " WHERE id = %s;"
        params.append(id)
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar devolução: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_devolucao(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Devolucao WHERE id = %s;", (id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar devolução: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# Funções CRUD para Reserva
def create_reserva(data_reserva, data_limite_emprestimo):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO Reserva (data_reserva, data_limite_emprestimo) VALUES (%s, %s) RETURNING id;",
            (data_reserva, data_limite_emprestimo)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        print(f"Erro ao criar reserva: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def read_reserva(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM Reserva WHERE id = %s;", (id,))
        return dict(cur.fetchone()) if cur.rowcount > 0 else None
    except Exception as e:
        print(f"Erro ao ler reserva: {e}")
    finally:
        cur.close()
        conn.close()

def update_reserva(id, data_reserva=None, data_limite_emprestimo=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        query = "UPDATE Reserva SET "
        params = []
        if data_reserva: query += "data_reserva = %s, "; params.append(data_reserva)
        if data_limite_emprestimo: query += "data_limite_emprestimo = %s, "; params.append(data_limite_emprestimo)
        query = query.rstrip(", ") + " WHERE id = %s;"
        params.append(id)
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        print(f"Erro ao atualizar reserva: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def delete_reserva(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Reserva WHERE id = %s;", (id,))
        conn.commit()
    except Exception as e:
        print(f"Erro ao deletar reserva: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# Menu Interativo
def menu():
    tabelas = {
        "1": ("Titulo", create_titulo, read_titulo, update_titulo, delete_titulo),
        "2": ("Usuario", create_usuario, read_usuario, update_usuario, delete_usuario),
        "3": ("Cliente", create_cliente, read_cliente, update_cliente, delete_cliente),
        "4": ("Bibliotecario", create_bibliotecario, read_bibliotecario, update_bibliotecario, delete_bibliotecario),
        "5": ("Emprestimo", create_emprestimo, read_emprestimo, update_emprestimo, delete_emprestimo),
        "6": ("Devolucao", create_devolucao, read_devolucao, update_devolucao, delete_devolucao),
        "7": ("Reserva", create_reserva, read_reserva, update_reserva, delete_reserva)
    }

    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("Escolha uma tabela:")
        for key, (nome, *_) in tabelas.items():
            print(f"{key}. {nome}")
        print("0. Sair")
        
        escolha_tabela = input("Digite o número da tabela: ")
        if escolha_tabela == "0":
            print("Saindo...")
            break
        if escolha_tabela not in tabelas:
            print("Opção inválida!")
            continue

        tabela_nome, create_func, read_func, update_func, delete_func = tabelas[escolha_tabela]
        
        print(f"\nTabela selecionada: {tabela_nome}")
        print("1. Criar")
        print("2. Ler")
        print("3. Atualizar")
        print("4. Deletar")
        print("5. Voltar")
        
        operacao = input("Escolha a operação: ")
        
        if operacao == "5":
            continue
        
        if operacao == "1":  # Criar
            if tabela_nome == "Titulo":
                isbn = input("ISBN: ")
                titulo_obra = input("Título da obra: ")
                data_publicacao = input("Data de publicação (YYYY-MM-DD): ")
                idioma = input("Idioma: ")
                numero_pagina = int(input("Número de páginas: "))
                new_id = create_func(isbn, titulo_obra, data_publicacao, idioma, numero_pagina)
                print(f"{tabela_nome} criado com ID: {new_id}")
            elif tabela_nome == "Usuario":
                cpf = input("CPF: ")
                primeiro_nome = input("Primeiro nome: ")
                sobrenome = input("Sobrenome: ")
                data_nascimento = input("Data de nascimento (YYYY-MM-DD): ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                new_id = create_func(cpf, primeiro_nome, sobrenome, data_nascimento, email, telefone)
                print(f"{tabela_nome} criado com ID: {new_id}")
            elif tabela_nome == "Cliente":
                id_usuario = int(input("ID do usuário: "))
                limite_emprestimo = int(input("Limite de empréstimo: "))
                new_id = create_func(id_usuario, limite_emprestimo)
                print(f"{tabela_nome} criado com ID: {new_id}")
            elif tabela_nome == "Bibliotecario":
                id_usuario = int(input("ID do usuário: "))
                new_id = create_func(id_usuario)
                print(f"{tabela_nome} criado com ID: {new_id}")
            elif tabela_nome == "Emprestimo":
                data_validade = input("Data de validade (YYYY-MM-DD): ")
                data_emprestimo = input("Data de empréstimo (YYYY-MM-DD): ")
                new_id = create_func(data_validade, data_emprestimo)
                print(f"{tabela_nome} criado com ID: {new_id}")
            elif tabela_nome == "Devolucao":
                status = input("Status: ")
                data_devolucao = input("Data de devolução (YYYY-MM-DD): ")
                new_id = create_func(status, data_devolucao)
                print(f"{tabela_nome} criado com ID: {new_id}")
            elif tabela_nome == "Reserva":
                data_reserva = input("Data de reserva (YYYY-MM-DD): ")
                data_limite_emprestimo = input("Data limite de empréstimo (YYYY-MM-DD): ")
                new_id = create_func(data_reserva, data_limite_emprestimo)
                print(f"{tabela_nome} criado com ID: {new_id}")

        elif operacao == "2":  # Ler
            id = int(input("Digite o ID: "))
            resultado = read_func(id)
            print(resultado if resultado else f"{tabela_nome} não encontrado")

        elif operacao == "3":  # Atualizar
            id = int(input("Digite o ID: "))
            if tabela_nome == "Titulo":
                isbn = input("Novo ISBN (deixe em branco para não alterar): ") or None
                titulo_obra = input("Novo título (deixe em branco para não alterar): ") or None
                data_publicacao = input("Nova data de publicação (YYYY-MM-DD, deixe em branco para não alterar): ") or None
                idioma = input("Novo idioma (deixe em branco para não alterar): ") or None
                numero_pagina = input("Novo número de páginas (deixe em branco para não alterar): ")
                numero_pagina = int(numero_pagina) if numero_pagina else None
                update_func(id, isbn, titulo_obra, data_publicacao, idioma, numero_pagina)
            elif tabela_nome == "Usuario":
                cpf = input("Novo CPF (deixe em branco para não alterar): ") or None
                primeiro_nome = input("Novo primeiro nome (deixe em branco para não alterar): ") or None
                sobrenome = input("Novo sobrenome (deixe em branco para não alterar): ") or None
                data_nascimento = input("Nova data de nascimento (YYYY-MM-DD, deixe em branco para não alterar): ") or None
                email = input("Novo email (deixe em branco para não alterar): ") or None
                telefone = input("Novo telefone (deixe em branco para não alterar): ") or None
                update_func(id, cpf, primeiro_nome, sobrenome, data_nascimento, email, telefone)
            elif tabela_nome == "Cliente":
                id_usuario = input("Novo ID do usuário (deixe em branco para não alterar): ")
                id_usuario = int(id_usuario) if id_usuario else None
                limite_emprestimo = input("Novo limite de empréstimo (deixe em branco para não alterar): ")
                limite_emprestimo = int(limite_emprestimo) if limite_emprestimo else None
                update_func(id, id_usuario, limite_emprestimo)
            elif tabela_nome == "Bibliotecario":
                id_usuario = input("Novo ID do usuário (deixe em branco para não alterar): ")
                id_usuario = int(id_usuario) if id_usuario else None
                update_func(id, id_usuario)
            elif tabela_nome == "Emprestimo":
                data_validade = input("Nova data de validade (YYYY-MM-DD, deixe em branco para não alterar): ") or None
                data_emprestimo = input("Nova data de empréstimo (YYYY-MM-DD, deixe em branco para não alterar): ") or None
                update_func(id, data_validade, data_emprestimo)
            elif tabela_nome == "Devolucao":
                status = input("Novo status (deixe em branco para não alterar): ") or None
                data_devolucao = input("Nova data de devolução (YYYY-MM-DD, deixe em branco para não alterar): ") or None
                update_func(id, status, data_devolucao)
            elif tabela_nome == "Reserva":
                data_reserva = input("Nova data de reserva (YYYY-MM-DD, deixe em branco para não alterar): ") or None
                data_limite_emprestimo = input("Nova data limite de empréstimo (YYYY-MM-DD, deixe em branco para não alterar): ") or None
                update_func(id, data_reserva, data_limite_emprestimo)
            print(f"{tabela_nome} atualizado com sucesso")

        elif operacao == "4":  # Deletar
            id = int(input("Digite o ID: "))
            delete_func(id)
            print(f"{tabela_nome} deletado com sucesso")

        else:
            print("Operação inválida!")

if __name__ == "__main__":
    menu()