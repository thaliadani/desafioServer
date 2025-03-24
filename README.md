# Desafio: Criando um Servidor Web HTTP e HTTPS em Python

Bem-vindo ao desafio da nossa disciplina de redes de computadores. 
Neste desafio, você aprenderá a criar um servidor web local utilizando Python.
O objetivo é compreender o funcionamento dos protocolos HTTP e HTTPS, explorando diferenças entre requisições não seguras e seguras.

🛠 Requisitos
Python instalado.
Wireshark (opcional, para captura de pacotes).
OpenSSL instalado (para gerar certificado SSL).

🚀 Desafio 1: Criar um Servidor HTTP

## Passo 1: Rodar o servidor HTTP
Abra o Prompt de Comando.
Navegue até uma pasta de sua escolha:
cd Users/projeto/nomeDaSuaPastaaaa

Execute o servidor HTTP:
python -m http.server 8080
O número 8080 é a porta do servidor. Você pode trocá-la por outra, como 5000 ou 8000.

Abra o navegador e acesse:
http://localhost:8080

## Passo 2: Analisar as Requisições HTTP

Abra as Ferramentas do Desenvolvedor no navegador:
No Chrome/Edge: F12 ou Ctrl + Shift + J.
Vá até a aba Network (Rede).
Atualize a página e observe as requisições HTTP.
Verifique o status code (200 OK, 404 Not Found, etc.).
Veja os métodos (GET, POST, etc.).

## Desafio Extra: Capturar tráfego HTTP com Wireshark (Opcional)

Abra o Wireshark e selecione sua interface de rede (Wi-Fi ou Ethernet).
Use o filtro http para visualizar apenas pacotes HTTP.
Acesse http://localhost:8080 novamente e veja os pacotes sendo capturados.

### Pergunta de reflexão: O que aconteceria se capturássemos pacotes HTTP de um site real?

## Desafio 2: Criar um Servidor HTTPS

Agora, vamos adicionar criptografia ao nosso servidor.

## Passo 1: Gerar um Certificado Autoassinado
No terminal, execute o comando abaixo para gerar um certificado SSL:

openssl req -x509 -newkey rsa:2048 -keyout chave.pem -out cert.pem -days 365 -nodes

Isso criará dois arquivos: chave.pem (chave privada) e cert.pem (certificado).

## Passo 2: Criar o Servidor HTTPS

Crie um arquivo chamado server_https.py e adicione o codigo deste repositório:

## Passo 3: Rodar o Servidor HTTPS

No terminal, execute:
python server_https.py
Acesse no navegador:
https://localhost:8443

O navegador pode mostrar um aviso de segurança porque o certificado é autoassinado. Clique em Avançado e prossiga.

Pergunta de reflexão: Qual a diferença ao capturar pacotes HTTPS no Wireshark em comparação com HTTP?

## Criamos um servidor HTTP simples.✅ Exploramos as requisições no navegador.✅ Configuramos um servidor HTTPS para criptografia de dados.
