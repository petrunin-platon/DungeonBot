# Hero Wars: Knowledge Engine Bot

Olá! Este é um programa que joga a Masmorra dos Titãs por você no jogo Hero Wars. Você o liga, vai cuidar da sua vida — e ele abre as portas, monta os times e coleta as recompensas.

Este manual foi escrito para que qualquer pessoa possa entender. Explicamos termos desconhecidos na hora e, ao final de cada seção, indicamos para onde ir a seguir.

## O que o bot sabe fazer

O bot não é um "clicador" irracional. Ele olha para a tela do jogo da mesma forma que você olharia e decide por conta própria o que fazer a seguir. Veja o que ele sabe fazer:

- :eye: **Vê a tela.** A cada fração de segundo, ele tira uma captura de tela da janela do jogo e reconhece botões, portas e inimigos nela.
- :door-open: **Escolhe a porta.** Ele vai para as salas na ordem que você definiu e evita aquelas que são perigosas no momento.
- :users: **Monta a equipe.** Para cada sala, ele tem um "pack" (é assim que chamamos uma equipe de cinco titãs). O próprio bot posiciona os titãs nos seus lugares.
- :heart-pulse: **Monitora a saúde.** Após cada batalha, ele lê o PV (pontos de vida) e a energia dos titãs e decide se o pack está pronto para a próxima batalha.
- :swords: **Chama você se a batalha for ruim.** A janela «Intervenção necessária» aparece: você pode tentar a batalha novamente com outro pack, aceitá-la ou jogar manualmente. Se você se afastar do computador, o bot pode decidir sozinho.
- :chart-no-axes-column: **Aprende com suas batalhas.** Lembra qual pack venceu quais inimigos e, da próxima vez, já o escala de primeira.
- :send: **Escreve no Telegram.** Se você quiser, ele enviará o resumo da sessão e um alerta quando algo der errado.

> [!note] Exemplo. Araji entrou na batalha com 36% de vida e, após o combate, caiu para 8%. O bot vê isso, entende que a batalha foi ruim e ou pergunta a você, ou rebobina a batalha por conta própria e tenta novamente com outro pack.

### O que o bot não faz

- Ele joga **apenas a Masmorra dos Titãs**. Outros modos de jogo não são conhecidos por ele.
- Ele **não joga "na nuvem"**. O jogo roda no seu telefone Android, e o PC com Windows olha para a tela do telefone e clica nela através do cabo USB. É necessário ter tanto o telefone quanto o computador.
- Ele não é mágico: se a conexão com o jogo for perdida, ele espera honestamente até que ela volte e informa você sobre isso.

### Isso é seguro para a conta?

O bot tenta se comportar como uma pessoa real, e não como um robô:

- cada clique atinge um **ponto aleatório** do botão, e não sempre o mesmo lugar;
- antes de clicar, ele aguarda uma **pausa de reação** — de 0,3 a 0,8 segundo após o botão aparecer;
- ele clica **no máximo duas vezes por segundo**.

> [!warning] Nenhum programa pode dar garantia total: as regras do jogo são definidas por sua distribuidora. O bot não faz nada "super-humano de tão rápido", mas a decisão de usá-lo é sua.

### O que vem a seguir no manual

- **O que você precisa e instalação** — o que baixar e configurar uma única vez.
- **Conectando o telefone** — o primeiro início do farm.
- **Principal e minibarra** — como ler a janela e o pequeno painel sob o jogo.
- **Pausa e interrupção** — botões e teclas de atalho.
- **Mestre de regras** — como ensinar ao bot seus packs e a ordem das portas.
- **Quando a batalha foi ruim** — janelas de intervenção e como o bot decide sozinho.
- **Telegram, estatísticas, se algo der errado** — todo o resto.

