import socket

class Cliente:
    def __init__(self, host='127.0.0.1', porta=12345):
        self.host = host
        self.porta = porta

    def start(self):
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.connect((self.host, self.porta))
                    id_cliente = input("Digite o ID para solicitar informações (ou 'sair' para encerrar): ")
                    if id_cliente.lower() == 'sair':
                        break
                    sock.send(id_cliente.encode())
                    resposta = sock.recv(1024).decode()
                    print(f"Resposta do servidor: {resposta}")
            except Exception as e:
                print(f"Erro ao se conectar ao servidor: {e}")
                break

if __name__ == "__main__":
    cliente = Cliente()
    cliente.start()
