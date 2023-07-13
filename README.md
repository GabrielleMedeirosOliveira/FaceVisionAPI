# Face Vision API - Sistema de Reconhecimento Facial
![Python](https://img.shields.io/badge/Python-ffca1d?style=for-the-badge&logo=python&logoColor=347ab4) ![Docker](https://img.shields.io/badge/Docker-2496ed?style=for-the-badge&logo=Docker&logoColor=white) ![Fly.dev](https://img.shields.io/badge/fly.dev-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) ![Django](https://img.shields.io/badge/Django-092e20?style=for-the-badge&logo=django&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-black?style=for-the-badge&logo=opencv&logoColor=white) ![Redoc](https://img.shields.io/badge/redoc-47a427?style=for-the-badge&logo=swagger&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-ff6c37?style=for-the-badge&logo=Postman&logoColor=white)

Este é um sistema desenvolvido em Python que permite o reconhecimento facial, consiste em uma API com três endpoints para o correto funcionamento. 

## 📍 Funcionalidades:

- Endpoint 1: **/process_image/** - Este endpoint recebe um parâmetro de string que pode ser um índice de câmera local ou uma URL da imagem. Ele realiza o reconhecimento facial utilizando o framework OpenCV, dependendo da configuração selecionada. Após o reconhecimento facial, a imagem é convertida em formato base64 e salva localmente. Como uma opção adicional, é possível integrar um serviço de mensageria para enviar a imagem em base64 para uma fila.

- Endpoint 2: **/process_image/id** - Este endpoint permite a visualização da imagem resultante do reconhecimento facial. Ele retorna um stream que pode ser consumido por qualquer cliente. Este endpoint realiza as mesmas ações do primeiro endpoint, mas sem o reconhecimento facial.

- Endpoint 3: **/process_image/id/result** - Este endpoint também retorna um stream, mas inclui o reconhecimento facial. Ele executa as mesmas ações do segundo endpoint, mas adiciona a sobreposição das informações de reconhecimento facial no vídeo.


 ## 🛠️ Configuração e Uso
Para inciar este projeto, é necessário instalar as dependências, que serão utilizadas no projeto. Portanto utilize o comando abaixo para instalar e atualizar tais dependências:

```bash
### Atualizar o pip
    pip install --upgrade pip

### Instalar as dependências
    pip install -r requirements.txt
```
Este projeto já conta com o Docker configurado e pronto para uso. Basta buildar e subir os containers utilizando os seguintes comandos:

```bash
    docker-compose up --build
                ou
    docker compose up --build
```
Mas caso queira rodar localmente o projeto em sua máquina basta usar o comando abaixo:

```bash
    python manage.py runserver
            ou
    python3 manage.py runserver
```

**ATENÇÃO:** Os comandos podem variar com a versão do Python e do Docker compose instalada em sua máquina.

 **🧪 Sobre os testes**

Essa aplicação possui testes, que serão utilizados para validar, se todas as regras de negócio foram aplicadas de maneira correta.
Os testes estão localizados em `face_vision/tests.py`. Para rodá-los é necessário que no seu terminal utilize o seguinte comando:

```bash
    python manage.py tests.py
                ou
    python3 manage.py tests.py
```
**🟠 Postman**

Dentro da pasta `documentation` há um arquivo json chamado `FacialRecognitionAPI.postman_collection` esse aquivo é um conjunto de requisições HTTP para poder testar a nossa API.

**🟢 Redoc**

Caso queira mais informações da API, dentro da pasta `documentation/public` há um index.html com a nossa documentação!

## 📞 Contato
Para qualquer dúvida ou sugestão sobre este projeto, entre em contato 🥰

- Nome: Gabrielle Medeiros Oliveira
- E-mail: gabriellemedeiros51@gmail.com
- Linkedin: https://www.linkedin.com/in/gabriellemedeirosoliveira/
- Whatsapp : https://contate.me/gabriellemedeirosoliveira