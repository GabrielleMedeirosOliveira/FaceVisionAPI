# Face Vision API - Sistema de Reconhecimento Facial
![Python](https://img.shields.io/badge/Python-ffca1d?style=for-the-badge&logo=python&logoColor=347ab4) ![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white) ![Fly.dev](https://img.shields.io/badge/fly.dev-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) ![Django](https://img.shields.io/badge/Django-092e20?style=for-the-badge&logo=django&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-black?style=for-the-badge&logo=opencv&logoColor=white) ![Swagger](https://img.shields.io/badge/swagger-47a427?style=for-the-badge&logo=swagger&logoColor=white)

Este é um sistema desenvolvido em Python que permite o reconhecimento facial, consiste em uma API com três endpoints para o correto funcionamento. 

## Funcionalidades:

- Endpoint 1: **/reconhecimentos** - Este endpoint recebe um parâmetro de string que pode ser um índice de câmera local ou uma URL da imagem. Ele realiza o reconhecimento facial utilizando o framework OpenCV, dependendo da configuração selecionada. Após o reconhecimento facial, a imagem é convertida em formato base64 e salva localmente. Como uma opção adicional, é possível integrar um serviço de mensageria para enviar a imagem em base64 para uma fila.

- Endpoint 2: **/reconhecimentos/id** - Este endpoint permite a visualização da imagem resultante do reconhecimento facial. Ele retorna um stream que pode ser consumido por qualquer cliente. Este endpoint realiza as mesmas ações do primeiro endpoint, mas sem o reconhecimento facial.

- Endpoint 3: **/reconhecimentos/id/analisado** - Este endpoint também retorna um stream, mas inclui o reconhecimento facial. Ele executa as mesmas ações do segundo endpoint, mas adiciona a sobreposição das informações de reconhecimento facial no vídeo.

### Integração com Serviço de Mensageria (opcional)
É possível integrar um serviço de mensageria para enviar as informações de imagem em base64 para uma fila com a utilização local do RabbitMQ como serviço de mensageria. 

 ## 🛠️ Configuração e Uso
**Projeto ainda em produção!!**


## 📞 Contato
Para qualquer dúvida ou sugestão sobre este projeto, entre em contato 🥰

- Nome: Gabrielle Medeiros Oliveira
- E-mail: gabriellemedeiros51@gmail.com
- Linkedin: https://www.linkedin.com/in/gabriellemedeirosoliveira/
- Whatsapp : https://contate.me/gabriellemedeirosoliveira