> [!done] Agora você sabe o que o bot faz. A seguir — o que você precisa instalar, uma única vez. [Próxima seção →](#2)

## O que você vai precisar e instalação

Isso é feito **uma única vez**. Depois você simplesmente abre o programa com um duplo clique. Dedique cerca de quinze minutos a isso — o resto será fácil.

### O que é necessário ter

- :monitor: **Computador com Windows.** É nele que o programa e o bot funcionam.
- :smartphone: **Celular Android com Hero Wars.** O jogo roda no celular, e o computador observa a tela dele e faz os cliques.
- :terminal: **Cabo USB.** De preferência o cabo que carrega o celular e transfere arquivos: existem cabos que são "apenas para carregamento", por eles o computador não verá o celular.
- :folder: **Arquivo compactado do programa** (arquivo `.zip`, que contém o `HeroWarsBot.exe`).

> [!note] O jogo continua no celular. O bot não instala nada de extra nele e não mexe nos arquivos do jogo: ele apenas olha para a tela e clica nela, exatamente como você faria com o dedo.

### Passo A. Descompacte o programa

1. **Descompacte o arquivo** — clique nele com o botão direito e selecione "Extrair tudo...". Escolha uma pasta simples sem letras russas, por exemplo `C:\HeroWarsBot`.
2. **Verifique se os arquivos estão no lugar** — na pasta deve haver o `HeroWarsBot.exe` ao lado de outros arquivos e pastas.

> [!warning] Primeiro descompacte o arquivo e só depois execute o programa. Se você abrir o `.exe` diretamente de dentro do arquivo, os outros arquivos do programa ficarão inacessíveis e ele não funcionará como deveria.

> [!tip] Esta pasta é a "casa" do bot. Junto do `HeroWarsBot.exe`, ele criará seus próprios arquivos: configurações, estatísticas, histórico de batalhas. Portanto, não mova o `.exe` separado dos outros arquivos e, se for mudar de lugar, mova a pasta inteira.

### Passo B. Instale o scrcpy

O scrcpy é um pequeno programa que mostra a tela do celular em uma janela no computador. O bot "olha" exatamente para essa janela. Junto com ele é instalado o **adb** — um assistente através do qual o bot clica na tela do celular.

1. **Baixe o scrcpy** — na [página do projeto](https://github.com/Genymobile/scrcpy/releases) escolha a versão mais recente para Windows (arquivo `.zip` com "win64" no nome).
2. **Descompacte o arquivo** — o ideal é em uma pasta simples sem espaços nem letras russas, por exemplo `C:\scrcpy`. Dentro dela devem estar os arquivos `scrcpy.exe` e `adb.exe`.
3. **Adicione a pasta ao PATH** — assim o Windows saberá onde procurar esses programas. Veja abaixo como fazer isso.

**Como adicionar a pasta ao PATH:**

1. **Abra as configurações** — pressione a tecla Windows, digite "variáveis de ambiente" e selecione "Editar as variáveis de ambiente do sistema".
2. **Encontre "Path"** — na janela que se abrir, clique em "Variáveis de Ambiente", na lista superior selecione a linha `Path` e clique em «Editar».
3. **Adicione a pasta** — clique em "Novo", digite `C:\scrcpy` (a sua pasta, se for diferente) e feche todas as janelas clicando em "OK".

> [!note] O PATH é uma lista de pastas onde o Windows procura por programas quando você os chama pelo nome. Adicionou a pasta à lista — e o `scrcpy` com o `adb` serão encontrados de qualquer lugar.

### Passo C. Verifique se o scrcpy foi instalado

1. **Abra o "Prompt de Comando"** — tecla Windows, digite `cmd`, pressione Enter. Se a janela já estava aberta antes da instalação, feche-a e abra novamente: a janela antiga não sabe sobre as novas pastas.
2. **Verifique o scrcpy** — digite `scrcpy --version` e pressione Enter. A versão do programa deverá aparecer.

Se em vez da versão o Windows exibir "não é reconhecido como um comando interno ou externo", significa que a pasta não entrou no PATH. Volte ao passo B e verifique se no PATH está inserida a pasta onde se encontra o `scrcpy.exe`.

### Passo D. Configure o celular

O celular deve permitir que o computador o controle. Isso se chama "Depuração USB" (um modo criado para desenvolvedores de aplicativos). O bot o utiliza para clicar na tela.

1. **Ative o modo de desenvolvedor** — vá em "Configurações" → "Sobre o telefone" e toque **7 vezes seguidas** em "Número da versão". O celular avisará que você agora é um desenvolvedor.
2. **Encontre "Opções do desenvolvedor"** — este item aparecerá nas configurações (às vezes dentro de «Sistema» ou "Configurações adicionais").
3. **Ative duas configurações** — "Depuração USB" **e** "Depuração USB (Configurações de segurança)".
4. **Conecte o cabo** — quando o celular perguntar "Permitir a depuração USB a partir deste computador?", marque "Sempre permitir" e toque em "OK".

![Seção "Opções do desenvolvedor" com duas configurações de depuração ativadas](images/usb_debug.png)

> [!warning] Ative **ambas** as configurações. Se apenas a primeira estiver ativada, a imagem do celular chegará ao computador, mas os cliques não chegarão ao jogo: o bot vai "clicar", mas o jogo não perceberá nada.

Agora vamos verificar a conexão. Conecte o celular pelo cabo, abra o "Prompt de Comando" e digite `adb devices`. Na lista deve haver uma linha com a palavra `device` ao lado do número do celular.

- :check: `device` — tudo certo, o celular está pronto.
- :triangle-alert: `unauthorized` — o celular está aguardando sua permissão. Olhe para a tela dele e toque em "Permitir".
- :triangle-alert: lista vazia — o computador não vê o celular. Tente outro cabo ou outra porta USB.

### Passo E. Primeira execução do programa

1. **Abra a pasta do programa** — aquela onde você descompactou o arquivo.
2. **Dê um duplo clique em `HeroWarsBot.exe`** — a janela do programa se abrirá.
3. **Olhe ao redor** — à esquerda há uma barra com as seções, no meio a página principal. Enquanto o celular não estiver conectado, o cabeçalho mostrará «Aguardando o telefone» — isso é normal.

> [!tip] Inicie o programa sempre a partir da pasta dele (ou crie um atalho para `HeroWarsBot.exe`: botão direito → "Enviar para" → "Área de trabalho"). Dessa forma, ele encontrará suas configurações e arquivos.

> [!done] Tudo pronto: o programa foi descompactado, o scrcpy e o celular estão configurados. Agora vamos conectar o celular e iniciar o primeiro farm. [Próxima seção →](#3)

## Conectando o telefone e primeiro farm

Agora vamos conectar o telefone e iniciar o bot pela primeira vez — tudo levará cerca de cinco minutos. Primeiro lembre-se: no monitor haverá **duas janelas**.

- :monitor: **Janela do programa** — aquela onde você está lendo este manual. Nela ficam botões, configurações e o registro (é assim que chamamos o feed de mensagens onde o bot grava o que está fazendo).
- :smartphone: **Janela do jogo** — o "espelho" da tela do telefone no monitor, chamada `HeroWarsBot_Arena`. O bot "olha" exatamente para ela.

### O que está na página principal na primeira execução

Enquanto você ainda não salvou as configurações nenhuma vez, na página principal (o primeiro botão da barra esquerda) fica o cartão «Por onde começar» com o texto «3 passos · cerca de 5 minutos».

![Primeira execução: cartão «Por onde começar», texto vermelho «Aguardando o telefone…» e botão azul «Conectar telefone»](images/connect_phone.png)

- :smartphone: **«Conecte o telefone»** — marcado com a palavra «agora». Quando o telefone se conectar, o número do passo será substituído por um visto verde. É disso que cuidaremos agora.
- :sliders-vertical: **«Confira os packs por sala»** — o link «Abrir →» leva ao «Mestre de Regras» (segundo botão na barra esquerda, ícone com controles deslizantes). Lá você diz ao bot quais titãs usar ao entrar em cada sala.
- :send: **«Configure o Telegram para SOS»** — opcional. O bot escreverá para você no Telegram se precisar de ajuda.

> [!warning] Os packs são o mais importante antes do primeiro farm. O bot escala em cada uma das quatro salas (água, terra, fogo e mista) o pack gravado no «Mestre de Regras», pois ele não pode adivinhar seus titãs. Como configurar isso está na seção sobre o «Mestre de Regras» mais adiante no manual. O cartão «Por onde começar» desaparecerá quando você salvar as configurações no «Mestre de Regras» pela primeira vez.

### Passo A. Conecte o telefone

1. **Prepare o telefone** — conecte-o com o cabo e desbloqueie a tela. Ambas as configurações de depuração USB devem estar ativadas, conforme a [seção 2](#2).
2. **Clique em «Conectar telefone»** — é o botão azul grande no canto superior direito. Enquanto o programa procura o telefone, nele aparece a mensagem «Conectando…». Pode demorar até 20 segundos.
3. **Encontre a janela do jogo** — uma nova janela `HeroWarsBot_Arena` aparecerá com a tela do telefone. Não está vendo? Ela pode ter ficado escondida atrás da janela do programa: procure-a na barra de tarefas na parte inferior da tela.
4. **Verifique o selo no cabeçalho** — o selo vermelho «Aguardando o telefone…» deve ficar verde: «conectado». E o botão azul se transformará no botão verde «Começar o farm». (O cabeçalho é a barra superior da janela, o selo é o retângulo com o texto.)

![Telefone conectado: texto verde «conectado», botão «Começar o farm» e a janela do jogo ao lado](images/phone_connected.png)

A janela não apareceu e o registro diz "A janela do scrcpy não apareceu ou o utilitário não foi encontrado!"? Verifique em ordem:

- :smartphone: A tela do telefone está desbloqueada e o cabo está bem firme. Tente outra porta USB.
- :terminal: No prompt de comando, `adb devices` exibe a palavra `device` ao lado do seu telefone. Se exibir `unauthorized`, autorize a depuração na tela do telefone.
- :terminal: No prompt de comando, `scrcpy --version` responde com a versão. Não respondeu? A pasta do scrcpy não entrou no PATH — volte à [seção 2](#2). Após corrigir o PATH, o programa deve ser fechado e aberto novamente.

### Passo B. Vá para o corredor da Masmorra

A Masmorra dos Titãs é o modo de jogo no qual você desce pelos andares e combate inimigos em cada sala. O **corredor** é a tela entre as batalhas: nela é possível ver uma porta com uma bandeira e mais nada aberto. É do corredor que o bot começa.

1. **Abra o jogo** — no telefone, inicie o Hero Wars e entre na Masmorra dos Titãs.
2. **Fique no corredor** — se houver uma batalha em andamento, termine-a manualmente e feche a janela de resultado. É necessária uma tela tranquila com a porta e a bandeira.

![Corredor da Masmorra dos Titãs: uma bandeira é visível junto à porta](images/dungeon_corridor.png)

> [!warning] Não inicie o farm no meio de uma batalha. Primeiro o bot inspeciona a tela e coloca a casa em ordem: se vir uma batalha — recuará dela; se vir a janela de resultado com o botão "Novamente" — cancelará essa batalha e jogará a sala de novo; se vir a seleção de equipe — fará a batalha e a cancelará imediatamente. Ele continuará funcionando depois, mas sua vitória terá sido em vão.

### Passo C. Inicie o farm

> [!warning] **O idioma do programa deve coincidir com o idioma do jogo.** Os botões com texto ("Atacar", "OK", "Novamente") e a bandeira na porta são reconhecidos pelo bot através de imagens no idioma selecionado no programa. Esse é o botão com duas letras ("RU" / "PT") na parte inferior da barra esquerda. Se o jogo estiver em um idioma, no programa deve estar o mesmo idioma. Se os idiomas forem diferentes, o bot simplesmente não encontrará os botões.

1. **Clique em «Começar o farm»** — botão verde no lugar de «Conectar telefone». O programa ajustará automaticamente a janela do jogo para o tamanho correto e a colocará no canto superior esquerdo da tela.
2. **Não se assuste se a janela do programa desaparecer** — ela foi minimizada para a barra de tarefas, e um painel estreito apareceu sob o jogo — a **minibarra**. Nela você pode ver o que o bot está fazendo. Para restaurar a janela: ícone «Abrir a janela do programa» na minibarra (passe o mouse para ver a dica) ou o botão na barra de tarefas.
3. **Observe o jogo** — após alguns segundos, o bot clicará na porta e a primeira sala começará. Cada sala leva cerca de meio minuto a um minuto.
4. **Lembre-se de como parar o bot** — a tecla F10 o para imediatamente, F9 o coloca em pausa (o bot terminará a sala atual e aguardará). As teclas funcionam quando a janela do jogo ou a janela do programa estiver ativa.

Ao abrir a janela do programa, dê uma olhada no registro. Antes de cada linha há um horário — nós o omitimos aqui. Veja o que deve aparecer:

- `[УМНЫЙ СТАРТ] Сканирую экран для восстановления контекста...` — o bot está analisando a tela.
- `[УМНЫЙ СТАРТ] Контекст не требует экстренных действий. Начинаю с HALLWAY.` — tudo certo, ele começa pelo corredor ("HALLWAY" significa corredor).
- `[СТАТИСТИКА] Комнат: 1` — a primeira sala foi concluída. Tudo funcionando!
- :triangle-alert: `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — o bot aguarda até que a janela do jogo volte a ficar em primeiro plano. Clique nela com o mouse e o trabalho continuará.

Passou um minuto e o bot não clica em nada? Verifique:

- :gamepad-2: No jogo está exibido o corredor da Masmorra dos Titãs no momento, e não o menu, a loja ou uma batalha.
- :globe: O idioma do programa coincide com o idioma do jogo (aviso acima).
- :maximize-2: A janela do jogo está inteiramente na tela: não está esticada, nem maximizada, nem fora da borda. Caso contrário, pare o bot (F10), clique em «Redefinir o tamanho da janela do jogo» e comece novamente.
- :terminal: No registro não há linhas com "[ОШИБКА]". Se houver — iremos analisá-las na seção "Se algo der errado".

### Enquanto o bot estiver trabalhando

- :monitor: A janela do jogo deve ficar visível: não a cubra com outras janelas e não a minimize. Se clicar em outra janela, o bot pausará e aguardará.
- :smartphone: Não feche a janela do jogo nem puxe o cabo. Se a janela desaparecer, o programa parará o bot sozinho ("A janela do scrcpy foi fechada — parando o bot").
- :maximize-2: Não estique nem meça a janela do jogo: o bot mede seu tamanho ao iniciar e usa essa medida dali em diante.
- :gamepad-2: Não clique na tela do telefone você mesmo: o bot clica via ADB e vocês vão interferir um no outro. Se quiser jogar manualmente — coloque o bot em pausa (F9) e espere até que ele fique no corredor.
- :triangle-alert: Não bloqueie o computador (Win+L): em um PC bloqueado, o bot não vê a tela e espera até que você volte.
- :moon: Para farm noturno, desative a suspensão do computador: nas «Configurações» do Windows, abra «Sistema» → «Energia» e para tela e suspensão escolha «Nunca». Um monitor suspenso ou desligado equivale a um computador bloqueado: o bot parará e ficará aguardando. Os nomes das opções dependem da versão do Windows.

### Botões no cabeçalho

No canto superior direito, ao lado do selo, existem três ícones. Passe o mouse sobre qualquer um para ver a legenda.

![Cabeçalho da janela: selo do telefone, três botões e botões da janela](images/header_buttons.png)

- :moon: **«Desligar a tela do telefone»** — apaga a tela do telefone, mas o jogo continua rodando e o bot vê tudo. Prático à noite: reduz o desgaste da tela e o consumo de bateria. O programa traz a janela do jogo para a frente e envia Alt+O (é assim que o scrcpy apaga a tela). Para religar a tela — use o botão de liga/desliga do telefone. Há um botão idêntico na minibarra.
- :refresh-cw: **«Reiniciar o scrcpy»** — fecha a janela do jogo e a abre novamente. Útil caso a imagem do telefone tenha congelado. Funciona apenas com a janela iniciada pelo próprio programa. Não clique nele enquanto o bot estiver trabalhando: a janela perdida será considerada pelo programa como uma desconexão e ele parará o bot.
- :maximize-2: **«Redefinir o tamanho da janela do jogo»** — restaura a janela `HeroWarsBot_Arena` para o tamanho de 1606 × 748 e a posiciona no canto superior esquerdo. Este é o tamanho padrão: a busca por botões foi configurada para ele. Se tiver esticado ou maximizado a janela — clique neste botão antes de «Começar o farm» (embora «Começar o farm» faça isso automaticamente). A janela é larga: em um monitor Full HD (1920 × 1080) ela cabe inteira, e o bot vê apenas o que está na tela.

### Janela do programa sem a borda do Windows

A janela do programa não possui a borda padrão do Windows, por isso tem seus próprios botões no canto superior direito atrás de uma linha fina:

- :minus: **«Minimizar»** — esconde a janela na barra de tarefas.
- :square: **«Maximizar»** — expande a janela para a tela inteira; depois disso o botão passa a se chamar «Restaurar tamanho». Dar um duplo clique no cabeçalho faz o mesmo.
- :x: **«Fechar»** — fecha o programa e, junto com ele, a janela do jogo se ela tiver sido aberta por ele. Se o bot estiver trabalhando, primeiro perguntará «Parar o bot?»; o botão «Parar e fechar» o parará imediatamente, e o resumo da sessão não será enviado ao Telegram.
- :grip-vertical: **Mover a janela** — arraste pelo cabeçalho: pela área vazia no topo ou pelo título.
- **Redimensionar** — pelo canto inferior direito (três linhas diagonais). A janela não ficará menor do que o limite mínimo.

> [!note] Não confunda «Minimizar» e «Minimizar para a minibarra». «Minimizar» apenas esconde a janela na barra de tarefas. «Minimizar para a minibarra» é um botão na página principal enquanto o bot trabalha: ele também mostra a minibarra sob o jogo.

> [!done] O telefone está conectado, o bot concluiu a primeira sala — a base está pronta. A seguir, vamos entender o que a página principal mostra e como ler o registro. [Próxima seção →](#4)

## Página principal e registro

A página principal é o primeiro botão na barra esquerda, e é ela que você verá com mais frequência. Ela parece com o painel de um carro: na parte superior — números ("para onde vamos" e "como vamos"), na parte inferior — o registro, onde o próprio bot escreve o que faz. Vamos analisar o que fica onde e como não se perder nas linhas do registro.

### Cartão superior: ele muda de aparência sozinho

Na parte superior da página principal há um cartão grande, mas ele exibe coisas diferentes — dependendo do estado atual do bot:

- :sliders-vertical: **«Configuração de início»** — o bot está parado, mas as configurações já foram salvas. É "com o que o bot vai para a batalha": meta, modo e limites.
- :activity: **«Sessão atual»** — o bot está trabalhando. Números ao vivo: quanto foi coletado, quanto foi concluído, quanto tempo se passou.
- :file-text: **«Resumo da sessão»** — o bot parou. O cartão mostra o resultado e o motivo pelo qual ele parou.
- :list: **«Por onde começar»** — apenas enquanto você ainda não salvou as configurações nenhuma vez (descrito na [seção 3](#3)).

Uma sessão é uma execução do bot: desde o «Começar o farm» até a parada.

### Configuração de início

Quatro selos, e cada um responde a uma pergunta. Os números vêm das suas configurações; portanto, se algo não lhe agradar, clique em «Alterar no Mestre de regras →» no canto superior direito do cartão: o «Mestre de Regras» se abrirá.

![Página principal antes da execução: cartão «Configuração de início» e registro vazio](images/main_config.png)

- :target: **«Meta da sessão»** — quando o bot deve parar. A meta é **uma só**: titanita, salas, andares ou tempo. Se várias forem definidas nas configurações, é considerada a primeira na ordem "titanita → salas → andares → tempo". Se nada foi alterado — a meta é 120 de titanita, o que equivale a 10–20 salas. «Sem limite» significa que todas as metas estão em zero e o bot continuará até que você o pare.
- :shield-check: **«Modo»** — selo «O bot decide sozinho» com a marcação «LIG» ou «DESL». Ativado: em caso de batalha ruim, o próprio bot tentará novamente com outro pack. Desativado: ele chamará você. Detalhes — nas seções sobre o «Mestre de Regras».
- :heart-pulse: **«Limite de pânico de PV»** — por exemplo, 40%. Se após a batalha restou a algum titã menos vida que isso, a batalha é considerada ruim. Um pack é um time de cinco titãs; PV representa os pontos de vida (saúde).
- :calendar: **«Reinício do dia»** — por exemplo, 05:00. A partir deste horário começa um novo dia no jogo: o bot calcula as estatísticas do dia e esquece quanta vida os titãs tinham ontem.

> [!note] O bot lê as configurações **uma única vez, quando você clica em «Começar o farm»**. Se alterar algo durante a execução — o bot só saberá disso na próxima inicialização. Portanto, enquanto o bot estiver trabalhando, o cartão exibirá exatamente as configurações com as quais ele iniciou.

### Sessão atual

Quando o bot é iniciado, o cartão se transforma em «Sessão atual». No canto superior direito brilha o estado:

- :activity: **«Farm em andamento»** — tudo certo, o bot está trabalhando.
- :pause: **«Pausa»** — você clicou em «Pausa» (ou o próprio bot entrou em pausa suave). O botão passa a ser «Continuar».
- :triangle-alert: **«Aguardando sua decisão»** — a janela «Intervenção necessária» está na tela, o bot aguarda sua resposta.
- :refresh-cw: **«Iniciando o bot»** — primeiros segundos após «Começar o farm».

![Farm em andamento: selos da sessão com barras de progresso em direção à meta](images/main_session.png)

São quatro selos:

1. **«Titanita na sessão»** — quanta titanita o bot coletou. Isso é uma **contagem, não uma leitura da tela**: 6 por sala e 12 se no jogo o ícone "x2" estiver aceso. Se a meta for titanita, "coletado / necessário", a porcentagem e a barra aparecerão ao lado.
2. **«Andares concluídos»** — o andar é contabilizado quando o bot recolhe a recompensa no ponto de salvamento (assim é chamado o local no final do andar onde se clica em "Ativar" e "Resgatar"). Ao lado fica registrado em qual porta ele entrou por último: água, terra, fogo ou mista.
3. **«Batalhas na sessão»** — por exemplo, «12 vitórias de 14». Vitória é uma sala concluída com sucesso. Rebobinagem (otkat) é uma batalha que o bot jogou de novo: ela também conta como batalha, portanto o "total" pode ser maior que as "vitórias".
4. **«Tempo de sessão»** — horas:minutos:segundos e em texto pequeno «sala em média 28 s». A média é calculada pelas salas, sem contar a parada no ponto de salvamento.

> [!tip] Se a meta for salas ou tempo, a porcentagem fica à direita no formato "35% de 100" ou "35% de 120 min" — o valor da meta não cabe no próprio número. A barra sob o selo permanece a mesma.

> [!note] Quando a meta é atingida, o bot não abandona o andar pelo meio. Ele escreverá no registro `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, concluirá as salas restantes e parará antes do ponto de salvamento sem clicar em "Ativar": ele recolherá a recompensa do andar em primeiro lugar na próxima execução. Exceção — meta por andares: nesse caso o bot para imediatamente após a recompensa.

### Resumo da sessão

O bot parou — o cartão mostra o resumo, e a janela se restaura automaticamente da minibarra. No topo fica registrado o motivo da parada: o botão «PARAR», a janela do scrcpy fechada, o encerramento normal do trabalho ou o que o próprio bot escreveu (por exemplo, que a meta foi atingida).

![Resumo da sessão: motivo da parada, números e o botão «Detalhes»](images/main_summary.png)

Os mesmos quatro selos da sessão aparecem, mas agora são os números finais; em «Batalhas» é adicionado "janelas SOS: N" (quantas vezes o bot chamou você). O botão **«Detalhes»** abre uma janela com todo o relatório do bot: tempos médios por etapa, salas mais demoradas, quantas rebobinagens ocorreram e quantas delas o bot fez **sem você**. O ícone ✕ à direita oculta o resumo, e a «Configuração de início» volta a ser exibida. Se você clicar em «Começar o farm», o resumo desaparecerá sozinho.

> [!note] Se o Telegram estiver configurado, o resumo chegará lá automaticamente em qualquer parada normal. O botão «PARAR» (F10) encerra o bot instantaneamente, por isso o resumo não é enviado ao Telegram nesse caso.

### Registro: o que há nele e como ler

A parte inferior da página principal é o **«Registro de trabalho»**. O bot grava nela cada passo seu, e o programa exibe isso na janela. Não se assuste com a quantidade de linhas: não é preciso ler tudo, o registro é necessário quando algo dá errado ou quando se está curioso.

Cada linha é estruturada da mesma forma:

`10:26:17.486 [НАВИГАЦИЯ] Двери (слева направо): EARTH (0.98), FIRE (0.97)`

1. **Horário** — em cinza. Horas:minutos:segundos e milésimos de segundo.
2. **Rótulo em colchetes** — "quem fala" e sobre qual assunto. Ele é colorido: a cor indica a qual seção do registro a linha pertence.
3. **Texto** — o que exatamente aconteceu. Uma linha longa é quebrada e a continuação fica abaixo do texto, não abaixo do horário.

Uma linha sem rótulo (por exemplo, ` ---> HYPERION: ХП 100%, Энергия 79%`) — é a continuação da linha acima dela e pertence à mesma seção.

### "Pílulas" de filtro

Acima do registro há cinco botões no estilo "pílula". Clique em um — e no registro permanecerão apenas as linhas dessa seção. A seleção é memorizada: abra o programa amanhã e a mesma pílula estará selecionada.

![Registro com as pílulas «Tudo», «Batalhas», «Regras», «Sistema» e «Erros»](images/journal_pills.png)

- **«Tudo»** — tudo em sequência.
- **«Batalhas»** (rótulos verdes) — o andamento do percurso: salas, tempo, saúde dos titãs, rebobinagens. Rótulos `[КОМБАТ]`, `[СТАТИСТИКА]`, `[ВРЕМЯ]`, `[СОСТОЯНИЕ]`, `[АНАЛИЗАТОР]`, `[ОТКАТ]`, `[ЛИМИТ]`, `[ИТОГ]`.
- **«Regras»** (rótulos amarelos) — decisões do bot: qual pack escalar, por que rebobinou a batalha, o que memorizou. Rótulos `[ТАКТИКА]`, `[КОМАНДА]`, `[ПРАВИЛА]`, `[ОБУЧЕНИЕ]`, `[SOS_CLOSE]`.
- **«Sistema»** (rótulos azuis) — todo o resto: corredor e portas (`[НАВИГАЦИЯ]`), inicialização (`[УМНЫЙ СТАРТ]`), conexão. As linhas do próprio programa com o rótulo `[GUI]` são cinzas, mas também ficam aqui.
- **«Erros»** (rótulos vermelhos) — tudo o que exige atenção: `[ОШИБКА]`, `[ВНИМАНИЕ]`, `[СТОРОЖ]`, `[SOS]`. Ao lado do nome há um número — quantas linhas desse tipo foram acumuladas.

> [!warning] Um número vermelho em «Erros» nem sempre é uma falha. A linha `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` também entra lá — o bot está apenas esperando você trazer a janela do jogo de volta para o primeiro plano. Leia o texto da linha em vez de se assustar com a cor.

### Exemplos de linhas reais

Estas são linhas de uma sessão real do bot (o horário foi omitido para simplificar). Aprenda a ler estas cinco — e entenderá qualquer registro.

- `[НАВИГАЦИЯ] Выбрана комната EARTH (порядок: water → mix → earth → fire)` — o bot escolheu a porta de terra. Entre parênteses está a sua ordem de portas. O número na linha "Portas (da esquerda para a direita)" acima indica o grau de certeza do bot ao reconhecer a porta (1 — certeza absoluta).
- `[ВРЕМЯ] Комната 2 (earth): коридор 12.8 с | сборка 3.3 с | бой 8.0 с | результат 9.1 с | всего 33.2 с` — relatório da sala: quanto tempo levou o deslocamento até a porta, a montagem da equipe, a batalha e o fechamento da janela de resultado.
- `[СТАТИСТИКА] Комнат: 3 | Титанит: 36` — a terceira sala foi concluída, 36 de titanita coletada. Estes números vão para os selos da sessão.
- `[ТАКТИКА] Откатываю бой сам и переиграю паком [...] (взят: ваш список запасных паков).` — a batalha foi ruim e o bot (modo «O bot decide sozinho») a rebobina e tenta novamente com o pack reserva. Se o reserva se sair bem: `[ТАКТИКА] Запасной пак [...] справился. Запоминаю его против этих врагов.`
- `[ОТКАТ] Запускаю протокол отката боя...` — início da rebobinagem: "Novamente" → pausa → "Recuar". Cada linha dessas adiciona uma batalha ao selo «Batalhas na sessão».

> [!tip] No início de cada sessão, o bot escreve `[ТАКТИКА] Плохой бой: ХП ниже 30% | потеря больше 60% | ...` — os limites pelos quais ele julgará as batalhas. Se algo acontecer "de forma diferente do que você esperava", primeiro compare essa linha com as suas configurações.

### Botões abaixo do registro

![Botões abaixo do registro: «Salvar log», «Enviar log ao autor», «Limpar»](images/journal_buttons.png)

- :save: **«Salvar log»** — salvará todo o registro em um arquivo de texto. O programa sugerirá automaticamente o nome `gui_log_...txt` e a pasta `bot_data/logs`; você pode escolher outra.
- :mail: **«Enviar log ao autor»** — primeiro fará o mesmo salvamento, depois abrirá seu e-mail com uma mensagem pronta. **Anexe o arquivo ao e-mail você mesmo** (e o `battle_log.csv` da mesma pasta): o programa não pode fazer isso por você. Não tem cliente de e-mail? Escreva para o autor usando o endereço da seção «Sobre».
- :x: **«Limpar»** — remove as linhas da janela, mas antes perguntará «Limpar o registro?». Isso é seguro: o log completo é salvo automaticamente pelo bot na pasta `bot_data/logs`, e os números da sessão não são zerados.

Você pode selecionar texto no registro com o mouse e copiar com Ctrl+C ou com o botão direito («Copiar»). O registro não pode ser editado — ele é apenas para leitura. Se você rolar o registro para cima para ler algo, ele não "fugirá" para baixo com as novas linhas; role até o final e ele voltará a rolar junto com o bot.

> [!note] A janela lembra das últimas 50.000 linhas e exibe as 4.000 mais recentes — caso contrário, em um farm longo ela ficaria lenta. Todo o resto está no arquivo `bot_data/logs/bot_log_...txt`: o próprio bot o mantém, e normalmente não é necessário salvar o registro manualmente.

Enquanto o registro estiver vazio, no seu lugar estará o aviso «O registro está vazio». As linhas aparecerão após a conexão do telefone. Uma pílula sem conteúdo exibirá «Nada aqui ainda» e «Ainda não houve linhas assim» — para «Erros», isso é uma boa notícia.

> [!done] Agora você lê a página principal como o painel de um carro: sabe o que significam os selos e as cores dos rótulos do registro. A seguir — a minibarra, o pequeno painel sob o jogo. [Próxima seção →](#5)

## Minibarra abaixo do jogo

Enquanto o bot está trabalhando, você geralmente não precisa da janela principal do programa. Por isso, ela se recolhe para a barra de tarefas e, sob a imagem do jogo, aparece uma barra estreita — a **minibarra**. É como o painel de um carro: com um único olhar dá para ver se o bot está rodando, o que ele está fazendo agora, quanto já avançou e se está chamando você.

![Minibarra abaixo da janela do jogo durante o farm](images/mini_bar.png)

### Quando ela aparece e onde fica

- :monitor: **Aparece sozinha.** O bot iniciou («Começar o farm») — a janela do programa se minimiza e a minibarra fica logo abaixo do jogo. Se você abriu a janela do programa e quer ocultá-la novamente enquanto o bot trabalha, clique em «Minimizar para a minibarra» na tela principal.
- :smartphone: **Fica colada abaixo do jogo** e tem exatamente a mesma largura da tela do jogo. Se você mover a janela do jogo, a minibarra vai atrás (o programa verifica isso duas vezes por segundo).
- :eye: **Não cobre o jogo em nenhum pixel.** Isso é importante: o bot «olha» para a tela tirando capturas da janela. Se o painel cobrisse o jogo, o bot veria a barra em vez dos botões.
- :maximize-2: **Sem espaço embaixo** (janela do jogo na borda inferior da tela) — a barra ficará acima do título da janela. Se também não houver espaço ali, ela não aparecerá e a janela do programa continuará na barra de tarefas. Se você minimizar a janela do jogo, a barra se esconderá e voltará junto com ela.

> [!tip] A minibarra não aparece, mas o bot está rodando? Mova a janela do jogo mais para cima: é preciso cerca de 100 pixels de espaço livre abaixo dela. Você pode mover a janela, mas não pode alterar o tamanho dela (já explicamos isso na seção 3).

### O que há no painel: cinco colunas da esquerda para a direita

- :activity: **Estado.** Uma palavra e um ponto colorido que «respira» enquanto tudo estiver bem: «INICIANDO», «FARMANDO», «PAUSA», «PAUSA DE DEPURAÇÃO» ou o vermelho «SOS». Abaixo — **o que o bot está fazendo agora** e quantos segundos: por exemplo, «Batalha · Fogo · 12 s». Depois «Salas: 12 · andares: 2» e o tempo da sessão, por exemplo «Tempo 00:42:17».
- :target: **Meta.** Nome da meta, quanto foi feito, quanto falta e a barra de progresso. Abaixo — «~28 s por sala» (tempo médio; antes da primeira sala estará «tempo por sala — após a primeira») e a previsão «meta em ≈ 1 h 10 min». O bot calcula a previsão com base na velocidade **desta** sessão, por isso varia no início e depois estabiliza. Se não houver meta («Sem limite»), não haverá barra, e em vez da previsão aparecerá «≈ N de titanita por hora».
- :heart-pulse: **Saúde da equipe.** Quadrados dos titãs que estiveram na última batalha e seus PVs depois dela — na mesma ordem em que aparecem na tela do jogo. Antes da primeira batalha, estará escrito «ainda sem batalhas». A cor do número indica: vermelho — PV abaixo do limite de pânico (geral ou individual), amarelo — abaixo do limite em que o bot cura o titã, cor normal — tudo certo. Um travessão «—» significa que não foi possível encontrar o ícone do titã na janela de resultado.
- :list: **Eventos.** As últimas quatro linhas, com a mais recente no topo e maior. À esquerda há uma marca colorida, à direita o horário.
- :gamepad-2: **Botões.** Quatro botões dispostos em um quadrado 2×2.

### O que o bot pode estar «fazendo agora»

Na primeira coluna, o próprio bot indica a etapa atual. Veja o que essas palavras significam:

- **«Corredor»**, **«Escolhendo a porta»**, **«Montando a equipe»**, **«Batalha»**, **«Janela de resultado»** — ciclo normal de uma sala. Nas etapas «Montando a equipe», «Batalha», «Janela de resultado» e «Recuo», o elemento da sala é adicionado: «Batalha · Água · 12 s».
- **«Ponto de salvamento»** — andar concluído, o bot resgata a recompensa.
- **«Recuo»** — a batalha foi ruim, o bot recua e se prepara para tentar novamente.
- **«Verificando a tela»** — após iniciar, o bot analisa a tela e decide por onde começar (isso é o «início inteligente»).
- **«Pausa no corredor»**, **«Esperando sua decisão»**, **«Você está jogando»** — o bot está parado porque você pausou, porque ele fez uma pergunta ou porque você escolheu «Jogar manualmente».
- **«Esperando a janela do jogo»** e **«Esperando conexão»** — o bot está esperando: ou o jogo não está em primeiro plano (veja abaixo), ou não há conexão com o servidor do jogo.

Se a mesma mensagem continuar por mais tempo do que o normal, o número de segundos à direita vai subir para indicar que o bot está travado ou parado.

### Eventos: marcas e o que elas significam

A marca à esquerda mostra sobre o que é o evento:

- **Nome do elemento** («Água», «Terra», «Fogo», «Misto») — sala concluída. Uma linha como «Sala 45 concluída · 28 s · menor PV: Araji 36%» mostra quantos segundos a sala levou e quem ficou com a menor vida.
- **«Andar»** — andar concluído («Andar concluído, 3 no total»).
- **«Recuo»** — a batalha está sendo repetida. **«SOS»** — o motivo do chamado em palavras simples.
- **«Pausa»** — «Pausa: o bot termina a batalha e espera», depois «O bot espera no corredor».
- **«Bot»** — «Bot iniciado», «Pausa retirada, o bot continua», «Sem resposta há 10 min — o bot decidiu sozinho».
- **«Limite»** — a sessão atingiu a meta, o bot joga até o ponto de salvamento.
- **«Atenção»** — «A janela do jogo não está ativa — o bot espera. Clique no jogo».
- **«Erro»** — o texto do erro exatamente como foi gerado pelo bot.

Linhas longas são cortadas com reticências. O texto completo sempre estará no log da tela principal.

### Botões

Passe o mouse por cima para ver a descrição. Todos os botões fazem o mesmo que os seus «irmãos maiores» na tela principal e no cabeçalho.

- :pause: **Pausa / Continuar** — «Pausa suave: o bot termina a batalha e espera (F9)». Durante a pausa, o ícone vira um triângulo verde e esse mesmo botão retira a pausa. Enquanto o bot está apenas iniciando, o botão fica indisponível.
- :square-filled: **PARAR** — «Parada de emergência: o bot para na hora, sem resumo no Telegram (F10)».
- :moon: **Tela do telefone** — «Desligar a tela do telefone», enquanto o jogo continua rodando.
- :maximize-2: **Abrir** — «Abrir a janela do programa». A minibarra desaparecerá. Clicar no ícone do programa na barra de tarefas produz o mesmo resultado. Se quiser trazer a barra de volta, clique no botão «Minimizar para a minibarra» na tela principal.

> [!note] Quando o bot chama você, a minibarra fica vermelha e a janela «Intervenção necessária» aparece sozinha no centro da imagem do jogo — não é preciso abrir a janela do programa. O primeiro botão nesse momento não pausa nem dá «continuar»: ele traz a janela SOS para a frente caso esteja oculta sob outras janelas (descrição — «Mostrar a janela SOS: o bot espera sua decisão»). Assim que você responder na janela, a minibarra volta ao normal. Explicaremos como responder no capítulo sobre janelas SOS.

![Minibarra durante um SOS](images/mini_bar_sos.png)

### Regra principal: o bot só funciona enquanto o jogo estiver em primeiro plano

O bot tira capturas de tela e procura os botões nelas. Se outro navegador, aplicativo de mensagem ou gerenciador de arquivos cobrir o jogo, a captura vai pegar essa outra janela e não o jogo: o bot pode acabar clicando no lugar errado. Por isso, assim que outra janela fica ativa, ele para e espera. No log aparece a linha «[ВНИМАНИЕ] Окно игры перекрыто … Бот ждет фокуса…» («[ATENÇÃO] A janela do jogo está coberta ... O bot aguarda o foco...»), na minibarra surge a marca «Atenção» e a etapa «Esperando a janela do jogo». Se você clicar no jogo, aparece «[ИНФО] Окно снова активно. Продолжаем работу.» («[INFO] Janela ativa novamente. Continuando o trabalho.»).

- :monitor: **Clicar na minibarra não faz o bot parar.** A minibarra foi feita para não roubar o foco da janela: o jogo continua sendo a janela «principal» enquanto você clica nos botões do painel.
- :triangle-alert: **«Abrir» para o bot temporariamente.** A janela do programa ficou ativa, mas o jogo não, então o bot vai parar na próxima etapa. Quando terminar, clique na janela do jogo e o bot continuará. Esse tempo de espera não é considerado travamento pelo sistema de vigilância.
- :gamepad-2: Quer usar o computador enquanto o bot faz o farm? Abra as outras janelas **ao lado** e não em cima do jogo, evitando clicar sobre elas. Ou deixe para fazer isso durante uma pausa (F9).

> [!warning] As teclas de atalho F9 e F10 só funcionam quando a janela do jogo ou a janela do programa estiver ativa. Se você pressionar F10 no navegador, o bot não vai parar: as teclas não respondem se você estiver mexendo em outro programa. Saiba mais na seção sobre pausa e parada.

> [!done] Agora você já consegue ler a minibarra como um painel de controle e sabe por que não deve cobrir o jogo com outras janelas. A seguir — pausa, parada e teclas de atalho. [Próxima seção →](#6)

## Pausa, parada e atalhos de teclado

O bot anda pela Masmorra sozinho, mas às vezes você precisa desacelerá-lo: você quer jogar manualmente, sair para resolver algo ou simplesmente terminar. Para isso, existem **quatro formas**, e elas se diferenciam por **quão suavemente** o bot para. Pense em um carro: «pausa» é encostar no acostamento e desligar o motor, enquanto «parada de emergência» é tirar a chave com o carro em movimento. Ambos funcionam, mas de formas diferentes.

### Pausa suave: «Pausa F9»

A forma mais cuidadosa. Clique no botão «Pausa» na tela principal, na minibarra ou pressione a tecla **F9**.

1. **Clique em «Pausa» ou F9.** No log aparecerá a linha `[GUI] Сигнал 'Мягкая пауза' отправлен. Бот остановится перед следующей дверью.`
2. **Espere o bot terminar a sala.** Ele não abandona a batalha que já está em andamento: vai jogá-la até o fim, fechar a janela de resultados e registrar o resumo da sala.
3. **O bot para no corredor.** No log: `[МЯГКАЯ ПАУЗА] Бот ждет в коридоре...`. O status na tela principal será «Pausa», na minibarra — «PAUSA», e o botão ficará verde com «Continuar».
4. **Faça o que precisa e clique em «Continuar» (ou pressione F9 novamente).** O bot escreve `[ИНФО] Пауза снята. Кэш составов и здоровья очищен. Включаю механизм Умного Старта.` e continua.

> [!note] «Cache limpo» significa que o bot **esqueceu** quais formações estavam selecionadas e quanta vida os Titãs tinham: enquanto você mexia no jogo, tudo pode ter mudado. Antes da próxima batalha, ele olhará novamente para a tela de seleção de equipe e lerá a vida a partir dela. «Início Inteligente» é quando o bot primeiro observa o que está na tela no momento e só depois decide o que fazer (por exemplo, fecha uma janela de resultado esquecida).

- :eye: **Durante a pausa, você pode olhar para o celular e alterar as configurações na janela do programa.** Mas o bot só aplicará as configurações no próximo «Começar o farm» (mais detalhes na seção sobre a tela principal).
- :door-open: **Se você clicou em algo no jogo — volte para o corredor da Masmorra** (onde a bandeira ao lado da porta é visível) e só então clique em «Continuar». Assim, o bot entenderá exatamente onde está.
- :gauge: **O tempo continua contando mesmo na pausa.** Se a meta da sessão for tempo («120 minutos»), a pausa consumirá parte desse tempo. Por outro lado, o «vigia» (o mecanismo que monitora se o bot travou) não conta o tempo de pausa e não emitirá alarme.

> [!tip] Quer se ausentar durante a noite ou por muito tempo? Não é necessária uma pausa suave para isso: defina uma meta (titanita, salas, andares ou tempo) na tela principal, e o bot chegará sozinho ao ponto de salvamento, parará e enviará o resumo.

### Quando o bot entra em pausa sozinho

Às vezes o bot pede ajuda e entra em pausa suave sozinho. Nesse caso, o botão também exibirá «Continuar», e o log mostrará `[ВНИМАНИЕ] Бот на мягкой паузе: ...` com o motivo. Isso acontece quando:

- o bot não passou por nenhuma sala por três vezes seguidas durante 5 minutos (o vigia decidiu que ele travou);
- a reinicialização da batalha falhou (a tela não foi reconhecida, os botões não foram pressionados);
- a batalha não começou, mesmo após uma longa espera;
- você não respondeu à janela «Nenhum pack adequado», e não há pack reserva.

Nesses casos, primeiro **olhe para a tela do celular**, corrija o problema (feche a janela desnecessária, volte ao corredor) e só depois clique em «Continuar». Se o Telegram estiver configurado, o bot enviará uma mensagem com captura de tela.

### Parada de emergência: «PARAR F10»

O botão vermelho «PARAR» (ou a tecla **F10**) para o bot **imediatamente**: o programa encerra o processo do bot. No log — `[GUI] ЭКСТРЕННЫЙ СТОП. Процесс убит.`, no cartão de resumo o motivo será «parado pelo botão «PARAR»».

> [!warning] O que é perdido com F10: o bot não tem tempo de escrever o bloco `[ИТОГ]` no log e **não envia o resumo da sessão para o Telegram**. Se ele estava em batalha naquele momento, a batalha continuará no jogo (ou permanecerá na tela) — você verá isso no celular. As salas já concluídas permanecem salvas nas estatísticas: o bot as registra imediatamente após cada sala.

Quando usar exatamente esse botão: o bot está se comportando de maneira estranha (clicando onde não deve, não respondendo a «Pausa») ou você precisa parar tudo imediatamente. Em outros casos, é melhor usar a pausa ou Ctrl+Q.

### Atalhos de teclado: o que funciona onde

- :pause: **F9** — pausa / «Continuar» (o mesmo que o botão «Pausa» na tela principal).
- :square-filled: **F10** — «PARAR».
- :gamepad-2: **Ctrl+Q** — parar **com resumo**: o bot terminará a sala iniciada, parará no corredor, encerrará e enviará o resumo da sessão. No log: `[ИНФО] Команда 'Ctrl+Q' принята! Бот завершит бой и остановится.`, motivo da parada — «Parada manual pelo usuário (Ctrl+Q)».
- :triangle-alert: **Ctrl+Shift+Q** — parar **imediatamente, mas com resumo**: o bot imprime `[ЭКСТРЕННАЯ ОСТАНОВКА]`, registra `[ИТОГ]` e faz **uma** tentativa de enviar o resumo para o Telegram (sem repetições, para não atrasar).

Detalhes importantes pelos quais as teclas às vezes «não funcionam»:

- **A janela do programa escuta F9 e F10** e apenas quando **a janela do jogo ou a janela do programa está ativa**. Se você pressionar F10 no navegador ou aplicativo de mensagens — nada acontecerá. Se o jogo estiver minimizado ou coberto por outra janela, use os botões da minibarra: eles funcionam sempre, porque a minibarra não tira o foco do jogo.
- **O próprio bot escuta Ctrl+Q e Ctrl+Shift+Q**, e não a janela do programa, portanto eles funcionam enquanto o bot estiver rodando, mesmo que outra janela esteja ativa.
- **Essas combinações também são conhecidas por outros programas.** Ctrl+Q fecha muitos programas (Word, Telegram Desktop), e Ctrl+Shift+Q — navegadores. Enquanto o bot estiver rodando, não as pressione em outras janelas: o bot também «ouvirá» isso e parará.
- **O bot verifica Ctrl+Q quando está no corredor** diante da próxima porta. Na pausa suave, ele fica parado e não verifica nada, portanto Ctrl+Q só funcionará depois de «Continuar». Mas se o bot estiver aguardando sua resposta na janela SOS, Ctrl+Q o parará imediatamente.
- **Manter a tecla pressionada não repete a ação:** um clique — um comando.
- Se pressionar F9 ou F10 quando o bot não estiver rodando, aparecerá no log `[GUI] Нажата F9, но бот не запущен.`

### Botão de fechar a janela e encerramento do scrcpy

- :x: **O botão de fechar a janela do programa enquanto o bot está rodando.** Abrirá a pergunta «Parar o bot?». O botão «Parar e fechar» fechará o programa e o bot, e a janela do jogo (scrcpy) — se foi aberta pelo próprio programa — será fechada imediatamente, sem enviar o resumo para o Telegram. Se não quiser isso, feche a janela da pergunta e primeiro pare o bot de forma suave.
- :smartphone: **Fechou a janela do jogo (`HeroWarsBot_Arena`) manualmente.** O programa escreverá `[GUI] Окно scrcpy закрыто — останавливаю бота (он напишет итог и пришлёт его в Telegram).` O bot sozinho terminará de escrever o resumo da sessão e o enviará para o Telegram; se não responder em 10 segundos, o programa o parará como se fosse F10.
- :pencil: Se houver alterações não salvas no «Assistente de regras», o botão de fechar primeiro perguntará «Salvar alterações?».

### O que escolher

- **Quero fazer uma pausa e voltar** — «Pausa» (F9). Clique em «Continuar» quando estiver pronto.
- **Quero terminar e receber o resumo** — Ctrl+Q (o bot terminará a sala, parará e enviará o resumo para o Telegram).
- **Preciso parar agora mesmo, mas preciso do resumo** — Ctrl+Shift+Q.
- **O bot travou ou está se comportando de forma estranha** — «PARAR» (F10), depois analise o log.
- **O bot chamou você pela janela SOS e você quer terminar** — o botão «Parar o bot» nessa janela: o bot parará sozinho e enviará o resumo. Analisaremos a janela SOS separadamente.

### Resumo da sessão no Telegram

Se o Telegram estiver configurado, o resumo chegará em qualquer parada, **exceto pelo botão «PARAR»** e ao fechar a janela do programa: o bot escreve se você o parou manualmente («Bot parado por você»), se concluiu a meta («Farm concluído») ou se falhou com erro, quanto tempo se passou, quantas salas, andares e titanita, se houve rollback e janelas SOS. Se não houver conexão com a internet, o bot tentará enviar o resumo mais duas vezes (após 10 e 30 segundos) e depois desligará. Como conectar o Telegram estará em uma seção separada.

> [!done] Agora você sabe como pausar o bot de forma suave e como pará-lo definitivamente, e o que cada tecla faz. A seguir — configuração de regras: como ensinar o bot a definir os packs necessários. [Próxima seção →](#7)

## Mestre de Regras: «Base e salas»

«Mestre de Regras» — o segundo botão na barra esquerda (ícone com seletores). Aqui você explica ao bot três coisas: **quando parar**, **o que considerar uma batalha ruim** e **qual equipe usar em cada sala**. Uma equipe (pack) é um time de 3 a 5 titãs. A página está dividida em três abas na parte superior: «Base e salas», «Autotática e PV» e «Regras e interceptações». Neste capítulo abordamos a primeira, a mais importante: sem ela o bot não sabe nem quem colocar na batalha.

![Aba «Base e salas»: no topo dois cartões com configurações, abaixo quatro linhas com equipes](images/rules_base.png)

No topo fica «Parâmetros da sessão» (dois cartões), abaixo — «Equipes por sala». Na parte inferior da página, igual em todas as abas, há uma barra cinza com os botões: «Salvar configurações» e «Restaurar / Redefinir». Falaremos sobre ela no final da seção. O mais importante para lembrar de imediato: **enquanto você não clicar em «Salvar configurações», nada estará gravado** — nenhuma alteração chegará ao bot.

### Cartão «Metas e limites»

- :target: **«Meta da sessão»** — quando o bot deve terminar. A meta é sempre **uma**, de quatro opções: «Titanita», «Salas», «Andares» ou «Tempo» (tempo — em minutos). Escolha o tipo na lista e digite o número no campo. O campo aceita apenas números. A legenda "0 — sem limite" significa: zero desativa a meta, e o bot continuará jogando até você pará-lo. A seta circular à direita («Zerar meta») define 0.
- :gem: **O bot calcula a Titanita sozinho**, sem ler da tela: 6 por uma sala comum e 12 se houver o ícone "x2" na janela de resultado. Portanto, "120 titanita" equivale a cerca de 20 salas sem "x2". Enquanto você nunca tiver salvo as configurações, o bot usará por padrão a meta de "120 titanita".
- :layers: **O bot não abandona um andar no meio.** Ao atingir a meta «Titanita», «Salas» ou «Tempo», ele não para no lugar: escreve no log `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, conclui as salas restantes do andar e para diante do ponto de salvamento, sem clicar em "Ativar". Assim, o andar não fica incompleto, e o bot resgatará a recompensa e contabilizará o andar logo ao iniciar a próxima sessão. Se o ponto de salvamento não for encontrado em 6 salas (há 5 salas por andar), o bot parará como estiver. A meta «Andares» é acionada assim que o ponto de salvamento for concluído.
- :gauge: **O tempo continua contando durante a pausa.** A meta "Tempo — 120" significa 120 minutos a partir do clique em «Começar o farm», incluindo todas as pausas.
- :calendar: **«Hora de virada do dia (hora local)»** — a que horas começa o seu novo dia de jogo. Por padrão, é 05:00. Disso depende a qual dia as batalhas pertencem nas estatísticas, além da memória do bot sobre a vida dos titãs: ela existe dentro de um único dia de jogo e, em um novo dia, o bot começa do zero. Defina a hora após a qual você considera o dia novo (por exemplo, quando vai dormir).
- :send: **«Configurar Telegram»** — abre uma janela separada onde a comunicação com o mensageiro é ativada. Ao lado do botão há um ponto e a legenda: verde «Avisos SOS ativados» ou cinza «Telegram não configurado». Como conectar, veremos na seção sobre o Telegram. Aqui o importante é uma coisa: o botão «Aplicar» nessa janela altera apenas esta página. Para gravar a configuração no arquivo, você ainda precisa clicar em «Salvar configurações».

> [!tip] Qual meta escolher? «Tempo» é conveniente quando você tem uma janela de tempo livre ("deixe o bot rodar por uma hora enquanto preparo o jantar"). «Titanita» — quando precisa obter uma quantidade específica de recompensa. «Salas» e «Andares» — quando deseja concluir exatamente uma certa quantia. Na dúvida, deixe «Titanita» e 120: é uma corrida de teste curta.

### Cartão «Segurança e modo»

Aqui se define **o que é uma batalha ruim**. O bot lê os pontos de vida (PV) dos titãs na janela de resultado e compara dois números com os seus.

- :heart-pulse: **«Limite de pânico de PV, %»** — abaixo de qual vida após a batalha ela é considerada ruim. Por padrão, 40.
- :swords: **«Delta de perda de PV, %»** — quanto PV um único titã pode perder em uma única batalha. Por padrão, 30.

Ambos os campos aceitam números inteiros de 0 a 100; se digitar algo diferente, o campo ficará vermelho com a mensagem «Digite um número de 0 a 100», e não será possível salvar as configurações até que você corrija.

Exemplo prático com limite 40 e delta 30:

- Araji entrou na batalha com 100% e saiu com 80% — **tudo bem**: perdeu 20 e continuou acima de 40.
- Araji entrou com 100% e saiu com 55% — **batalha ruim**. 55 está acima do limite, mas perdeu 45, quando o permitido era 30.
- Araji entrou com 50% e saiu com 35% — **batalha ruim**. Perdeu apenas 15, mas 35 está abaixo do limite de pânico.
- Qualquer titã morreu ou não foi encontrado na janela de resultado — **batalha ruim** sempre, não importa o que você definir.

As perdas são calculadas a partir da vida com a qual o titã **entrou** na batalha, e não a partir de 100%. Por isso, um titã ferido atinge o limite mais cedo do que um saudável. Quanto maior o limite e menor o delta, mais rigoroso é o bot e mais frequentemente ele chama você; zero no limite desativa a verificação "abaixo do limite" (exceto mortes), e 100 no delta desativa a verificação de perdas.

> [!note] O limite e o delta são gerais para todos os titãs. Para um titã individual, é possível definir seu próprio limite, além de ativar a regra "se três perderem muito — batalha ruim". Isso é feito na aba vizinha «Autotática e PV».

Abaixo há dois alternadores:

- :shield-check: **«O bot decide sozinho»** («Reverte batalhas ruins e escolhe a equipe») — por padrão **desativado**. Desativado: batalha ruim → janela «Intervenção necessária», o bot espera por você. Ativado: o bot reverte a batalha sem questionar, joga novamente com a equipe reserva e também escolhe a equipe sozinho com base no PV dos titãs. Detalhes na seção sobre operação autônoma do bot. Ative quando já tiver observado o bot funcionando e confiar nas equipes reserva.
- :swords: **«Controle manual do ultimate de Angus»** («Global, em todas as salas») — por padrão **desativado**, e então qualquer batalha, inclusive com Angus, ocorre em modo automático. Ativado: para equipes com Angus, o bot clica em "Batalha", ativa o modo automático por um par de segundos para soltar o ultimate de Angus e desativa novamente. O bot não reverte esse tipo de batalha sozinho, mas chama você. Na inicialização, é possível ver no log o que foi selecionado: `[ТАКТИКА] Ангус: ...`.

### Equipes por sala

Sob a legenda «A equipe principal vai primeiro; as reservas, em ordem, se a batalha for ruim», há quatro linhas — por salas: «Terra», «Água», «Fogo» e «Misto». Cada uma é um cartão separado.

- :users: **Equipe principal** — os quadros dos titãs sob o nome da sala. O bot a utiliza se não houver motivo para fazer o contrário (por exemplo, se uma regra da aba «Regras e interceptações» for acionada). Os titãs são exibidos da esquerda para a direita, **como aparecem na tela do jogo**. Se não houver equipe — em vez dos quadros aparece a legenda «Pack não definido».
- :pencil: **Lápis («Mudar equipe»)** — abre a janela «Monte a equipe».
- :list: **«Equipes reserva»** com o número "N un." — lista suspensa (seta para baixo/para cima). O bot tenta as equipes reserva em ordem se a batalha for ruim e ele decidir sozinho («O bot decide sozinho» ativado ou você não respondeu à janela a tempo). Em cada sala há até 5. Dentro, cada equipe reserva é uma linha `#1`, `#2` e assim por diante, e à direita há um X («Remover equipe»). O botão «Adicionar equipe» abre a mesma janela «Monte a equipe».
- :plus: **«Condição»** — «+ Condição»: atalho para criar uma regra para esta sala, por exemplo "se for contra Angus — use esta equipe". A janela «Nova regra» será aberta com a sala já selecionada. Como preenchê-la, veremos na seção de regras.

Defina a equipe principal em todas as quatro salas **antes do primeiro farm**: o bot não conhece seus titãs e não vem com equipes pré-definidas.

Como montar uma equipe:

1. **Clique no lápis** na sala desejada. A janela «Monte a equipe» será aberta.
2. **Clique nos titãs** que deseja colocar. Clique novamente para remover. No topo há uma contagem: «Escolhidos: 3 / 5» e a dica «Pronto para aplicar» (quando houver dois, exibirá «Mínimo 3 · faltam 1»).
3. **Considere o elemento da sala.** Em «Terra», «Água» e «Fogo» entram apenas titãs desse elemento, e em «Misto» — todos, incluindo Métis (ela é de elemento elario e não entra em outras salas: «Métis — só na sala mista»). Quando 5 titãs são selecionados, os demais são bloqueados.
4. **Clique em «Aplicar»** (ou «Cancelar», se mudar de ideia; «Limpar» remove todos os titãs de uma vez).

![Janela «Monte a equipe» para a sala «Água»: três titãs selecionados, no rodapé «Aplicar»](images/rules_picker.png)

> [!warning] «Aplicar» na janela «Monte a equipe» apenas altera a página: a equipe ainda **não está gravada** no arquivo. Ela será gravada quando você clicar em «Salvar configurações». A equipe principal de cada sala fica no arquivo `bot_data/rules/<стихия>.yml`, as reservas e todos os números ficam em `profile.yml`. Não é necessário editar esses arquivos manualmente.

Uma equipe reserva que já existe na lista (em qualquer ordem de titãs) não pode ser adicionada uma segunda vez: aparecerá o aviso «Essa equipe reserva já existe».

> [!tip] Quais equipes colocar como reserva? Dê escolha ao bot: faça com que a equipe reserva seja diferente da principal em pelo menos um par de titãs. Se Araji costuma sair ferido da batalha, coloque na equipe reserva titãs que aguentem melhor o dano.

### Salvamento e «Restaurar / Redefinir»

A barra inferior mostra o status: «Todas as alterações salvas» (check verde) ou «Há alterações não salvas» (ícone amarelo). Enquanto o bot estiver rodando, ao lado é exibido «O bot usará as novas configurações na próxima inicialização».

- :save: **«Salvar configurações»** grava apenas o que você alterou e exibe o aviso «Configurações salvas». Enquanto o botão não for clicado, o bot não saberá das suas edições. No log aparecerá `[GUI] Профиль настроек сохранен!`.
- :rotate-ccw: **«Restaurar / Redefinir»** — botão vermelho; primeiro perguntará «Restaurar configurações?». As configurações retornarão às **últimas salvas** (cópia `bot_data/profile.yml.bak`). Se não houver cópia, `profile.yml` será excluído e o bot usará os valores padrão. As edições não salvas serão perdidas. As equipes principais e regras nos arquivos `bot_data/rules` não são afetadas por este botão, mas o formulário da página as relerá do disco.
- :triangle-alert: **Se você sair da página com alterações não salvas** (para outra seção ou fechando na cruz da janela), surgirá «Salvar alterações?» com os botões «Salvar», «Não salvar» e «Cancelar».

O bot lê as configurações **uma única vez, quando você clica em «Começar o farm»**. Você pode alterá-las durante o funcionamento, mas elas só terão efeito após a parada e uma nova inicialização. Mesmo «Pausa» e «Continuar» não as atualizam. O cartão «Configuração de início» na página principal mostra exatamente as configurações com as quais o bot está trabalhando no momento.

> [!warning] Se o arquivo `profile.yml` estiver danificado, no topo do log principal aparecerá `[ОШИБКА] Файл profile.yml поврежден!`, na página serão exibidos valores padrão e «Salvar configurações» se recusará a gravar («profile.yml está danificado — configurações não salvas»). Clique em «Restaurar / Redefinir».

> [!done] Agora você sabe como definir a meta, os limites e as equipes para cada sala. A seguir — a aba «Autotática e PV»: a ordem das portas e como o bot cura e troca os titãs. [Próxima seção →](#8)

## Assistente de regras: «Autotática e PV»

Segunda aba do «Assistente de regras». Na primeira («Base e salas»), você definiu as equipes e os limites comuns. Aqui você explica ao bot **como se comportar quando algo der errado**: qual porta abrir primeiro, o que considerar uma batalha ruim, quantas vezes tentar outra equipe, quanto tempo esperar por você e como curar os titãs feridos. Todos os campos já vêm preenchidos com valores razoáveis, então o bot funciona mesmo sem suas alterações. Mude apenas quando perceber que ele não está se comportando como você deseja.

![Aba «Autotática e PV»: faixa no topo, quatro portas, dois cartões lado a lado e limites pessoais na parte inferior](images/tactics_tab.png)

Assim como na primeira aba, **nada é gravado até que você clique em «Salvar configurações»**, e o bot lê as configurações apenas uma vez, quando você clica em «Começar o farm». Se você alterar algo durante o farm, as mudanças só farão efeito após parar e iniciar novamente.

### Faixa azul no topo

Ela explica resumidamente o que o bot faz em caso de uma batalha ruim: faz o recuo (rollback) e joga novamente com uma equipe de reserva, salvando a equipe bem-sucedida em uma regra.

Se o interruptor «O bot decide sozinho» estiver desativado na primeira aba, uma frase adicional aparecerá na faixa. Ela é importante, por isso vamos explicá-la em detalhes. **Sem a opção «O bot decide sozinho», duas coisas не funcionam: equipes de reserva e a equipe de cura.** Todo o resto nesta aba funciona sempre:

- :door-open: ordem das portas;
- :gauge: tempo de espera pela sua resposta na janela SOS (a janela onde o bot chama você quando a batalha é ruim);
- :triangle-alert: critérios de batalha ruim;
- :heart-pulse: limites de pânico pessoais.

### «Prioridade das portas»

No corredor, o bot frequentemente vê várias portas ao mesmo tempo: uma para cada elemento («Água», «Terra», «Fogo») ou «Misto». Dentro da sala os inimigos esperam por você, e cada elemento exige sua própria equipe. A ordem define **qual porta o bot abrirá primeiro**. Por padrão, a ordem é: «Água», «Misto», «Terra», «Fogo».

Os quatro espaços vão da esquerda para a direita com setas entre eles; cada um tem um número de 1 a 4. Clique em um espaço e escolha um elemento. Não há duplicatas: se você escolher um elemento que já está em outra posição, eles simplesmente **trocam de lugar**. Se a ordem era «Água, Misto, Terra, Fogo» e você escolheu «Fogo» para o primeiro lugar, ela se tornará «Fogo, Misto, Terra, Água».

Duas observações para você não se surpreender no jogo:

- Se uma porta for **proibida por uma regra «Skip»** (veja mais na seção sobre «Regras e interceptações»), o bot a pulará, mesmo que seja a primeira da ordem. Se todas as portas forem proibidas, ele escolherá a primeira da ordem.
- Se «O bot decide sozinho» estiver ativado, o bot às vezes **escolherá outra porta por conta própria**, fora da ordem: para onde a cura de um titã ferido funcione ou evitando uma porta perigosa para os feridos. Essa escolha aparece no registro com a linha `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`.

### Cartão «Critérios de batalha ruim e SOS»

- :swords: **«Equipes reserva a tentar por sala»** — quantas vezes em uma mesma sala o bot pode recuar a batalha e tentar novamente com outra equipe. De 1 a 3, por padrão 2. Se esgotar as tentativas e a batalha continuar ruim, o bot chamará você. Funciona apenas com «O bot decide sozinho». Não é possível definir mais de 3: não faz sentido tentar a mesma batalha dez vezes, e cada tentativa consome tempo.
- :gauge: **«Tempo da janela SOS sem resposta, min»** — quantos minutos o bot espera por sua resposta na janela «Intervenção necessária» antes de decidir por conta própria. De 0 a 60, por padrão 10. A legenda abaixo do campo diz «0 — esperar sempre»: **zero significa "esperar para sempre"**, e o bot ficará parado esperando por você até de manhã. Isso funciona mesmo **sem** a opção «O bot decide sozinho». O que exatamente o bot decidirá sozinho (recuar a batalha, aceitá-la ou pausar) está explicado na seção sobre janelas SOS.
- :users: **«Considerar a batalha ruim se»** — perdas gerais da equipe: «titãs ≥ 3» e «perderam ≥ 40» «% PV cada». Essa verificação pega os casos em que **cada um isoladamente aguenta**, mas juntos a equipe desmorona. Se três titãs потеряли 40% ou mais, a batalha é ruim, mesmo que nenhum tenha caído abaixo do limite de pânico. A legenda «0 titãs — не проверять» significa: coloque 0 no primeiro campo e a verificação será desativada. O primeiro campo vai de 0 a 5, o segundo de 0 a 100.

Um exemplo prático. Equipe: Araji, Hyperion, Rigel, Iyari, Lumira. Após a batalha, Araji perdeu 45%, Rigel 42%, Iyari 40% e os outros 10% cada. Três titãs perderam "40% ou mais" — a batalha é ruim, mesmo que todos tenham ficado acima do limite de pânico. Se Iyari tivesse perdido apenas 35%, seriam apenas dois titãs nessa situação, e a verificação geral não encontraria problemas.

> [!note] Os outros critérios de batalha ruim — limite de pânico e perda permitida — estão na primeira aba «Base e salas». A batalha é considerada ruim se **pelo menos um** critério for atingido: alguém morreu ou não foi detectado na tela, alguém está com PV abaixo do limite, alguém perdeu mais do que o permitido ou a regra de perdas gerais foi acionada.

Se você digitar um valor inválido (letra ou número fora dos limites), o campo ficará vermelho, exibindo «Um número de … a …», e não será possível salvar as configurações até que você corrija.

### Cartão «Equipe de cura automática na sala Mista»

É comum acontecer o seguinte: um titã leva muito dano por algumas batalhas seguidas e fica com metade da vida. Cedo ou tarde ele cairá abaixo do limite e a batalha se tornará ruim. A "cura" ocorre quando o bot **monta automaticamente uma equipe especial** para recuperar o ferido (incluindo um curandeiro que restaura a vida dele). O bot só monta essa equipe para a sala «Misto», pois nela é possível colocar qualquer titã.

Isso só funciona com «O bot decide sozinho» e apenas se sua própria regra de cura não tiver sido acionada (sua regra tem prioridade).

- :heart-pulse: **«Curar o titã se os PV estiverem abaixo de, %»** — por padrão 60. Se o titã tiver mais vida que esse número, é considerado saudável. **0 desativa** a equipe de cura totalmente. Mas há um limite inferior: se os PV do titã já estiverem **abaixo do limite de pânico**, ele não poderá ser curado na sala «Misto» e o bot não mexerá nele.
- :users: **«Quem tirar da equipe pelo ferido»** — três posições com setas. Quando o ferido precisa entrar na equipe e não há vaga, alguém tem que sair. Clique na posição e escolha o titã: a lista é dividida em colunas por elementos. **«— auto —»** (opção padrão) significa: o bot remove a partir do final da equipe, mas **não toca nos curandeiros**. Para a equipe «Hyperion, Rigel, Iyari, Lumira, Amon», seriam Amon e depois Lumira. Se você escolher um titã que já está em outra posição, eles trocarão de lugar.

Como o bot cura, em termos simples:

1. Смотрит, у кого ХП ниже 60%, но выше порога паники, и кого из них не запретили правила «Skip».
2. Лечит **по одному**, начиная с того, кто ближе всего к своему порогу. Сначала основных (из базовых паков), потом запасных.
3. Если раненого в паке нет — он встаёт на место убранного. Но титанов, которых и так лечат в «своей» комнате (водных и земляных: в их базовом паке есть лекарь), бот в «Смешанную» не тянет, только если там они два боя подряд не поднимаются выше порога. Огненных лечить в «своей» комнате нечем, поэтому для них отхил включается сразу.
4. Если раненый уже в паке, но два боя подряд не поднимается — вместо убранного встаёт **здоровый и заряженный лекарь** (ХП от 80%, энергия от 60%).
5. Пак не берётся, если в нём не осталось лекаря, он проигрывает этим врагам, опасен для раненых или требует ручного боя (Ангус).

Por que o bot é tão cuidadoso? Ele não vai curar um titã que você não tenha indicado em lugar nenhum: o bot nunca escala sozinho um titã que не esteja nas suas equipes ou regras. Se não for possível montar a equipe (o titã não encaixar no slot), o bot não para: usa a equipe normal e **não tenta curar esse titã novamente até o final da execução**.

No registro, isso pode ser visto nas linhas `[ТАКТИКА] Пак отхила (бот собрал сам): ...` e `[ТАКТИКА] Отхил: ...` (explicando por que o ferido não está sendo curado).

### Cartão «Limites de pânico pessoais dos titãs, % PV»

O limite de pânico comum (40 por padrão) aplica-se a todos. No entanto, há titãs que você prefere не perder cedo e outros que suportam bem ficar com PV baixo. Para estes, você pode definir um **limite próprio**.

- Na parte inferior há a legenda «Os outros titãs: limite comum 40%» (o número vem da primeira aba). Enquanto não houver limites pessoais, aparecerá «Sem limites pessoais — todos os titãs usam o comum».
- Clique em «Definir limite pessoal para um titã». Uma pequena janela «Limite de pânico pessoal» se abrirá: escolha o titã na lista e digite um valor de 0 a 100. Clique em «Aplicar». A janela exibe a dica «Limite comum — 40%» para você comparar. A lista mostrará apenas os titãs que ainda não possuem limite pessoal.
- Cada limite definido aparece como um bloco com o titã e um número amarelo. Clique no bloco para alterar o limite (não é possível mudar o titã; você precisará removê-lo e adicioná-lo novamente). O **ícone X** no bloco remove o limite pessoal, fazendo o titã voltar a usar o comum.

A batalha é ruim se os PV do titã após o combate ficarem **abaixo do seu limite pessoal**. Exemplo: limite comum em 40, mas Rigel está configurado com 60. Se Rigel terminar com 55%, a batalha é ruim, embora para os outros 55% fosse aceitável.

> [!tip] Por onde começar? Não mude nada até observar algumas dezenas de salas. Se notar que o bot chama você sempre por causa do mesmo titã, defina um limite pessoal mais baixo para ele. Se o bot trocar de equipe com muita frequência para curar, **reduza** o número em «Curar o titã se os PV estiverem abaixo de, %». Se não quiser que ele cure, coloque 0.

> [!warning] Se você definir o «Tempo da janela SOS sem resposta, min» para 0 e for dormir, e o bot abrir uma janela de ajuda, ele esperará até de manhã. É melhor deixar entre 10 e 15 minutos e configurar o Telegram: assim você saberá do problema imediatamente e, se não puder responder, o bot decidirá sozinho.

> [!done] Agora você sabe como definir a ordem das portas, o que considerar uma batalha ruim e como o bot cura os feridos. A seguir — Telegram e as janelas que pedem a sua ajuda. [Próxima seção →](#9)

## Assistente de regras: «Regras e interceptações»

A terceira aba do "Assistente de regras". Na primeira você definiu o **pack principal** de cada sala, na segunda — como o bot se comporta em caso de emergência. Aqui você ensina a ele as **exceções**: «normalmente use o pack principal, mas se acontecer isto — faça diferente». Cada exceção dessas é chamada de **regra**. E uma "interceptação" é quando a regra "intercepta" a escolha do pack principal e coloca o seu.

A regra é sempre lida da mesma forma: **«se [condição] — então [ação]»**. Por exemplo:

- :heart-pulse: «Se o PV de Araji estiver abaixo de 50% — use o pack com o curador Sigurd».
- :swords: «Se na sala estiverem Angus, Sylva e Verdok — use este pack».
- :door-open: «Se o PV de Araji estiver abaixo de 30% — não entre no «Fogo»».
- :users: «Se na sala estiverem Angus, Avalon e Eden — pare e pergunte a mim».

![Aba «Regras e interceptações»: filtros de elementos, lista de regras com ícones, packs e alternadores](images/rules_intercepts.png)

As regras de cada elemento são próprias: «Terra», «Água», «Fogo» e «Misto» têm listas separadas. Quando o bot entra na porta de «Fogo», ele analisa apenas as regras de «Fogo». Assim como nas outras abas, **nada é salvo até você clicar em «Salvar configurações»**, e o bot lê as regras apenas uma vez, quando você clica em «Começar o farm».

> [!note] Você não precisará escrever muitas das regras. Se a opção «O bot decide sozinho» estiver ativada, o bot **memoriza sozinho** os packs bem-sucedidos após um recuo e adiciona "regras douradas". Elas aparecerão nesta mesma lista (mais sobre elas abaixo). Suas próprias regras são necessárias quando você já sabe que "não se deve fazer assim" ou "nesta situação específica é preciso usar exatamente este pack".

### Quais tipos de regras existem

A condição de uma regra é uma de três, e a ação também é uma de três. Juntas, elas formam os tipos comuns:

- :heart-pulse: **Resgate por PV ou por energia.** A condição é "PV (ou energia) de determinado titã abaixo de N%", a ação é usar outro pack. Na lista fica o ícone **«CURA»** (por PV) ou **«ENERGIA»**. É assim que se faz a cura: quando o titã está ferido, usa-se o pack com curador.
- :swords: **Contra estes inimigos.** A condição é "todos estes inimigos estão na sala", a ação é usar seu pack. Ícone **«INIMIGOS»**. Os inimigos podem ser escolhidos entre os 13 que o bot reconhece na Masmorra.
- :door-open: **«Skip» — proibição.** A condição é "PV ou energia do titã abaixo de N%", a ação é não usar este titã e não entrar nesta sala. Ícone **«PULAR»**, à direita a indicação «Pular a sala».
- :users: **«Perguntar a você».** Qualquer condição, e a ação é não decidir sozinho, mas chamar você. À direita a indicação **«Perguntar a você»**, e o ícone depende da condição («PV», «ENERGIA», «INIMIGOS»). Quando ela disparar, o bot abrirá a janela «Nenhum pack adequado» e esperará sua resposta. Se você não responder no tempo definido na "Auto-tática", ele decidirá sozinho.

O ícone "PV" (em vez de «CURA») significa que a condição é por PV, mas a ação é «Perguntar a você». Se não houver condição alguma, não há ícone, e abaixo do nome está escrito «Sem condição — a regra nunca dispara».

Agora sobre o «Skip», porque ele faz dois trabalhos ao mesmo tempo. Exemplo: no «Fogo» existe a regra "Araji, PV abaixo de 30%".

1. **Porta.** Enquanto Araji tiver menos de 30%, o bot não irá para o «Fogo» e escolherá outra porta. Se todas as portas forem proibidas, o bot pegará a primeira na ordem.
2. **"Lista negra".** Nesta sala Araji não será colocado: qualquer pack que o contenha será descartado pelo bot, que pegará o próximo. Se até o pack **principal** contiver o titã proibido, não haverá o que colocar — o bot parará e abrirá a janela «Nenhum pack adequado».

> [!warning] O «Skip» não pode ser feito por inimigos. O bot descobre os inimigos **somente após** entrar na porta, portanto não pode escolher a porta com base neles. Na janela da regra para «Por inimigos», a caixa de seleção «Skip» fica indisponível. Se quiser evitar uma sala com determinados inimigos, coloque a regra «Perguntar a você», e a decisão será sua.

### Em qual ordem o bot verifica as regras

Quando a batalha começa, o bot percorre as regras da sala **nesta ordem**:

1. **«Skip».** Primeiro o bot monta a "lista negra" de titãs: quem foi proibido por uma regra «Skip» que disparou. Um pack com tal titã não servirá, mesmo que a própria regra o peça (isso é chamado de veto: a proibição é mais forte que qualquer regra).
2. **Resgate.** Regras em que a condição contém PV ou energia do titã. Incluem-se aqui também as regras "contra inimigos, quando Araji < 50% de PV" (inimigos mais PV): elas são verificadas logo aqui, **antes** das regras normais sobre inimigos.
3. **Contra inimigos.** Regras em que a condição contém apenas inimigos.
4. **Pack principal** da sala — se nada servir.

Dentro de cada grupo, o bot vai **de cima para baixo** e pega a primeira regra que disparar. É por isso que as setas são necessárias: se duas regras sobre inimigos servirem ao mesmo tempo, vencerá a que estiver mais acima. Já a regra de "Resgate" é sempre mais forte que "Contra inimigos", não importa onde estejam na lista. Regras **desativadas** não participam da verificação.

As condições são comparadas com o que o bot sabe sobre seus titãs (ele obtém o PV e a energia na tela de seleção de equipe e após as batalhas). Se o bot ainda não viu a vida do titã, ele a considera cheia, e a regra "abaixo de N%" não disparará. Se houver vários titãs na condição (isso acontece em regras memorizadas pelo próprio bot), **todas** as condições devem ser cumpridas ao mesmo tempo. Com inimigos é o mesmo: a regra só disparará se **todos** os listados estiverem na sala.

### Lista de regras: o que há na linha

No topo — «Regras ativas» e uma placa cinza com o número de regras, à direita a dica: «Escolha um elemento para mudar a ordem» (quando todas são mostradas) ou «A regra mais acima na lista é verificada primeiro» (quando um elemento está selecionado). Abaixo ficam os botões de filtro «Tudo», «Terra», «Água», «Fogo», «Misto» e o botão «Nova regra». Abaixo deles, os cabeçalhos das colunas "№", «Condição», «Ação», «Lig.».

Em cada linha, da esquerda para a direita:

- **Número** — posição na lista do seu elemento. Quanto menor o número, mais cedo a regra é verificada. Quando **um** elemento está selecionado, ao lado do número aparecem as setas «Subir» e «Descer». Se «Tudo» estiver selecionado — não há setas: os elementos são mostrados em sequência e não competem entre si.
- **Ícones** — elemento da sala e tipo de regra («CURA», «PV», «ENERGIA», «INIMIGOS», «PULAR»).
- **Nome** e a linha cinza abaixo — a condição em palavras, por exemplo «Araji: PV abaixo de 50%» ou «Inimigos na sala: Angus, Sylva».
- **Ação** — seta e quadrados dos titãs do pack (da esquerda para a direita, como no jogo) com a legenda «troca de pack». Ou a placa «Perguntar a você» / «Pular a sala».
- **Alternador «Lig.»** — ativar ou desativar a regra.
- **Lápis** «Editar» e **X** «Excluir».

Se não houver regras, no lugar da lista estará escrito: "Não há regras. Clique em «Nova regra» — ou o bot memorizará a regra sozinho após um recuo."

### Alternador, setas, X e «Limpar»

- :check: **Alternador.** Uma regra desativada fica opaca, mas **permanece na lista**, e o bot simplesmente a ignora. Esta é a melhor maneira de "remover uma regra temporariamente": não é preciso montar o pack novamente. Ao iniciar, a linha `[ПРАВИЛА] Выключено правил: N, бот их пропускает.` aparecerá no log.
- :chevron-up: **Setas «Subir» e «Descer»** trocam a regra de posição com a vizinha. Elas são necessárias quando duas regras do mesmo grupo podem servir ao mesmo tempo e importa qual será verificada primeiro.
- :x: **X «Excluir».** Abaixo aparecerá a notificação "Regra «…» excluída" com o botão **«Desfazer»**. Enquanto a notificação estiver na tela, a regra pode ser restaurada para o mesmo lugar.
- :trash-2: **«Limpar todas as regras»** exclui apenas o que está **visível agora**. Se «Água» estiver selecionada — as regras de água serão excluídas; se «Tudo» estiver selecionado — todas. Primeiro o bot perguntará: «Excluir todas as regras?» e escreverá quantas e de quais tipos (botão «Excluir todas»). Depois haverá também a notificação «Regras excluídas: N» com o botão «Desfazer».

Todas essas ações alteram apenas a página. Elas entrarão nos arquivos após clicar em «Salvar configurações», e **apenas os elementos em que algo mudou** serão gravados. Se você sair da página sem salvar, a janela perguntará «Salvar alterações?».

> [!tip] Se tiver dúvidas se deve excluir uma regra ou não, é melhor desativá-la pelo alternador. Para as regras que o bot memorizou sozinho, há ainda outro motivo (veja abaixo): o bot não mexe nem recria regras desativadas, enquanto uma regra excluída pode aparecer novamente.

### Janela «Nova regra» passo a passo

Clique em «Nova regra» (ou no botão «Condição» na primeira aba, na parte inferior do card da sala). A janela se abrirá. Se um elemento estiver selecionado, ela o sugerirá imediatamente. O lápis na linha abre a mesma janela com o título «Editar regra».

![Janela «Nova regra»: elemento e nome, três gatilhos, campos de condição, ação e equipe](images/rule_editor.png)

1. **Escolha o elemento no campo «Elemento da sala».** A regra funcionará apenas lá. O elemento determina quais titãs podem ser escolhidos: na «Terra» apenas os de terra, na «Água» apenas os de água, e no «Misto» quaisquer titãs. Se alterar o elemento mais tarde — a janela ajustará a seleção sozinha.
2. **Nomeie a regra (opcional).** O campo «Nome da regra» pode ser deixado em branco: assim o nome será formado a partir da condição, por exemplo «Araji: PV abaixo de 50%». Esse nome o bot escreverá no log quando a regra disparar.
3. **Escolha o «Gatilho»** — o que o bot deve observar: «Por PV», «Por energia» ou «Por inimigos».
   - «Por PV» e «Por energia»: escolha **«Titã»** e digite um número no campo «PV abaixo de, %» (ou «Energia abaixo de, %») de 0 a 100. O padrão para PV é 35, para energia é 100. Se digitar algo que não seja um número ou um valor fora dos limites, o campo ficará vermelho e abaixo dele aparecerá «Um número de 0 a 100».
   - «Por inimigos»: marque na grade «Inimigos perigosos na sala» todos os que devem estar **juntos**. Ao lado será exibido «· escolhidos: N». Se ninguém for escolhido — não será possível salvar.
4. **Escolha a «Ação ao disparar».** Existem duas caixas de seleção excludentes: "Parar e perguntar a mim" e «Proibir a entrada na sala (Skip)». Se nenhuma for marcada, a regra **colocará um pack**.
5. **Exigir teste prévio dos titãs (opcional).** A regra disparará apenas se os titãs escolhidos (de 1 a 5, de quaisquer elementos) já tiverem lutado nesta execução. Por exemplo, o pack pede Sigurd, mas você não quer usá-lo antes que ele tenha lutado ao menos uma vez. O X ao lado remove o teste prévio. O teste prévio existe apenas em regras que definem um pack. Após uma pausa suave e uma luta manual, o bot esquece o estado dos titãs, e o teste começa do zero.
6. **Escolha a «Equipe para esta regra».** Clique em «Escolher equipe» e na janela «Monte a equipe» defina **de 3 a 5 titãs** (da mesma forma que para o pack principal). Para «Perguntar a você» e «Skip» não é necessária uma equipe, onde estará escrito «Esta ação não precisa de equipe».
7. **Clique em «Salvar regra».** Enquanto o botão estiver cinza, a parte inferior da janela mostrará o que está faltando: «Escolha uma equipe: de 3 a 5 titãs», «Escolha pelo menos um inimigo» ou «Corrija o número: de 0 a 100». «Cancelar» fecha a janela sem alterações.

A nova regra vai para a **primeira posição** do seu elemento, e a regra alterada permanece na sua posição (se você mudou o elemento, irá para a primeira posição no novo). Ela entrará no arquivo, assim como tudo o mais, após clicar em «Salvar configurações». Se você abriu a janela pelo botão «Condição» da primeira aba, após salvar aparecerá a notificação "Regra «…» adicionada à aba «Regras e interceptações»".

> [!note] Uma regra que o bot memorizou sozinho pode ser aberta com o lápis e editada. Tudo o que não é visível na janela (por exemplo, "tolerância a perdas" ou uma condição extra de PV) **será mantido como está**. A janela mostrará essa condição em uma linha cinza "Ainda na condição (será mantido como está): …".

### Regras que o bot memorizou sozinho

Se a opção «O bot decide sozinho» estiver ativada, aparecerão na lista regras que não foram escritas por você. Elas são identificadas pelo nome:

- :refresh-cw: **«Auto: Angus + Sylva na sala»** — o bot recuou de uma luta ruim, jogou novamente com outro pack e este conseguiu vencer. O bot memorizou: "contra estes inimigos, use este pack". Abaixo do nome está escrito «Memorizada pelo bot após um recuo» (ou «Seu pack após um recuo, memorizado pelo bot», se o pack foi escolhido por você na janela SOS). Se o pack perdeu por causa de uma condição (por exemplo, "Araji abaixo de 50%"), ela é adicionada à condição. Essa regra vai para a primeira posição.
- :star: **«Dourada: Angus + Sylva na sala»** — «O pack venceu esses inimigos muitas vezes». Ao iniciar, o bot analisa o histórico e pega um pack que, contra essa composição de inimigos, realizou **5 lutas ou mais** e venceu **80% ou mais**. O pack principal, packs de regras de resgate e seus packs de reserva não entram nas regras "douradas".

No arquivo, essas regras são nomeadas de forma diferente ("Anti-pack contra: …", "Regra dourada contra: …"), e é assim que são gravadas no log: `[ОБУЧЕНИЕ] Новое правило '…': пак […]. Сохранено на 1-е место.` A janela simplesmente as exibe de forma curta e compreensível. Se você renomear a regra — verá o seu próprio nome.

O que é útil saber sobre essas regras:

- **O bot não duplica regras.** Uma regra com a mesma condição não é criada uma segunda vez: o pack da regra antiga é alterado e ela sobe para o topo.
- **Nem todo recuo bem-sucedido é memorizado.** Se a luta ruim aconteceu apenas porque o titã entrou nela ferido, mas com 100% de PV tudo ficaria bem ("os inimigos não têm nada a ver com isso"), a regra não é criada.
- **O bot não mexe em regras desativadas:** não as ativa nem as sobrescreve. Ele não memorizará o mesmo pack novamente, e uma regra "dourada" desativada não voltará.
- **Regras excluídas podem voltar.** A "regra dourada" será criada novamente na próxima inicialização, a menos que haja outra regra contra esses inimigos. Se não gostar — desative-a pelo alternador. A regra "Auto" será recriada pelo bot se o recuo terminar da mesma forma novamente.
- **Enquanto a janela estiver aberta, o bot pode gravar uma nova regra no arquivo.** Quando você clicar em «Salvar configurações», a janela relerá o arquivo e colocará essas novas regras no topo sem perder nada. Se der uma olhada na aba sem mudar nada, verá a lista atualizada do disco.

> [!warning] Se o arquivo de regras do elemento estiver danificado (por exemplo, foi editado manualmente e houve um erro de recuo de texto), a janela exibirá, por exemplo para a água: «O arquivo de regras está danificado: bot_data/rules/water.yml — a janela não altera as regras deste elemento». Os outros elementos continuarão funcionando. Não é necessário editar o arquivo manualmente: clique em «Enviar log ao autor» na tela principal e descreva o ocorrido.

> [!tip] Por onde começar? Não escreva nada com antecedência. Jogue algumas dezenas de salas com a opção «O bot decide sozinho» ativada e dê uma olhada aqui: o bot já terá memorizado várias regras. Desative as ruins e suba as boas com as setas. Adicione suas próprias regras quando vir um problema recorrente: "Araji vive andando ferido" — regra de resgate; "esta composição de inimigos sempre mata meu pack principal" — regra contra inimigos.

> [!done] Agora você sabe como ensinar exceções ao bot e entende por que ele escolhe exatamente este pack. A seguir — Telegram e as janelas que pedem sua ajuda. [Próximo capítulo →](#10)

## Quando a batalha vai mal: janelas SOS

Na maioria das vezes, o bot resolve tudo sozinho. Mas às vezes ele se depara com uma situação em que não dá para continuar sem uma pessoa: a batalha foi vencida, mas o custo foi alto demais, ou as regras não fornecem nenhum pack adequado. Nesses casos, o bot **para e chama você** com uma janela no meio da tela. SOS é um sinal de socorro, como o de um navio: "preciso de ajuda". Enquanto você não responder, o bot não clica em nada e fica aguardando (mas não para sempre, veja mais abaixo).

Existem três janelas, e cada uma é para um caso específico:

- :triangle-alert: **«Intervenção necessária»** — a batalha terminou, mas o resultado foi ruim. Esta é a janela principal, é a que aparece com mais frequência.
- :users: **«Nenhum pack adequado»** — o bot ainda não começou a batalha: as regras não dão um pack para esta sala.
- :check: **«O pack deu conta»** — você mesmo escolheu outro pack, ele venceu, e o bot pergunta se deve memorizá-lo.

![Janela «Intervenção necessária»: motivo, sala, inimigos, seu pack com barras de HP e três botões](images/sos_window.png)

> [!note] Quando a janela aparece: se «O bot decide sozinho» estiver **desativado** (padrão), a janela se abre após **cada** batalha ruim. Se estiver ativado, o bot tenta primeiro resolver sem você e só chama quando não consegue: a batalha foi manual (Angus), a janela de resultado não pôde ser lida, você escolheu o pack, no bot na sala já recuou tantas vezes quanto permitido, ou não há pack de reserva. O que é uma "batalha ruim" e como configurá-la — nas seções sobre «Base e salas» e "Auto-tática".

### Janela «Intervenção necessária»

No topo — resumo: «A batalha foi mal. O que fazemos?». Abaixo — os fatos, para você decidir sem precisar olhar o log:

- **«Motivo».** O que exatamente o bot não gostou. Por exemplo: "Limite crítico! Araji tem 12% de HP (limite: 40%)", "Delta de perdas excedido! Rigel perdeu 45% de HP (tolerância: 30%)", "FATAL! Iyari morreu…", "Grandes perdas no pack!…" ou "Não foi possível ler a janela de resultado: não foi encontrado…". Os nomes dos titãs aparecem no idioma do programa.
- **«Sala».** Elemento da porta e número da sala: "Fogo · sala 54".
- **«Inimigos».** Quadrados dos titãs contra os quais a batalha ocorreu. Se os inimigos não forem reconhecidos, a linha não aparecerá.
- **«Seu pack».** Cada titão com sua barra de vida e a inscrição "HP antes da batalha → HP depois": "36% → 12%". Se o HP do titão estiver abaixo do seu limite de pânico (geral ou pessoal), a barra e o número ficam **vermelhos**. Se acabou de entrar na batalha já ferido e saiu quase sem HP, você verá isso imediatamente.
- **Timer.** Na parte inferior: "Sem resposta, o bot decidirá sozinho em 9:41". O último minuto fica amarelo, depois "O bot está decidindo…". Se na "Auto-tática" estiver definido como 0, a linha não aparece: o bot esperará por você indefinidamente.

Botões (da direita para a esquerda, o principal é o mais à direita):

1. **«Reverter a batalha»** (azul). Jogar novamente esta batalha com outro pack. A janela se esconderá e «Monte a equipe» será aberta com o pack atual; altere os titãs e clique em «Reverter com este pack». O que acontecerá em seguida está na seção «Recuo» abaixo. Se você fechar «Monte a equipe» sem escolher nada, a janela SOS voltará, nada será perdido.
2. **«Ignorar»** (cinza). Aceitar a batalha como está: a sala é contabilizada, o bot continua com o HP restante. Adequado quando as perdas são aceitáveis para você (por exemplo, o titão já entrou ferido e no geral está tudo bem).
3. **«Jogar manualmente»** (cinza). O bot não clica em nada e você mesmo passa essa sala no jogo. O bot espera até você voltar ao corredor: a bandeira da porta deve ficar visível por 2 segundos seguidos. Se a última tela foi a janela de resultado, a sala é contabilizada; se você recuou sem vencer, não. Se fechou a janela de resultado sem jogar novamente, a batalha é contabilizada como foi. Após jogar manualmente, o bot esquece o HP dos titãs e as composições nos slots (relerá sozinho na tela de seleção de equipe) e continua jogando sozinho.

> [!warning] Uma batalha onde a **ult manual do Angus** foi usada não pode ser revertida: na janela de resultado não há o botão "Tentar Novamente". Em vez de «Reverter a batalha», a janela mostrará o botão vermelho **«Parar o bot»**, restando apenas «Ignorar» ou «Jogar manualmente».

### Recuo: o que o bot faz após a sua escolha

A janela se fechou, o comando foi enviado ao bot. A partir daí ele faz tudo sozinho, e no registro (log) isso fica visível pela tag `[ОТКАТ]`:

1. Clica em **"Tentar Novamente"** na janela de resultado e aguarda o carregamento da batalha (às vezes leva de 20 a 30 segundos ou mais, por isso ele espera até um minuto).
2. Coloca a batalha **em pausa** (uma vez) e clica em **"Recuar"**.
3. Retorna ao corredor, entra na **mesma sala** e escala o seu novo pack.

Se a batalha for ruim novamente — a janela voltará. Se for boa — é aqui que aparece a janela «O pack deu conta» (detalhada abaixo).

Se a conexão com o jogo for perdida (a imagem de "carregando" não termina), o bot não desiste: espera o jogo por até 15 minutos e registra isso no log. Somente se o recuo falhar completamente, o bot salva uma captura de tela em `bot_data/debug/`, entra em pausa suave e envia uma mensagem para você no Telegram. Mais detalhes na seção sobre solução de problemas.

### Janela «Nenhum pack adequado»

Aparece quando o bot já escolheu a porta e olhou para os inimigos, mas **não há nada para escalar**. Acontece por dois motivos, ambos decorrentes das suas regras:

- a regra "Me perguntar" foi acionada (ela serve exatamente para isso);
- o pack principal da sala contém um titão proibido pela regra «Skip» (o bot escreve algo como «ФАТАЛЬНО: Все паки отбракованы…»).

A janela pergunta: «As regras não dão um pack para esta sala. O que fazemos?». Ela contém os mesmos campos «Motivo», «Sala» e «Inimigos», mas sem barras: a batalha ainda não aconteceu. Botões:

- **«Montar um pack novo»** (azul) — abre «Monte a equipe», onde o botão se chama «Aplicar». O bot escalará os titãs selecionados e **memorizará imediatamente o pack como uma regra** "contra estes inimigos" (não há verificação antes de salvar aqui, preste atenção).
- **«Jogar manualmente»** — você passa a sala sozinho, o bot espera no corredor. A sala é contabilizada se você vencer.
- **«Parar o bot»** (vermelho) — o bot escreve o resumo da sessão e se desliga.

O botão «Ignorar» não existe aqui: não há o que aceitar, pois não houve batalha.

### Janela «O pack deu conta»

Esta janela aparece quando a batalha é vencida por um pack que **você escolheu** (através de «Reverter a batalha» ou «Tentar outro», na janela ou no Telegram). Se o pack de reserva foi escolhido pelo próprio bot e deu certo, o bot o memorizará sozinho e não perguntará nada.

Dentro — a sala, os inimigos (da última janela SOS, se ela ocorreu há não mais de 15 minutos) e o seu pack com o HP após a batalha. Pergunta: «O pack em teste venceu. Salvá-lo como regra contra estes inimigos?». Botões:

- **«Salvar pack»** (verde) — o bot memorizará a regra "contra estes inimigos" com este pack. Na lista de regras, ela aparecerá como "Auto: …" ou «Seu pack após um recuo, memorizado pelo bot».
- **«Tentar outro»** — abre novamente «Monte a equipe» e faz o recuo: o bot jogará novamente a batalha vencida com outro pack.

Se você não responder — após o tempo do timer (legenda "Sem resposta, o bot salvará o pack sozinho em…"), o bot salvará o pack sozinho, como se você tivesse clicado em «Salvar pack».

### O "X" da janela e «Parar o bot?»

As janelas não têm uma opção de "apenas fechar": se você fechar a janela, o bot continuará esperando uma resposta. Por isso, o botão "X" pergunta: **«Parar o bot?»**. Se responder «Parar o bot» — o bot encerrará, escreverá o resumo e o enviará no Telegram. Se ele não responder em 10 segundos, o programa o interromperá sozinho. Na janela «O pack deu conta», a pergunta é diferente: a parada lá é a mesma do "PARAR F10", **o resumo da sessão não será enviado ao Telegram**. Se mudou de ideia — clique em «Cancelar», a janela permanecerá.

### O que acontece se você não responder

Sempre que você não responder dentro do tempo definido em "Auto-tática" («Tempo da janela SOS sem resposta, min»: padrão 10, até 60, 0 — esperar sempre), o bot registra `[ТАКТИКА] Ответа нет 10 мин. Решаю сам.`, a janela se fecha e você recebe uma mensagem no Telegram informando que o bot decidiu sozinho. Isso funciona mesmo com «O bot decide sozinho» desativado. A decisão depende da janela:

- **«Intervenção necessária»:** se houver um pack de reserva e a batalha puder ser revertida (não for Angus, as tentativas na sala não tiverem acabado) — faz o **recuo** e usa o pack de reserva; caso contrário, se todos os titãs estiverem vivos — a batalha é **aceita** («Ignorar»); caso contrário (alguém morreu ou não foi encontrado na janela) — entra em **pausa suave**.
- **«Nenhum pack adequado»:** se houver um pack de reserva sem feridos e sem titãs proibidos — o bot o escala **e não memoriza a regra**; se não houver — entra em **pausa suave**.
- **«O pack deu conta»:** o pack é salvo.

A pausa suave é como o botão "Pausa F9": o bot espera no corredor até você clicar em «Continuar».

> [!tip] Respondeu no mesmo instante em que o bot já havia decidido sozinho? Não tem problema: o bot ignorará a resposta antiga e escreverá `[ЛОГИКА] Пропускаю ответ ...: он пришёл на прошлое окно.`

### Responder pelo Telegram

Se o Telegram estiver configurado, **a mesma pergunta** chega no chat: captura de tela do jogo, legenda (sala, inimigos, motivo, pack com HP) e botões. Você pode responder onde for mais conveniente: se responder no chat — a janela no computador se fechará sozinha, e vice-versa.

- **«Reverter (Montar pack)»** (verde) — o bot pedirá para você escrever no chat os nomes de **3–5 titãs** separados por vírgula ou espaço, mostrará quem ele reconheceu e perguntará "Tudo certo?" («Confirmar pack» / «Escrever outro»). Para a batalha manual do Angus e para «Nenhum pack adequado», em vez deste botão haverá o vermelho «Parar o bot».
- **«Jogar manualmente»** e **«Ignorar (Continuar)»** — o mesmo que na janela. Em «Nenhum pack adequado», não há o botão «Continuar».
- A mensagem «O pack deu conta» só chega no Telegram se o pack tiver sido enviado por lá também: «Confirmar e Salvar» ou «Reverter e Tentar Novamente».

Se a internet cair, a mensagem será enviada mais tarde (o bot tenta novamente), enquanto a janela no computador permanece aberta. A configuração do Telegram está na seção dedicada a ele.

### Mini-barra e janelas SOS

Se a janela do programa estiver minimizada na mini-barra, a janela SOS aparecerá **no centro do jogo**. A mini-barra fica vermelha nesse momento, e o seu botão «SOS» traz a janela perdida para a frente do jogo.

> [!tip] Como escolher? Olhe para «Seu pack». Se um titão entrou ferido e perdeu vida, mas os outros estão bem — geralmente «Ignorar» é suficiente. Se os inimigos são conhecidos e muito mais fortes — escolha «Reverter a batalha» com outro pack. Se não entendeu nada — escolha «Jogar manualmente». O recuo custa tempo (a batalha precisa ser recarregada, o que leva de 20 a 30 segundos ou mais), enquanto «Ignorar» não custa nada.

> [!done] Agora você sabe o que significa cada janela SOS, o que cada botão faz e o que o bot fará sem você. A seguir — como o bot decide sozinho enquanto você não está por perto. [Próxima seção →](#11)

## Como o bot decide sozinho

Na seção sobre janelas de SOS, você viu que o bot chama você após uma batalha ruim. Mas ele nem sempre chama: se você ativar «O bot decide sozinho» (aba «Base e salas», seção 7), o bot **primeiro tenta resolver sem você** e só pede ajuda quando não consegue. Aqui explicaremos como ele pensa. Sem fórmulas: apenas as perguntas que o bot faz a si mesmo e exemplos.

Imagine um parceiro experiente sentado ao seu lado no celular. A batalha correu mal e você saiu para tomar um chá. Ele não vai ficar sentado esperando. Ele vai lembrar o que já funcionou contra aqueles inimigos, jogar a batalha novamente com outra formação e registrar o que deu certo. É exatamente assim que o bot se comporta. Só que ele tem regras para não fazer besteira.

> [!note] Por padrão, «O bot decide sozinho» está **desativado**, e nada do que é descrito abaixo acontece nesse modo: após cada batalha ruim, o bot simplesmente abre uma janela de SOS. Se você ativar a chave e clicar em «Salvar configurações», isso passará a valer a partir do próximo «Começar o farm». O que exatamente pode ser ajustado já analisamos na seção 8 («Autotática e PV»), e aqui falaremos sobre **o que o bot faz com esses números**.

### Batalha ruim: o que o bot faz passo a passo

1. **Percebe que a batalha foi ruim.** Alguém morreu ou ficou abaixo do limite de pânico, perdeu mais do que a tolerância ou três titãs enfraqueceram de uma vez (seções 7 e 8). No log surge a linha `[ТАКТИКА] Плохой бой: ...` com o motivo.
2. **Verifica se pode fazer o recuo sozinho.** Não é possível em quatro casos: a batalha foi manual (habilidade suprema do Angus, que não tem o botão "Jogar novamente" na janela de resultado), a janela de resultado não pôde ser lida, o pack foi escalado por **você** (então a decisão também é sua) ou o bot já gastou as tentativas nessa sala. Se não puder, a janela SOS abre e o log registra `[ТАКТИКА] Сам не откатываю: ... Спрашиваю вас.` com o motivo.
3. **Procura uma equipe reserva.** Como — na próxima seção. Se não houver nenhuma adequada — abre a janela SOS novamente.
4. **Recua e joga novamente.** Executa os mesmos passos de `[ОТКАТ]` que seriam feitos após sua escolha ("Jogar novamente", pausa, "Recuar"), escalando a equipe reserva na mesma sala. No log aparece `[ТАКТИКА] Откатываю бой сам и переиграю паком ... (взят: ...)`.
5. **Analisa o resultado.** Se a equipe reserva der conta — o bot prossegue e, via de regra, memoriza o pack (detalhes abaixo). Se a batalha for ruim novamente — faz uma segunda tentativa, e assim por diante até esgotar as tentativas («Equipes reserva a tentar por sala», padrão 2, máximo 3). Depois disso, ele chama você.

> [!tip] O bot recua a batalha inteira a cada vez, em vez de "corrigir em tempo real". O recuo custa tempo (a batalha precisa ser recarregada, o que pode levar de 20 a 30 segundos ou mais), portanto ele evita tentativas em vão: veja abaixo como ele escolhe o pack.

### De onde o bot tira a equipe reserva

Ele percorre a lista de cima para baixo e pega a **primeira adequada**:

1. **Suas «Equipes reserva»** — aba «Base e salas», card da sala. São pegas na ordem em que você as organizou. No log essa fonte é chamada de "sua lista de equipes reserva".
2. **Packs das regras deste elemento** — no log, "regras do elemento". Possui sua própria ordem interna: primeiro as regras "contra estes inimigos", depois packs que já venceram exatamente esses inimigos (os melhores em PV restante primeiro), depois os demais "anti-packs", e por fim todo o resto, incluindo o pack principal da sala.
3. **Histórico de batalhas** — no log, "histórico de batalhas". Esta é a última fila, e são considerados apenas os packs que já venceram esses inimigos. O bot lembra das batalhas das últimas 20 execuções.

O que o bot **nunca escalará** como reserva:

- um pack que já perdeu nesta sala (para não repetir o erro);
- um pack que "perde para estes inimigos": da última vez contra eles a batalha recuou por culpa dos inimigos, e o pack não tem mais vitórias do que derrotas. Um único fracasso **não estraga um bom pack**: se ele venceu contra esses inimigos cinco vezes e perdeu uma, o bot ainda o utilizará;
- um pack com um titã proibido por uma regra "Skip";
- um pack com um titã cujos PV já estão **abaixo do limite de pânico**: o bot não o mandará para a batalha em uma derrota certa;
- do histórico — um pack que contém um titã não especificado por você em nenhum lugar (nem nos packs, nem nas regras). No histórico permanecem packs de regras excluídas há muito tempo, e o bot não os ressuscita.

Além disso, existem os packs "perigosos": aqueles em que um titã ferido, a julgar pelas batalhas passadas, não sobreviverá até o final da luta. O bot os escolhe **em último caso**, apenas se não houver nada melhor. Como ele determina isso — veja na seção "Titã ferido" abaixo.

O motivo pelo qual o bot não escolheu determinado pack pode ser visto no log: `[ТАКТИКА] Не беру запасной пак ...` seguido do motivo. Se as reservas acabaram e a batalha continua ruim, isso não é uma falha, mas sim um honesto "não sei mais o que escalar".

### Memorizar ou não: a regra «Auto: ... na sala»

A equipe reserva deu conta. O bot registra isso na regra "contra estes inimigos — escale este pack", e na próxima vez que encontrar a mesma formação inimiga, irá escalá-lo imediatamente. Na lista, esta regra aparece como «Auto: ... na sala» e vai para a primeira posição (seção 9). No log: `[ТАКТИКА] Запасной пак ... справился. Запоминаю его против этих врагов.`

Mas acontece de **não ser possível memorizar**. Exemplo: Araji entrou na batalha com 36% de vida e caiu para 5%. O pack principal não tem culpa: se Araji estivesse saudável, a batalha teria corrido bem. Se o bot registrasse a regra "contra estes inimigos use a reserva", ele começaria a escalar o pack reserva onde o principal se sai muito bem, desperdiçando a sua força. Por isso o bot verifica: **"com 100% de PV em todos, a batalha teria sido ruim?"**. Se não — significa que os inimigos não têm culpa, o auxílio foi pontual e a regra não é criada.

No log isso fica visível imediatamente: `[ТАКТИКА] Враги ни при чём: в бой вошли раненые ...` e потом `Правило не запоминаю: это была разовая помощь раненым титанам`.

Tampouco será possível memorizar em outros três casos:

- se o bot não reconheceu os inimigos (`[ОБУЧЕНИЕ] Враги не распознаны — правило не сохраняю`): a regra "sem inimigos" seria acionada em qualquer sala;
- se você desativou a regra com o mesmo pack na chave seletora: o bot não altera regras desativadas;
- se o pack foi escolhido por você mesmo: nesse caso a decisão cabe à sua janela «O pack deu conta» (seção 10).

### Titã ferido: ajuda antecipada, e não após a batalha

A habilidade mais valiosa do bot é **evitar uma batalha ruim**, em vez de consertá-la depois. Enquanto está na tela de seleção de equipe, ele olha para a vida dos titãs e para o histórico: "como terminaram as batalhas com este pack nesta sala?". Para isso, o bot registra quantos PV um titã costuma **perder** em batalha com esse pack (média das últimas cinco batalhas, sendo necessárias pelo menos duas). Se os PV do titã ferido ao entrar menos a perda média **ficarem abaixo do limite de pânico**, o bot não arrisca e escala imediatamente um pack reserva, antes da batalha começar.

Exemplo: Araji com 36% de PV entra no elemento Fogo. Nas últimas batalhas ali ele costumava perder cerca de 29%. Conta: 36 − 29 = 7%, sendo que o limite de pânico é 40. A batalha quase certamente terminaria mal, então o bot escala um pack reserva, por exemplo com Moloch, **imediatamente**. Esta é uma ajuda pontual, e a regra não é memorizada.

Dois detalhes para o comportamento do bot fazer sentido:

- **A energia também é importante.** Se o titã atualmente tem uma quantidade de energia semelhante às batalhas anteriores (diferença não superior a 25%), o bot usa exatamente essas batalhas para a previsão. Araji com boa energia no elemento Fogo perde pouco PV, enquanto sem energia perde muito, e a previsão leva isso em consideração.
- **Uma batalha não é estatística.** Com menos de duas batalhas, o bot não confia na previsão e não altera nada.

O bot não substitui antecipadamente packs de regras de resgate ("se Araji estiver abaixo de 50% — escale Sigurd", seção 9): você os configurou justamente para titãs feridos, e a sua intenção é mais importante do que a previsão dele.

### Escolha da porta com base na vida

Se o bot estiver decidindo sozinho e houver **várias portas permitidas** visíveis no corredor, ele não escolhe apenas por ordem (seção 8, «Prioridade das portas»), mas considerando os feridos:

1. Primeiro ele entra na porta **onde o ferido será curado**: seja pela sua regra de resgate ou pela montagem automática de um pack de cura pelo próprio bot.
2. Uma porta na qual o titã ferido corra perigo, a julgar por batalhas anteriores, o bot **pula**, caso haja outra opção.
3. Caso contrário, segue a ordem normal.

Pode ser identificado pela linha `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`. Uma porta proibida por uma regra "Skip" nunca será aberta pelo bot. Como ele ainda não vê os inimigos atrás da porta, aqui ele se baseia no pack básico da porta.

### Pack de cura na sala "Mista"

Se um titã ferido puder ser curado e a sua regra de cura não tiver sido acionada, o bot **monta sozinho um pack de cura**: ele coloca o titã ferido na sala "Mista" e, se necessário, um curador saudável e carregado. Curam um de cada vez, os principais antes dos reservas, e aqueles que estiverem abaixo do limite de pânico não são curados. Todos os detalhes (o limite «Curar o titã se os PV estiverem abaixo de, %», «Quem tirar da equipe pelo ferido», o próprio Sigurd para Rigel) estão na seção 8. O ponto importante aqui é: trata-se da mesma **ajuda pontual** que uma equipe reserva de previsão. Nenhuma regra é criada após isso, e no resultado final ela é contabilizada separadamente ("packs de cura (montados pelo bot)").

### «Regras de ouro»: o bot aprende com todo o histórico

O bot toma todas essas decisões durante o jogo. Porém, as "regras de ouro" são calculadas **uma única vez, ao iniciar o farm**. O bot analisa o histórico de batalhas e procura um pack que tenha enfrentado a mesma formação de inimigos por **5 batalhas ou mais e vencido 80% ou mais**. Ele registra esse pack como a regra «Dourada: ... na sala» (seção 9). No log: `[ОБУЧЕНИЕ] ...: 'Золотое правило против: ...' — пак ... Сохранено на 1-е место.`.

Não se tornará uma regra de ouro:

- o pack principal da sala, packs de regras de resgate e suas «Equipes reserva» (servem para ajuda, não para todas as batalhas);
- packs de cura montados pelo próprio bot: necessários apenas enquanto o titã estiver ferido;
- um pack com um titã que não consta em seus packs nem em suas regras;
- um pack contra inimigos que já possuem uma regra existente (sua, «Auto» ou desativada).

As regras de ouro não existem enquanto «O bot decide sozinho» estiver desativado. Surgiu uma regra insatisfatória? **Desative-a na chave seletora**, sem excluir: se for excluída, ela retornará na próxima execução; se for apenas desativada, o bot não irá alterá-la.

### Se você não responder à janela SOS

Isso não é mais "o bot decide sozinho", mas sim "o bot decide por você" (seção 10, "O que acontece se você não responder"). Funciona mesmo com «O bot decide sozinho» desativado: quando atinge o tempo limite («Tempo da janela SOS sem resposta, min»), o bot recuará a batalha com uma equipe reserva, aceitará a batalha ou entrará em pausa suave. A cada ocorrência ele registra `[ТАКТИКА] Ответа нет N мин. Решаю сам.`, fecha a janela e envia uma mensagem no Telegram.

### Como saber o que o bot fez sem você

Ao final da sessão, no bloco «Resumo da sessão» (botão «Detalhes») e na linha `[ИТОГ]`, há contadores:

- **"recuos"**: quantas batalhas foram jogadas novamente no total;
- **"destes, sem você"**: quantos desses recuos o bot realizou sozinho, sem perguntar, tanto por previsão quanto por tempo limite;
- **"packs de cura (montados pelo bot)"**: quantas vezes ele curou o titã ferido com um pack de cura.

O mesmo resumo chegará ao Telegram: «Reversões: 6» (bot sozinho: 5). Se quase tudo for "sem você", o bot está se saindo bem. Se o número estiver crescendo e as regras de ouro não aparecerem, significa que os mesmos inimigos estão derrotando o seu pack principal repetidamente. Acesse a aba «Regras e interceptações» para verificar quais regras ele memorizou e considere se não é hora de alterar o pack principal.

> [!warning] O bot toma decisões com base no **histórico** e na previsão, sem prever o futuro da batalha. Ele pode errar: nos primeiros dias, com pouco histórico, a equipe reserva é selecionada quase ao acaso. Não se assuste se nas primeiras dezenas de salas «O bot decide sozinho» fizer recuos com mais frequência do que você gostaria. Quanto mais batalhas houver no histórico, mais precisa será a escolha.

> [!tip] Por onde começar? Configure ao menos uma ou duas **«Equipes reserva»** em cada sala (seção 7): assim o bot não procurará no escuro. Ative «O bot decide sozinho» e por alguns dias observe apenas as linhas com `[ТАКТИКА]` e o «Resumo da sessão». Se não gostar do que o bot está fazendo, basta desativar a chave seletora e tudo voltará a funcionar por janelas de SOS.

> [!done] Agora você entende quando e como o bot resolve as situações sem você, o que ele memoriza e quando pede ajuda. A seguir — Telegram: como receber mensagens quando não estiver perto do computador. [Próxima seção →](#12)

## Telegram

O bot pode enviar mensagens para você no Telegram enquanto estiver longe do computador: foi à cozinha, foi dormir, saiu para o trabalho. Se a batalha precisar da sua ajuda, uma captura de tela e botões aparecerão no chat. Pressionou o botão no celular — o bot fez exatamente o que você pediu. Se tudo estiver correndo bem, o bot fica em silêncio: as mensagens chegam **apenas em caso de problemas** e **uma vez ao final da sessão**.

O que você vai precisar: o aplicativo Telegram e cinco minutos. Só é necessário configurar uma vez.

> [!note] Telegram — opcional. Sem ele, o bot funciona da mesma forma, você apenas vê as janelas de SOS na tela do computador e não recebe o resumo da sessão. Mas se planeja deixar o bot rodando à noite, configure-o: assim você saberá de qualquer problema imediatamente, e não só de manhã.

### O que é necessário preparar

Você precisa de duas coisas, ambas obtidas no próprio Telegram:

- :send: **Token do bot** (a chave pela qual o programa acessa o seu bot). É uma longa sequência de números e letras, por exemplo `123456789:AAH…`. O token é fornecido pelo bot especial **@BotFather**.
- :user: **Chat ID** (número do chat). É o número pelo qual o Telegram sabe para quem entregar a mensagem: para você, e não para outra pessoa.

> [!warning] O token é como a senha do seu bot. Não o mostre a ninguém, não o envie em capturas de tela nem em e-mails (nem mesmo ao autor do programa). Tire a captura de tela da janela «Configurações do Telegram» enquanto o token estiver oculto por pontos.

### Passo a passo

1. **Crie o seu bot.** No Telegram, procure por **@BotFather** (o verdadeiro tem um selo azul de verificação ao lado) e toque em «Iniciar». Escreva `/newbot` para ele, crie um nome (qualquer um, só você o verá) e um nome de usuário que termine em `bot`, por exemplo `moi_titan_bot`. Em resposta, o BotFather enviará uma mensagem com o token: copie-o.
2. **Descubra o seu Chat ID.** Procure pelo bot **@getmyid_bot**, toque em «Iniciar» — ele responderá com a linha `Your user ID` e um número. Esse é o seu Chat ID, copie o número. Se esse bot não responder, há um caminho alternativo: escreva qualquer palavra para o **seu** bot do passo 1, abra no navegador o endereço `https://api.telegram.org/bot<твой токен>/getUpdates` (em vez de `<твой токен>`, insira o seu token) e encontre na resposta `"chat":{"id":` — o número logo após ele é o seu Chat ID.
3. **Toque em «Iniciar» no seu bot.** Procure o bot que você criou no passo 1 e toque em «Iniciar» (ou escreva `/start` para ele). Sem isso, o Telegram **não permitirá** que o bot envie mensagens primeiro para você. Essa é a causa mais comum para as mensagens não chegarem.
4. **Abra a janela no programa.** Clique no ponto do Telegram no painel à esquerda ou no botão **«Configurar Telegram»** na aba «Base e salas» (seção 7). A janela «Configurações do Telegram» será aberta.
5. **Preencha os campos.** Ative a opção «Enviar mensagens para o Telegram». No campo «Token do bot (do @BotFather)», cole o token; no campo «ID do chat», cole o número. O mais prático é usar o botão **«Colar»** ao lado do campo: ele pega o que você copiou. O token é exibido com pontos; o ícone de olho o revela para verificar se foi colado corretamente. O botão direito do mouse no campo também oferece a opção «Colar».
6. **Teste a conexão.** Clique em **«Testar o Telegram»**. Após alguns segundos, aparecerá à direita em verde «Mensagem enviada — veja o Telegram», e no chat com o seu bot — a mensagem «Teste de conexão: tudo funciona». Chegou — está tudo pronto.
7. **Salve.** Clique em **«Aplicar»** e, em seguida, na parte inferior da página, em **«Salvar configurações»**.

![Janela «Configurações do Telegram»: interruptor, campos de token e ID do chat, botões «Colar» e «Testar o Telegram»](images/telegram_window.png)

> [!warning] «Aplicar» apenas transfere os valores para a página «Master de regras», eles **não são gravados** no arquivo. Enquanto você não clicar em «Salvar configurações», a mensagem «Há alterações não salvas» permanecerá destacada na parte inferior, e o bot não saberá nada sobre o Telegram. Se você sair da página sem salvar, o programa perguntará «Salvar alterações?».

> [!tip] «Testar o Telegram» testa o que está escrito na janela no momento, mesmo que você ainda não tenha salvado nada. Portanto, teste **antes** de clicar em «Aplicar»: encontrou um erro — corrigiu — testou novamente. O teste roda em segundo plano, a janela não trava e você não precisará esperar mais de 20 segundos por uma resposta.

### Se o teste falhar

Abaixo do botão aparecerá uma linha vermelha «Não enviada: …» com o motivo. Os mais comuns:

- **«Preencha o token e o ID do chat»** — um dos campos está vazio.
- `Unauthorized` — o token é inválido: falta um caractere, há um espaço extra ou não foi copiado por inteiro. Cole novamente usando o botão «Colar».
- `chat not found` ou `Forbidden` — o Chat ID está incorreto ou você não tocou em «Iniciar» no **seu** bot (passo 3). Verifique ambos os pontos.
- **«falha de conexão com o Telegram»** — não há internet ou o Telegram não abre neste computador. Verifique se o Telegram (ou o site telegram.org) está funcionando no mesmo PC.

Se mesmo após a correção a mensagem não chegar, crie um novo bot no @BotFather (passo 1) e comece do zero: é mais rápido do que procurar um erro de digitação.

### Como saber se o Telegram está ativado

No painel à esquerda, o botão do Telegram possui um ponto: ao passar o mouse por cima, aparecerá a dica **«Telegram: ativado»** ou **«Telegram: não configurado»**. Ativado significa que o interruptor está ligado e ambos os campos estão preenchidos. Isso **não é um teste de conexão**: se o token é válido ou não, apenas o botão «Testar o Telegram» mostrará. O mesmo é visível na aba «Base e salas»: ao lado do botão «Configurar Telegram», acende em verde «Avisos SOS ativados» ou em cinza «Telegram não configurado». O ponto é atualizado automaticamente alguns segundos após salvar.

### Que tipo de mensagens chegam

O idioma das mensagens é o mesmo selecionado na janela do programa.

- :swords: **Janela SOS** — título «Precisamos da sua ajuda» (ou «Nenhum pack adequado»), captura de tela do jogo e legenda: sala, inimigos (contra quem estavam lutando), motivo, seu pack com barras de vida e energia. Botões na parte inferior. É a mesma pergunta da janela no computador (seção 10).
- :triangle-alert: **Alertas** — mensagem curta sem botões informando o que aconteceu e o que fazer. São elas: «Não foi possível reverter a batalha» (bot em pausa suave, olhe para a tela do celular), «Parece que o bot travou» (5 minutos sem mudar de sala) e uma mensagem semelhante quando não é possível iniciar a batalha (muito provavelmente sem conexão com o servidor do jogo), «A tela do PC está bloqueada» (o bot não vê o jogo há mais de um minuto; desbloqueie o PC e ele continuará sozinho) e «Você não respondeu — o bot decidiu sozinho».
- :chart-no-axes-column: **Resumo da sessão** — quando o bot para: quanto tempo se passou, quantidade de salas, andares e titanita, se houve reversões e janelas SOS («pelo bot: N» são as reversões feitas sem você), as salas mais demoradas. Se o bot parar devido a uma falha, o título mostrará «O bot parou com um erro» e o motivo.

O resumo chega em qualquer interrupção: atingiu a meta, pressionou Ctrl+Q, Ctrl+Shift+Q, o bot parou com um erro. **Não chega** após «STOP F10» nem após «Parar e fechar» (seção 6), pois essas ações encerram o bot instantaneamente.

### Botões abaixo da mensagem SOS

Pressione-os no Telegram da mesma forma que na janela do computador:

- **«Reverter (Montar pack)»** (verde). O bot enviará: «Escreva os nomes de 3-5 titãs no chat». Escreva-os no chat separados por vírgula ou espaço, por exemplo `гиперион, сигурд, нова` ou de forma abreviada, pelas três primeiras letras: `гип сиг нов`. O bot responderá quem ele reconheceu e perguntará «Tudo certo?»: **«Confirmar pack»** iniciará a reversão, **«Escrever outro»** permitirá digitar novamente. Se não encontrar de 3 a 5 titãs, o bot informará quantos reconheceu e pedirá para digitar novamente.
- **«Jogar manualmente»** (azul). O bot não clica em nada e aguarda até que você termine a sala sozinho.
- **«Ignorar (Continuar)»** (cinza). Aceitar a batalha como está e continuar.
- **«Parar o bot»** (vermelha). Em vez de «Reverter», ela é exibida quando a batalha foi jogada manualmente (ultimate do Angus) ou não há pack adequado. Na janela «Nenhum pack adequado», o botão «Continuar» não aparece.

Quando o pack que você escolheu vence a batalha, a pergunta «O pack deu conta» chega ao Telegram com dois botões: **«Confirmar e Salvar»** (memorizar o pack com uma regra) e **«Reverter e Tentar Novamente»** (escrever outro). Ela só vai para o chat se o pack tiver sido enviado também a partir do Telegram.

Após o clique, resta apenas um botão verde «Selecionado: …» abaixo da mensagem, e os demais desaparecem. Você só pode responder **uma vez**: o bot não processa cliques em mensagens antigas. Respondeu no chat — a janela no computador fechará sozinha; respondeu no computador — o bot deixará de aguardar a resposta do Telegram.

> [!tip] O bot decidiu sozinho enquanto você procurava o celular? Sem problemas. A mensagem «Você não respondeu — o bot decidiu sozinho» chegará, e os botões na pergunta antiga não terão mais efeito. O tempo que o bot espera por você é definido em «Auto-tática» (seção 8, «Tempo da janela SOS sem resposta, min»).

### Se a internet cair

O bot não para nem espera o Telegram: a mensagem é enviada em segundo plano. Se falhar devido à conexão, ele tenta novamente após **30 segundos, 1, 2, 5 e 10 minutos** (cerca de 18 minutos), e no registro aparecem as linhas `Сообщение в Telegram не ушло (...). Пробую снова через N с.` e ao final `Сообщение в Telegram: отправлено с N-й попытки`. O mesmo vale para a janela SOS: ela permanece na tela do computador e a pergunta será enviada ao Telegram quando a conexão voltar. O resumo da sessão é repetido pelo bot em intervalos mais curtos (após 10 e 30 segundos), pois ele se desliga em seguida. Erros do próprio Telegram (token incorreto) o bot não repete: eles precisam ser corrigidos nas configurações.

> [!note] O bot não aceita comandos «a qualquer momento» enviados por você (parar, pausar a partir do chat). O Telegram responde apenas às perguntas feitas pelo próprio bot. Não é possível parar o bot pelo chat, exceto pelo botão «Parar o bot» abaixo da mensagem SOS.

> [!done] O Telegram está configurado e agora o bot poderá chamar você onde quer que esteja. A seguir — estatísticas: quantas salas, andares e titanita foram acumulados por dia. [Próxima seção →](#13)

## Estatísticas

A página «Estatísticas» responde à pergunta «quanto eu joguei?»: quanta titanita, salas, andares e poção de titãs foram acumulados em uma semana, um mês e todo o período. Abre pelo botão **«Estatísticas»** na barra à esquerda, no topo está escrito «Estatísticas de atividade».

Esses números o bot **calcula sozinho**, e não lê da tela do jogo. Passou uma sala — registrou: **6 de titanita e 25 de poção**, e se na janela de resultado havia o ícone «x2» — **12 de titanita e 50 de poção**. Recebeu a recompensa no ponto de salvamento — registrou o andar. A sala que você jogou com as mãos e que o bot contabilizou (seção 10), ele também registra. Os resumos ficam no arquivo `bot_data/stats.json` e são armazenados «por dias de jogo».

> [!note] O **dia de jogo** começa não à meia-noite, mas na hora de reinício que você definiu no «Mestre de regras» (por padrão 5:00, seção 7). Portanto, tudo o que o bot acumulou às 02:30 da madrugada fica registrado no dia de **ontem**: no jogo, a essa hora, ainda é o dia de ontem. Se «Titanita (hoje)» de manhã for igual a zero, embora você tenha jogado à noite, é assim mesmo que deve ser.

### O que há na página

No canto superior esquerdo uma dica, à direita a seleção do **«Período»**, abaixo deles cinco blocos, o gráfico e na parte inferior «Correção manual».

- :calendar: **Período** — «7 dias», «14 dias», «30 dias» ou «Todo o período». O selecionado fica aceso em azul. Na primeira abertura fica em «14 dias».
- :gem: **«Titanita»** — soma do período.
- :calendar: **«Titanita (hoje)»** — apenas do dia de jogo atual. Não depende do período.
- :flask-conical: **«Poção de titãs»**, :door-open: **«Salas»** e :layers: **«Andares»** — somas do período.

Números até 100 000 no bloco são escritos por extenso (`98 540`), e os longos são abreviados: `105.5K` — são cento e cinco mil e quinhentos, `1.24M` — um milhão duzentos e quarenta mil. O número completo aparecerá se passar o mouse sobre o bloco. «Todo o período» pega os contadores gerais do arquivo, e não a soma das colunas, por isso os blocos coincidem com o histórico, mesmo que haja muitas colunas.

> [!tip] Os números a página lê **a cada abertura**, e não ao longo do jogo. O bot está funcionando e os números não mudam? Vá para outra página e volte.

![Página «Estatísticas»: blocos, gráfico por dias e coluna selecionada com placa](images/stats_page.png)

### Gráfico: colunas e cliques

Abaixo do título «Atividade de titanita» há uma legenda de como as colunas estão reunidas: «por dia», «por semana» ou «por mês». Não há mais de quinze colunas para que o gráfico não vire uma cerca:

- **7 e 14 dias** — um dia por coluna.
- **30 dias** — por semana (de segunda a domingo; as semanas das pontas são incompletas — nelas estão apenas os dias que caíram no período).
- **«Todo o período»** — por dias enquanto houver menos de duas semanas de dados; depois por semanas, e quando houver mais de quinze semanas — por meses.

À esquerda uma escala com grade pontilhada, os números na escala são curtos (`3.6K`, `140K`). As legendas sob as colunas, se não couberem, são mostradas alternadamente; a última (a de hoje) é visível sempre. Um dia sem jogo — um espaço vazio, não há coluna. Para um período sem dados, o gráfico dirá «Sem dados para este período».

1. **Passe o mouse sobre a coluna.** Acima dela aparecerá o número exato de titanita. É apenas uma dica, nada muda.
2. **Clique na coluna.** Ela ficará mais brilhante, as outras escurecerão, ao lado aparecerá um painel com data e número. Na semana, o painel detalha a titanita **por dia**, no mês — **por semana**. No canto superior esquerdo acenderá uma legenda azul, por exemplo «Dia mostrado: 19.10.2026 · hoje» (ou «Semana mostrada», «Mês mostrado»).
3. **Observe os blocos.** Eles agora mostram os números dessa coluna: titanita, poção, salas e andares por dia, semana ou mês. «Titanita (hoje)» continua sendo o atual.
4. **Volte aos totais.** Clique na mesma coluna novamente ou na legenda azul com o X (✕). Se mudar o período — a seleção também é redefinida.

### Tabela

O botão **«Tabela»** à direita acima do gráfico mostra as mesmas colunas em lista: «Data», «Titanita», «Salas», «Andares», «Poção de titãs». Datas recentes no topo, na parte inferior a linha **«Total»**. A linha também pode ser selecionada com um clique, e os blocos mostrarão os números dela. O botão nessa hora se transforma em **«Gráfico»** e devolve a imagem. A tabela é conveniente quando são necessários números exatos para todos os dias de uma vez.

![Tabela: datas, titanita, salas, andares e poção, na parte inferior «Total»](images/stats_table.png)

### Correção manual

O bot calcula pela sua própria aritmética (6 ou 12 de titanita por sala), e no jogo o número pode ser outro: você jogou sozinho, o bot estava desligado, o programa foi iniciado não desde a manhã. Para que a estatística bata com o jogo, existe o cartão **«Correção manual»**.

1. **Escolha o dia.** Na lista — «Hoje», «Ontem» e mais cinco dias passados, sete no total. Precisa de um dia mais antigo? Escolha o período «7 dias» ou «14 dias» e clique na coluna dele: esse dia será inserido na lista sozinho (pela coluna semanal e mensal não é inserido — apenas pela diária).
2. **Digite o número total do jogo.** No campo «Titanita por dia» — o que é mostrado no jogo **por todo o dia**, e não «quanto adicionar». Para o dia selecionado já está o que está gravado agora.
3. **Clique em «Aplicar»** (ou Enter no campo).

Exemplo. O bot gravou 90 de titanita no dia, e no jogo para esse mesmo dia são 150. Você digita **150** — o programa adiciona a diferença de 60 e recalcula o restante: aproximadamente **+5 salas, +1 andar e +250 de poção**. Essa é uma estimativa: considera-se que as primeiras 10 salas do dia deram 6 de titanita cada, e as outras 12. Se você jogou diferente, as salas e andares podem ser ligeiramente diferentes dos reais, e a titanita ficará exatamente como a sua.

Quando tudo der certo, aparecerá na parte inferior a notificação «Titanita за 19.10.2026: 150», e no log da principal entrará a linha `[СТАТИСТИКА] Данные за 2026-10-19 синхронизированы! Дельта: +60 тит., +5 комн., +250 зелий.` Se digitou menos do que o gravado, os números diminuirão.

O que pode dar errado:

- **«Digite um número inteiro a partir de 0»** — no campo há letras, vírgula, menos ou está vazio. O campo ficará vermelho.
- **«O bot coletou 90 nesse dia sozinho; não é possível indicar menos»** — não é possível escrever menos do que o bot coletou **sozinho**, pois isso foi gravado honestamente. Baixar o número só é possível até esse valor.
- **«Esse dia já tem exatamente isso»** — você digitou o mesmo número, não há o que mudar.

> [!warning] «Aplicar» grava os números **imediatamente** em `bot_data/stats.json`. Botões «Salvar configurações» não existem aqui e não são necessários, como no «Mestre de regras» (seção 7). Cancelar a edição por botão não é possível, mas nada impede de digitar o número anterior novamente.

> [!note] A correção altera **apenas as estatísticas**. O «Resumo da sessão» na principal e o objetivo da sessão (seção 4) são calculados separadamente, pelo que o bot acumulou nesta execução, e da página «Estatísticas» não dependem.

### «Redefinir»: apagar todo o histórico

O botão **«Redefinir»** (com a lixeira, à direita no cartão «Correção manual») zera toda a estatística: titanita, salas, andares e poção de todos os dias. Clicou sem querer? Nada acontecerá: primeiro o programa perguntará «Redefinir as estatísticas?» e lembrará que cancelar isso não é possível. Pelo botão «Redefinir» na janela você confirma, pelo botão «Cancelar» — recusa. Após a redefinição aparecerá a notificação «Estatísticas redefinidas», e no log a linha `[СТАТИСТИКА] Вся история полностью сброшена!`.

Apaga-se apenas a estatística. Regras, packs, configurações, `profile.yml` e logs de batalha permanecem. Se o bot estiver funcionando nesse momento, ele continua e conta a partir do zero, e o objetivo da sessão não é alterado.

> [!tip] Quer redefinir "para testar"? Primeiro salve uma cópia: feche o programa e copie o arquivo `bot_data/stats.json` para outro lugar (a pasta do programa é aberta pelo botão «Pasta do bot» na página «Sobre»). Devolver o histórico é possível colocando o arquivo de volta.

### Perguntas frequentes

- **Os números não batem com o jogo.** O bot calcula, não lê a tela: 6 ou 12 de titanita por sala. Se você pegou titanita de outras fontes, o jogo mostrará mais. Compare e ajuste pela «Correção manual».
- **O dia de hoje está vazio, mas eu joguei.** Verifique a hora de reinício: antes dela o bot escreve no "ontem" (veja "Dia de jogo" acima). Mudou a hora no «Mestre de regras»? Reinicie o programa para que a página também a pegue.
- **Poucas colunas, mas o período é grande.** Dias em que o bot não funcionou ficam vazios no gráfico. «Todo o período» e meses por padrão comprimem o gráfico: para ver dias específicos, pegue «7 dias» ou «14 dias».
- **No log `[СТАТИСТИКА] ВНИМАНИЕ: Файл stats.json поврежден`.** O arquivo com o histórico não foi lido (por exemplo, o computador foi desligado no momento da gravação). O bot começa uma nova estatística do zero e sobrescreverá o arquivo. Copie-o com antecedência se o histórico antigo for importante.

> [!done] Agora você sabe como ler os números, alternar períodos, verificar estatísticas com o jogo e apagá-las. A seguir — o que fazer se algo der errado. [Próxima seção →](#14)

## Se algo der errado

Uma boa notícia: o bot sabe se virar sozinho na maioria dos problemas. Se travar — vai analisar a tela e começar de novo. Se a internet cair — vai esperar. Se o computador for bloqueado — vai aguardar e continuar. Você só é necessário quando ele **pedir expressamente** (entrar em pausa, mandar mensagem no Telegram) ou quando ele não clicar em nada e não der para entender o motivo pelo log. Esta seção é sobre ambos os casos: o que o bot faz sem você, como entender onde está a falha e o que clicar.

Regra para todos os casos: **não entre em pânico e não tenha pressa**. Não há problema em parar o bot, reiniciar e rodar novamente: as estatísticas, esquadrões, regras e configurações ficam salvas em arquivos e não vão sumir.

### Como entender que algo está errado

- :triangle-alert: **Número vermelho no botão «Erros»** no log da tela principal. Ele não conta apenas falhas: avisos também entram aqui (por exemplo, "janela do jogo sobreposta"). O número em si não é motivo para pânico, basta abrir o botão e ler as linhas.
- :pause: **Estado «Pausa» e botão verde «Continuar», mesmo sem você ter pausado.** Significa que o bot parou sozinho e está esperando por você. No log haverá a linha `[ВНИМАНИЕ] Бот на мягкой паузе: ...` com o motivo.
- :send: **Mensagem no Telegram** (se estiver configurado, seção 12): «Parece que o bot travou», «Não foi possível reverter a batalha», «A tela do PC está bloqueada».
- :eye: **Silêncio.** Linhas não aparecem no log há um minuto ou mais, e nada acontece no jogo. Isso também é um sinal: veja a seção "Casos frequentes" abaixo.

Marcadores no log que indicam um problema:

- `[СТОРОЖ]` — o bot decidiu que travou e recomeçou sozinho.
- `[СЕТЬ]` — parece não haver conexão com o servidor do jogo.
- `[ЭКРАН]` — o computador não permite capturar a tela (está bloqueado).
- `[ОТКАТ]` — passos da reversão de batalha e seus erros (seção 10).
- `[ВНИМАНИЕ]` — o bot pede atenção: pausa, janela do jogo fechada.
- `[ОШИБКА]` — algo quebrou; ao lado está escrito o quê.
- `[ADB]` e `[VISION]` — conexão com o telefone e cliques.

### O que o bot faz sozinho

Aqui você não clica em nada. Apenas saiba que isso é normal e não estraga a sessão.

- :gauge: **Travou: 5 minutos sem passar de nenhuma sala.** Este é o "vigia" (nome da verificação que monitora se o bot encalhou). O bot escreve `[СТОРОЖ] Бот 5 мин не прошёл ни одной комнаты ... Тревога 1 из 3.`, salva uma captura de tela, envia uma mensagem no Telegram (se configurado) e faz um **«início inteligente»**: olha novamente para a tela e decide de onde continuar. Se não resolver, e após mais 5 minutos houver outro alerta. **Terceiro alerta seguido** (ou seja, cerca de 15 minutos sem salas) — o bot entra em pausa suave e espera por você. O tempo que o bot ficou esperando você (janela SOS, pausa, janela de outro programa sobre o jogo), o vigia não conta.
- :activity: **Empacou no mesmo lugar.** A tela de seleção de equipe não apareceu em 30 segundos ou a tela de resultado não apareceu em 3 minutos. Então `[СТОРОЖ] Зависание: ...`, captura de tela e o mesmo início inteligente, mas sem alerta no Telegram.
- :globe: **A batalha não começa (provavelmente sem conexão com o servidor do jogo).** O botão "Auto" foi pressionado, mas a batalha não inicia. O bot tenta mais duas vezes seguidas, depois aguarda e tenta de novo: após 30 segundos, 1, 2, 4 e 8 minutos. Tudo isso no log como `[СЕТЬ] Бой не начался N раз(а) подряд ... Жду N с и пробую снова.` Se mesmo assim não resolver (cerca de 15 minutos): captura de tela, mensagem «Parece que o bot travou» e pausa suave.
- :rotate-ccw: **A conexão caiu durante a reversão da batalha.** O bot não desiste e **espera o jogo por até 15 minutos**: escreve `[ОТКАТ] Бой не загрузился ... Не сдаюсь`, salva uma captura de tela e uma vez por minuto avisa `Всё ещё жду игру`. A conexão voltou — a reversão vai terminar sozinha (`Игра снова откликается`). Não voltou em 15 minutos — «Não foi possível reverter a batalha», mensagem no Telegram e pausa.
- :monitor: **Computador bloqueado (Win+L) ou a tela desligou.** O Windows não permite capturas de tela e o bot não enxerga nada. Ele **não falha**, mas tenta novamente a cada 2 segundos: `[ЭКРАН] Не удаётся сделать снимок экрана ... Похоже, ПК заблокирован`. Se passar de um minuto — uma mensagem «A tela do PC está bloqueada». Desbloqueou — `[ЭКРАН] Снимок экрана снова работает`, o bot continua sozinho.
- :layers: **A janela do jogo foi coberta por outra janela.** O bot espera até que ela volte a ser a principal (`[ВНИМАНИЕ] Окно игры перекрыто ... Бот ждет фокуса`). Clique na janela do jogo e ele continuará. O motivo disso está na seção 5.
- :target: **O clique não foi registrado.** Se 4 segundos após o clique a tela não mudar, o bot clica novamente: `[VISION] Клик по '...' не зарегистрирован сервером ... Повторяю...`. Linhas ocasionais assim são normais: o telefone às vezes "pensa".
- :smartphone: **A conexão via cabo com o telefone oscilou.** O bot escreve `[ADB] Постоянное соединение с телефоном оборвалось ... Переподключусь при следующем нажатии` e se reconecta.
- :send: **A mensagem no Telegram não foi enviada devido à internet.** O bot vai tentar reenviar mais tarde (seção 12) e continua funcionando.

> [!note] Quantas vezes o bot travou durante a sessão pode ser visto no bloco `[ИТОГ]` no log (linha com a palavra "travamentos"). Casos raros não são problema. Se houver muitos, procure a causa na seção "Casos frequentes" abaixo.

### O bot entrou em pausa sozinho: o que fazer

Ele parou porque não dá para continuar sem você. Siga estes passos:

1. **Olhe para a tela do jogo.** A janela `HeroWarsBot_Arena` mostra onde o bot encalhou: tela de resultado, batalha, menu de pausa, o "cogumelo" de carregamento ou algo inesperado (janela de outro programa, anúncio, aviso do jogo).
2. **Leia as últimas linhas do log.** Abra o botão «Erros» e olhe no final: ali diz por que o bot parou (`[СТОРОЖ]`, `[ОТКАТ] ОШИБКА`, `[СЕТЬ]`).
3. **Volte o jogo para o corredor da Masmorra.** Feche o que sobrou, espere a batalha terminar ou carregar e vá até a tela com a porta e a bandeira.
4. **Clique em «Continuar».** O bot analisará a tela novamente (início inteligente) e seguirá em frente.

> [!note] A pausa após uma reversão fracassada também acontece assim: a batalha manual terminou a tempo, o botão "Tentar novamente" não está mais na tela de resultado e não é possível reverter. A tela de resultado permanece visível — não precisa fechar nada, após clicar em «Continuar» o bot vai clicar em "OK" sozinho. Olhe nessa tela quem sobreviveu.

> [!tip] O bot não entra em pausa por qualquer detalhe, mas sim quando tentou e não conseguiu. Portanto, antes de clicar em «Continuar», entenda **o que exatamente** deu errado. Se a causa permanecer (sem internet, jogo fechado), o bot vai parar de novo em poucos minutos.

### Casos frequentes: o que verificar e o que fazer

**O bot não clica em nada e o log está silencioso.** O mais provável é que ele não esteja vendo o jogo ou não consiga encontrar nada nele. Verifique em ordem:

1. **A janela do jogo está no lugar.** Ela se chama `HeroWarsBot_Arena`, não está minimizada nem fechada. Se a janela não existir, o bot não escreve sobre isso, mas a verifica silenciosamente a cada meio segundo. Por isso, o silêncio no log com a janela ausente é algo comum. Clique em «Conectar telefone»: a janela abrirá novamente.
2. **O tamanho da janela não mudou.** O bot mede a janela uma vez na inicialização e usa essa medida dali em diante. Se redimensionou, maximizou ou moveu a janela após o início — pare o bot (F10), clique em «Redefinir o tamanho da janela do jogo» e depois em «Começar o farm» novamente. Detalhes na seção 3.
3. **No jogo — corredor da Masmorra**, e não menu, loja, evento externo ou janela de anúncio.
4. **O idioma do programa coincide com o idioma do jogo** (duas letras na parte inferior do painel esquerdo). Caso contrário, o bot não reconhecerá os botões.
5. **Nada está cobrindo a janela do jogo.** Qualquer janela sobre o jogo — e o bot fica aguardando o foco.

**O bot "vê" e clica, mas nada acontece no jogo.** No log aparecem várias linhas seguidas "Клик по ... не зарегистрирован сервером ... Повторяю...". Significa que o comando de clique não está chegando ao telefone. Verifique:

- As **duas** configurações de depuração no telefone devem estar ativadas: "Depuração USB" e "Depuração USB (configurações de segurança)". Sem a segunda, a imagem aparece, mas os toques não funcionam (seção 2).
- O telefone está desbloqueado, o cabo está bem conectado. Tente outra porta USB.
- No prompt de comando, `adb devices` mostra ao lado do telefone `device`, e não `unauthorized` ou uma lista vazia.
- Se não resolver: pare o bot, clique em «Reiniciar o scrcpy», depois em «Começar o farm».

**O bot clica no lugar errado ou confunde os titãs.** Na maioria das vezes a janela do jogo não está no tamanho correto ou foi alterada após a inicialização (redefinição de tamanho, como acima). O tamanho está correto, mas o bot continua errando — salve uma captura de tela desse momento e envie ao autor junto com o log (abaixo).

**A janela do programa "não responde".** O próprio programa se monitora: se a janela não responder por 5 segundos, ele registra em um arquivo em qual linha de código travou. O arquivo fica em `bot_data/debug/` e se chama `ui_freeze_<дата>_<время>.txt`. O que fazer:

1. **Espere um minuto.** Muitas vezes a janela volta sozinha: ela está ocupada com um processamento pesado.
2. **O bot funciona independentemente da janela.** Precisa pará-lo e os botões não respondem? Pressione Ctrl+Shift+Q: essa atalho é escutado pelo próprio bot, e não pela janela do programa (seção 6).
3. **Não voltou — feche a janela pelo X.** Se não fechar — pelo Gerenciador de Tarefas (Ctrl+Shift+Esc). Depois verifique lá mesmo se `HeroWarsBot.exe` ou `python` ainda estão na lista: se sim, feche-os também, caso contrário o bot continuará clicando no jogo sem a janela.
4. **Envie o arquivo `ui_freeze_...txt` ao autor.** Há apenas nomes de arquivos e linhas de código do programa, nada pessoal.

**O bot parou, mas você não o parou.** Abra o cartão «Resumo da sessão» na tela principal (botão «Detalhes») e veja o motivo:

- «janela do scrcpy fechada» — a janela do jogo foi fechada ou desapareceu (cabo desconectado, telefone bloqueou). Conecte o telefone novamente.
- «o bot terminou» — o processo encerrou sem motivo. Se houver Telegram, o resumo foi enviado para lá; se não houver, procure no log a linha `[ОШИБКА] Бот остановился из-за ошибки:` e o texto abaixo dela.
- "Esquadrão não encontrado nas regras" — a sala não tem um esquadrão principal definido. Abra «Mestre de Regras» → «Base e salas» e defina-o em todas as quatro salas (seção 7).
- "Erro: ..." — o programa travou. Envie o log ao autor (abaixo).

> [!warning] Após clicar em «PARAR» (F10), o bot não tem tempo de escrever o bloco `[ИТОГ]` e não envia o resumo no Telegram: ele foi encerrado abruptamente (seção 6). Isso não é uma falha.

**O telefone "dormiu" ou a tela apagou.** O programa executa o scrcpy no modo "impedir que o telefone durma" (`--stay-awake`). O botão «Desligar a tela do telefone» apaga apenas a **tela**: o jogo continua e o bot enxerga tudo. Mas se o telefone foi bloqueado ou desconectado do cabo, a janela do jogo mostrará a tela de bloqueio ou ficará vazia, e o bot não encontrará nada. Desbloqueie o telefone, verifique o cabo e clique em «Reiniciar o scrcpy».

**Mensagens do Telegram não chegam.** O mais provável é que não tenha clicado em "Iniciar" no seu bot ou o token/Chat ID esteja incorreto — explicação na seção 12. O bot continua funcionando normalmente.

**O bot escala titãs errados ou decide diferente do que você queria.** Isso não é uma falha, são as regras: leia as seções 7–11 (esquadrões, limites, regras, «O bot decide sozinho»). A decisão do bot sempre pode ser encontrada no log pelas linhas `[ТАКТИКА]`.

### Onde ficam os logs e capturas de tela

O botão **«Pasta do bot»** na página «Sobre» abre a pasta de onde o programa foi executado. Nela ficam os arquivos que o próprio bot cria. O necessário está dentro da pasta `bot_data`:

- :file-text: `bot_data/logs/bot_log_<дата>_<время>.txt` — **log completo de cada execução do bot.** O bot o escreve sozinho, linha por linha, por isso ele permanece mesmo após uma queda ou fechamento do programa. É o arquivo principal para análise.
- :gauge: `bot_data/logs/timings_<дата>_<время>.csv` — quanto tempo levou cada sala (corredor, montagem, batalha, resultado).
- :swords: `bot_data/logs/battle_log_<дата>_<время>.jsonl` e `battle_log.csv` — histórico de batalhas: sala, inimigos, esquadrão, resultado, PV e energia dos titãs.
- :image: `bot_data/debug/` — **capturas de tela para análise.** O nome indica o que aconteceu: `stuck_...` — travou, `sos_...` — janela SOS, `rollback_wait_...` — aguardou o jogo durante a reversão, `rollback_fail_...` — reversão falhou, `start_fail_...` — batalha não iniciou, `result_unreadable_...` — não leu a janela de resultado. Em seguida o número da sala, elemento e horário (`stuck_комната12_water_2026-10-19_14-03-21.png`). Lá também fica `ui_freeze_...txt`, se a janela do programa tiver travado.

> [!warning] O bot limpa os arquivos antigos sozinho: ao iniciar, em `bot_data/logs/` permanecem 20 arquivos novos de cada tipo (`.txt`, `.jsonl`, `timings_*.csv`), e em `bot_data/debug/` — 50 capturas de tela novas. Se quiser salvar os logs após uma noite problemática, **copie-os para outro lugar antes da próxima execução do bot**. Da mesma forma é apagado o log que você salvou pelo botão «Salvar log» na pasta padrão: salve-o em outro lugar, por exemplo, na Área de Trabalho.

> [!warning] Não exclua nem renomeie `profile.yml` (suas configurações e Telegram) e a pasta `bot_data`: nela estão as estatísticas, as regras que o bot memorizou e o histórico de batalhas. Apagar é permitido apenas em `bot_data/debug` e logs antigos, e apenas quando não forem necessários.

### Como enviar o log ao autor

Quando não for possível resolver o problema, o caminho mais rápido é enviar ao autor o que aconteceu.

1. **Lembre-se de quando foi.** O horário e o número aproximado de salas (`[СТАТИСТИКА] Комнат: N`) ajudam a encontrar o ponto certo no log longo.
2. **Encontre os arquivos.** O log é `bot_data/logs/bot_log_...` daquela noite, as capturas de tela estão em `bot_data/debug/` com horário semelhante no nome e, em caso de travamento da janela, também o `ui_freeze_...txt`.
3. **Clique em «Enviar log ao autor»** abaixo do log na tela principal. O programa oferecerá para salvar o conteúdo atual do log (que é o arquivo `gui_log_...txt`) e depois abrirá seu e-mail com uma mensagem pronta para o endereço do autor.
4. **Anexe os arquivos ao e-mail você mesmo.** O programa não sabe anexar arquivos ao e-mail: ele apenas abre a mensagem. Anexe `gui_log_...txt` ou `bot_log_...txt`, capturas de tela e (se houver) `ui_freeze_...txt`.
5. **Descreva em palavras:** o que fez, o que esperava, o que viu e quando foi. Uma frase curta "não funciona" quase não ajuda o autor.

> [!warning] **Nunca anexe** `profile.yml` nem `bot_data/profile.yml.bak`: neles está o token do seu bot do Telegram. A captura de tela da janela «Configurações do Telegram» também deve ser enviada apenas com o token oculto (com pontos).

> [!note] O e-mail não abriu (cliente de e-mail não configurado)? Na página «Sobre» há o botão «Escrever ao autor»: se não for possível abrir o e-mail, ele copia o endereço para a área de transferência, e você poderá escrever de qualquer e-mail.

### Se nada resolver

Vá do mais simples ao mais complexo, verificando a cada passo se o bot voltou a funcionar:

1. **«Pausa» → volte o jogo para o corredor → «Continuar».**
2. **«PARAR» (F10) → «Começar o farm».** O bot começará com um início inteligente e entenderá sozinho onde está.
3. **Pare o bot e clique em «Reiniciar o scrcpy».** Depois clique em «Começar o farm» novamente.
4. **Feche o programa e abra-o novamente.** Se o telefone "travou", retire e recoloque o cabo.
5. **Reinicie o computador e o telefone.** Parece brincadeira, mas resolve metade dos problemas estranhos.

Os objetivos da sessão (tempo, salas, andares, titanita) após a reinicialização são contados do zero, mas as estatísticas, esquadrões e regras permanecem: ficam salvos em arquivos.

> [!done] Agora você sabe como o bot se salva sozinho, o que fazer quando ele parar e como coletar e enviar o log. Resta a última seção: sobre o programa e como apoiar o projeto. [Próxima seção →](#15)

## Sobre o programa e suporte

A última página no menu à esquerda é «Sobre». Ela é sobre o próprio programa: qual versão você possui, se está tudo no lugar, para onde escrever ao autor e como dizer "obrigado". Não há nada para configurar nela, mas aqui estão dois botões úteis: «Verificar atualizações» e «Pasta do bot».

### O que há na página

- :shield-check: **Cartão do programa** no topo. Nome «Hero Wars: Knowledge Engine Bot», ao lado — **número da versão** (por exemplo, `v1.6.1`) e o rótulo `Beta`. "Beta" significa "sendo testado na prática": o programa funciona, mas o autor ainda o está aprimorando e erros são possíveis. Abaixo do nome — uma breve descrição. À direita, quatro botões, detalhados abaixo.
- :user: **«Autor e licença»**: nome do autor, e-mail e licença. Clique no endereço de e-mail — uma mensagem será aberta.
- :monitor: **«Estado dos componentes»**: verificação de que o computador tem tudo o que precisa para funcionar. Detalhes abaixo.
- :heart: **«Apoiar o projeto»**: formas de agradecer ao autor. Isso é opcional.

> [!tip] Informe a versão ao autor ao relatar um problema: ela mostra imediatamente qual versão exata do programa você está usando. A versão fica no cartão no topo, ao lado do nome.

### Quatro botões no cartão

1. **«Verificar atualizações».** Abre no navegador a página de lançamentos do projeto no GitHub (GitHub é o site onde o autor armazena o programa; "lançamento" é uma versão pronta que você pode baixar). Compare o número mais recente com o seu. Se for mais recente — você pode atualizar; se for igual — você já tem a versão mais recente.
2. **«Pasta do bot».** Abre no Explorador de Arquivos do Windows a pasta de onde o programa foi executado: aquela onde ficam suas configurações e dados. Útil quando você precisa copiar arquivos ou encontrar um log.
3. **«Escrever ao autor».** Abre um e-mail para o endereço do autor no seu programa de e-mail. Se não houver programa de e-mail no computador, o e-mail não abrirá. Nesse caso, o próprio programa colocará o endereço na área de transferência (memória temporária de onde se cola com Ctrl+V) e avisará no rodapé da janela: «Não foi possível abrir — copiado para a área de transferência». Cole o endereço em um e-mail de qualquer provedor.
4. **«GitHub do projeto».** Abre a página principal do projeto no GitHub: lá estão o código-fonte e a descrição.

> [!note] O programa **não busca atualizações na internet por conta própria**: «Verificar atualizações» apenas abre a página, e a decisão é sua. Foi projetado assim para que nada mude sem o seu conhecimento.

### Como atualizar o programa

A atualização não é instalada por cima — você baixa a nova versão e transfere seus dados para ela. Assim suas formações e estatísticas não serão perdidas.

1. **Pare o bot e feche o programa.** O X da janela, se o bot estiver rodando, perguntará se deseja pará-lo.
2. **Baixe a nova versão** na página de lançamentos (botão «Verificar atualizações») e descompacte em uma nova pasta, não por cima da antiga.
3. **Transfira seus dados.** Da pasta antiga para a nova, copie o arquivo `profile.yml` e a pasta `bot_data` inteira. O novo programa sem eles começa "do zero": configurações vazias e estatísticas vazias.
4. **Execute o novo programa** e dê uma olhada em «Sobre»: o número da versão deve ser o novo, e todos os três componentes devem estar em ordem.
5. **Não exclua a pasta antiga ainda.** Trabalhe por alguns dias na versão nova. Se estiver tudo bem — pode removê-la.

> [!warning] Não copie os arquivos de `bot_data` um por um "apenas o necessário", mas transfira a pasta inteira: as regras que o bot memorizou sozinho, o histórico de batalhas e as estatísticas estão interligados e não podem ser reconstruídos do zero.

### «Estado dos componentes»

O programa verifica automaticamente se há tudo do que o bot precisa para funcionar. A verificação ocorre em segundo plano cada vez que a página é acessada. Enquanto ocorre, exibe-se «verificando».

- :smartphone: **ADB** — serviço através do qual o computador clica no telefone. Deve estar como «encontrado».
- :monitor: **scrcpy** — programa que mostra a tela do telefone em uma janela no computador. Deve estar como «encontrado».
- :image: **Base de modelos** — "imagens de amostra" de botões e titãs pelas quais o bot reconhece o que está em sua tela. Deve estar como «carregada».

O que fazer se algo estiver vermelho:

- **ADB ou scrcpy «não encontrado».** Significa que a pasta deles não foi adicionada ao `PATH` (lista de locais onde o Windows procura programas). Como fazer isso está na seção [«O que é necessário e instalação»](#2). Após editar o `PATH`, feche o programa e abra-o novamente: o programa já em execução não enxerga o novo `PATH`.
- **Base de modelos «não encontrada».** Arquivos desapareceram da pasta do programa. Na maioria das vezes, o arquivo não foi descompactado completamente ou o antivírus removeu algo. Descompacte o arquivo novamente em uma nova pasta e transfira `profile.yml` e `bot_data`, como ao atualizar.

### O que está na pasta do bot e o que não pode ser excluído

Abra-a com o botão «Pasta do bot». Há muitos arquivos lá, mas você só precisa de alguns. O restante é do sistema e o programa precisa deles para funcionar.

- :file-text: `HeroWarsBot.exe` — o próprio programa. O bot também funciona a partir dele, não possui um arquivo separado. Todos os outros arquivos e pastas ao lado dele (`guide`, `ui`, bibliotecas, arquivos com extensão `.dll` e outros) são parte do programa. **Não exclua nem renomeie nada deles**, caso contrário ele deixará de ser executado.
- :file-text: `profile.yml` — suas configurações: objetivo da sessão, limites, Telegram. **Nelo está o token do seu bot do Telegram, portanto não o envie a ninguém.** Aparece após clicar pela primeira vez em «Salvar configurações».
- :folder: `bot_data` — tudo o que o programa e o bot gravaram sozinhos. Isso é o **mais valioso** que você tem. Dentro:
  - `stats.json` — estatísticas (página «Estatísticas»);
  - pasta `rules` — suas formações e regras, incluindo as memorizadas pelo bot;
  - pasta `logs` — histórico de batalhas e log do bot (`bot_log_...txt`);
  - pasta `debug` — capturas de tela para análise (janelas SOS, travamentos, reversões malsucedidas);
  - `titan_state.json` — vida e energia dos titãs para o dia de jogo;
  - `profile.yml.bak` — cópia de segurança das configurações. É a partir dela que funciona «Restaurar / Redefinir» no «Mestre de Regras». **Ela também contém o token do Telegram**;
  - `ui_settings.json` — idioma selecionado da janela;
  - `sos_info.json`, `temp_sos.png`, `temp_test.png` — pequenos arquivos de trabalho para mensagens no Telegram.
- :pause: `pause.flag` — "sinalizador de pausa". Aparece quando o bot está em pausa suave. Se sobrou da vez anterior, o próprio programa o excluirá na inicialização.

> [!warning] **Não exclua nem renomeie** `profile.yml` e `bot_data`. Se você excluir `bot_data` — as estatísticas, formações, regras e tudo o que o bot aprendeu serão perdidos. Se você realmente precisar liberar espaço, pode apagar o conteúdo de `bot_data/debug` e logs antigos em `bot_data/logs`. Mas o próprio bot mantém apenas os últimos 20 logs e as últimas 50 capturas de tela, portanto o espaço normalmente não é um problema.

> [!tip] **Faça um backup uma vez por semana.** Copie `profile.yml` e a pasta `bot_data` para um pendrive ou para a nuvem. Se o computador quebrar ou você reinstalar o Windows, poderá baixar o programa novamente e recuperar as formações e estatísticas a partir da cópia. O token do Telegram está na cópia — guarde-a com você, e não em uma pasta compartilhada.

### Autor e licença

O programa foi escrito e é mantido por **Platon Petrunin**. Dúvidas, erros e ideias — botão «Escrever ao autor» ou o endereço no cartão «Autor e licença».

A licença se chama **PolyForm Noncommercial 1.0.0**. Em palavras simples:

- :check: usar para si mesmo, para o seu próprio jogo gratuitamente — o quanto quiser;
- :check: estudar o código e alterá-lo para si mesmo também é permitido;
- :x: **não é permitido lucrar**: vender o programa ou o seu `.exe`, fingir ser seu sob outro nome, integrar em serviços pagos. Para isso, é necessária a permissão por escrito do autor.

> [!note] Este é um resumo simples, não um texto jurídico. Se o seu caso for incomum (por exemplo, quer distribuir o programa a amigos ou à comunidade), escreva primeiro ao autor. O texto completo da licença está no arquivo `LICENSE` no projeto do GitHub.

### Como apoiar o projeto

O programa é gratuito e o autor o desenvolve em seu tempo livre. Se ele economiza seu tempo e paciência, você pode agradecer em dinheiro. Isso é **voluntário**: o bot funciona da mesma forma, quer você tenha pago ou não, e não há nenhuma "função paga".

No rodapé da página «Sobre» há três blocos:

1. **«Criptomoeda».** Três carteiras: `USDT · TRC20`, `Bitcoin · BTC` e `Ethereum · ETH`. O endereço completo fica visível no campo. Você pode copiá-lo com o botão «Copiar» à direita (na parte inferior aparecerá «Endereço copiado»), com um duplo clique no campo (selecionará tudo) ou com o botão direito do mouse — «Copiar».
2. **«Doar pelo Telegram».** Três linhas — rublos (`RUB`), euros (`EUR`) e dólares (`USD`). Em cada uma há dois botões: **«Aplicativo»** abre o pagamento no aplicativo do Telegram, **«Navegador»** — no navegador, caso o Telegram não esteja instalado. Escolha a moeda que for mais conveniente.
3. **«Transferências diretas».** Botões «Apoiar no Boosty» e «YooMoney (RUB)»: abrem-se as páginas desses serviços, depois segue como um pagamento normal.

> [!warning] **Cuidado com criptomoedas.** Transfira apenas na rede especificada ao lado da carteira: para `USDT` é `TRC20`, e não outra. O dinheiro enviado para a rede errada **não pode ser recuperado**. Obtenha o endereço apenas a partir do programa, com o botão «Copiar»: em sites e mensagens de terceiros ele pode ser alterado. Na primeira vez, envie uma quantia pequena.

### Perguntas frequentes

- **Minha versão é antiga — isso é grave?** Não. O programa não para de funcionar só porque uma nova versão foi lançada. Mas versões mais recentes costumam corrigir erros, portanto dê uma olhada na página de lançamentos a cada poucas semanas.
- **A «Pasta do bot» não abriu.** Aparecerá a mensagem «Não foi possível abrir a pasta». Abra-a você mesmo: Explorador de Arquivos, a pasta onde você descompactou o programa.
- **Por que não há o botão "Atualizar"?** O programa não baixa nada por conta própria para não quebrar suas configurações sem autorização. Você atualiza manualmente, seguindo os passos acima.
- **Se eu não apoiar, algo vai mudar?** Nada. O bot funciona da mesma forma para todos.

> [!done] Esta é a última seção. Agora você sabe tudo para iniciar o bot, configurá-lo para você, entender suas decisões e corrigir se algo der errado. Bom jogo! Se ainda tiver dúvidas, o botão «Escrever ao autor» está abaixo.
