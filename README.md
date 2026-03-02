# Projeto-IOT1

🖱️ Simulação de Sensor de Movimento

Este projeto é uma simulação de um sensor de movimento utilizando Python e uma interface web.
Ele demonstra como eventos do sistema (movimento do mouse) podem ser capturados no backend e refletidos em tempo real em uma interface visual no navegador.

A aplicação funciona como um sensor virtual: quando o mouse se move dentro da área indicada na tela, o sistema detecta o movimento e ativa um efeito visual no círculo, simulando o disparo de um sensor.

⚙️ Como o projeto funciona

O sistema é dividido em duas partes principais:

🐍 Backend (detecção de movimento)

O script em Python monitora o movimento do mouse utilizando a biblioteca pynput.
Sempre que um movimento é detectado, ele atualiza o estado que será lido pela interface web.

Arquivo responsável:

Sensor.py – escuta eventos de movimento do mouse. 

Sensor

🌐 Frontend (interface visual)

A interface web exibe um círculo que representa a área de um sensor de movimento.

Quando o movimento é detectado, a página verifica o estado periodicamente e aplica uma animação no círculo, simulando o acionamento do sensor.

Arquivos da interface:

sensor.html – estrutura da página e script que consulta o estado do sensor. 

sensor

style.css – estilos visuais e animação de piscar do sensor. 

style

circulo.png – imagem utilizada como representação do sensor.

▶️ Ordem correta para executar o projeto

Para que a simulação funcione corretamente, siga a ordem abaixo:

1️⃣ Instalar dependências do Python

Instale a biblioteca necessária:

pip install pynput
2️⃣ Executar o script de detecção

Rode o script Python responsável por capturar o movimento do mouse:

python Sensor.py

Esse script ficará rodando em segundo plano monitorando os movimentos.

3️⃣ Abrir a interface web

Abra o arquivo:

sensor.html

em qualquer navegador.

A página irá consultar constantemente o estado do sensor e atualizar o círculo na tela.

🧠 Funcionamento da simulação

O usuário move o mouse.

O Python detecta o movimento.

O estado do sensor é atualizado.

A página web consulta esse estado.

O círculo na interface pisca, simulando a ativação de um sensor de movimento.
