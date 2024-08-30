import mysql.connector


def conectar_banco():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='#umdoistres',
        database='farmacia'
    )


def criar_medicamento(nome_medicamento, fabricante, quantidade, valor):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        comando = 'INSERT INTO medicamentos (nome_medicamento, fabricante, quantidade, valor) VALUES (%s, %s, %s, %s)'
        cursor.execute(comando, (nome_medicamento,
                       fabricante, quantidade, valor))
        conexao.commit()
        cursor.close()
        conexao.close()
        return "Medicamento cadastrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar medicamento: {e}"


def alterar_medicamento(id_medicamento, coluna, novo_valor):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        comando = f'UPDATE medicamentos SET {
            coluna} = %s WHERE idMedicamento = %s'
        cursor.execute(comando, (novo_valor, id_medicamento))
        linhas_afetadas = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if linhas_afetadas == 0:
            return "Nenhum medicamento foi alterado. Verifique o ID informado."
        else:
            return "Medicamento atualizado com sucesso!"
    except Exception as e:
        return f"Erro ao atualizar medicamento: {e}"


def buscar_por_nome(nome_medicamento):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        comando = 'SELECT * FROM medicamentos WHERE LOWER(nome_medicamento) LIKE %s'
        cursor.execute(comando, (f'{nome_medicamento.lower()}%',))
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultado
    except Exception as e:
        return f"Erro ao buscar medicamento: {e}"


def remover_medicamento(id_medicamento):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        comando = 'DELETE FROM medicamentos WHERE idMedicamento = %s'
        cursor.execute(comando, (id_medicamento,))
        conexao.commit()

        if cursor.rowcount == 0:
            mensagem = "Nenhum medicamento encontrado com o ID especificado."
        else:
            mensagem = "Medicamento removido com sucesso!"

        cursor.close()
        conexao.close()
        return mensagem
    except Exception as e:
        return f"Erro ao remover medicamento: {e}"


def exibir_todos():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        comando = 'SELECT * FROM medicamentos'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultado
    except Exception as e:
        return f"Erro ao exibir medicamentos: {e}"


def exibir_um(id_medicamento):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        comando = 'SELECT * FROM medicamentos WHERE idMedicamento = %s'
        cursor.execute(comando, (id_medicamento,))
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultado
    except Exception as e:
        return f"Erro ao exibir medicamento: {e}"
