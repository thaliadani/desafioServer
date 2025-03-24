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

O Wireshark é um analisador de pacotes de rede (packet sniffer) que permite capturar, visualizar e inspecionar o tráfego que passa por uma rede em tempo real. Ele é amplamente utilizado por profissionais de segurança, administradores de rede e desenvolvedores para diagnosticar problemas, analisar protocolos e detectar possíveis ameaças.

Material de apoio: https://www.youtube.com/watch?v=TYk6ejP7dmI

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

## Questões a serem respondidas:
### O que acontece quando tentamos acessar https://localhost:8443 no navegador?Por que aparece um aviso de segurança?

### No Wireshark, use o filtro tls. Os dados das requisições HTTPS aparecem de forma legível? Explique o motivo.
Não aparece pelo fato de ser outro tipo de protocolo, o tls é um padrão de segurança da internet, já o HTTPS é uma forma de comunicação entre cliente e servidor.
### Quais pacotes aparecem na negociação do protocolo TLS? O que significa Client Hello e Server Hello?
Application Data, Continuation Data, Server Hello, Client Hello,Change Cipher Spec,Client Key Exchange,Encrypted Alert,etc. Para estabelecer conexão e criptografia entre os dois durante a comunicação do cliente e servidor durante o handshake TLS/SSL.
### Qual é a principal vantagem do HTTPS em relação ao HTTP?
O HTTPS é mais seguro do que HTTP pelo fato de usar criptografia para proeger os dadps.
### Por que não devemos inserir senhas ou informações sensíveis em sites sem HTTPS?
O HTTPS usa criptografia para proteger os dados do usuário e o HTTP não possui nenhuma proteção.
### O que aconteceria se um atacante capturasse pacotes HTTP em uma rede pública (Wi-Fi de um café, por exemplo)?
Ele conseguiria pegar todos os dados,ou seja teria seus arquivos.
### Como o Wireshark pode ser usado para diagnosticar problemas de rede além de capturar pacotes HTTP/HTTPS?
O Wireshark mostra de forma detelhada o processo dos pacotes em tempo real, armazena os dados para acessar offline, gera um relátorio detlhado do tráfego e filtra o log para facilitar a busca.
### Dê um exemplo de uma aplicação real onde a análise de tráfego de rede pode ser útil.
Para saber se um site tem algum tipo de malwares e outras ameaças, para verificar se algo está mal configurado na rede.
### Como funciona o processo de verificação de um certificado SSL em um site real?
A verificação faz com que o site seja autenticado e possibilita uma conexão segura usando criptografia.
### O HTTPS pode ser quebrado? Se sim, como e em quais casos?
Sim, depende da força da cifra e do tamanho da chave. Para ser quebrado pode se usar o TLS1.0 com uma chave RSA de 1024 e SHA-1.Pode ser usado para testar se o site realmente está bem protegido, em caso de investigações policiais.
