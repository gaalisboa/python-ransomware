# Cybersecurity com Python
Dois mini projetos de código, um visando demonstrar como seria um ransomware e outro um keylogger em python.
## encryption (ransomware)
Contém 2 códigos, um para criptografar e outro para descriptografar os arquivos dentro da pasta "reallyimportantfiles", além de criar um arquivo com mensagem de "resgate" dos arquivos criptografados.
## keylogger
Contém 1 código que lê o que é digitado no teclado do usuário ao mesmo tempo que vai gravando em um arquivo .txt, e de tempos em tempos manda "versões" desse arquivo para o email desejado (atacante). É interessante notar que a extensão é ".pyw", sendo assim, não abre nenhuma janela ou terminal quando está sendo executado, assim deixando-o mais furtivo para o usuário.
## Como se defender
A maioria dos ataques podem ser bloqueados apenas mantendo o sistema, firewalls e anti vírus atualizados, evitando abrir ou baixar arquivos sem certeza de que são de fontes confiáveis e evitar sites suspeitos. Um dos casos específicos para devs, é fazer uso de ambientes controlados (máquinas virtuais) nos momentos de pesquisa e estudo, principalmente na área de ciber segurança, pois pode acabar comprometendo a network local ou ter efeitos colaterais indesejados pelo usuário no próprio computador e nos demais dispositivos conectados à mesma rede.

# Como rodar os códigos
Antes de tudo, verifique a instalação do python:
- `python -V`

Crie o ambiente virtual e instale as dependencias:
- `python -m venv venv`
- `pip install requirements.txt`

Crie um arquivo .env e insira os campos `email=seu_email` e `app_key=sua_key` para receber as keylogs no email (ainda adiciona as logs ao arquio .txt se o arquivo .env não for configurado).

Essa `app_key` é da respectiva conta associada em `email`. Para criar uma key, acesse https://myaccount.google.com/apppasswords com uma conta que tenha autenticação de 2 fatores ativa.

Agora é só rodar os códigos. Lembrando que, uma vez que os arquivos são criptografados, se criptografados de novo, a descriptografia retornará os arquivos para o último estado (ainda criptografados)
Caso queira que o keylogger pare de rodar no background, abra o gerenciador de tarefas e procure pelo processo do python respectivo do programa para finalizá-lo.
