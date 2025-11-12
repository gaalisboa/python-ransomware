# Cyber security com Python
Dois mini projetos de código, um visando demonstrar como seria um ransomware e outro um keylogger em python.
## encryption (ransomware)
contém 2 códigos, um para criptografar e outro para descriptografar os arquivos dentro da pasta "reallyimportantfiles", além de criar um arquivo com mensagem de "resgate" dos arquivos criptografados.
## keylogger
contém 1 código que lê o que é digitado no teclado do usuário ao mesmo tempo que vai gravando em um arquivo .txt, e de tempos em tempos manda "versões" desse arquivo para o email desejado (atacante). É interessante notar que a extensão é ".pyw", sendo assim, não abre nenhuma janela ou terminal quando está sendo executado, assim deixando-o mais furtivo para o usuário.
## Como se defender
A maioria dos ataques podem ser bloqueados apenas mantendo o sistema, firewalls e anti vírus atualizados, evitando abrir ou baixar arquivos sem certeza de que são de fontes confiáveis e evitar sites suspeitos. Um dos casos específicos para devs, é fazer uso de ambientes controlados (máquinas virtuais) nos momentos de pesquisa e estudo, principalmente na área de ciber segurança, pois pode acabar comprometendo a network local ou ter efeitos colaterais indesejados pelo usuário no próprio computador e nos demais dispositivos conectados à mesma rede.