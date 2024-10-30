import socket
import threading

class Servidor:
    def __init__(self, host='127.0.0.1', porta=12345):
        self.porta = porta
        self.dados = {
            1: "Informação 1",
            2: "Informação 2",
            3: "Informação 3"
        }
        self.servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor_socket.bind((host, porta))
        self.servidor_socket.listen(5)
        print(f"Servidor ouvindo na porta {porta}...")

    def handle_client(self, cliente_socket):
        try:
            id_cliente = cliente_socket.recv(1024).decode()
            
            if id_cliente.lower() == 'sair':
                print("Cliente se desconectou.")
                return
            
            if not id_cliente.isdigit():
                resposta = "Erro: ID inválido. Por favor, envie um número inteiro."
                cliente_socket.send(resposta.encode())
                return
            
            id_cliente = int(id_cliente)
            print(f"Solicitação recebida: ID {id_cliente}")

            if id_cliente in self.dados:
                resposta = self.dados[id_cliente]
            else:
                resposta = "Erro: ID não encontrado."
            cliente_socket.send(resposta.encode())
        except Exception as e:
            print(f"Erro no processamento do cliente: {e}")
        finally:
            cliente_socket.close()

    def start(self):
        while True:
            cliente_socket, endereco = self.servidor_socket.accept()
            print(f"Conexão recebida de {endereco}")
            thread = threading.Thread(target=self.handle_client, args=(cliente_socket,))
            thread.start()

if __name__ == "__main__":
    servidor = Servidor()
    servidor.start()
