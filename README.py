#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `thunderbird` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `thunderbird` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/use `thunderbird` on Linux Ubuntu._

# ## Descrição [2]
# 
# ### `thunderbird`
# 
# O Thunderbird é um cliente de e-mail de código aberto desenvolvido pela Mozilla Foundation. Ele oferece uma plataforma versátil para gerenciar e-mails, calendários, contatos e feeds de notícias em um único aplicativo. Com recursos avançados de organização, filtro de mensagens, busca eficiente e suporte para extensões, o Thunderbird é uma escolha popular entre os usuários que buscam um cliente de e-mail robusto e personalizável. Além disso, sua ênfase na segurança e na privacidade, incluindo a integração com criptografia S/MIME e OpenPGP, torna-o uma opção atraente para aqueles que valorizam a proteção de suas comunicações eletrônicas. O Thunderbird é compatível com várias plataformas, incluindo Windows, macOS e Linux, tornando-se uma ferramenta versátil para gerenciamento de e-mail e comunicação pessoal e profissional.
# 
# ### Add-in/Add-on: `Provider for Calendar`
# 
# "Provider for Calendar" (Provedor para Calendário) é uma extensão para o cliente de e-mail Mozilla Thunderbird que permite a sincronização e a integração de calendários em sua interface. Essa extensão é frequentemente usada em conjunto com o Thunderbird e o aplicativo de calendário Lightning para fornecer recursos de gerenciamento de calendário mais avançados.
# 
# Com o "Provider for Calendar", você pode conectar seu cliente de e-mail Thunderbird ao seu serviço de calendário online, como o Google Calendar, CalDAV ou outros, permitindo que você visualize e gerencie seus eventos e compromissos diretamente do Thunderbird. Ele torna mais fácil a organização de compromissos, reuniões e tarefas, bem como a sincronização desses eventos entre vários dispositivos.
# 
# Para usar o "Provider for Calendar", geralmente é necessário configurar a extensão com os detalhes de sua conta de calendário online e, em seguida, você poderá acessar e gerenciar seus calendários diretamente no Thunderbird. Essa extensão é especialmente útil para pessoas que desejam unificar suas comunicações por e-mail e seus compromissos de calendário em um único aplicativo de gerenciamento de informações pessoais.
# 
# ### Add-in/Add-on: `Send Later`
# 
# A funcionalidade "Send Later" (Enviar depois) no Thunderbird é uma característica que permite que você agende o envio de e-mails para uma data e hora futura específicas. Isso pode ser útil quando você deseja redigir um e-mail, mas não deseja que ele seja entregue imediatamente. Com o "Send Later", você pode definir a hora exata em que deseja que o e-mail seja enviado, o que pode ser útil para garantir que seus e-mails sejam entregues no momento mais adequado para o destinatário ou para evitar que sejam enviados fora do horário comercial, por exemplo.
# 
# Para usar a função "Send Later" no Thunderbird, você normalmente precisa de uma extensão ou complemento chamado "Send Later" ou "SendLater". Essa extensão adiciona essa funcionalidade ao cliente de e-mail, permitindo que você agende o envio de e-mails de acordo com suas preferências. Certifique-se de instalar a extensão apropriada no Thunderbird e siga as instruções fornecidas para configurar e usar o recurso "Send Later" de acordo com suas necessidades.

# ## Revisão(ões)/Versão(ões)

# |Revisão número|Data da revisão|Descrição da revisão|Autor da revisão|
# |:-:|:--------:|:------------------------------------------------------|:----------------------------|
# |0  |04/10/2023|<ul><li>Revisão inicial/criação do documento.</li></ul>|Eden Denis F. da S. L. Santos|

# ## Controle de configuração/instalação nos Sistemas Operacionais (SO) vs. Computador
# 
# |Numero|Computador          |Sistema Operacional (SO) |Tipo de sistema |Status da configuração/instalação |
# |:----:|:------------------:|:-----------------------:|:--------------:|:--------------------------------:|
# |1     |Dell Precision 7520 |Kali   Linux             |Debian          |OK                                |
# |2     |Dell Precision 7520 |Linux Ubuntu             |Ubuntu          |N/A                               |
# |3     |Dell Precision 7520 |Linux Xubuntu            |Ubuntu          |OK                                |
# |4     |Dell Precision 7520 |Windows                  |Windows         |Pendente                          |
# |5     |Asus                |Kali   Linux             |Debian          |N/A                               |
# |6     |Asus                |Linux Ubuntu             |Ubuntu          |Pendente                          |
# |7     |Asus                |Linux Xubuntu            |Ubuntu          |Pendente                          |
# |8     |Asus                |Windows                  |Ubuntu          |Pendente                          |
# 

