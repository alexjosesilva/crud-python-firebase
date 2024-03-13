
import firebase_admin
from firebase_admin import credentials, firestore

# Inicialize o Firebase
cred = credentials.Certificate("config/crudpythonfirebase-firebase-adminsdk-1vmax-93c55b5361.json")
firebase_admin.initialize_app(cred)

# Obtenha uma referência ao banco de dados Firestore
db = firestore.client()

if (db != None):
    print("conecao OK")

# Função para criar um novo registro
def create_document(collection, data):
    db.collection(collection).add(data)

# Função para ler todos os registros de uma coleção
def read_documents(collection):
    docs = db.collection(collection).stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

# Função para atualizar um registro existente
def update_document(collection, doc_id, data):
    db.collection(collection).document(doc_id).update(data)

# Função para deletar um registro existente
def delete_document(collection, doc_id):
    db.collection(collection).document(doc_id).delete()

# funcao para retonrar o ultimo registo inserido
def get_last_document_id(collection):
    try:
        query = db.collection(collection).limit(1)
        docs = query.stream()
        for doc in docs:
            return doc.id  # Retorna o ID e os dados do documento
        return None  # Retorna None se a coleção estiver vazia
    except Exception as e:
        print("An error occurred:", e)
        return None
    
def get_document_count(collection):
    try:
        query = db.collection(collection)
        docs = query.get()
        return len(docs)
    except Exception as e:
        print("An error occurred:", e)
        return None

# Testando as funções ==============================================================

# Criar um novo registro
new_data = {"name": "John", "age": 30, "city": "New York"}
create_document("users", new_data)

# Ler todos os registros
print("Registros antes da atualização:")
read_documents("users")


# exibir a quantididade de registros
print("numero de registros: ")
print(get_document_count("users"))

# Atualizar um registro - substituir n4XY8eb9SFs0AQdjKkv6 pelo id do registro a ser deletado
document_id = get_last_document_id("users") 
print(document_id)
update_data = {"age": 31}
update_document("users", document_id, update_data)

# Ler todos os registros novamente
print("\nRegistros após a atualização:")
read_documents("users")

# Deletar um registro
delete_document("users", "document_id")
print("\nRegistro deletado. Registros restantes:")
read_documents("users")