# ## 1. Configurar/Instalar/usar o `thunderbird` no Linux Ubuntu [1]
# 
# Para configurar/instalar/usar o `thunderbird` no `Kali Linux`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
#     

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# Para instalar o `Thunderbird` no `Kali Linux`, você pode seguir os seguintes passos:
# 
# 1. **Instale o `Thunderbird`:** Após atualizar a lista de pacotes, instale o `Thunderbird` usando o `apt`. Execute o comando: `sudo apt install thunderbird -y`
# 
#     Este comando baixará e instalará o `Thunderbird` e todas as suas dependências.
# 
# 2. **Verifique a Instalação:** Após a conclusão da instalação, você pode verificar se o `Thunderbird` foi instalado corretamente. Para isso, você pode tentar iniciá-lo a partir do terminal com o comando: `thunderbird`
# 
#     Ou procure o `Thunderbird` no menu de aplicativos do seu ambiente de desktop.
# 
# Lembre-se de que o `Kali Linux` é uma distribuição focada em testes de penetração e segurança cibernética. Portanto, é importante ter cuidado ao instalar e usar softwares que não estão diretamente relacionados a essas tarefas, pois eles podem afetar a estabilidade e a segurança do sistema.
# 

# ### 1.1 Adicionar complementos (add-in/add-on)
# 
# ### 1.1.1 Add-in/Add-on: `Provider for Calendar` [3]
# 
# O complemento que você pode usar para gerenciar o calendário do Google no Thunderbird é o "Provider for Google Calendar". Este complemento permite que o Thunderbird leia e escreva eventos e tarefas para um calendário do Google, proporcionando um acesso bidirecional.
# 
# Para instalar o complemento, você precisa:
# 
# 1. Baixar o arquivo do complemento "Provider for Google Calendar" do site de complementos do Thunderbird.
# 
# 2. No Thunderbird, clicar no menu e selecionar "Complementos" para abrir o Gerenciador de Complementos.
# 
# 3. Clicar no ícone de engrenagem e escolher "Instalar Complemento a partir de arquivo...".
# 
# 4. Localizar o arquivo baixado em sua máquina e abrir para iniciar a instalação.
# 
# 5. Após a instalação, você precisa reiniciar o Thunderbird.
# 
# Para importar seu calendário para o Lightning (o calendário do Thunderbird), você deve:
# 
# 1. Ir ao menu "Arquivo" do Thunderbird e selecionar "Novo". No submenu, escolher "Calendário".
# 
# 2. No assistente que abre, selecionar "Na rede" e continuar.
# 
# 3. Escolher "Calendário do Google".
# 
# 4. Prosseguir inserindo o endereço de e-mail do Google e autorizando o complemento a gerenciar seus calendários.
# 
# 5. Escolher os calendários que deseja usar no Thunderbird e finalizar o processo.
# 
# Lembre-se de que algumas limitações podem existir ao usar o calendário do Google com o Thunderbird, por isso é recomendável ler a documentação fornecida pelo complemento para qualquer solução de problemas específicos.
# 
# 

# #### 1.1.2 Add-in/Add-on: `Send Later` [3]
# 
# Se você não encontrou a opção para agendar o envio de e-mail diretamente no Thunderbird, é possível que essa funcionalidade não esteja disponível na versão padrão do programa. Em algumas versões do Thunderbird, agendar o envio de um e-mail é um recurso que pode ser adicionado através de uma extensão, como a "Enviar mais tarde".
# 
# Se você estiver procurando agendar um e-mail e não vê a opção "Agendar envio" diretamente na interface, provavelmente precisará instalar essa extensão. Aqui estão os passos que você pode seguir para instalar uma extensão no Thunderbird:
# 
# 1. Abra o Thunderbird e clique no menu `Tools` ("Ferramentas") na barra de menu superior.
# 
# 2. Selecione `Add-ons and Themes` ("Complementos") para abrir o Gerenciador de Complementos.
# 
# 3. Na barra de pesquisa, digite `Send Later` ("Enviar mais tarde") para encontrar a extensão.
# 
# 4. Clique em "Adicionar a Thunderbird" para instalar a extensão.
# 
# 5. Após a instalação, você precisará reiniciar o Thunderbird.
# 
# 6.Depois de reiniciar, ao compor um novo e-mail, você deverá ver novas opções para agendar o envio.
# 
# Lembre-se de que o Thunderbird precisa estar aberto no horário programado para o envio, ou ele enviará o e-mail assim que o programa for aberto. Se você continuar tendo problemas ou se a extensão "Enviar mais tarde" não fornecer a funcionalidade que você precisa, pode ser útil consultar o suporte do Thunderbird ou pesquisar fóruns comunitários para obter ajuda adicional específica para a sua versão do Thunderbird.

# ## 1.2 Código completo configurar/instalar
# 
# Para instalar o `thunderbird` no `Kali Linux` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt update -y
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install thunderbird -y
#     thunderbird
#     ```

# ## Referências
# 
# [1] OPENAI. ***Instalar thunderbird no kali linux:*** https://chat.openai.com/c/ca32a491-3dc6-4a66-bdc3-0f56f6d16943 (texto adaptado). Acessado em: 04/11/2023 13:58.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). Acessado em: 04/11/2023 13:58.
# 
# [3] OPENAI. ***Agendar envio de e-mails:*** https://chat.openai.com/c/71faaa05-25e2-4816-a559-dfaee1f04f7c (texto adaptado). Acessado em: 19/12/2023 18:45.
