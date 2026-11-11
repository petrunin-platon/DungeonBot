# Hero Wars: Knowledge Engine Bot

¡Hola! Este es un programa que completa automáticamente la Mazmorra de titanes por ti en el juego Hero Wars. Lo activas, vas a hacer tus cosas y él abre puertas, forma equipos y recoge recompensas.

Esta guía está escrita para que cualquiera pueda entenderla. Explicamos las palabras desconocidas de inmediato y, al final de cada sección, te indicamos a dónde ir a continuación.

## Qué sabe hacer el bot

El bot no es un «autoclicker» sin sentido. Mira la pantalla del juego tal como lo harías tú y decide por sí mismo qué hacer a continuación. Esto es lo que sabe hacer:

- :eye: **Ve la pantalla.** Cada fracción de segundo toma una captura de la ventana del juego y reconoce en ella botones, puertas y enemigos.
- :door-open: **Elige la puerta.** Entra en las salas en el orden que le has configurado y evita aquellas donde actualmente sea peligroso.
- :users: **Coloca el equipo.** Para cada sala tiene un «pack» (así llamamos al equipo de cinco titanes). El bot coloca a los titanes en sus puestos por sí solo.
- :heart-pulse: **Supervisa la salud.** Después de cada combate lee los PS (salud) y la energía de los titanes y decide si el pack está listo para el siguiente combate.
- :swords: **Te llama si el combate va mal.** Aparece la ventana «Se requiere intervención»: puedes volver a jugar el combate con otro pack, aceptarlo o jugarlo a mano. Si te has alejado del ordenador, el bot puede decidir solo.
- :chart-no-axes-column: **Aprende de sus combates.** Recuerda qué pack venció a qué enemigos y la próxima vez lo coloca de inmediato.
- :send: **Escribe en Telegram.** Si lo deseas, te enviará el resumen de la sesión y una alarma cuando algo salga mal.

> [!note] Ejemplo. Araji entró al combate con el 36% de salud y tras el combate cayó al 8%. El bot ve esto, entiende que el combate fue malo y te pregunta o bien deshace el combate por sí solo y lo vuelve a jugar con otro pack.

### Qué no hace el bot

- Completa **solo la Mazmorra de titanes**. Los demás modos de juego no los conoce.
- **No juega «en la nube»**. El juego se ejecuta en tu teléfono Android, y el PC con Windows mira la pantalla del teléfono y pulsa en ella a través del cable USB. Se necesitan tanto el teléfono como el ordenador.
- No es un mago: si se pierde la conexión con el juego, espera honestamente a que vuelva y te informa de ello.

### ¿Es seguro para la cuenta?

El bot intenta comportarse como una persona real y no como un robot:

- cada pulsación cae en un **punto aleatorio** del botón, no siempre en el mismo;
- antes de pulsar mantiene una **pausa de reacción**: de 0,3 a 0,8 segundos después de que aparece el botón;
- pulsa **no más de dos veces por segundo**.

> [!warning] Ningún programa puede dar una garantía total: las reglas del juego las establece su editor. El bot no hace nada «inhumanamente rápido», pero la decisión de usarlo depende de ti.

### Qué viene a continuación en la guía

- **Qué necesitarás e instalación**: qué conseguir e instalar una sola vez.
- **Conectamos el teléfono**: el primer inicio del farmeo.
- **Inicio y mini barra**: cómo leer la ventana y el pequeño panel debajo del juego.
- **Pausa y detención**: botones y atajos de teclado.
- **Maestro de reglas**: cómo enseñar al bot tus packs y el orden de las puertas.
- **Cuando el combate salió mal**: ventanas de intervención y cómo decide el bot solo.
- **Telegram, estadísticas, si algo sale mal**: todo lo demás.

> [!done] Ahora sabes qué sabe hacer el bot. A continuación: lo que necesitas instalar una sola vez. [Siguiente sección →](#2)

## Qué necesitarás e instalación

Esto se hace **una sola vez**. Después simplemente ejecutas el programa haciendo doble clic. Dedica a todo esto unos quince minutos; después será muy fácil.

### Qué necesitas tener

- :monitor: **Un ordenador con Windows.** En él se ejecuta el programa y el bot.
- :smartphone: **Un teléfono Android con Hero Wars.** El juego se ejecuta en el teléfono, y el ordenador mira su pantalla y pulsa en ella.
- :terminal: **Un cable USB.** Es mejor el que usas para cargar el teléfono y transferir archivos: existen cables «solo de carga», y a través de ellos el ordenador no verá el teléfono.
- :folder: **Archivo comprimido del programa** (archivo `.zip`, dentro está `HeroWarsBot.exe`).

> [!note] El juego se queda en el teléfono. El bot no instala nada innecesario en él ni toca los archivos del juego: solo mira la pantalla y pulsa en ella tal como lo harías tú con el dedo.

### Paso A. Descomprime el programa

1. **Descomprime el archivo** — haz clic derecho sobre él y selecciona «Extraer todo...». Elige una carpeta sencilla sin caracteres especiales o cirílicos, por ejemplo `C:\HeroWarsBot`.
2. **Comprueba que los archivos estén en su sitio** — en la carpeta debe estar `HeroWarsBot.exe` junto a los demás archivos y carpetas.

> [!warning] Primero descomprime el archivo y solo después ejecuta el programa. Si abres el `.exe` directamente desde el archivo comprimido, los demás archivos del programa no estarán disponibles y no funcionará correctamente.

> [!tip] Esta carpeta es el «hogar» del bot. Junto a `HeroWarsBot.exe` creará por sí mismo sus propios archivos: configuraciones, estadísticas, historial de combates. Por tanto, no muevas el `.exe` por separado de los demás archivos, y si cambias de lugar, mueve la carpeta entera.

### Paso B. Instala scrcpy

scrcpy es un pequeño programa que muestra la pantalla del teléfono en una ventana del ordenador. El bot «mira» precisamente esa ventana. Junto con él se instala **adb**, el asistente a través del cual el bot pulsa en la pantalla del teléfono.

1. **Descarga scrcpy** — en la [página del proyecto](https://github.com/Genymobile/scrcpy/releases) elige la última versión para Windows (archivo `.zip` con «win64» en el nombre).
2. **Descomprime el archivo** — lo más cómodo es en una carpeta sencilla sin espacios ni caracteres especiales, por ejemplo `C:\scrcpy`. Dentro deben estar los archivos `scrcpy.exe` y `adb.exe`.
3. **Añade la carpeta al PATH** — así Windows sabrá dónde buscar estos programas. Mira a continuación cómo hacerlo.

**Cómo añadir la carpeta al PATH:**

1. **Abre la configuración** — pulsa la tecla Windows, escribe «variables de entorno» y selecciona «Editar las variables de entorno del sistema».
2. **Busca «Path»** — en la ventana que se abre pulsa «Variables de entorno», en la lista superior selecciona la línea `Path` y pulsa «Editar».
3. **Añade la carpeta** — pulsa «Nuevo», escribe `C:\scrcpy` (tu carpeta, si es diferente) y cierra todas las ventanas con el botón «Aceptar».

> [!note] PATH es la lista de carpetas donde Windows busca programas cuando los llamas por su nombre. Añades la carpeta a la lista y `scrcpy` junto con `adb` se encontrarán desde cualquier lugar.

### Paso C. Comprueba que scrcpy se haya instalado correctamente

1. **Abre el «Símbolo del sistema»** — tecla Windows, escribe `cmd`, pulsa Intro. Si la ventana ya estaba abierta antes de la instalación, ciérrala y vuelve a abrirla: la antigua no conoce las carpetas nuevas.
2. **Comprueba scrcpy** — escribe `scrcpy --version` y pulsa Intro. Debería aparecer la versión del programa.

Si en lugar de la versión Windows dice «no se reconoce como un comando interno o externo», significa que la carpeta no se añadió al PATH. Vuelve al paso B y comprueba que en el PATH esté inscrita la carpeta donde se encuentra `scrcpy.exe`.

### Paso D. Configura el teléfono

El teléfono debe permitir que el ordenador lo controle. Esto se llama «Depuración por USB» (un modo pensado para desarrolladores de aplicaciones). El bot lo utiliza para pulsar en la pantalla.

1. **Activa el modo de desarrollador** — entra en «Ajustes» → «Acerca del teléfono» y pulsa **7 veces seguidas** en «Número de compilación». El teléfono indicará que ahora eres desarrollador.
2. **Busca «Opciones para desarrolladores»** — este apartado aparecerá en los ajustes (a veces dentro de «Sistema» o «Ajustes adicionales»).
3. **Activa dos ajustes** — «Depuración por USB» **y** «Depuración por USB (Ajustes de seguridad)».
4. **Conecta el cable** — cuando el teléfono pregunte «¿Permitir depuración por USB desde este ordenador?», marca «Permitir siempre» y pulsa «Aceptar».

![Sección «Opciones para desarrolladores» con dos ajustes de depuración activados](images/usb_debug.png)

> [!warning] Activa **ambos** ajustes. Si solo está activado el primero, la imagen del teléfono llegará al ordenador, pero las pulsaciones no llegarán al juego: el bot estará «pulsando», pero el juego no notará nada.

Ahora comprobaremos la conexión. Conecta el teléfono con el cable, abre el «Símbolo del sistema» y escribe `adb devices`. En la lista debe haber una línea con la palabra `device` junto al número del teléfono.

- :check: `device` — todo bien, el teléfono está listo.
- :triangle-alert: `unauthorized` — el teléfono espera tu autorización. Mira su pantalla y pulsa «Permitir».
- :triangle-alert: la lista está vacía — el ordenador no ve el teléfono. Prueba otro cable u otro puerto USB.

### Paso E. Primer inicio del programa

1. **Abre la carpeta del programa** — aquella donde descomprimiste el archivo.
2. **Haz doble clic en `HeroWarsBot.exe`** — se abrirá la ventana del programa.
3. **Echa un vistazo** — a la izquierda hay una barra con secciones, en el centro la página principal. Mientras el teléfono no esté conectado, en el encabezado dice «Esperando el teléfono»; esto es normal.

> [!tip] Ejecuta siempre el programa desde su carpeta (o crea un acceso directo a `HeroWarsBot.exe`: botón derecho → «Enviar a» → «Escritorio»). Así encontrará sus ajustes y archivos.

> [!done] Todo listo: programa descomprimido, scrcpy y teléfono configurados. Ahora conectemos el teléfono e iniciemos el primer farmeo. [Siguiente sección →](#3)

## Conectamos el teléfono y первый фарм

Ahora conectaremos el teléfono e iniciaremos el bot por primera vez; todo llevará unos cinco minutos. Primero recuerda: en el monitor habrá **dos ventanas**.

- :monitor: **Ventana del programa**: en la que estás leyendo esta guía. En ella hay botones, ajustes y el registro (así se llama el historial de mensajes donde el bot anota lo que hace).
- :smartphone: **Ventana del juego**: el «espejo» de la pantalla del teléfono en el monitor, se llama `HeroWarsBot_Arena`. El bot «mira» precisamente ahí.

### Qué hay en la pantalla principal en el primer inicio

Mientras no hayas guardado la configuración ni una sola vez, en la página principal (primer botón de la barra izquierda) estará la tarjeta «Por dónde empezar» con la leyenda «3 pasos · unos 5 minutos».

![Primer inicio: tarjeta «Por dónde empezar», texto rojo «Esperando el teléfono...» y botón azul «Conectar teléfono»](images/connect_phone.png)

- :smartphone: **«Conecta el teléfono»**: marcado con la palabra «ahora». Cuando el teléfono se conecte, el número del paso se cambiará por un tick verde. Eso es lo que haremos ahora.
- :sliders-vertical: **«Revisa los packs por sala»**: el enlace «Abrir →» lleva al «Maestro de reglas» (segundo botón en la barra izquierda, icono con deslizadores). Allí le indicas al bot con qué titanes entrar en cada sala.
- :send: **«Configura Telegram para SOS»**: opcional. El bot te escribirá en Telegram si necesita ayuda.

> [!warning] Los packs son lo más importante antes del primer farmeo. El bot coloca en cada una de las cuatro salas (agua, tierra, fuego y mixta) el pack guardado en el «Maestro de reglas», ya que no puede adivinar tus titanes. Cómo configurarlo se explica en la sección sobre el «Maestro de reglas» más adelante en la guía. La tarjeta «Por dónde empezar» desaparecerá cuando guardes la configuración en el «Maestro de reglas» por primera vez.

### Paso A. Conecta el teléfono

1. **Prepara el teléfono** — conéctalo con el cable y desbloquea la pantalla. Ambos ajustes de depuración por USB deben estar activados, como en la [sección 2](#2).
2. **Pulsa «Conectar teléfono»** — es el botón azul grande arriba a la derecha. Mientras el programa busca el teléfono, dirá «Conectando...». La espera puede tardar hasta 20 segundos.
3. **Busca la ventana del juego** — aparecerá una nueva ventana `HeroWarsBot_Arena` con la pantalla del teléfono. ¿No la ves? Puede haberse escondido detrás de la ventana del programa: búscala en la barra de tareas en la parte inferior de la pantalla.
4. **Comprueba el indicador del encabezado** — el rojo «Esperando el teléfono...» debe volverse verde: «conectado». Y el botón azul se convertirá en un botón verde «Empezar a farmear». (El encabezado es la barra superior de la ventana; el indicador es el rectángulo con texto.)

![Teléfono conectado: texto verde «conectado», botón «Empezar a farmear» y al lado la ventana del juego](images/phone_connected.png)

¿La ventana no apareció y en el registro dice «Окно scrcpy не появилось или утилита не найдена!»? Comprueba por orden:

- :smartphone: La pantalla del teléfono está desbloqueada, el cable está bien firme. Prueba otro puerto USB.
- :terminal: En el símbolo del sistema `adb devices` muestra la palabra `device` junto a tu teléfono. Si indica `unauthorized`, autoriza la depuración en la pantalla del teléfono.
- :terminal: En el símbolo del sistema `scrcpy --version` responde con la versión. ¿No responde? La carpeta con scrcpy no se añadió al PATH; vuelve a la [sección 2](#2). Después de editar el PATH, debes cerrar el programa y volver a abrirlo.

### Paso B. Entra en el pasillo de la Mazmorra

La Mazmorra de titanes es un modo de juego donde bajas por los pisos y combates con enemigos en cada sala. El **pasillo** es la pantalla entre combates: en ella se ve una puerta con una bandera y nada más está abierto. El bot empieza desde el pasillo.

1. **Abre el juego** — en el teléfono inicia Hero Wars y entra en la Mazmorra de titanes.
2. **Quédate en el pasillo** — si hay un combate en curso, termínalo tú mismo y cierra la ventana de resultados. Se necesita una pantalla tranquila con la puerta y la bandera.

![Pasillo de la Mazmorra de titanes: junto a la puerta se ve la bandera](images/dungeon_corridor.png)

> [!warning] No inicies el farmeo en medio de un combate. Primero el bot examina la pantalla y pone orden: si ve un combate, se retirará de él; si ve la ventana de resultados con el botón «De nuevo», cancelará este combate y volverá a jugar la sala; si ve la selección de equipo, librará el combate y lo cancelará de inmediato. Luego seguirá funcionando, pero tu victoria se perderá en vano.

### Paso C. Empieza a farmear

> [!warning] **El idioma del programa debe coincidir con el idioma del juego.** Los botones con texto («Atacar», «Aceptar», «De nuevo») y la bandera de la puerta son reconocidos por el bot a través de imágenes en el idioma seleccionado en el programa. Es el botón con dos letras («RU» o «ES») en la parte inferior de la barra izquierda. Si el juego está en español, el programa debe estar en «ES». Si los idiomas son diferentes, el bot simplemente no encontrará los botones.

1. **Pulsa «Empezar a farmear»** — el botón verde donde estaba «Conectar teléfono». El programa ajustará automáticamente la ventana del juego al tamaño correcto y la colocará en la esquina superior izquierda de la pantalla.
2. **No te asustes si la ventana del programa desaparece** — se ha minimizado a la barra de tareas y debajo del juego ha aparecido una barra estrecha: la **mini barra**. En ella se ve lo que está haciendo el bot. Para restaurar la ventana: el icono «Abrir la ventana del programa» en la mini barra (pasa el ratón por encima y aparecerá la sugerencia) o el botón en la barra de tareas.
3. **Observa el juego** — tras unos segundos el bot pulsará en la puerta y comenzará la primera sala. Una sala tarda aproximadamente entre medio minuto y un minuto.
4. **Recuerda cómo detener al bot** — la tecla F10 lo detiene de inmediato, F9 lo pone en pausa (el bot terminará de jugar la sala y esperará). Las teclas funcionan cuando la ventana del juego o la ventana del programa están activas.

Al maximizar la ventana del programa, echa un vistazo al registro. Delante de cada línea hay una hora; la hemos omitido. Esto es lo que debería aparecer:

- `[УМНЫЙ СТАРТ] Сканирую экран для восстановления контекста...` — el bot examina el entorno.
- `[УМНЫЙ СТАРТ] Контекст не требует экстренных действий. Начинаю с HALLWAY.` — todo está bien, comienza desde el pasillo («HALLWAY» significa «pasillo» en inglés).
- `[СТАТИСТИКА] Комнат: 1` — primera sala completada. ¡Todo funciona!
- :triangle-alert: `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — el bot espera a que la ventana del juego vuelva a ser la principal. Haz clic en ella con el ratón y el trabajo continuará.

¿Ha pasado un minuto y el bot no pulsa nada? Comprueba:

- :gamepad-2: En el juego actualmente estás en el pasillo de la Mazmorra de titanes, no en un menú, tienda o combate.
- :globe: El idioma del programa coincide con el idioma del juego (advertencia anterior).
- :maximize-2: La ventana del juego está entera en la pantalla: no estirada, no maximizada, no fuera de los bordes. De lo contrario, detén al bot (F10), pulsa «Restablecer el tamaño de la ventana del juego» y vuelve a empezar.
- :terminal: En el registro no hay líneas con «[ОШИБКА]». Si las hay, las analizaremos en la sección «Si algo sale mal».

### Mientras el bot trabaja

- :monitor: La ventana del juego debe estar a la vista: no la cubras con otras ventanas ni la minimices. Si haces clic en otra ventana, el bot se detendrá y esperará.
- :smartphone: No cierres la ventana del juego ni muevas el cable. Si la ventana desaparece, el programa detendrá al bot por sí solo («Окно scrcpy закрыто — останавливаю бота»).
- :maximize-2: No estires ni maximices la ventana del juego: el bot mide su tamaño al iniciar y luego usa esa referencia.
- :gamepad-2: No pulses la pantalla del teléfono tú mismo: el bot pulsa a través de ADB y os interferiréis mutuamente. Si quieres jugar manualmente, pon el bot en pausa (F9) y espera a que se quede en el pasillo.
- :triangle-alert: No bloquees el ordenador (Win+L): en un PC bloqueado el bot no ve la pantalla y espera a que vuelvas.
- :moon: Para farmear de noche, desactiva la suspensión del ordenador: en la «Configuración» de Windows abre «Sistema» → «Inicio/apagado» y para la pantalla y la suspensión selecciona «Nunca». Un monitor en suspensión o apagado es lo mismo que uno bloqueado: el bot se detendrá y esperará. Los nombres de las opciones dependen de la versión de Windows.

### Botones del encabezado

Arriba a la derecha, junto al indicador, hay tres iconos. Pasa el ratón sobre cualquiera de ellos y aparecerá una descripción.

![Encabezado de la ventana: indicador del teléfono, tres botones y botones de ventana](images/header_buttons.png)

- :moon: **«Apagar la pantalla del teléfono»**: apaga la pantalla del teléfono, pero el juego continúa ejecutándose y el bot sigue viéndolo todo. Cómodo de noche: menos carga en la pantalla y la batería. El programa trae la ventana del juego al frente y pulsa Alt+O en ella (así apaga la pantalla scrcpy). Para reactivar la pantalla: pulsa el botón de encendido del teléfono. En la mini barra hay un botón idéntico.
- :refresh-cw: **«Reiniciar scrcpy»**: cierra la ventana del juego y la vuelve a abrir. Útil si la imagen del teléfono se congela. Solo funciona con la ventana iniciada por el propio programa. No la pulses mientras el bot esté funcionando: si la ventana desaparece, el programa lo considerará un corte de conexión y detendrá el bot.
- :maximize-2: **«Restablecer el tamaño de la ventana del juego»**: devuelve a la ventana `HeroWarsBot_Arena` el tamaño 1606 × 748 y la coloca en la esquina superior izquierda. Es el tamaño estándar: la búsqueda de botones está ajustada a él. Si estiraste o maximizaste la ventana, pulsa el botón antes de «Empezar a farmear» (aunque «Empezar a farmear» hace lo mismo automáticamente). La ventana es ancha: en un monitor Full HD (1920 × 1080) cabe entera, y el bot solo ve lo que hay en pantalla.

### Ventana del programa sin marco de Windows

La ventana del programa no tiene el marco habitual de Windows, por lo que tiene sus propios botones, arriba a la derecha tras una fina línea:

- :minus: **«Minimizar»**: oculta la ventana en la barra de tareas.
- :square: **«Maximizar»**: pone la ventana a pantalla completa; después el botón se llama «Restaurar tamaño». Hacer doble clic en el encabezado hace lo mismo.
- :x: **«Cerrar»**: cierra el programa y junto con él la ventana del juego si la abrió el programa. Si el bot está funcionando, primero preguntará «¿Detener el bot?»; el botón «Detener y cerrar» lo detendrá de inmediato y el resumen de la sesión no se enviará a Telegram.
- :grip-vertical: **Mover la ventana**: arrastrando el encabezado, desde el espacio vacío de arriba o desde el título.
- **Cambiar el tamaño**: desde la esquina inferior derecha (tres líneas diagonales). La ventana no se volverá extremadamente pequeña.

> [!note] No confundas «Minimizar» y «Minimizar a la mini barra». «Minimizar» simplemente oculta la ventana en la barra de tareas. «Minimizar a la mini barra» es un botón en la pantalla principal mientras el bot está funcionando: además muestra la mini barra debajo del juego.

> [!done] Teléfono conectado, el bot ha completado la primera sala: la base está lista. A continuación veremos qué muestra la página principal y cómo leer el registro. [Siguiente sección →](#4)

## Página principal y registro

Inicio es el primer botón en la barra izquierda, y es el que verás más a menudo. Es similar al panel de control de un coche: arriba, los números («a dónde vamos» y «cómo vamos»); abajo, el registro donde el bot anota por sí solo lo que hace. Analizaremos dónde está cada cosa y cómo no perderse entre las líneas del registro.

### Tarjeta superior: cambia de aspecto automáticamente

En la parte superior de la página principal hay una tarjeta grande, pero muestra cosas diferentes según el estado actual del bot:

- :sliders-vertical: **«Configuración de inicio»**: el bot está detenido y los ajustes ya están guardados. Es «con qué irá el bot al combate»: objetivo, modo y umbrales.
- :activity: **«Sesión actual»**: el bot está funcionando. Números en vivo: cuánto se ha recogido, cuánto se ha superado y cuánto tiempo ha transcurrido.
- :file-text: **«Resumen de la sesión»**: el bot se ha detenido. La tarjeta muestra qué se ha conseguido y por qué se ha detenido.
- :list: **«Por dónde empezar»**: solo mientras no hayas guardado la configuración ni una sola vez (se describe en la [sección 3](#3)).

Una sesión es una sola ejecución del bot: desde «Empezar a farmear» hasta la detención.

### Configuración de inicio

Cuatro indicadores y cada uno responde a una pregunta. Los números se toman de tus ajustes, por lo que, si algo no te convence, pulsa «Cambiar en el Maestro de reglas →» en la esquina superior derecha de la tarjeta: se abrirá el «Maestro de reglas».

![Página principal antes del inicio: tarjeta «Configuración de inicio» y registro vacío](images/main_config.png)

- :target: **«Objetivo de la sesión»**: cuándo debe detenerse el bot. El objetivo es **uno**: titanita, salas, pisos o tiempo. Si en la configuración se establecen varios, se toma el primero en el orden «titanita → salas → pisos → tiempo». Si no has cambiado nada, el objetivo es 120 de titanita (entre 10 y 20 salas). «Sin límite» significa que todos los objetivos son cero y el bot continuará hasta que lo detengas.
- :shield-check: **«Modo»**: indicador «El bot decide solo» con la etiqueta «ON» u «OFF». Activado: tras un mal combate, el bot volverá a jugar el combate por sí solo con otro pack. Desactivado: te llamará. Detalles en las secciones sobre el «Maestro de reglas».
- :heart-pulse: **«Umbral de pánico de PS»**: por ejemplo, 40%. Si después de un combate a alguno de los titanes le queda menos salud, el combate se considera malo. Un pack es un equipo de cinco titanes; los PS son la salud.
- :calendar: **«Reinicio del día»**: por ejemplo, 05:00. A partir de esa hora comienza un nuevo día en el juego: el bot calcula las estadísticas del día y olvida cuánta salud tenían los titanes ayer.

> [!note] El bot lee los ajustes **una sola vez, cuando pulsas «Empezar a farmear»**. Si cambias algo durante el funcionamiento, el bot solo se enterará en el siguiente inicio. Por lo tanto, mientras el bot funciona, la tarjeta muestra exactamente los ajustes con los que arrancó.

### Sesión actual

Cuando el bot está iniciado, la tarjeta se transforma en «Sesión actual». Arriba a la derecha brilla el estado:

- :activity: **«Farmeo en curso»**: todo está bien, el bot está trabajando.
- :pause: **«Pausa»**: has pulsado «Pausa» (o el bot ha entrado por sí solo en pausa suave). El botón habrá cambiado a «Continuar».
- :triangle-alert: **«Esperando tu decisión»**: en la pantalla está la ventana «Se requiere intervención» y el bot espera respuesta.
- :refresh-cw: **«Iniciando el bot…»**: los primeros segundos tras «Empezar a farmear».

![Farmeo en curso: indicadores de sesión con barras de progreso hacia el objetivo](images/main_session.png)

Hay cuatro indicadores:

1. **«Titanita en la sesión»**: cuánta titanita ha recogido el bot. Esto es un **conteo, no una lectura de pantalla**: 6 por sala y 12 si en el juego brilla el icono «x2». Si el objetivo es titanita, al lado aparecerá «recogido / necesario», porcentajes y una barra.
2. **«Pisos superados»**: un piso se contabiliza cuando el bot recoge la recompensa en el punto de guardado (así se llama el lugar al final del piso donde se pulsa «Activar» y «Reclamar»). Al lado se indica en qué puerta ha entrado en último lugar: agua, tierra, fuego o mixta.
3. **«Combates en la sesión»**: por ejemplo, «12 victorias de 14». Una victoria es una sala contabilizada. Un deshacer es un combate que el bot ha vuelto a jugar: también cuenta como combate, por lo que el «total» puede ser mayor que las «victorias».
4. **«Tiempo de sesión»**: horas:minutos:segundos y en pequeño «sala de media 28 s». El promedio se calcula por salas, sin contar la espera en el punto de guardado.

> [!tip] Si el objetivo son salas o tiempo, los porcentajes están a la derecha como «35% de 100» o «35% de 120 min» (el objetivo no cabe dentro de la cifra). La barra debajo del indicador es la misma.

> [!note] Cuando se alcanza el objetivo, el bot no abandona el piso a la mitad. Escribirá en el registro `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, completará las salas restantes y se detendrá ante el punto de guardado sin pulsar «Activar»: recogerá la recompensa del piso en primer lugar en el siguiente inicio. La excepción es el objetivo por pisos: en ese caso, el bot se detiene inmediatamente después de la recompensa.

### Resumen de la sesión

El bot se ha detenido: la tarjeta muestra el resumen y la ventana se restaura automáticamente desde la mini barra. Arriba figura el motivo de la detención: el botón «STOP», la ventana de scrcpy cerrada, la finalización habitual del trabajo o lo que el propio bot haya escrito (por ejemplo, que se alcanzó el objetivo).

![Resumen de la sesión: motivo de detención, cifras y botón «Detalles»](images/main_summary.png)

Los mismos cuatro indicadores que en la sesión, pero ahora son las cifras definitivas; en «Combates» se añade «ventanas SOS: N» (cuántas veces te ha llamado el bot). El botón **«Detalles»** abre una ventana con el informe completo del bot: tiempos medios por etapas, las salas más largas, cuántos deshaceres hubo y cuántos de ellos realizó el bot **sin ti**. El icono ✕ a la derecha oculta el resumen y en su lugar vuelve a verse la «Configuración de inicio». Si pulsas «Empezar a farmear», el resumen desaparecerá por sí solo.

> [!note] Si Telegram está configurado, el resumen llegará allí automáticamente en cualquier detención habitual. El botón «STOP» (F10) interrumpe el bot al instante, por lo que el resumen a Telegram no se enviará en ese caso.

### Registro: qué hay en él y cómo leerlo

La parte inferior de la pantalla principal es el **«Registro de trabajo»**. El bot anota en él cada paso que da y el programa lo muestra en la ventana. No te asustes por la cantidad de líneas: no es necesario leerlo todo; el registro se necesita cuando algo sale mal o cuando sientes curiosidad.

Cada línea está estructurada de la misma manera:

`10:26:17.486 [НАВИГАЦИЯ] Двери (слева направо): EARTH (0.98), FIRE (0.97)`

1. **Hora**: en gris. Horas:minutos:segundos y milésimas de segundo.
2. **Etiqueta entre corchetes**: «quién habla» y sobre qué asunto. Está coloreada: el color indica a qué sección del registro pertenece la línea.
3. **Texto**: qué ha ocurrido exactamente. Una línea larga se ajusta y la continuación se coloca debajo del texto, no debajo de la hora.

Una línea sin etiqueta (por ejemplo, ` ---> HYPERION: ХП 100%, Энергия 79%`) es la continuación de la línea superior y pertenece a la misma sección.

### Píldoras de filtro

Encima del registro hay cinco botones «píldora». Pulsa uno y en el registro solo quedarán las líneas de esa sección. La elección se recuerda: si abres el programa mañana, estará seleccionada la misma píldora.

![Registro con píldoras «Todo», «Combates», «Reglas», «Sistema» y «Errores»](images/journal_pills.png)

- **«Todo»**: todo junto.
- **«Combates»** (etiquetas verdes): desarrollo del recorrido: salas, tiempo, salud de los titanes, deshaceres. Etiquetas `[КОМБАТ]`, `[СТАТИСТИКА]`, `[ВРЕМЯ]`, `[СОСТОЯНИЕ]`, `[АНАЛИЗАТОР]`, `[ОТКАТ]`, `[ЛИМИТ]`, `[ИТОГ]`.
- **«Reglas»** (etiquetas amarillas): decisiones del bot: qué pack colocar, por qué deshizo un combate, qué recordó. Etiquetas `[ТАКТИКА]`, `[КОМАНДА]`, `[ПРАВИЛА]`, `[ОБУЧЕНИЕ]`, `[SOS_CLOSE]`.
- **«Sistema»** (etiquetas celestes): todo lo demás: pasillo y puertas (`[НАВИГАЦИЯ]`), inicio (`[УМНЫЙ СТАРТ]`), conexión. Las líneas del propio programa con la etiqueta `[GUI]` son grises, pero también están aquí.
- **«Errores»** (etiquetas rojas): todo lo que requiere atención: `[ОШИБКА]`, `[ВНИМАНИЕ]`, `[СТОРОЖ]`, `[SOS]`. Junto al nombre aparece un número: cuántas líneas de este tipo se han acumulado.

> [!warning] Un número rojo en «Errores» no siempre es un fallo. Ahí entra también `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...`: el bot simplemente espera a que devuelvas la ventana del juego al primer plano. Lee el texto de la línea en lugar de asustarte por el color.

### Ejemplos de líneas reales

Estas son líneas de una sesión real del bot (la hora se omite por brevedad). Aprende a leer estas cinco y entenderás cualquier registro.

- `[НАВИГАЦИЯ] Выбрана комната EARTH (порядок: water → mix → earth → fire)` — el bot ha elegido la puerta de tierra. Entre paréntesis figura tu orden de puertas. El número en la línea «Puertas (de izquierda a derecha)» superior indica qué tan seguro está el bot de haber reconocido la puerta (1: totalmente).
- `[ВРЕМЯ] Комната 2 (earth): коридор 12.8 с | сборка 3.3 с | бой 8.0 с | результат 9.1 с | всего 33.2 с` — informe de la sala: cuánto tiempo se necesitó para ir a la puerta, montar el equipo, combatir y cerrar la ventana de resultados.
- `[СТАТИСТИКА] Комнат: 3 | Титанит: 36` — tercera sala completada, 36 de titanita recogida. Estos números son los que llegan a los indicadores de la sesión.
- `[ТАКТИКА] Откатываю бой сам и переиграю паком [...] (взят: ваш список запасных паков).` — el combate resultó malo y el bot (modo «El bot decide solo») lo vuelve a jugar con un pack de reserva. Si el de reserva lo logra: `[ТАКТИКА] Запасной пак [...] справился. Запоминаю его против этих врагов.`
- `[ОТКАТ] Запускаю протокол отката боя...` — inicio del deshacer: «De nuevo» → pausa → «Retirarse». Cada línea de este tipo añade un combate en el indicador «Combates en la sesión».

> [!tip] Al principio de cada sesión, el bot escribe `[ТАКТИКА] Плохой бой: ХП ниже 30% | потеря больше 60% | ...`: los umbrales según los cuales juzgará los combates. Si algo sale «diferente a lo que esperabas», comprueba primero esta línea con tus ajustes.

### Botones debajo del registro

![Botones debajo del registro: «Guardar registro», «Enviar registro al autor», «Limpiar»](images/journal_buttons.png)

- :save: **«Guardar registro»**: guardará todo el registro en un archivo de texto. El programa propondrá automáticamente el nombre `gui_log_...txt` y la carpeta `bot_data/logs`; se puede elegir otra.
- :mail: **«Enviar registro al autor»**: primero realiza la misma acción de guardado y luego se abrirá tu cliente de correo con un mensaje preparado. **Adjunta el archivo al correo tú mismo** (junto con `battle_log.csv` de la misma carpeta): el programa no puede hacerlo por sí solo. ¿No tienes programa de correo? Escribe al autor a la dirección indicada en la sección «Acerca de».
- :x: **«Limpiar»**: elimina las líneas de la ventana, pero primero preguntará «¿Limpiar el registro?». Es seguro: el bot guarda automáticamente el registro completo en la carpeta `bot_data/logs` y las cifras de la sesión no se reinician.

Puedes seleccionar texto en el registro con el ratón y copiarlo con Ctrl+C o haciendo clic derecho («Copiar»). El registro no se puede modificar: es solo de lectura. Si desplazas el registro hacia arriba para leer, no «se escapará» hacia abajo con las nuevas líneas; desplázate hasta el final y volverá a avanzarse junto con el bot.

> [!note] La ventana recuerda las últimas 50 000 líneas y muestra las últimas 4000; de lo contrario, en un farmeo largo se ralentizaría. Todo lo demás se encuentra en el archivo `bot_data/logs/bot_log_...txt`: el bot lo gestiona por sí solo y normalmente no hace falta guardar el registro a mano.

Mientras el registro esté vacío, en su lugar aparecerá el texto «El registro está vacío». Las líneas aparecerán después de conectar el teléfono. Una píldora vacía muestra «Aún no hay nada aquí» y «Todavía no hubo líneas de este tipo»; para «Errores» esto es una buena noticia.

> [!done] Ahora lees la pantalla principal como un panel de control: sabes qué significan los indicadores y los colores de las etiquetas del registro. A continuación: la mini barra, un pequeño panel debajo del juego. [Siguiente sección →](#5)

## Mini barra debajo del juego

Mientras el bot trabaja, la ventana principal del programa normalmente no la necesitas. Por eso se minimiza sola a la barra de tareas, y debajo de la imagen del juego aparece una barra estrecha — **mini barra**. Es como el panel de control de un coche: de un vistazo se ve si el bot se mueve, qué está haciendo ahora, cuánto ha recorrido ya y si te está llamando.

![Mini barra debajo de la ventana del juego durante el farmeo](images/mini_bar.png)

### Cuándo aparece y dónde se coloca

- :monitor: **Aparece sola.** El bot se ha iniciado («Empezar a farmear») — la ventana del programa se minimiza y debajo del juego aparece la mini barra. Si has maximizado la ventana del programa y quieres volver a ocultarla mientras el bot trabaja, haz clic en «Minimizar a la mini barra» en la pantalla principal.
- :smartphone: **Se sitúa justo debajo del juego** y tiene exactamente el mismo ancho que la imagen del juego. Si mueves la ventana del juego, la mini barra la sigue (el programa lo comprueba dos veces por segundo).
- :eye: **No tapa el juego ni por un píxel.** Esto es importante: el bot «mira» la pantalla tomando capturas de la ventana. Si la barra se superpusiera al juego, el bot la vería a ella en lugar de los botones.
- :maximize-2: **Si no hay espacio abajo** (la ventana del juego está en el borde inferior de la pantalla), la barra se colocará sobre el título de la ventana. Si tampoco hay espacio ahí, no se mostrará y la ventana del programa se quedará en la barra de tareas. Si minimizas la ventana del juego, la barra se ocultará y volverá junto con ella.

> [!tip] ¿No ves la mini barra y el bot está funcionando? Mueve la ventana del juego más arriba: se necesitan unos 100 píxeles de espacio libre debajo. Puedes mover la ventana, pero no cambiar su tamaño (esto lo vimos en la sección 3).

### Qué hay en la barra: cinco columnas de izquierda a derecha

- :activity: **Estado.** Una palabra y un punto de color que «respira» mientras todo esté bien: «INICIO», «FARMEANDO», «PAUSA», «PAUSA DE DEPURACIÓN» o un «SOS» rojo. Abajo — **lo que hace el bot justo ahora** y cuántos segundos lleva: por ejemplo, «Combate · Fuego · 12 s». Luego «Salas: 12 · pisos: 2» y el tiempo de la sesión, por ejemplo «Tiempo 00:42:17».
- :target: **Objetivo.** El nombre del objetivo, cuánto se ha hecho, cuánto se necesita y una barra de progreso. Abajo — «~28 s por sala» (tiempo medio; antes de la primera sala dirá «tiempo por sala — tras la primera») y el pronóstico «objetivo en ≈ 1 h 10 min». El bot calcula la estimación según la velocidad de **esta** sesión, por lo que al principio varía y luego se estabiliza. Si no hay objetivo («Sin límite»), no hay barra y en lugar de estimación muestra «≈ N de titanita por hora».
- :heart-pulse: **Salud del equipo.** Los cuadros de los titanes que estuvieron en el último combate y sus PS después de este, en el mismo orden en que aparecen en la pantalla del juego. Antes del primer combate pone «aún no hay combates». El color del número te orienta: rojo — PS por debajo del umbral de pánico (general o personal), amarillo — por debajo del umbral a partir del cual el bot cura al titán, color normal — todo bien. Un guion «—» significa que no se pudo encontrar el icono del titán en la ventana de resultado.
- :list: **Eventos.** Las últimas cuatro líneas, la más reciente arriba y más grande. A la izquierda una etiqueta de color, a la derecha la hora.
- :gamepad-2: **Botones.** Cuatro botones en un cuadrado de 2×2.

### Qué puede «hacer ahora» el bot

En la primera columna, el bot indica por sí mismo en qué etapa está. Esto es lo que significan esas palabras:

- **«Pasillo»**, **«Eligiendo puerta»**, **«Montando el equipo»**, **«Combate»**, **«Ventana de resultado»** — el ciclo habitual de una sala. A las etapas «Montando el equipo», «Combate», «Ventana de resultado» y «Retirada» se les añade el elemento de la sala: «Combate · Agua · 12 s».
- **«Punto de guardado»** — piso superado, el bot recoge la recompensa.
- **«Retirada»** — la batalla fue mala, el bot se retira y prepara la repetición.
- **«Revisa la pantalla»** — tras el inicio, el bot examina la pantalla y decide por dónde empezar (este es el «inicio inteligente»).
- **«Pausa en el pasillo»**, **«Esperando tu decisión»**, **«Juegas tú»** — el bot está detenido porque pulsaste pausa, porque te ha consultado o porque elegiste «Jugar a mano».
- **«Espera la ventana del juego»** y **«Espera conexión»** — el bot está esperando: bien porque el juego no está en primer plano (ver abajo), o bien porque no hay conexión con el servidor del juego.

Si el mismo texto se mantiene más de lo normal, el número de segundos a la derecha aumenta y te avisará de que el bot en realidad está detenido.

### Eventos: etiquetas y lo que significan

La etiqueta de la izquierda muestra de qué trata el evento:

- **Nombre del elemento** («Agua», «Tierra», «Fuego», «Mixto») — sala completada. Una línea como «Sala 45 completada · 28 s · menos PS: Araji 36%» indica cuántos segundos llevó la sala y quién se quedó con la salud más baja.
- **«Piso»** — piso superado («Piso superado, 3 en total»).
- **«Retirada»** — el combate se repite. **«SOS»** — motivo de la llamada en palabras sencillas.
- **«Pausa»** — «Pausa: el bot terminará el combate y esperará», luego «El bot espera en el pasillo».
- **«Bot»** — «Bot iniciado», «Pausa quitada, el bot sigue», «Sin respuesta 10 min — el bot decidió solo».
- **«Límite»** — la sesión alcanzó el objetivo, el bot termina de jugar hasta el punto de guardado.
- **«Atención»** — «La ventana del juego no está activa — el bot espera. Haz clic en el juego».
- **«Error»** — el texto del error tal y como lo escribió el bot.

Las líneas largas se recortan con puntos suspensivos. El texto completo siempre está disponible en el registro de la pantalla principal.

### Botones

Pasa el ratón por encima y aparecerá una etiqueta. Todos los botones hacen lo mismo que sus equivalentes «mayores» en la ventana principal y en la cabecera.

- :pause: **Pausa / Continuar** — «Pausa suave: el bot termina el combate y espera (F9)». En pausa, el icono se convierte en un triángulo verde y el mismo botón quita la pausa. Mientras el bot solo se está iniciando, el botón no está disponible.
- :square-filled: **STOP** — «Parada de emergencia: el bot se detiene al instante, sin resumen en Telegram (F10)».
- :moon: **Pantalla del teléfono** — «Apagar la pantalla del teléfono», el juego sigue funcionando.
- :maximize-2: **Maximizar** — «Abrir la ventana del programa». La mini barra desaparecerá. El botón de la ventana del programa en la barra de tareas da el mismo resultado. Si quieres volver a ver la barra, usa el botón «Minimizar a la mini barra» en la pantalla principal.

> [!note] Cuando el bot te llama, la mini barra se pone roja y la ventana «Se requiere intervención» aparece sola, en el centro de la imagen del juego; no hace falta abrir la ventana del programa. En ese momento, el primer botón no pone en pausa ni «continúa»: muestra la ventana SOS si ha quedado debajo de otras ventanas (la etiqueta es «Mostrar la ventana SOS: el bot espera tu decisión»). Una vez respondes en la ventana, la mini barra vuelve a la normalidad. Cómo responder lo veremos en la sección sobre las ventanas SOS.

![Mini barra durante un SOS](images/mini_bar_sos.png)

### Regla principal: el bot solo funciona mientras el juego está en primer plano

El bot toma capturas de pantalla y busca botones en ellas. Si otro navegador, mensajería o el explorador de archivos se coloca sobre el juego, aparecerán en la captura en lugar del juego: el bot podría hacer clic «donde no debe». Por eso, en cuanto otra ventana pasa a estar activa, se detiene y espera. En el registro aparece la línea «[ВНИМАНИЕ] Окно игры перекрыто … Бот ждет фокуса…», en la mini barra — la etiqueta «Atención» y la etapa «Espera la ventana del juego». Si haces clic en el juego — «[ИНФО] Окно снова активно. Продолжаем работу.»

- :monitor: **Hacer clic en la mini barra no detiene al bot.** La mini barra está diseñada para no convertirse en la ventana activa: el juego sigue siendo el «principal» mientras pulsas botones en el panel.
- :triangle-alert: **«Maximizar» detiene al bot temporalmente.** La ventana del programa pasa a estar activa y el juego no, por lo que el bot se detendrá en el paso más cercano. Cuando termines, haz clic en la ventana del juego y el bot continuará. El vigilante no considera este tiempo de espera como una «congelación».
- :gamepad-2: ¿Quieres trabajar en el ordenador mientras el bot farmea? Abre otras ventanas **al lado**, no sobre el juego, y no hagas clic en ellas. O pospone tus tareas hasta hacer una pausa (F9).

> [!warning] Las teclas rápidas F9 y F10 solo funcionan cuando la ventana del juego o la ventana del programa están activas. Si pulsas F10 en el navegador, el bot no se detendrá: las teclas no responden cuando estás ocupado en otra cosa. Más detalles en la sección sobre pausa y parada.

> [!done] Ahora ya lees la mini barra como un panel de control y sabes por qué no se debe ocultar el juego debajo de otras ventanas. A continuación: pausa, parada y teclas rápidas. [Siguiente sección →](#6)

## Pausa, parada y teclas rápidas

El bot recorre la Mazmorra solo, pero a veces hace falta frenarlo: quieres jugar manualmente, ausentarte por asuntos propios o simplemente terminar. Para ello hay **cuatro métodos**, y se diferencian en **cuán suavemente** se detiene el bot. Imagina un coche: la «pausa» es aparcar en el arcén y apagar el motor, mientras que la «parada de emergencia» es sacar la llave en marcha. Ambos funcionan, pero de forma distinta.

### Pausa suave: «Pausa F9»

El método más cuidadoso. Pulsa el botón «Pausa» en la pantalla principal, en la mini barra o la tecla **F9**.

1. **Pulsa «Pausa» o F9.** En el registro aparecerá la línea `[GUI] Сигнал 'Мягкая пауза' отправлен. Бот остановится перед следующей дверью.`
2. **Espera a que el bot termine la sala.** No abandona el combate que ya está en curso: lo terminará, cerrará la ventana de resultado y anotará el resumen de la sala.
3. **El bot se detiene en el pasillo.** En el registro: `[МЯГКАЯ ПАУЗА] Бот ждет в коридоре...`. El estado en la pantalla principal es «Pausa», en la mini barra «PAUSA», y el botón pasa a ser el verde «Continuar».
4. **Haz tus asuntos y pulsa «Continuar» (o F9 de nuevo).** El bot escribe `[ИНФО] Пауза снята. Кэш составов и здоровья очищен. Включаю механизм Умного Старта.` y continúa.

> [!note] «Caché limpiada» significa que el bot **ha olvidado** qué equipos estaban puestos y cuánta salud tenían los titanes: mientras te ocupabas del juego, todo pudo haber cambiado. Antes del siguiente combate, volverá a mirar la pantalla de selección de equipo y leerá la salud desde allí. El «inicio inteligente» ocurre cuando el bot primero mira lo que hay en pantalla y solo después decide qué hacer (por ejemplo, cerrar una ventana de resultado olvidada).

- :eye: **Durante la pausa puedes mirar el teléfono y cambiar ajustes en la ventana del programa.** Pero el bot solo aplicará los nuevos ajustes en el siguiente «Empezar a farmear» (más detalles en la sección sobre la pantalla principal).
- :door-open: **Si has tocado algo en el juego, vuelve al pasillo de la Mazmorra** (donde se vea el banderín en la puerta) y luego pulsa «Continuar». De este modo el bot entenderá con certeza dónde se encuentra.
- :gauge: **El tiempo transcurre también durante la pausa.** Si el objetivo de la sesión es el tiempo («120 minutos»), la pausa consumirá parte de ese tiempo. En cambio, el «vigilante» (el que supervisa si el bot se ha congelado) no cuenta el tiempo de pausa y no dará la alarma.

> [!tip] ¿Quieres ausentarte toda la noche o por mucho tiempo? No necesitas la pausa suave para eso: establece un objetivo (titanita, salas, pisos o tiempo) en la pantalla principal y el bot llegará solo al punto de guardado, se detendrá y te enviará el resumen.

### Cuándo el bot pone la pausa él mismo

A veces el bot pide ayuda y se pone él mismo en pausa suave. En ese caso, el botón también muestra «Continuar» y en el registro se escribe `[ВНИМАНИЕ] Бот на мягкой паузе: ...` con el motivo. Esto ocurre cuando:

- el bot no ha superado ninguna sala tres veces seguidas durante 5 minutos (el vigilante decidió que se congeló);
- la retirada del combate falló (no se reconoció la pantalla, no se pulsaron los botones);
- el combate ni siquiera empezó, incluso tras una larga espera;
- no respondiste a la ventana «No hay pack adecuado» y no hay equipo de reserva.

En esos casos, primero **mira la pantalla del teléfono**, corrige lo que se haya roto (cierra la ventana sobrante, vuelve al pasillo) y solo entonces pulsa «Continuar». Si Telegram está configurado, el bot enviará un mensaje con una captura de pantalla.

### Parada de emergencia: «STOP F10»

El botón rojo «STOP» (o la tecla **F10**) detiene al bot **al instante**: el programa fuerza el cierre del proceso del bot. En el registro aparece `[GUI] ЭКСТРЕННЫЙ СТОП. Процесс убит.`, y en la tarjeta de resumen el motivo es «detenido con el botón «STOP»».

> [!warning] Lo que se pierde con F10: el bot no tiene tiempo de escribir el bloque `[ИТОГ]` en el registro y **no envía el resumen de la sesión a Telegram**. Si en ese momento estaba en combate, el combate en el juego continuará (o se quedará en pantalla); lo verás en el teléfono. Las salas ya superadas quedan guardadas en las estadísticas: el bot las registra inmediatamente después de cada sala.

Cuándo se necesita precisamente este botón: si el bot se comporta de forma extraña (hace clic donde no debe, no responde a «Pausa») o si hace falta pararlo todo de inmediato. En los demás casos es mejor usar la pausa o Ctrl+Q.

### Teclas rápidas: qué funciona y dónde

- :pause: **F9** — pausa / «Continuar» (lo mismo que el botón «Pausa» en la pantalla principal).
- :square-filled: **F10** — «STOP».
- :gamepad-2: **Ctrl+Q** — detenerse **con resumen**: el bot terminará la sala iniciada, se detendrá en el pasillo y enviará el resumen de la sesión. En el registro: `[ИНФО] Команда 'Ctrl+Q' принята! Бот завершит бой и остановится.`, motivo de parada — «Parada manual por el usuario (Ctrl+Q)».
- :triangle-alert: **Ctrl+Shift+Q** — detenerse **al instante, pero con resumen**: el bot escribe `[ЭКСТРЕННАЯ ОСТАНОВКА]`, registra `[ИТОГ]` y realiza **un** intento de enviar el resumen a Telegram (sin reintentos, para no retrasarse).

Detalles importantes por los cuales las teclas a veces «no funcionan»:

- **F9 y F10 las escucha la ventana del programa** y solo cuando **la ventana del juego o la ventana del programa están activas**. Si pulsas F10 en el navegador o en la mensajería, no ocurrirá nada. Si el juego está minimizado o tapado por otra ventana, usa los botones de la mini barra: funcionan siempre porque la mini barra no le quita el foco activo al juego.
- **Ctrl+Q y Ctrl+Shift+Q las escucha el propio bot**, no la ventana del programa, por lo que funcionan mientras el bot esté en ejecución, incluso si otra ventana está activa.
- **Estas combinaciones también son conocidas por otros programas.** Ctrl+Q cierra muchos programas (Word, Telegram Desktop), y Ctrl+Shift+Q — los navegadores. Mientras el bot trabaja, no las pulses en otras ventanas: el bot también las «escuchará» y se detendrá.
- **El bot comprueba Ctrl+Q cuando está en el pasillo** ante la siguiente puerta. En pausa suave está detenido y no comprueba nada, por lo que Ctrl+Q solo funcionará tras pulsar «Continuar». Y si el bot espera tu respuesta en la ventana SOS, Ctrl+Q lo detendrá al instante.
- **Mantener pulsada la tecla no repite nada:** una pulsación es una orden.
- Si pulsas F9 o F10 cuando el bot no está en ejecución, en el registro aparecerá `[GUI] Нажата F9, но бот не запущен.`

### La cruz de la ventana y el cierre de scrcpy

- :x: **La cruz de la ventana del programa mientras el bot trabaja.** Se abrirá la pregunta «¿Detener el bot?». El botón «Detener y cerrar» cerrará el programa y el bot; y la ventana del juego (scrcpy), si la abrió el propio programa, de inmediato — el resumen no se enviará a Telegram. Si no quieres esto, cierra la ventana de la pregunta y primero detén el bot de forma suave.
- :smartphone: **Si cierras la ventana del juego (`HeroWarsBot_Arena`) tú mismo.** El programa escribirá `[GUI] Окно scrcpy закрыто — останавливаю бота (он напишет итог и пришлёт его в Telegram).` El bot terminará de escribir el resumen de la sesión y lo enviará a Telegram; si no responde en 10 segundos, el programa lo detendrá como con F10.
- :pencil: Si en el «Maestro de reglas» hay cambios sin guardar, la cruz preguntará primero «¿Guardar los cambios?».

### Qué elegir

- **Quiero hacer una pausa y volver** — «Pausa» (F9). Pulsa «Continuar» cuando estés listo.
- **Quiero terminar y recibir el resumen** — Ctrl+Q (el bot terminará la sala, se detendrá y enviará el resumen a Telegram).
- **Necesito parar ahora mismo pero quiero el resumen** — Ctrl+Shift+Q.
- **El bot se ha roto o actúa de forma extraña** — «STOP» (F10), luego revisa el registro.
- **El bot te ha llamado con la ventana SOS y quieres terminar** — el botón «Detener el bot» en esa ventana: el bot se detendrá solo y enviará el resumen. Analizaremos la ventana SOS por separado.

### Resumen de sesión en Telegram

Si Telegram está configurado, el resumen llega tras cualquier parada, **excepto con el botón «STOP»** y al cerrar la ventana del programa: el bot indica si lo detuviste tú mismo («Bot detenido por ti»), si completó el objetivo («Farmeo terminado») o si cayó con un error, cuánto tiempo pasó, cuántas salas, pisos y titanita, si hubo retiradas y ventanas SOS. Si no hay conexión a internet, el bot intentará enviar el resumen dos veces más (a los 10 y 30 segundos) y luego se apagará. Cómo conectar Telegram se explica en una sección independiente.

> [!done] Ahora ya sabes cómo pausar suavemente el bot y cómo detenerlo por completo, y qué hace cada tecla. A continuación: la configuración de reglas para enseñar al bot a colocar los equipos necesarios. [Siguiente sección →](#7)

## Maestro de reglas: «Base y salas»

El «Maestro de reglas» es el segundo botón de la barra izquierda (el icono con deslizadores). Aquí le explicas al bot tres cosas: **cuándo detenerse**, **qué considerar un mal combate** y **con qué equipo ir a cada sala**. Un equipo (o pack) es una formación de 3 a 5 titanes. La página se divide arriba en tres pestañas: «Base y salas», «Autotáctica y PS» y «Reglas e intercepciones». En esta sección tratamos la primera, la más importante: sin ella el bot no sabe ni a quién poner en combate.

![Pestaña «Base y salas»: arriba dos tarjetas con ajustes, abajo cuatro filas con equipos](images/rules_base.png)

Arriba — «Parámetros de sesión» (dos tarjetas), abajo — «Equipos por sala». En la parte inferior de la página, idéntica en cada pestaña, hay una barra gris con botones: «Guardar ajustes» y «Restaurar / Restablecer». Hablaremos de ella al final de la sección. Lo principal que debes recordar de inmediato: **mientras no pulses «Guardar ajustes», nada queda registrado** — ninguna modificación llegará al bot.

### Tarjeta «Objetivos y límites»

- :target: **«Objetivo de la sesión»** — cuándo debe terminar el bot. El objetivo es siempre **uno**, entre cuatro: «Titanita», «Salas», «Pisos» o «Tiempo» (el tiempo en minutos). Elige la opción en la lista y escribe el número en el campo. El campo solo acepta dígitos. La nota «0 — sin límite» significa: el cero desactiva el objetivo y el bot seguirá jugando hasta que lo detengas. La flecha circular a la derecha («Restablecer objetivo») pone 0.
- :gem: **El bot calcula la titanita por sí mismo**, no la lee de la pantalla: 6 por una sala normal y 12 si en la ventana de resultado hay un icono de «x2». Por eso, «120 de titanita» son aproximadamente 20 salas sin «x2». Mientras no hayas guardado los ajustes ninguna vez, el bot tomará por sí mismo el objetivo de «120 de titanita».
- :layers: **El bot no abandona un piso a la mitad.** Al alcanzar el objetivo de «Titanita», «Salas» o «Tiempo», no se detiene en el acto: escribe en el registro `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.`, completa las salas restantes del piso y se coloca ante el punto de guardado sin pulsar «Activar». De este modo el piso no queda a medias, y el bot recogerá la recompensa y contabilizará el piso como primera tarea en la siguiente ejecución. Si no se encuentra un punto de guardado tras 6 salas (en un piso hay 5), el bot se detendrá tal cual está. El objetivo «Pisos» se activa en cuanto se supera el punto de guardado.
- :gauge: **El tiempo transcurre también durante la pausa.** El objetivo «Tiempo — 120» significa 120 minutos desde que se pulsa «Empezar a farmear», incluyendo todas las pausas.
- :calendar: **«Hora de reinicio del día (hora local)»** — a qué hora empieza tu nuevo día de juego. Por defecto a las 05:00. De ella depende a qué día pertenecen los combates en las estadísticas, además de la memoria del bot sobre la salud de los titanes: esta vive dentro de un mismo día de juego y, al empezar un nuevo día, el bot comienza desde cero. Pon la hora a partir de la cual consideras que empieza un nuevo día (por ejemplo, cuando te vas a dormir).
- :send: **«Configurar Telegram»** — abre una ventana independiente donde se activa la conexión con la mensajería. Junto al botón hay un punto y una etiqueta: verde «Avisos SOS activados» o gris «Telegram sin configurar». Cómo conectarlo se explicará en la sección sobre Telegram. Aquí lo importante es esto: el botón «Aplicar» de esa ventana solo modifica esta página. Para que la configuración se guarde en el archivo, pulsa también «Guardar ajustes».

> [!tip] ¿Qué objetivo elegir? «Tiempo» es practical cuando tienes un hueco en tu horario («que el bot trabaje una hora mientras preparo la cena»). «Titanita» — cuando necesitas conseguir una cantidad determinada de recompensa. «Salas» y «Pisos» — cuando quieres hacer exactamente una cantidad fija. Si no estás seguro, deja «Titanita» y 120: es un inicio de prueba corto.

### Tarjeta «Seguridad y modo»

Aquí se decide **qué es un mal combate**. El bot lee la salud de los titanes en la ventana de resultado y compara dos números con los tuyos.

- :heart-pulse: **«Umbral de pánico de PS, %»** — por debajo de qué salud tras el combate la batalla se considera mala. Por defecto 40.
- :swords: **«Delta de pérdida de PS, %»** — cuánta salud puede perder un solo titán en un solo combate. Por defecto 30.

Ambos campos aceptan números enteros del 0 al 100; si escribes cualquier otra cosa, el campo se pondrá rojo con la nota «Escribe un número de 0 a 100» y no se podrán guardar los ajustes hasta que lo corrijas.

Un ejemplo real con umbral 40 y delta 30:

- Araji entró al combate con el 100%, salió con el 80% — **todo bien**: perdió 20, se mantuvo por encima de 40.
- Araji entró con el 100%, salió con el 55% — **mal combate**. 55 está por encima del umbral, pero ha perdido 45 y lo permitido es 30.
- Araji entró con el 50%, salió con el 35% — **mal combate**. Perdió solo 15, pero 35 está por debajo del umbral de pánico.
- Cualquier titán murió o no se encontró en la ventana de resultado — **mal combate** siempre, independientemente de lo que pongas.

Las pérdidas se calculan desde la salud con la que el titán **entró** al combate, no desde el 100%. Por eso un titán herido alcanza el umbral antes que uno sano. Cuanto más alto sea el umbral y menor la delta, más estricto será el bot y con más frecuencia te llamará; un cero en el umbral desactiva la comprobación de «por debajo del umbral» (salvo bajas), y 100 en la delta desactiva la comprobación de pérdidas.

> [!note] El umbral y la delta son generales para todos los titanes. Para un titán individual puedes establecer su propio umbral, y además activar la regla «si tres han perdido mucho — mal combate». Esto se hace en la pestaña contigua «Autotáctica y PS».

Abajo hay dos interruptores:

- :shield-check: **«El bot decide solo»** («Revierte las malas batallas y elige un equipo») — por defecto **desactivado**. Desactivado: mal combate → ventana «Se requiere intervención», el bot te espera. Activado: el bot revierte sin preguntas el combate y vuelve a jugar con un equipo de reserva, además de seleccionar por sí mismo el equipo según la salud de los titanes. En detalle — en la sección sobre el funcionamiento autónomo del bot. Actívalo cuando ya hayas visto funcionar al bot y confíes en los equipos de reserva.
- :swords: **«Control manual de la definitiva de Angus»** («Global, en todas las salas») — por defecto **desactivado**, por lo que cualquier combate, incluido el de Angus, se realiza en combate automático. Si lo activas — para los equipos con Angus el bot pulsa «A luchar», durante un par de segundos activa el combate automático para la definitiva de Angus y lo vuelve a desactivar. El bot no revertirá por sí mismo un combate así, sino que te llamará. Al iniciar, en el registro se ve lo seleccionado: `[ТАКТИКА] Ангус: ...`.

### Equipos por sala

Debajo de la leyenda «El equipo principal va primero; los de reserva, por orden, si la batalla va mal» hay cuatro filas, correspondientes a las salas: «Tierra», «Agua», «Fuego» y «Mixto». Cada una es una tarjeta independiente.

- :users: **El equipo principal** — los cuadros de los titanes debajo del nombre de la sala. El bot lo coloca si no hay motivos para hacer otra cosa (por ejemplo, si se activó una regla de la pestaña «Reglas e intercepciones»). Los titanes se muestran de izquierda a derecha, **tal como se ubican en la pantalla del juego**. Si no hay equipo — en lugar de los cuadros aparece el texto «Pack no established» (o «Pack no establecido»).
- :pencil: **Lápiz («Cambiar equipo»)** — abre la ventana «Arma el equipo».
- :list: **«Equipos de reserva»** con la cantidad «N ud.» — lista desplegable (flecha abajo/arriba). El bot prueba los equipos de reserva por orden si el combate es malo y él decide solo («El bot decide solo» activado o no respondiste a la ventana a tiempo). En cada sala hay hasta 5. Dentro, cada equipo de reserva es una fila `#1`, `#2`, etc., y a la derecha una cruz («Quitar equipo»). El botón «Añadir equipo» abre la misma ventana «Arma el equipo».
- :plus: **«Condición»** — «+ Condición»: un acceso rápido a la regla para esa sala, por ejemplo «si es contra Angus — pon este equipo». Se abrirá la ventana «Nueva regla» con esa sala ya seleccionada. Cómo rellenarla se explicará en la sección de reglas.

Establece el equipo principal en las cuatro salas **antes del primer farmeo**: el bot no conoce a tus titanes y «de fábrica» no tiene equipos configurados.

Cómo armar un equipo:

1. **Haz clic en el lápiz** de la sala deseada. Se abrirá la ventana «Arma el equipo».
2. **Haz clic en los titanes** que quieras añadir. Si haces clic de nuevo, lo quitas. Arriba está el contador: «Elegidos: 3 / 5» y el aviso «Listo para aplicar» (con dos pone «Mínimo 3 · faltan 1»).
3. **Ten en cuenta el elemento de la sala.** En «Tierra», «Agua» y «Fuego» solo entran titanes de ese elemento, mientras que en «Mixto» entran todos, incluida Metis (ella es «elarita» y no entra en otras salas: «Metis — solo en la sala mixta»). Cuando se seleccionan 5, los demás titanes se bloquean.
4. **Pulsa «Aplicar»** (o «Cancelar» si cambiaste de opinión; «Limpiar» quita a todos los titanes de golpe).

![Ventana «Arma el equipo» para la sala «Agua»: tres titanes seleccionados, abajo «Aplicar»](images/rules_picker.png)

> [!warning] «Aplicar» en la ventana «Arma el equipo» solo cambia la página: el equipo aún **no queda registrado** en el archivo. Se registrará cuando pulses «Guardar ajustes». El equipo principal de cada sala se guarda en el archivo `bot_data/rules/<стихия>.yml`, los de reserva y todos los números — en `profile.yml`. No hace falta editar estos archivos a mano.

No se puede añadir por segunda vez un equipo de reserva que ya existe en la lista (en cualquier orden de titanes): aparecerá el aviso «Ese equipo de reserva ya existe».

> [!tip] ¿Qué equipos poner como reserva? Dale opciones al bot: haz que el equipo de reserva se diferencie del principal al menos por un par de titanes. Si Araji suele salir herido del combate, pon en el equipo de reserva a quienes encajen mejor los golpes.

### Guardado y «Restaurar / Restablecer»

La barra inferior muestra el estado: «Todos los cambios guardados» (marca de verificación verde) o «Hay cambios sin guardar» (icono amarillo). Mientras el bot trabaja, al lado se indica «El bot usará los nuevos ajustes en su próximo inicio».

- :save: **«Guardar ajustes»** guarda únicamente lo que has cambiado y muestra la notificación «Ajustes guardados». Mientras no se pulse el botón, el bot no sabrá de tus cambios. En el registro aparecerá `[GUI] Профиль настроек сохранен!`.
- :rotate-ccw: **«Restaurar / Restablecer»** — botón rojo; primero preguntará «¿Restaurar los ajustes?». Los ajustes volverán a los **últimos guardados** (copia `bot_data/profile.yml.bak`). Si no hay copia, `profile.yml` se eliminará y el bot tomará los valores por defecto. Los cambios sin guardar se perderán. Este botón no toca los equipos principales ni las reglas en los archivos `bot_data/rules`, pero el formulario de la página los volverá a leer del disco.
- :triangle-alert: **Si sales de la página con cambios sin guardar** (a otra sección o con la cruz de la ventana), aparecerá «¿Guardar los cambios?» con los botones «Guardar», «No guardar» y «Cancelar».

El bot lee los ajustes **una sola vez, когда pulsas «Empezar a farmear»**. Puedes cambiarlos durante el funcionamiento, pero solo surtirán efecto tras detener y volver a iniciar. Ni siquiera «Pausa» y «Continuar» los actualizan. La tarjeta «Configuración de inicio» en la pantalla principal muestra precisamente los ajustes con los que el bot está trabajando actualmente.

> [!warning] Si el archivo `profile.yml` está dañado, arriba en el registro de la pantalla principal aparecerá `[ОШИБКА] Файл profile.yml поврежден!`, la página mostrará valores estándar y «Guardar ajustes» se negará a escribir («profile.yml está dañado: los ajustes no se guardaron»). Pulsa «Restaurar / Restablecer».

> [!done] Ahora ya sabes cómo definir el objetivo, los umbrales y los equipos para cada sala. A continuación: la pestaña «Autotáctica y PS»: el orden de las puertas y la forma en que el bot cura y cambia a los titanes. [Siguiente sección →](#8)

## Asistente de reglas: «Autotáctica y PS»

La segunda pestaña del Asistente de reglas. En la primera («Base y salas») definiste los packs y los umbrales generales. Aquí le explicas al bot **cómo comportarse cuando algo sale mal**: qué puerta abrir primero, qué considerar una mala batalla, cuántas veces probar otro pack, cuánto tiempo esperarte y cómo curar a los titanes heridos. Todos los campos ya están rellenados con números razonables, por lo que el bot funciona incluso sin tus cambios. Modifícalos cuando veas que se comporta de una manera que no te gusta.

![Pestaña «Autotáctica y PS»: banner superior, cuatro puertas, dos tarjetas al lado y umbrales personales abajo](images/tactics_tab.png)

Al igual que en la primera pestaña, **nada se guarda hasta que haces clic en «Guardar ajustes»**, y el bot lee la configuración una sola vez al hacer clic en «Empezar a farmear». Si cambias algo durante el farm, surtirá efecto tras detenerlo y volver a iniciarlo.

### Banner azul superior

En él se explica brevemente lo que hace el bot durante una mala batalla: la retira y vuelve a jugar con un pack de reserva, y recuerda el pack con éxito en una regla.

Si en la primera pestaña está desactivado el interruptor «El bot decide solo», se añade otra frase al banner. Es importante, por lo que la analizaremos por separado. **Sin «El bot decide solo» no funcionan dos cosas: los packs de reserva y el pack de curación.** Todo lo demás en esta pestaña funciona siempre:

- :door-open: orden de las puertas;
- :gauge: la espera de tu respuesta a la ventana SOS (la ventana en la que el bot te llama cuando la batalla es mala);
- :triangle-alert: criterios de mala batalla;
- :heart-pulse: umbrales de pánico personales.

### «Prioridad de puertas»

En el pasillo, el bot a menudo ve varias puertas a la vez: una por cada elemento (agua, tierra, fuego) o «Mixto». Dentro de la sala te esperan enemigos, y el pack para cada elemento es diferente. El orden decide **qué puerta abrirá primero el bot**. Por defecto es así: «Agua», «Mixto», «Tierra», «Fuego».

Hay cuatro posiciones de izquierda a derecha con flechas entre ellas; cada una tiene un número del 1 al 4. Haz clic en una posición y elige un elemento. No hay duplicados: si eliges un elemento que ya está en otra posición, simplemente **se intercambian**. Si era «Agua, Mixto, Tierra, Fuego» y eliges «Fuego» para la primera posición, pasará a ser «Fuego, Mixto, Tierra, Agua».

Dos aclaraciones para no sorprenderse en el juego:

- Si la puerta está **prohibida por la regla «Skip»** (sobre ellas, en la sección «Reglas e intercepciones»), el bot la saltará, incluso si es la primera en orden. Si todas las puertas están prohibidas, tomará la primera en orden.
- Si «El bot decide solo» está activado, a veces el bot **elegirá él mismo otra puerta**, fuera de orden: hacia donde funcione la curación del titán herido, o rodeando una puerta peligrosa para los heridos. Esta elección es visible en el registro con la línea `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`.

### Tarjeta «Criterios de mala batalla y SOS»

- :swords: **«Equipos de reserva a probar por sala»** — cuántas veces por sala el bot puede retirar él mismo la batalla y volver a jugar con otro pack. De 1 a 3, por defecto 2. Si agota los intentos y la batalla sigue siendo mala, el bot te llama. Solo funciona con «El bot decide solo». No se pueden poner más de tres: no tiene sentido volver a jugar una batalla diez veces, y cada intento cuesta tiempo.
- :gauge: **«Tiempo de la ventana SOS sin respuesta, min»** — cuántos minutos espera el bot a que respondas a la ventana «Se requiere intervención» antes de decidir por sí mismo. De 0 a 60, por defecto 10. La etiqueta bajo el campo dice «0: esperar siempre»: **cero significa «esperar siempre»**, el bot se quedará esperando hasta la mañana si es necesario. Esto funciona incluso **sin** «El bot decide solo». Lo que exactamente decidirá el bot por sí mismo (retirar la batalla, aceptarla o pausar) está en la sección sobre ventanas SOS.
- :users: **«Considerar mala la batalla si»** — pérdidas generales del pack: «titanes ≥ 3» y «perdieron ≥ 40» «% PS cada uno». Esta comprobación detecta el caso en que **cada uno por separado resiste**, pero juntos el pack «se desmoronó». Si tres titanes perdieron un 40% o más, la batalla es mala, aunque ninguno haya caído por debajo del umbral de pánico. La etiqueta «0 titanes: no comprobar» significa: pon 0 en el primer campo y la comprobación se desactivará. El primer campo va de 0 a 5, el segundo de 0 a 100.

Un ejemplo real. Pack: Araji, Hyperion, Rigel, Iyari, Lumira. Tras la batalla, Araji perdió el 45%, Rigel el 42%, Iyari el 40% y los demás un 10%. Tres perdieron «40 o más»: la batalla es mala, incluso si cada uno conserva más de su umbral de pánico. Si Iyari hubiera perdido solo el 35%, habría solo dos y la comprobación general no tendría nada que objetar.

> [!note] Los demás signos de una mala batalla (el umbral de pánico y la tolerancia de pérdidas) están en la primera pestaña «Base y salas». Una batalla es mala si se activa **al menos un** signo: alguien murió o no fue encontrado en la ventana, alguien tiene los PS por debajo del umbral, alguien perdió más de la tolerancia o se activaron las pérdidas generales.

Si introduces un número incorrecto (una letra o un número fuera de los límites), el campo se pondrá rojo, debajo aparecerá «Un número de … a …» y no podrás guardar la configuración hasta que lo corrijas.

### Tarjeta «Equipo de curación automático en la sala Mixta»

Suele ocurrir lo siguiente: un titán recibe golpes durante un par de batallas seguidas y camina con la mitad de su salud. Tarde o temprano caerá por debajo del umbral y la batalla será mala. La «curación» ocurre cuando el bot **arma él mismo un equipo especial** para que curan al herido (se coloca un curador en él, y este recupera la salud del herido). El bot solo arma este equipo para la sala «Mixta», porque allí se puede colocar a cualquiera.

Esto solo funciona con «El bot decide solo», y solo si tu propia regla de curación no se activó (la regla es más prioritaria).

- :heart-pulse: **«Curar al titán si los PS bajan de, %»** — por defecto 60. Un titán con más salud que este número se considera sano. **0 desactiva** el equipo de curación por completo. Pero hay un límite inferior: si el titán ya tiene los PS **por debajo del umbral de pánico**, no se le puede curar en la sala «Mixta», y el bot no lo toca.
- :users: **«A quién sacar del equipo por el herido»** — tres posiciones con flechas. Cuando hay que colocar al herido y no hay sitio en el equipo, alguien saldrá. Haz clic en una posición y elige un titán: la lista está dividida en columnas por elementos. **«— auto —»** (opción por defecto) significa: el bot saca desde el final del equipo, pero **no toca a los curadores**. Para el equipo «Hyperion, Rigel, Iyari, Lumira, Amón», serán Amón y luego Lumira. Si eliges a un titán que ya está en otra posición, se intercambiarán.

Cómo cura el bot, en palabras sencillas:

1. Comprueba quién tiene los PS por debajo del 60%, pero por encima del umbral de pánico, y a quién de ellos no han prohibido las reglas «Skip».
2. Cura **de uno en uno**, empezando por el que esté más cerca de su umbral. Primero los principales (de los packs base), luego los de reserva.
3. Si el herido no está en el equipo, ocupa el lugar del eliminado. Pero a los titanes a los que ya se les cura en «su» sala (agua y tierra: su pack base tiene un curador), el bot no los lleva a la «Mixta», a menos que allí no suban por encima del umbral durante dos batallas seguidas. En la sala de fuego no hay con qué curar, por lo que para ellos la curación se activa de inmediato.
4. Si el herido ya está en el equipo, pero no sube durante dos batallas seguidas, en lugar del eliminado entra un **curador sano y cargado** (PS desde 80%, energía desde 60%).
5. El equipo no se selecciona si no queda ningún curador en él, si pierde contra estos enemigos, si es peligroso para los heridos o si requiere batalla manual (Angus).

¿Por qué el bot es tan precavido? No va a curar a alguien que no hayas indicado en ninguna parte: el bot no colocará por su cuenta a un titán que no esté en tus packs ni reglas. Si no se pudo armar el equipo (el titán no llegó a ocupar la casilla), el bot no se detiene, coloca el equipo habitual y **no vuelve a curar a este titán hasta el final de la ejecución**.

En el registro esto se ve mediante las líneas `[ТАКТИКА] Пак отхила (бот собрал сам): ...` y `[ТАКТИКА] Отхил: ...` (por qué no se cura al herido).

### Tarjeta «Umbrales de pánico personales de titanes, % PS»

El umbral de pánico común (40 por defecto) es para todos. Pero hay titanes que da lástima perder antes que a otros, y otros que soportan tranquilamente unos PS bajos. Para ellos puedes definir **su propio umbral**.

- Abajo la etiqueta «Los demás titanes: umbral común 40%» (el número viene de la primera pestaña). Mientras no haya umbrales personales, dirá «No hay umbrales personales: todos los titanes usan el común».
- Haz clic en «Fijar un umbral personal a un titán». Se abrirá una pequeña ventana «Umbral de pánico personal»: elige a un titán de la lista e introduce un número de 0 a 100. Haz clic en «Aplicar». La ventana sugiere «Umbral común: 40%» para que tengas con qué comparar. En la lista solo están los titanes que aún no tienen un umbral personal.
- Cada umbral definido es una etiqueta con el titán y un número amarillo. Haz clic en la etiqueta para cambiar el umbral (el titán no se puede cambiar, habrá que quitarlo y añadirlo de nuevo). La **cruz** en la etiqueta elimina el umbral, y el titán vuelve a regirse por el común.

Una batalla es mala si los PS de este titán tras la batalla están **por debajo de su umbral personal**. Ejemplo: el umbral común es 40, pero Rigel tiene 60. Rigel sale con el 55%: la batalla es mala, aunque para los demás el 55% estaría bien.

> [!tip] ¿Por dónde empezar? No cambies nada hasta ver un par de docenas de salas. Si notas que el bot te llama por el mismo titán, ponle un umbral personal más bajo. Si el bot cambia de equipo demasiado a menudo para curar, **reduce** el número en «Curar al titán si los PS bajan de». Si no quieres que cure en absoluto, pon 0.

> [!warning] Si pusiste el «Tiempo de la ventana SOS» en 0 y te fuiste a dormir, y el bot te llamó en la ventana, esperará hasta la mañana. Es mejor dejar 10-15 minutos y configurar Telegram: así sabrás del problema de inmediato, y si no llegas a tiempo, el bot decidirá solo.

> [!done] Ahora sabes cómo establecer el orden de las puertas, qué considerar una mala batalla y cómo cura el bot a los heridos. A continuación, Telegram y las ventanas que te piden ayuda. [Siguiente sección →](#9)

## Asistente de reglas: «Reglas e intercepciones»

La tercera pestaña del Asistente de reglas. En la primera definiste el **pack principal** para cada sala; en la segunda, cómo se comporta el bot ante un problema. Aquí le enseñas las **excepciones**: «por lo general usa el pack principal, pero si ocurre esto, hazlo de otra manera». Cada una de estas excepciones se llama **regla**. Y una «intercepción» es cuando una regla «intercepta» la elección del pack al principal y coloca el suyo.

Una regla siempre se lee igual: **«si [condición] — entonces [acción]»**. Por ejemplo:

- :heart-pulse: «Si Araji tiene los PS por debajo del 50%, usa el pack con el curador Sigurd».
- :swords: «Si en la sala están Angus, Sylva y Verdok, usa este pack».
- :door-open: «Si Araji tiene los PS por debajo del 30%, no entres en «Fuego»».
- :users: «Si en la sala están Angus, Avalon y Edén, detente y pregúntame».

![Pestaña «Reglas e intercepciones»: filtros de elementos, lista de reglas con iconos, packs e interruptores](images/rules_intercepts.png)

Las reglas son propias de cada elemento: «Tierra», «Agua», «Fuego» y «Mixto» tienen listas separadas. Cuando el bot entra por la puerta de «Fuego», solo consulta las reglas de «Fuego». Al igual que en las otras pestañas, **nada se guarda hasta que haces clic en «Guardar ajustes»**, y el bot lee las reglas una sola vez al hacer clic en «Empezar a farmear».

> [!note] Muchas reglas no tendrás que escribirlas en absoluto. Si «El bot decide solo» está activado, el bot **recuerda por sí mismo** los packs con éxito tras una retirada y añade él mismo «reglas doradas». Aparecerán en esta misma lista (más información sobre ellas a continuación). Tus propias reglas son necesarias cuando ya sabes que «eso no se puede hacer» o «en esta situación se necesita precisamente este pack».

### Qué tipos de reglas existen

La condición de una regla es una de tres, y la acción es una de tres. Juntas forman los tipos habituales:

- :heart-pulse: **Salvación por PS o por energía.** La condición es «los PS (o la energía) de tal titán están por debajo de N%», la acción es usar otro pack. En la lista aparece el icono **«CURACIÓN»** (por PS) o **«ENERGÍA»**. Así se hace la curación: cuando un titán está herido, se usa un pack con curador.
- :swords: **Contra estos enemigos.** La condición es «en la sala están todos estos enemigos», la acción es usar tu propio pack. El icono es **«ENEMIGOS»**. Los enemigos se pueden elegir entre los 13 que el bot reconoce en la Mazmorra.
- :door-open: **«Skip» — prohibición.** La condición es «los PS o la energía del titán están por debajo de N%», la acción es no colocar a este titán y no entrar en esta sala. El icono es **«SALTAR»**, con la nota a la derecha «Saltar la sala».
- :users: **«Preguntarte».** Cualquier condición, y la acción es no decidir solo, sino llamarte. A la derecha aparece la nota **«Preguntarte»**, y el icono depende de la condición («PS», «ENERGÍA», «ENEMIGOS»). Cuando se active, el bot abrirá la ventana «No hay pack adecuado» y esperará tu respuesta. Si no respondes dentro del tiempo configurado en «Autotáctica», decidirá solo.

El icono «PS» (y no «CURACIÓN») significa que la condición es por PS y la acción es «Preguntarte». Si no hay ninguna condición, no hay icono y debajo del nombre dice «Sin condición — la regla nunca se activa».

Ahora pasemos a «Skip», porque tiene dos funciones a la vez. Ejemplo: en «Fuego» hay una regla «Araji, PS por debajo del 30%».

1. **Puerta.** Mientras Araji tenga menos del 30%, el bot no irá a «Fuego» y elegirá otra puerta. Si todas las puertas están prohibidas, el bot tomará la primera en orden.
2. **«Lista negra».** En esta sala no colocarán a Araji: cualquier equipo donde esté él será descartado por el bot para tomar el siguiente. Si el pack **principal** también contiene al titán prohibido, no hay nada que colocar: el bot se detendrá y abrirá la ventana «No hay pack adecuado».

> [!warning] «Skip» no se puede aplicar «Por enemigos». El bot reconoce a los enemigos **después** de haber entrado por la puerta, por lo que no puede elegir puerta basándose en ellos. En la ventana de regla para «Por enemigos», la casilla «Skip» no está disponible. Si quieres evitar una sala con ciertos enemigos, pon la regla «Preguntarte», y entonces la decisión dependerá de ti.

### En qué orden comprueba las reglas el bot

Cuando empieza una batalla, el bot revisa las reglas de la sala **en este orden**:

1. **«Skip».** Primero, el bot elabora la «lista negra» de titanes: a quienes haya prohibido una regla «Skip» activada. Un equipo con tal titán no será válido, aunque otra regla lo solicite (esto se llama veto: la prohibición es más fuerte que cualquier regla).
2. **Salvación.** Reglas donde en la condición hay PS o energía del titán. Aquí también se incluyen las reglas «contra enemigos, con Araji < 50% PS» (enemigos más PS): se comprueban aquí mismo, **antes** de las reglas normales sobre enemigos.
3. **Contra enemigos.** Reglas donde en la condición solo hay enemigos.
4. **Pack principal** de la sala, si no ha encajado nada.

Dentro de cada grupo, el bot avanza **de arriba abajo** y toma la primera regla que se active. Por eso son necesarias las flechas: si dos reglas sobre enemigos encajan al mismo tiempo, ganará la que esté más arriba. En cambio, la regla de «Salvación» siempre es más fuerte que «Contra enemigos», sin importar dónde estén en la lista. Las reglas **desactivadas** no participan en la comprobación.

Las condiciones se comparan con lo que el bot sabe de tus titanes (toma los PS y la energía de la pantalla de selección de equipo y tras las batallas). Si el bot aún no ha visto la salud de un titán, la considera completa, y la regla «por debajo de N%» no se activará. Si en la condición hay varios titanes (ocurre en reglas que el bot recordó por sí mismo), deben cumplirse **todas** las condiciones a la vez. Con los enemigos es igual: la regla solo se activará si en la sala están **todos** los enumerados.

### Lista de reglas: qué hay en cada fila

En la parte superior está «Reglas activas» y un banner gris con el número de reglas; a la derecha, la sugerencia: «Elige un elemento para cambiar el orden» (cuando se muestran todas) o «La regla más arriba se comprueba primero» (cuando se elige uno). Más abajo están los botones de filtro «Todas», «Tierra», «Agua», «Fuego», «Mixto» y el botón «Nueva regla». Debajo de ellos, los encabezados de columna «N.º», «Condición», «Acción», «Act.».

En cada fila, de izquierda a derecha:

- **Número**: posición en la lista de su propio elemento. Cuanto menor sea el número, antes se comprueba la regla. Cuando se selecciona **un** elemento, junto al número aparecen las flechas «Subir» y «Bajar». Si está seleccionado «Todas», no hay flechas: los elementos se muestran seguidos y no compiten entre sí.
- **Iconos**: elemento de la sala y tipo de regla («CURACIÓN», «PS», «ENERGÍA», «ENEMIGOS», «SALTAR»).
- **Nombre** y línea gris debajo: la condición en palabras, por ejemplo «Araji: PS por debajo de 50%» o «Enemigos en la sala: Angus, Sylva».
- **Acción**: flecha y casillas de los titanes del equipo (de izquierda a derecha, como en el juego) con la etiqueta «cambio de pack». O el banner «Preguntarte» / «Saltar la sala».
- **Interruptor «Act.»**: activar o desactivar la regla.
- **Lápiz** «Editar» y **cruz** «Eliminar».

Si no hay reglas, en lugar de la lista dirá: «No hay reglas. Haz clic en «Nueva regla» o el bot recordará una regla por sí mismo tras una retirada.»

### Interruptor, flechas, cruz y «Limpiar»

- :check: **Interruptor.** La regla desactivada se vuelve tenue, pero **permanece en la lista**, y el bot simplemente la salta. Es la mejor manera de «quitar una regla temporalmente»: no hace falta armar el equipo de nuevo. Al iniciar, en el registro aparecerá la línea `[ПРАВИЛА] Выключено правил: N, бот их пропускает.`.
- :chevron-up: **Flechas «Subir» y «Bajar»**: cambian la posición de la regla con su vecina. Son necesarias cuando dos reglas del mismo grupo pueden encajar a la vez y es importante cuál se comprueba primero.
- :x: **Cruz «Eliminar».** En la parte inferior aparecerá la notificación «Regla "…" eliminada» con el botón **«Deshacer»**. Mientras la notificación esté en pantalla, la regla se puede restaurar en la misma posición.
- :trash-2: **«Borrar todas las reglas»** elimina solo lo que **está visible en este momento**. Si está seleccionada «Agua», se eliminarán las reglas de agua; si está seleccionada «Todas», todas. Primero el bot volverá a preguntar: «¿Eliminar todas las reglas?» y escribirá cuántas y cuáles (botón «Eliminar todas»). Luego también habrá una notificación «Reglas eliminadas: {n}» con el botón «Deshacer».

Todas estas acciones solo cambian la página. Llegarán a los archivos después de hacer clic en «Guardar ajustes», y solo se grabarán **los elementos donde haya cambiado algo**. Si sales de la página sin guardar, la ventana preguntará «¿Guardar los cambios?».

> [!tip] Si dudas sobre si eliminar una regla o no, es mejor desactivarla con el interruptor. En las reglas que el bot ha recordado por sí mismo hay otra razón (véase más abajo): el bot no toca ni vuelve a crear las desactivadas, mientras que una eliminada puede volver a aparecer.

### Ventana «Nueva regla» paso a paso

Haz clic en «Nueva regla» (o en el botón «Condición» de la primera pestaña, en la parte inferior de la tarjeta de sala). Se abrirá una ventana. Si hay un elemento seleccionado, la ofrecerá de inmediato. El lápiz en la fila abre la misma ventana con el título «Editar regla».

![Ventana «Nueva regla»: elemento y nombre, tres disparadores, campos de condición, acción y equipo](images/rule_editor.png)

1. **Elige el elemento en el campo «Elemento de la sala».** La regla solo funcionará allí. Del elemento depende qué titanes se pueden elegir: en «Tierra» solo de tierra, en «Agua» solo de agua y en «Mixto» cualquiera. Si cambias el elemento más tarde, la ventana ajustará la elección automáticamente.
2. **Nombra la regla (opcional).** El campo «Nombre de la regla» se puede dejar vacío: entonces el nombre se compondrá a partir de la condición, por ejemplo «Araji: PS por debajo de 50%». Este nombre es el que el bot escribirá después en el registro cuando la regla se active.
3. **Elige el «Disparador»**: qué debe observar el bot: «Por PS», «Por energía» o «Por enemigos».
   - «Por PS» y «Por energía»: elige **«Titán»** e introduce un número en el campo «PS por debajo de, %» (o «Energía por debajo de, %») de 0 a 100. Por defecto, los PS son 35 y la energía 100. Si no introduces un número o pones un número fuera de los límites, el campo se pondrá rojo y debajo aparecerá «Un número de 0 a 100».
   - «Por enemigos»: marca en la cuadrícula «Enemigos peligrosos en la sala» a todos los que deban estar **juntos**. Al lado se muestra «· elegidos: N». Si no eliges a ninguno, no podrás guardar.
4. **Elige «Acción al activarse».** Hay dos casillas, se excluyen mutuamente: «Detenerse y preguntarte» y «Prohibir entrar en la sala (Skip)». Si no se marca ninguna, la regla **usará un pack**.
5. **Requerir rodaje de titanes (opcional).** La regla solo se activará si los titanes elegidos (de 1 a 5, de cualquier elemento) ya han disputado una batalla en esta ejecución. Por ejemplo, el pack requiere a Sigurd, pero no quieres colocarlo hasta que haya luchado al menos una vez. La cruz de al lado elimina el rodaje. El rodaje solo está presente en las reglas que colocan un pack. Tras una pausa suave y una batalla manual, el bot olvida el estado de los titanes y el rodaje comienza de nuevo.
6. **Elige «Equipo para esta regla».** Haz clic en «Elegir equipo» y en la ventana «Arma el equipo» coloca **de 3 a 5 titanes** (al igual que para el pack principal). Para «Preguntarte» y «Skip» no hace falta equipo; allí dice «Esta acción no necesita equipo».
7. **Haz clic en «Guardar regla».** Mientras el botón esté en gris, en la parte inferior de la ventana dirá lo que falta: «Elige un equipo: de 3 a 5 titanes», «Elige al menos un enemigo» o «Corrige el número: de 0 a 100». «Cancelar» cierra la ventana sin cambios.

La nueva regla se coloca en la **primera posición** de su elemento; la modificada se queda en su sitio (si cambiaste de elemento, pasará a ser la primera en el nuevo). Al archivo, al igual que todo lo demás, llegará tras hacer clic en «Guardar ajustes». Si abriste la ventana con el botón «Condición» desde la primera pestaña, tras guardar aparecerá la notificación «Regla "…" añadida a la pestaña «Reglas e intercepciones»».

> [!note] Una regla que el bot ha recordado por sí mismo se puede abrir con el lápiz y editar. Todo lo que no sea visible en la ventana (por ejemplo, la «tolerancia de pérdidas» o una condición adicional de PS) **se conservará tal cual**. La ventana mostrará esta condición en una línea gris: «También en la condición (se conservará tal cual): …».

### Reglas que el bot recordó por sí mismo

Si «El bot decide solo» está activado, en la lista aparecen reglas que tú no escribiste. Se reconocen por su nombre:

- :refresh-cw: **«Auto: Angus + Sylva en la sala»**: el bot retiró una mala batalla, volvió a jugar con otro pack y este tuvo éxito. El bot recordó: «contra estos enemigos colocar este pack». Debajo del nombre dice «La recordó el bot tras una retirada» (o «Tu pack tras una retirada, lo recordó el bot», si elegiste tú el pack en la ventana SOS). Si el pack perdió debido a una condición (por ejemplo, «Araji por debajo del 50%»), esta se añade a la condición. Esta regla se coloca en la primera posición.
- :star: **«Dorada: Angus + Sylva en la sala»**: «El pack venció a menudo a estos enemigos». Al iniciar, el bot revisa el historial y toma el pack que haya disputado **5 batallas o más** contra esta composición de enemigos y haya ganado el **80% o más**. El pack principal, los packs de reglas de salvación y tus packs de reserva no entran en las «doradas».

En el archivo estas reglas se llaman de otra forma («Anti-pack contra: …», «Regla dorada contra: …»), y es exactamente así como se escriben en el registro: `[ОБУЧЕНИЕ] Новое правило '…': пак […]. Сохранено на 1-е место.`. La ventana simplemente las muestra de forma corta y clara. Si cambias el nombre de la regla, verás tu propio nombre.

Lo que es útil saber sobre estas reglas:

- **El bot no genera duplicados.** Una regla con la misma condición no se crea por segunda vez: la antigua cambia de pack y sube arriba.
- **No toda retirada con éxito se recuerda.** Si una mala batalla ocurrió solo porque el titán entró herido en ella, y con el 100% de PS todo habría estado bien («los enemigos no tenían la culpa»), la regla no se crea.
- **El bot no toca las reglas desactivadas:** no las activa ni las sobrescribe. No volverá a recordar el mismo pack, y una «dorada» desactivada no regresará.
- **Las reglas eliminadas pueden volver.** La «regla dorada» se creará de nuevo en el siguiente inicio mientras no haya otra regla contra estos enemigos. Si no te gusta, desactívala con el interruptor. El bot volverá a crear la regla «auto» si una retirada termina igual otra vez.
- **Mientras la ventana está abierta, el bot puede escribir una nueva regla en el archivo.** Cuando hagas clic en «Guardar ajustes», la ventana volverá a leer el archivo y colocará estas nuevas reglas arriba sin perder nada. Si visitas la pestaña sin cambiar nada, verás la lista actualizada desde el disco.

> [!warning] Si el archivo de reglas de un elemento está dañado (por ejemplo, se editó a mano y se cometió un error de sangrado), la ventana indicará, por ejemplo para el agua: «El archivo de reglas está dañado: bot_data/rules/water.yml — la ventana no cambia las reglas de este elemento». Los demás elementos funcionan. No hace falta editar el archivo a mano: haz clic en «Enviar registro al autor» en la pantalla principal y escribe lo sucedido.

> [!tip] ¿Por dónde empezar? No escribas nada de antemano. Juega un par de docenas de salas con «El bot decide solo» activado y echa un vistazo aquí: el bot ya habrá recordado varias reglas. Desactiva las que no funcionen y sube las buenas con las flechas. Añade tus propias reglas cuando veas un problema recurrente: «Araji siempre camina herido»: regla de salvación; «esta composición de enemigos siempre mata mi pack principal»: regla contra enemigos.

> [!done] Ahora sabes cómo enseñar excepciones al bot y entiendes por qué usa precisamente este pack. A continuación, Telegram y las ventanas que te piden ayuda. [Siguiente sección →](#10)

## Cuando el combate salió mal: ventanas SOS

Casi siempre el bot se desenvuelve solo. Pero a veces se topa con una situación en la que no se puede prescindir de una persona: el combate se ganó, pero el precio fue demasiado alto, o las reglas no dan ningún pack adecuado. Entonces el bot **se detiene y te llama** con una ventana en medio de la pantalla. SOS es una señal de socorro, como la de un barco: «se necesita ayuda». Mientras no respondes, el bot no presiona nada y espera (pero no para siempre, más sobre esto abajo).

Hay tres ventanas, y cada una tiene su propio caso:

- :triangle-alert: **«Se requiere intervención»** — el combate terminó, pero el resultado es malo. Es la ventana principal y aparece más a menudo que las demás.
- :users: **«No hay pack adecuado»** — el bot aún no ha empezado el combate: las reglas no le dan un pack para esta sala.
- :check: **«El pack lo logró»** — tú mismo elegiste otro pack, este ganó y el bot pregunta si debe recordarlo.

![Ventana «Se requiere intervención»: motivo, sala, enemigos, tu pack con barras de PS y tres botones](images/sos_window.png)

> [!note] Cuándo aparece la ventana: si «El bot decide solo» está **desactivado** (por defecto es así), la ventana se abre después de **cada** combate malo. Si está activado, el bot primero intenta salir adelante sin ti y solo te llama cuando no puede: el combate se jugó a mano (Angus), no se pudo leer la ventana de resultados, tú elegiste el pack, en la sala el bot ya revirtió tantas veces como está permitido, o no hay un pack de reserva. Qué es un «combate malo» y cómo configurarlo — en las secciones sobre «Base y salas» y «Autotáctica y PS».

### Ventana «Se requiere intervención»

Arriba — brevemente: «El combate salió mal. ¿Qué hacemos?». Abajo — datos concretos para que puedas decidir sin mirar el registro:

- **Motivo.** Qué no le gustó exactamente al bot. Por ejemplo: «¡Umbral crítico! Araji tiene 12% PS (umbral: 40%)», «¡Delta de pérdidas superada! Rigel perdió 45% PS (tolerancia: 30%)», «¡FATAL! Iyari ha muerto…», «¡Grandes pérdidas en el pack!…» o «No se pudo leer la ventana de resultados: no se encontraron…». Los nombres de los titanes están en el idioma del programa.
- **Sala.** Elemento de la puerta y número de sala: «Fuego · sala 54».
- **Enemigos.** Los cuadros de los titanes contra los que fue el combate. Si no reconoce a los enemigos, no habrá esta línea.
- **Tu pack.** Cada titán con su barra de salud y la leyenda «PS antes del combate → PS después»: «36% → 12%». Si los PS de un titán están por debajo de su umbral de pánico (general o personal), la barra y el número se muestran en **rojo**. Si acaba de entrar al combate ya herido y salió casi sin PS, se ve de inmediato.
- **Temporizador.** Abajo: «Si no respondes, el bot decidirá solo en 9:41». El último minuto es amarillo, luego «El bot está decidiendo…». Si en «Autotáctica y PS» está puesto 0, no hay esta línea: el bot te espera siempre.

Botones (de derecha a izquierda, el principal es el de más a la derecha):

1. **«Revertir el combate»** (azul). Volver a jugar este combate con otro pack. La ventana se ocultará y se abrirá «Arma el equipo» con el pack actual; cambia los titanes y presiona «Revertir con este pack». Lo que ocurrirá después se explica en la sección «Retirada» más abajo. Si cierras «Arma el equipo» sin elegir, la ventana SOS volverá y no se habrá perdido nada.
2. **«Ignorar»** (gris). Aceptar el combate tal como está: la sala se da por superada y el bot continúa con los PS que queden. Es adecuado cuando las pérdidas te parecen aceptables (por ejemplo, el titán ya entró herido de todos modos y en general todo está bien).
3. **«Jugar a mano»** (gris). El bot no presiona nada y tú mismo juegas esta sala en el juego. El bot espera a que vuelvas al pasillo: el banderín de la puerta debe verse durante 2 segundos seguidos. Si lo último fue la ventana de resultados, la sala se cuenta como superada; si te retiraste sin vencer, no. Si cerraste la ventana de resultados sin repetir el combate, este se cuenta como quedó. Después de jugar manualmente, el bot olvida los PS de los titanes y las alineaciones en las casillas (los leerá de nuevo de la pantalla de selección de equipo) y luego sigue jugando solo.

> [!warning] Un combate donde se usó la **habilidad definitiva manual de Angus** no se puede revertir: en su ventana de resultados no hay botón «Repetir». En lugar de «Revertir el combate», en la ventana habrá un botón rojo **«Detener el bot»**, y solo quedará «Ignorar» o «Jugar a mano».

### Retirada: qué hace el bot tras tu elección

La ventana se ha cerrado y la orden ha llegado al bot. A partir de ahí hace todo solo, y en el registro esto se ve por la etiqueta `[ОТКАТ]`:

1. Presiona **«Repetir»** en la ventana de resultados y espera a que cargue el combate (a veces tarda entre 20 y 30 segundos o más, por lo que espera hasta un minuto).
2. Pone el combate **en pausa** (una vez) y presiona **«Retirada»**.
3. Regresa al pasillo, entra a la **misma sala** y coloca tu nuevo pack.

Si el combate vuelve a salir mal, la ventana reaparecerá. Si sale bien, es aquí cuando aparece la ventana «El pack lo logró» (más abajo).

Si se pierde la conexión con el juego (la imagen de «cargando» no termina), el bot no se rinde: espera al juego hasta 15 minutos y lo anota en el registro. Solo si la retirada no se logra en absoluto, el bot guarda una captura de pantalla en `bot_data/debug/`, activa una pausa suave y te envía un mensaje por Telegram. Más detalles en la sección de problemas.

### Ventana «No hay pack adecuado»

Aparece cuando el bot ya eligió la puerta y observó a los enemigos, pero **no hay qué colocar**. Ocurre por dos razones, ambas derivadas de tus reglas:

- se activó la regla «Preguntarme» (está hecha justamente para eso);
- el pack principal de la sala contiene un titán que fue prohibido por la regla «Skip» (el bot escribe algo como «FATAL: Todos los packs han sido descartados…»).

La ventana pregunta: «Las reglas no dan un pack para esta sala. ¿Qué hacemos?» Contiene los mismos datos de «Motivo», «Sala» y «Enemigos», pero sin las barras: el combate aún no ha tenido lugar. Botones:

- **«Armar un pack nuevo»** (azul) — abre «Arma el equipo», donde el botón se llama «Aplicar». El bot colocará los titanes elegidos y **recordará de inmediato el pack con una regla** «contra estos enemigos» (aquí no hay verificaciones antes de guardar, ten cuidado).
- **«Jugar a mano»** — juegas la sala tú mismo mientras el bot espera en el pasillo. La sala se da por superada si ganas.
- **«Detener el bot»** (rojo) — el bot escribe el resumen de la sesión y se apaga.

Aquí no hay botón «Ignorar»: no hay nada que aceptar, ya que no hubo combate.

### Ventana «El pack lo logró»

Esta ventana aparece cuando un combate es ganado por un pack que **elegiste tú** (a través de «Revertir el combate» o «Probar otro», en la ventana o en Telegram). Si el pack de reserva lo eligió el propio bot y tuvo éxito, el bot lo recordará solo y no preguntará nada.

Por dentro contiene la sala, los enemigos (de la última ventana SOS, si ocurrió hace no más de 15 minutos) y tu pack con los PS tras el combate. Pregunta: «El pack en prueba ganó. ¿Guardarlo como regla contra estos enemigos?» Botones:

- **«Guardar pack»** (verde) — el bot recordará la regla «contra estos enemigos» con este pack. En la lista de reglas aparecerá como «Auto: …» o «Tu pack tras una retirada, lo recordó el bot».
- **«Probar otro»** — vuelve a «Arma el equipo» y a la retirada: el bot volverá a jugar el combate ganado con otro pack.

Si no respondes, al transcurrir el tiempo del temporizador (leyenda «Si no respondes, el bot guardará el pack solo en…»), el bot guardará el pack por su cuenta, como si hubieras presionado «Guardar pack».

### La cruz de la ventana y «¿Detener el bot?»

Las ventanas no tienen una opción de «simplemente cerrar»: si cierras la ventana, el bot se quedará esperando respuesta. Por eso la cruz pregunta: **«¿Detener el bot?»**. Si respondes «Detener el bot», el bot finalizará, escribirá el resumen y lo enviará a Telegram. Si no responde en 10 segundos, el programa lo detendrá por sí mismo. En la ventana «El pack lo logró» la pregunta es distinta: la detención allí es igual a la de «STOP F10», **el resumen de la sesión no se enviará a Telegram**. Si cambiaste de opinión, presiona «Cancelar» y la ventana permanecerá.

### Qué pasa si no respondes

Cada vez que no respondes dentro del plazo fijado en «Autotáctica y PS» («Tiempo de la ventana SOS sin respuesta, min»: por defecto 10, hasta 60, 0 es esperar siempre), el bot escribe `[ТАКТИКА] Ответа нет 10 мин. Решаю сам.`, la ventana se cierra y te llega un mensaje en Telegram avisando que el bot ha decidido por su cuenta. Esto funciona aunque «El bot decide solo» esté desactivado. La decisión depende de la ventana:

- **«Se requiere intervención»:** si hay un pack de reserva y el combate se puede revertir (no es Angus y los intentos en la sala no se han agotado) — **retirada** y pack de reserva; si no, pero todos los titanes están vivos — el combate **se acepta** («Ignorar»); de lo contrario (alguien murió o no fue encontrado en la ventana) — **pausa suave**.
- **«No hay pack adecuado»:** si hay un pack de reserva adecuado sin heridos ni titanes prohibidos — el bot lo coloca **y no guarda la regla**; si no lo hay — **pausa suave**.
- **«El pack lo logró»:** el pack se guarda.

La pausa suave es como el botón «Pausa F9»: el bot espera en el pasillo hasta que presiones «Continuar».

> [!tip] ¿Respondiste justo en el instante en que el bot ya había decidido por su cuenta? No pasa nada: el bot omitirá la respuesta antigua y escribirá `[ЛОГИКА] Пропускаю ответ ...: он пришёл на прошлое окно.`

### Responder desde Telegram

Si Telegram está configurado, la **misma pregunta** llega al chat: captura de pantalla del juego, leyenda (sala, enemigos, motivo, pack con PS) y botones. Puedes responder donde te sea más cómodo: si respondes en el chat, la ventana del ordenador se cerrará sola, y viceversa.

- **«Deshacer (Armar pack)»** (verde) — el bot te pedirá escribir en el chat los nombres de **3 a 5 titanes** separados por comas o espacios, te mostrará a quiénes reconoció y preguntará «¿Todo correcto?» («Confirmar pack» / «Escribir otro»). Para el combate manual de Angus y para «No hay pack adecuado», en su lugar aparece en rojo «Detener el bot».
- **«Jugar a mano»** e **«Ignorar (Continuar)»** — lo mismo que en la ventana. En «No hay pack adecuado» no existe «Continuar».
- «El pack lo logró» en Telegram solo llega si también enviaste el pack desde allí: «Confirmar y Guardar» o «Deshacer y Reintentar».

Si se pierde la conexión a Internet, el mensaje se enviará más tarde (el bot reintenta el envío), mientras que la propia ventana en el ordenador permanece. La configuración de Telegram se explica en la sección dedicada a él.

### Minibar y ventanas SOS

Si la ventana del programa está minimizada en la minibar, la ventana SOS aparecerá **en el centro del juego**. La minibar se vuelve roja en ese momento, y su botón «SOS» trae al frente la ventana extraviada por encima del juego.

> [!tip] ¿Cómo elegir? Mira «Tu pack». Si un titán entró herido y empeoró pero los demás están bien, a menudo basta con «Ignorar». Si los enemigos te resultan conocidos y son mucho más fuertes — «Revertir el combate» con otro pack. Si nada está claro — «Jugar a mano». Revertir cuesta tiempo (el combate se debe volver a cargar, lo que toma de 20 a 30 segundos o más), mientras que «Ignorar» no cuesta nada.

> [!done] Ahora ya sabes qué significa cada ventana SOS, qué hace cada botón y qué hará el bot sin ti. A continuación — cómo decide el bot solo cuando no estás cerca. [Siguiente sección →](#11)

## Cómo el bot decide solo

En la sección sobre ventanas SOS viste que el bot te llama tras una mala batalla. Pero no siempre llama: si activas «El bot decide solo» (pestaña «Base y salas», sección 7), el bot **primero intenta arreglárselas sin ti** y solo pide ayuda cuando no lo logra. Aquí veremos cómo piensa. No habrá fórmulas: solo las preguntas que se hace el bot y algunos ejemplos.

Imagínate a un compañero experimentado sentado a tu lado con el teléfono. La batalla salió mal y te fuiste por un té. No se quedará sentado esperando. Recordará qué funcionó antes contra esos enemigos, repetirá la batalla con otra alineación y anotará lo que dio resultado. Algo así es como se comporta el bot. Solo que tiene reglas para no meter la pata.

> [!note] «El bot decide solo» está **desactivado** por defecto, y todo lo que se explica a continuación no ocurre si está apagado: tras cada mala batalla, el bot simplemente abre la ventana SOS. Si activas el interruptor y pulsas «Guardar ajustes», surtirá efecto a partir del siguiente «Empezar a farmear». Qué se puede ajustar exactamente lo vimos en la sección 8 («Autotáctica y PS»), y aquí tratamos sobre **qué hace el bot con esos números**.

### Mala batalla: qué hace el bot paso a paso

1. **Nota que la batalla es mala.** Alguien murió o está por debajo del umbral de pánico, perdió más del límite o de repente tres cayeron (secciones 7 y 8). En el registro aparece la línea `[ТАКТИКА] Плохой бой: ...` con la causa.
2. **Comprueba si puede revertir la batalla por sí solo.** No puede en cuatro casos: la batalla fue manual (habilidad definitiva de Angus, no hay botón «Otra vez» en la ventana de resultados), la ventana de resultados no se pudo leer, el equipo lo pusiste **tú** (la decisión también es tuya) o el bot ya agotó sus intentos en esa sala. Si no se puede, se abre la ventana SOS y en el registro sale `[ТАКТИКА] Сам не откатываю: ... Спрашиваю вас.` con la causa.
3. **Busca un equipo de reserva.** Cómo lo hace, en la siguiente sección. Si no hay uno adecuado, abre la ventana SOS de nuevo.
4. **Revierte y vuelve a jugar.** Realiza los mismos pasos de `[ОТКАТ]` que tras tu elección («Otra vez», pausa, «Retirada»), y en esa misma sala pone el equipo de reserva. En el registro aparece `[ТАКТИКА] Откатываю бой сам и переиграю паком ... (взят: ...)`.
5. **Mira el resultado.** Si el de reserva lo logró, el bot continúa y normalmente recuerda el equipo (más abajo sobre esto). Si la batalla vuelve a ser mala, hace un segundo intento, y así hasta agotar los intentos («Equipos de reserva a probar por sala», por defecto 2, máximo 3). Luego te llama.

> [!tip] El bot siempre revierte la batalla completa en lugar de «corregir sobre la marcha». Revertir cuesta tiempo (hay que volver a cargar la batalla, lo cual puede tardar entre 20 y 30 segundos o más), por lo que no le gustan los intentos en vano: mira más abajo cómo elige el equipo.

### De dónde saca el bot el equipo de reserva

Va recorriendo la lista de arriba a abajo y toma el **primero que coincida**:

1. **Tus «Equipos de reserva»** — pestaña «Base y salas», tarjeta de la sala. Se toman en orden, tal como los organizaste. En el registro la fuente se llama «su lista de equipos de reserva».
2. **Equipos de las reglas de ese elemento** — en el registro «reglas de elemento». Tienen su propio orden interno: primero las reglas «contra estos enemigos», luego los equipos que ya han vencido a esos enemigos específicos (los mejores según los PS restantes primero), luego otros «antiequipos» y después todo lo demás, incluido el equipo principal de la sala.
3. **Historial de batallas** — en el registro «historial de batallas». Es el último turno y solo se toman equipos que ya hayan vencido a estos enemigos. El bot recuerda las batallas de los últimos 20 inicios.

Lo que el bot **nunca pondrá** como reserva:

- un equipo que ya haya perdido en esta sala (para no repetir el error);
- un equipo que «pierda contra estos enemigos»: la última vez contra ellos se revirtió la batalla por culpa de los enemigos y el equipo no tiene más victorias que derrotas. Un solo fallo **no arruina a un buen equipo**: si ganó contra esos enemigos cinco veces y perdió una, el bot aún lo elegirá;
- un equipo con un titán prohibido por la regla «Skip»;
- un equipo con un titán cuyos PS ya estén **por debajo del umbral de pánico**: el bot no lo enviará al combate a una muerte segura;
- del historial: un equipo donde haya un titán que no hayas indicado en ninguna parte (ni en equipos ni en reglas). En el historial quedan equipos de reglas eliminadas hace tiempo y el bot no los resucita.

Además existen equipos «peligrosos»: aquellos donde un titán herido, a juzgar por batallas anteriores, no sobrevivirá hasta el final. El bot los toma **en último lugar**, solo si no hay nada mejor. Cómo lo determina se explica en la parte «Titán herido» más abajo.

Por qué el bot no eligió un equipo u otro se puede ver en el registro: `[ТАКТИКА] Не беру запасной пак ...` y la causa. Si se acaban los de reserva y la batalla sigue siendo mala, no es un fallo, sino un honesto «no sé qué más poner».

### Recordar o no: regla «Auto: …»

El equipo de reserva lo logró. El bot guarda esto como regla «contra estos enemigos, pon este equipo» y la próxima vez que encuentre la misma alineación, la usará de inmediato. En la lista, esta regla aparece como «Auto: {names} en la sala» y se coloca en primer lugar (sección 9). En el registro: `[ТАКТИКА] Запасной пак ... справился. Запоминаю его против этих врагов.`

Pero a veces **no se debe recordar**. Ejemplo: Araji entró a la batalla con un 36% de salud y cayó al 5%. El equipo principal no tiene la culpa: si Araji hubiera estado sano, la batalla habría salido bien. Si el bot guardara la regla «contra estos enemigos pon la reserva», empezaría a usar el equipo de reserva donde el principal lo hace perfectamente, malgastando tu fuerza. Por eso el bot comprueba: **«¿con el 100% de PS en todos, la batalla habría sido mala?»** Si la respuesta es no, significa que los enemigos no tienen la culpa, la ayuda fue puntual y la regla no se crea.

En el registro esto se ve de inmediato: `[ТАКТИКА] Враги ни при чём: в бой вошли раненые ...` y luego `Правило не запоминаю: это была разовая помощь раненым титанам`.

Tampoco se recordará en otros tres casos:

- el bot no reconoció a los enemigos (`[ОБУЧЕНИЕ] Враги не распознаны — правило не сохраняю`): una regla «sin enemigos» se activaría en cualquier sala;
- desactivaste la regla con el mismo equipo mediante el interruptor: el bot no toca lo desactivado;
- tú mismo elegiste el equipo: entonces decide tu ventana «El pack lo logró» (sección 10).

### Titán herido: ayuda por adelantado, no tras la batalla

Lo más valioso que sabe hacer el bot es **evitar una mala batalla** en lugar de solucionar el desastre después. Mientras está en la pantalla de selección de equipo, observa la salud de los titanes y el historial: «¿cómo terminaron las batallas con este equipo en esta sala?» Para ello, el bot almacena cuántos PS suele **perder** el titán en una batalla con este equipo (promedio de las últimas cinco batallas, se necesitan al menos dos). Si los PS del herido al entrar menos la pérdida habitual **quedan por debajo del umbral de pánico**, el bot no arriesgará y pondrá el equipo de reserva de inmediato, antes del combate.

Ejemplo. Araji con un 36% de PS entra en Fuego. En las últimas batallas aquí solía perder cerca del 29%. Resultado: 36 − 29 = 7%, y el umbral de pánico es 40. La batalla casi seguro terminará mal, por lo que el bot pone el equipo de reserva, por ejemplo con Moloch, **de inmediato**. Es una ayuda puntual, la regla no se recuerda.

Dos detalles para que el bot no parezca extraño:

- **La energía también importa.** Si el titán tiene ahora una energía similar a la de batallas anteriores (diferencia no superior al 25%), el bot utiliza precisamente esas batallas para el pronóstico. Araji con buena energía en Fuego pierde poco, con la energía vacía pierde mucho, y el pronóstico lo tiene en cuenta.
- **Una batalla no es estadística.** Con menos de dos batallas, el bot no confía en el pronóstico y no cambia nada.

Los equipos de las reglas de rescate («si Araji está por debajo del 50%, pon a Sigurd», sección 9) no los sustituye por adelantado: los pusiste precisamente para el herido y tu intención es más importante que su pronóstico.

### Puerta por salud

Si el bot decide solo y en el pasillo se ven **varias puertas permitidas**, no elige simplemente por orden (sección 8, «Prioridad de puertas»), sino teniendo en cuenta a los heridos:

1. Primero va a la puerta **tras la cual curarán al herido**: se activará tu regla de rescate o el bot creará él mismo un equipo de curación.
2. La puerta tras la cual, a juzgar por batallas anteriores, el herido corre peligro, el bot la **omite** si hay otra opción.
3. De lo contrario, todo como siempre, por orden.

Se aprecia en la línea `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...`. Una puerta prohibida por la regla «Skip» nunca la abrirá. El bot aún no ve a los enemigos detrás de la puerta, por lo que aquí se basa en el equipo básico de la sala.

### Equipo de curación en «Mixta»

Si se puede curar al herido y tu regla de curación no se ha activado, el bot **crea él mismo un equipo de curación**: pone en la sala «Mixta» al herido y, si hace falta, a un sanador cargado y sano. Curan de uno en uno, los principales antes que los de reserva, y a los que están por debajo del umbral de pánico no los curan en absoluto. Todos los detalles (umbral «Curar al titán si los PS bajan de, %», «A quién sacar del equipo por el herido», ese mismo Sigurd para Rigel) están en la sección 8. Aquí solo importa una cosa: es una **ayuda puntual**, exactamente igual que el equipo de reserva del pronóstico. No se crea ninguna regla después y al final se contabiliza por separado («equipos de curación (creados por el bot)»).

### «Reglas doradas»: el bot aprende de todo el historial

Todas estas decisiones las toma el bot sobre la marcha. Pero las «reglas doradas» las resume **una sola vez, al iniciar el farmeo**. El bot revisa el historial de batallas y busca un equipo que contra la misma alineación de enemigos haya disputado **5 batallas o más y haya ganado el 80% o más**. A ese equipo lo guarda con la regla «Dorada: {names} en la sala» (sección 9). En el registro: `[ОБУЧЕНИЕ] ...: 'Золотое правило против: ...' — пак ... Сохранено на 1-е место.`

No se convertirá en regla dorada:

- el equipo principal de la sala, los equipos de reglas de rescate y tus «Equipos de reserva» (son para ayudar, no para cada batalla);
- los equipos de curación que creó el propio bot: solo hacen falta mientras el titán esté herido;
- un equipo con un titán que no esté en tus equipos ni reglas;
- un equipo contra enemigos para los cuales ya exista una regla (tuya, «Auto» o desactivada).

No hay reglas doradas mientras «El bot decide solo» esté desactivado. ¿Apareció una no deseada? **Desactívala con el interruptor** en lugar de borrarla: si la borras volverá al siguiente inicio, pero si la desactivas el bot no la tocará.

### Si no respondes a la ventana SOS

Esto ya no es «el bot decide solo», sino «el bot decide por ti» (sección 10, «Qué pasa si no respondes»). Funciona incluso si «El bot decide solo» está desactivado: al agotarse el tiempo de espera («Tiempo de la ventana SOS sin respuesta, min»), el bot revertirá la batalla con un equipo de reserva, la aceptará o entrará en pausa suave. Cada vez escribe `[ТАКТИКА] Ответа нет N мин. Решаю сам.`, cierra la ventana y envía un mensaje por Telegram.

### Cómo saber qué hizo el bot sin ti

Al final de la sesión, en el bloque «Resumen de la sesión» (botón «Detalles») y en la línea `[ИТОГ]`, hay contadores:

- **«reversiones»**: cuántas batallas se han vuelto a jugar en total;
- **«de ellas sin usted»**: cuántas de esas reversiones hizo el bot solo, sin preguntar, tanto por pronóstico como por tiempo de espera;
- **«equipos de curación (creados por el bot)»**: cuántas veces curó al herido con un equipo de curación.

El mismo resumen llegará a Telegram: «Reversiones: 6 (el bot solo: 5)». Si casi todo es «sin usted», el bot lo tiene bajo control. Si el número aumenta y no aparecen las «Reglas doradas», significa que los mismos enemigos rompen una y otra vez el equipo principal. Échale un vistazo a la pestaña «Reglas e intercepciones» para ver qué reglas ha recordado y piensa si no es momento de cambiar el equipo principal.

> [!warning] El bot decide según el **historial** y el pronóstico, no ve la batalla por adelantado. Puede equivocarse: en los primeros días, cuando hay poco historial, el equipo de reserva se elige al azar. No te asustes si durante las primeras decenas de salas «El bot decide solo» revierte batallas con más frecuencia de la deseada. Cuantas más batallas haya en el historial, más precisa será la elección.

> [!tip] ¿Por dónde empezar? Configura al menos uno o dos **«Equipos de reserva»** en cada sala (sección 7): así el bot no buscará a ciegas. Activa «El bot decide solo» y durante un par de días simplemente observa las líneas `[ТАКТИКА]` y el «Resumen de la sesión». Si no te gusta lo que hace el bot, desactiva el interruptor y todo volverá a las ventanas SOS.

> [!done] Ahora entiendes cuándo y cómo se las arregla el bot sin ti, qué recuerda y cuándo pide ayuda. A continuación, Telegram: cómo recibir mensajes cuando no estás ante el ordenador. [Siguiente sección →](#12)

## Telegram

El bot puede escribirte en Telegram mientras no estás frente al ordenador: fuiste a la cocina, te fuiste a dormir, te fuiste a trabajar. Si el combate necesita tu ayuda, al chat llegará una captura de pantalla y botones. Pulsaste un botón en el teléfono — el bot hizo lo que le dijiste. Si todo va sobre ruedas, el bot guarda silencio: los mensajes llegan **solo si hay problemas** y **una vez al final de la sesión**.

Lo que necesitarás: la aplicación Telegram y cinco minutos. Solo hay que configurarlo una vez.

> [!note] Telegram — по желанию. Без него бот работает так же, просто окна SOS ты видишь только на экране компьютера, а итога сессии нет. Но если планируешь оставлять бота на ночь, настрой: так ты узнаешь о проблеме сразу, а не утром.

### Qué hay que preparar

Necesitas dos cosas, ambas se obtienen en el propio Telegram:

- :send: **Token del bot** (la clave con la que el programa accede a tu bot). Es una cadena larga de números y letras, por ejemplo `123456789:AAH…`. El token lo proporciona un bot especial: **@BotFather**.
- :user: **Chat ID** (número del chat). Es un número por el cual Telegram sabe a quién entregar el mensaje: a ti y no a otra persona.

> [!warning] El token es como la contraseña de tu bot. No se lo muestres a nadie, no lo envíes en capturas de pantalla ni en correos (ni siquiera al autor del programa). Haz capturas de la ventana «Ajustes de Telegram» mientras el token esté oculto con puntos.

### Paso a paso

1. **Crea tu bot.** En Telegram busca **@BotFather** (el verdadero tiene un tic azul al lado) y pulsa «Iniciar». Escríbele `/newbot`, придумай имя (любое, его увидишь только ты) и логин, который заканчивается на `bot`, например `moi_titan_bot`. En respuesta, BotFather enviará un mensaje con el token: copialo.
2. **Averigua tu Chat ID.** Busca el bot **@getmyid_bot**, pulsa «Iniciar» — responderá con la línea `Your user ID` y un número. Ese es tu Chat ID, copia el número. Si este bot no responde, hay una alternativa: escribe cualquier palabra a **tu** bot del paso 1, abre en el navegador la dirección `https://api.telegram.org/bot<твой токен>/getUpdates` (sustituye `<твой токен>` por tu token) y busca en la respuesta `"chat":{"id":` — el número que está justo después es el Chat ID.
3. **Pulsa «Iniciar» en tu bot.** Busca el bot que creaste en el paso 1 y pulsa «Iniciar» (o escríbele `/start`). Sin esto, Telegram **no permitirá** que el bot te escriba primero. Es la causa más frecuente de que los mensajes no lleguen.
4. **Abre la ventana en el programa.** Pulsa el punto de Telegram en la barra de la izquierda o el botón **«Configurar Telegram»** en la pestaña «Base y salas» (sección 7). Se abrirá la ventana «Ajustes de Telegram».
5. **Rellénala.** Activa el interruptor «Enviar mensajes a Telegram». En el campo «Token del bot (de @BotFather)» pega el token, en el campo «ID del chat» pega el número. Lo más cómodo es el botón **«Pegar»** junto al campo: toma lo que has copiado. El token se muestra con puntos; el icono del ojo lo muestra para comprobar que se pegó correctamente. El botón derecho del ratón sobre el campo también es «Pegar».
6. **Prueba la conexión.** Pulsa **«Probar Telegram»**. Tras unos segundos, a la derecha aparecerá en verde «Mensaje enviado: revisa Telegram», y en el chat con tu bot, el mensaje «Prueba de conexión: todo funciona». Si llegó, todo está listo.
7. **Guarda.** Pulsa **«Aplicar»**, y luego abajo en la página **«Guardar ajustes»**.

![Ventana «Ajustes de Telegram»: interruptor, campos de token e ID del chat, botones «Pegar» y «Probar Telegram»](images/telegram_window.png)

> [!warning] «Aplicar» solo traslada los valores a la página del «Master de reglas», al archivo **no se escriben**. Hasta que no pulses «Guardar ajustes», abajo dirá «Hay cambios sin guardar» y el bot no sabrá nada de Telegram. Si te vas de la página sin guardar, el programa preguntará «¿Guardar los cambios?».

> [!tip] «Probar Telegram» comprueba lo que está escrito actualmente en la ventana, aunque todavía no hayas guardado nada. Por eso comprueba **antes** de «Aplicar»: si encuentras un error, corrígelo y vuelve a probar. La prueba se realiza en segundo plano, la ventana no se bloquea y no tendrás que esperar la respuesta más de 20 segundos.

### Si la prueba falló

Debajo del botón aparecerá una línea roja «No se envió: …» con la causa. Las más frecuentes:

- **«Rellena el token y el ID del chat»** — uno de los campos está vacío.
- `Unauthorized` — el token no es correcto: falta algún carácter, hay un espacio de más o no se copió entero. Vuelve a pegarlo con el botón «Pegar».
- `chat not found` o `Forbidden` — el Chat ID no es correcto o no has pulsado «Iniciar» en **tu** bot (paso 3). Comprueba ambos puntos.
- **«fallo de conexión con Telegram»** — no hay internet o Telegram no se abre desde este ordenador. Comprueba que en este mismo PC funcione Telegram (o el sitio web telegram.org).

Si tras corregirlo sigue sin llegar, crea un nuevo bot con @BotFather (paso 1) y empieza de nuevo: es más rápido que buscar una errata.

### Cómo saber si Telegram está activado

En la barra de la izquierda, junto al botón de Telegram, hay un punto: si pasas el ratón por encima, aparecerá la sugerencia **«Telegram: activado»** o **«Telegram: sin configurar»**. Activado significa que el interruptor está puesto y ambos campos están rellenos. Esto **no es una prueba de conexión**: solo el botón «Probar Telegram» mostrará si el token funciona. Lo mismo se ve en la pestaña «Base y salas»: junto al botón «Configurar Telegram» se ilumina en verde «Avisos SOS activados» o en gris «Telegram sin configurar». El punto se actualiza solo un par de segundos después de guardar.

### Qué mensajes llegan

El idioma de los mensajes es el mismo que se haya seleccionado en la ventana del programa.

- :swords: **Ventana SOS** — el título «Se necesita tu ayuda» (o «No hay pack adecuado»), una captura de pantalla del juego y la descripción: sala, enemigos (a por quiénes iban), motivo, tu pack con barras de salud y energía. Debajo, los botones. Es la misma pregunta que en la ventana del ordenador (sección 10).
- :triangle-alert: **Alertas** — un mensaje corto sin botones que te dice qué ha pasado y qué hacer. Son las siguientes: «No se pudo revertir el combate» (el bot está en pausa suave, mira la pantalla del teléfono), «Parece que el bot se ha bloqueado» (5 minutos sin sala) y un mensaje similar cuando no se puede iniciar el combate (lo más probable es que no haya conexión con el servidor del juego), «La pantalla del PC está bloqueada» (el bot no ve el juego durante más de un minuto; desbloquea el PC y continuará solo) y «No respondiste — el bot decidió solo».
- :chart-no-axes-column: **Resumen de la sesión** — cuando el bot se detiene: cuánto tiempo ha pasado, salas, pisos y titanita, si hubo reversiones y ventanas SOS («el bot solo: {n}» — son las reversiones que hizo sin ti), las salas más largas. Si el bot se cerró por un error, en el título dirá «El bot se cerró por un error» y la causa.

El resumen llega con cualquier detención: alcanzó el objetivo, pulsaste Ctrl+Q, Ctrl+Shift+Q, o el bot se cerró por un error. **No llega** tras «STOP F10» ni tras «Detener и закрыть» (sección 6), porque detienen el bot al instante.

### Botones debajo del mensaje SOS

Pulsa los botones en Telegram del mismo modo que en la ventana del ordenador:

- **«Deshacer (Armar pack)»** (verde). El bot enviará: «Escribe los nombres de 3-5 titanes en el chat». Escríbelos en el chat separados por comas o espacios, por ejemplo `гиперион, сигурд, нова` o de forma abreviada con las tres primeras letras: `гип сиг нов`. El bot responderá a quiénes ha reconocido y preguntará «¿Todo correcto?»: **«Confirmar pack»** iniciará la reversión, **«Escribir otro»** te permitirá volver a introducirlo. Si no encuentra entre 3 y 5 titanes, el bot dirá cuántos ha reconocido y pedirá que los escribas de nuevo.
- **«Jugar a mano»** (azul). El bot no pulsa nada y espera a que juegues la sala tú mismo.
- **«Ignorar (Continuar)»** (gris). Aceptar el combate tal como está y seguir adelante.
- **«Detener el bot»** (roja). En lugar de «Deshacer», se muestra cuando el combate fue manual (ulti de Angus) o cuando no hay un pack adecuado. La ventana «No hay pack adecuado» no tiene el botón «Continuar».

Cuando el pack que elegiste logre vencer, la pregunta «El pack lo logró» llega a Telegram con dos botones: **«Confirmar y Guardar»** (recordar el pack con una regla) y **«Deshacer y Reintentar»** (escribir otro). Solo va al chat si enviaste el pack también desde Telegram.

Después de pulsar, debajo del mensaje queda un único botón verde «Seleccionado: …», los demás desaparecen. Solo se puede responder **una vez**: el bot no escucha las pulsaciones en mensajes antiguos. Si respondiste en el chat, la ventana del ordenador se cerrará sola; si respondiste en el ordenador, el bot dejará de esperar respuesta desde Telegram.

> [!tip] ¿El bot decidió solo mientras buscabas el teléfono? No pasa nada. Llegará el mensaje «No respondiste — el bot decidió solo», y los botones de la pregunta antigua ya no harán nada. El tiempo que te espera el bot se configura en «Auto-táctica» (sección 8, «Tiempo de la ventana SOS sin respuesta, min»).

### Si se corta internet

El bot no se detiene ni espera a Telegram: el mensaje se envía en segundo plano. Si falla por la conexión, vuelve a intentarlo tras **30 segundos, 1, 2, 5 y 10 minutos** (unos 18 minutos en total), y en el registro se verán las líneas `Сообщение в Telegram не ушло (...). Пробую снова через N с.` y al final `Сообщение в Telegram: отправлено с N-й попытки`. Lo mismo ocurre con la ventana SOS: permanece en la pantalla del ordenador y la pregunta se enviará a Telegram cuando vuelva la conexión. El bot repite el resumen de la sesión de forma más breve (tras 10 y 30 segundos), porque después se apaga. Los errores del propio Telegram (token incorrecto) el bot no los reintenta: hay que corregirlos en los ajustes.

> [!note] El bot no acepta órdenes tuyas "en cualquier momento" (detener, pausar desde el chat). Telegram solo responde a las preguntas que el propio bot haya planteado. No se puede detener el bot desde el chat, salvo con el botón «Detener el bot» debajo del mensaje SOS.

> [!done] Telegram está configurado, y ahora el bot podrá llamarte estés donde estés. A continuación, las estadísticas: cuántas salas, pisos y titanita se han acumulado por días. [Siguiente sección →](#13)

## Estadísticas

La página «Estadísticas» responde a la pregunta "¿cuánto he jugado?": cuánta titanita, salas, pisos y pociones de titanes se han acumulado en una semana, un mes y en todo el tiempo. Se abre con el botón **«Estadísticas»** en la barra de la izquierda, y arriba dice «Estadísticas de actividad».

Estos números el bot **los calcula él mismo**, no los lee de la pantalla del juego. Ha completado una sala — anota: **6 de titanita y 25 de poción**, y si en la ventana de resultados había un icono «x2» — **12 de titanita y 50 de poción**. Ha recibido la recompensa en el punto de guardado — anota el piso. La sala que jugaste manualmente y que el bot dio por buena (sección 10), también la anota. Los resultados se guardan en el archivo `bot_data/stats.json` por "días de juego".

> [!note] El **día de juego** no empieza a medianoche, sino a la hora de reinicio que fijaste en el «Master de reglas» (por defecto a las 5:00, sección 7). Por eso, todo lo que el bot acumuló a las 02:30 de la noche queda anotado en el día **de ayer**: en el juego a esa hora todavía es el día de ayer. Si la «Titanita (hoy)» está a cero por la mañana aunque hayas jugado de noche, es totalmente normal.

### Qué hay en la página

Arriba a la izquierda hay una sugerencia, a la derecha la selección de **«Período»**, debajo cinco tarjetas, el gráfico y al final la «Corrección manual».

- :calendar: **Período** — «7 días», «14 días», «30 días» o «Todo el tiempo». El seleccionado se ilumina en azul. Al abrir por primera vez está en «14 días».
- :gem: **«Titanita»** — total del período.
- :calendar: **«Titanita (hoy)»** — solo del día de juego actual. No depende del período.
- :flask-conical: **«Poción de titanes»**, :door-open: **«Salas»** y :layers: **«Pisos»** — totales del período.

Los números hasta 100 000 en las tarjetas se escriben completos (`98 540`), y los más largos se abrevian: `105.5K` son ciento cinco mil quinientos, `1.24M` un millón doscientos cuarenta mil. El número completo aparecerá si pasas el ratón por encima de la tarjeta. «Todo el tiempo» toma los contadores generales del archivo y no la suma de las barras, por lo que las tarjetas coinciden con el historial aunque haya muchas barras.

> [!tip] La página lee los números **cada vez que se abre**, no a medida que juegas. ¿El bot está funcionando pero los números no cambian? Ve a otra página y vuelve.

![Página «Estadísticas»: tarjetas, gráfico por días y barra seleccionada con etiqueta](images/stats_page.png)

### Gráfico: barras y clics

Bajo el título «Actividad de titanita» figura una indicación de cómo se agrupan las barras: «por días», «por semanas» o «por meses». No hay más de quince barras para que el gráfico no se convierta en una empalizada:

- **7 y 14 días** — una barra por día.
- **30 días** — por semanas (de lunes a domingo; las semanas de los extremos pueden ser incompletas, incluyendo solo los días del período).
- **«Todo el tiempo»** — por días mientras haya menos de dos semanas de datos; luego por semanas, y cuando haya más de quince semanas, por meses.

A la izquierda hay una escala con cuadrícula punteada, los números de la escala son cortos (`3.6K`, `140K`). Las etiquetas debajo de las barras, si no caben, se muestran de dos en dos; la última (la de hoy) se ve siempre. Un día sin juego es un espacio vacío, no hay barra. Para un período sin datos el gráfico dirá «No hay datos para este período».

1. **Pasa el ratón sobre una barra.** Encima aparecerá el número exacto de titanita. Es solo una sugerencia, no cambia nada.
2. **Haz clic en una barra.** Se volverá más brillante, las demás se atenuarán y al lado aparecerá una etiqueta con la fecha y la cifra. En la etiqueta de una semana se detalla la titanita **por días**, y en la de un mes, **por semanas**. Arriba a la izquierda se iluminará un texto azul, por ejemplo «Día mostrado: 19.10.2026 · hoy» (o «Semana mostrada», «Mes mostrado»).
3. **Observa las tarjetas.** Ahora muestran las cifras de esa barra: titanita, poción, salas y pisos del día, semana o mes. «Titanita (hoy)» sigue mostrando el valor actual.
4. **Vuelve a los totales.** Haz clic de nuevo en la misma barra o en el texto azul con la cruz (✕). Si cambias de período, la selección también se restablecerá.

### Tabla

El botón **«Tabla»** arriba a la derecha del gráfico muestra las mismas barras en lista: «Fecha», «Titanita», «Salas», «Pisos», «Poción de titanes». Las fechas recientes arriba y abajo la fila **«Total»**. La fila también se puede seleccionar haciendo clic, y las tarjetas mostrarán sus cifras. El botón se convierte entonces en **«Gráfico»** y recupera la imagen. La tabla es práctica cuando necesitas números exactos de todos los días a la vez.

![Tabla: fechas, titanita, salas, pisos y poción, abajo «Total»](images/stats_table.png)

### Corrección manual

El bot calcula con su propia aritmética (6 o 12 de titanita por sala), pero en el juego la cifra puede ser diferente: jugaste tú mismo, el bot estaba apagado o se ejecutó el programa a mitad del día. Para que la estadística coincida con el juego, existe la tarjeta **«Corrección manual»**.

1. **Elige el día.** En la lista están «Hoy», «Ayer» y otros cinco días pasados, siete en total. ¿Necesitas un día más antiguo? Elige el período «7 días» o «14 días» y haz clic en su barra: ese día se colocará automáticamente en la lista (con las barras semanales o mensuales no se colocará, solo con la diaria).
2. **Escribe la cifra total del juego.** En el campo «Titanita por día» escribe lo que el juego muestra **para todo el día**, no "cuánto añadir". Para el día seleccionado ya figura lo que hay registrado actualmente.
3. **Pulsa «Aplicar»** (o Enter en el campo).

Ejemplo. El bot anotó 90 de titanita en el día, pero en el juego figuran 150 para ese mismo día. Introduces **150** — el programa añade la diferencia de 60 y recalcula el resto por sí solo: aproximadamente **+5 salas, +1 piso y +250 de poción**. Es una estimación: se considera que las 10 primeras salas del día dieron 6 de titanita cada una, y las demás 12. Si jugaste de otra forma, las salas y los pisos pueden diferir un poco de los reales, pero la titanita quedará exactamente como tú pusiste.

Cuando todo sale bien, abajo aparecerá el aviso «Titanita del 19.10.2026: 150», y en el registro de la pantalla principal se incluirá la línea `[СТАТИСТИКА] Данные за 2026-10-19 синхронизированы! Дельта: +60 тит., +5 комн., +250 зелий.` Si introdujiste menos de lo registrado, las cifras disminuirán.

Qué puede ir mal:

- **«Introduzca un número entero desde 0»** — hay letras, comas, signos menos o está vacío. El campo se pondrá rojo.
- **«El bot reunió 90 ese día por sí mismo; no puede indicar menos»** — no se puede escribir menos de lo que el bot ha conseguido **por sí mismo**, ya que eso quedó registrado de forma real. Solo se puede bajar la cifra hasta ese valor.
- **«Ese día ya tiene exactamente eso»** — introdujiste el mismo número, no hay nada que cambiar.

> [!warning] «Aplicar» escribe los datos **de inmediato** en `bot_data/stats.json`. Aquí no hay ni hace falta un botón «Guardar ajustes», como en el «Master de reglas» (sección 7). No se puede deshacer la modificación con un botón, pero nada te impide volver a introducir la cifra anterior.

> [!note] La corrección modifica **solo las estadísticas**. El «Resumen de la sesión» en la pantalla principal y el objetivo de la sesión (sección 4) se calculan por separado, según lo que el bot obtuvo en esta ejecución, y no dependen de la página «Estadísticas».

### «Restablecer»: borrar todo el historial

El botón **«Restablecer»** (con una papelera, a la derecha en la tarjeta «Corrección manual») pone a cero todas las estadísticas: titanita, salas, pisos y pociones de todos los días. ¿Pulsaste por error? No pasará nada: primero el programa preguntará «¿Restablecer las estadísticas?» y recordará que esto no se puede deshacer. Con el botón «Restablecer» de la ventana confirmas, y con el botón «Cancelar» rechazas. Tras restablecer, aparecerá el aviso «Estadísticas restablecidas» y en el registro la línea `[СТАТИСТИКА] Вся история полностью сброшена!`.

Solo se borran las estadísticas. Las reglas, los packs, los ajustes, `profile.yml` y los registros de combates se conservan. Si el bot está funcionando en ese momento, continúa y sigue contando desde cero, y el objetivo de la sesión no se altera.

> [!tip] ¿Quieres restablecer "a modo de prueba"? Guarda primero una copia: cierra el programa y copia el archivo `bot_data/stats.json` en otro sitio (la carpeta del programa se abre con el botón «Carpeta del bot» en la página «Acerca de»). Puedes recuperar el historial volviendo a colocar el archivo en su lugar.

### Preguntas frecuentes

- **Las cifras no coinciden con el juego.** El bot calcula, no lee la pantalla: 6 o 12 de titanita por sala. Si obtuviste titanita de otras fuentes, el juego mostrará más. Compara y ajusta a través de la «Corrección manual».
- **El día de hoy está vacío, pero he jugado.** Comprueba la hora de reinicio: antes de esa hora el bot escribe en "ayer" (mira "Día de juego" más arriba). ¿Cambiaste la hora en el «Master de reglas»? Reinicia el programa para que la página también la aplique.
- **Hay pocas barras para un período grande.** Los días en los que el bot no funcionó están vacíos en el gráfico. «Todo el tiempo» y los meses comprimen el gráfico por defecto: para ver días concretos, selecciona «7 días» o «14 días».
- **En el registro aparece `[СТАТИСТИКА] ВНИМАНИЕ: Файл stats.json поврежден`.** El archivo con el historial no se pudo leer (por ejemplo, el ordenador se apagó mientras escribía). El bot inicia unas nuevas estadísticas desde cero y sobrescribirá el archivo. Copialo de antemano si el historial antiguo es importante.

> [!done] Ahora ya sabes cómo leer los números, cambiar de período, comparar las estadísticas con el juego y borrarlas. A continuación, qué hacer si algo sale mal. [Siguiente sección →](#14)

## Si algo sale mal

Buenas noticias: el bot sabe salir por sí solo de la mayoría de los problemas. Si se bloquea, observará y empezará de nuevo. Si se pierde internet, esperará. Si bloqueas la computadora, se detendrá y continuará después. Solo te necesita cuando **él mismo lo pida** (se ponga en pausa, escriba en Telegram) o когда no presione nada y no se entienda por el registro qué sucede. Esta sección trata sobre ambos casos: qué hace el bot sin ti, cómo entender dónde está el fallo y qué presionar.

Regla para todos los casos: **no entres en pánico y no tengas prisa**. No pasa nada si detienes, reinicias y vuelves a ejecutar el bot: las estadísticas, alineaciones, reglas y ajustes están guardados en archivos y no irán a ninguna parte.

### Cómo saber si algo va mal

- :triangle-alert: **Un número rojo en la pestaña «Errores»** en el registro de la página principal. No solo cuenta fallos: también incluye advertencias (por ejemplo, "la ventana del juego está cubierta"). El número por sí solo no es motivo de susto: abre la pestaña y lee las líneas.
- :pause: **El estado «Pausa» y el botón verde «Continuar», хотя ты паузу не нажимал.** Significa que el bot se detuvo solo y te está esperando. En el registro aparecerá la línea `[ВНИМАНИЕ] Бот на мягкой паузе: ...` con el motivo.
- :send: **Un mensaje en Telegram** (si está configurado, sección 12): «Parece que el bot se ha bloqueado», «No se pudo revertir el combate», «La pantalla del PC está bloqueada».
- :eye: **Silencio.** No aparecen líneas en el registro durante un minuto o más, y en el juego no ocurre nada. Esto también es una señal: consulta la sección «Casos frecuentes» más abajo.

Etiquetas en el registro que indican un проблема:

- `[СТОРОЖ]` — el bot decidió que se bloqueó y volvió a empezar por sí solo.
- `[СЕТЬ]` — parece que no hay conexión con el servidor del juego.
- `[ЭКРАН]` — la computadora no permite hacer una captura de pantalla (está bloqueada).
- `[ОТКАТ]` — pasos de la reversión del combate y sus errores (sección 10).
- `[ВНИМАНИЕ]` — el bot requiere atención: pausa, ventana del juego cubierta o cerrada.
- `[ОШИБКА]` — algo se ha roto; al lado pone qué.
- `[ADB]` y `[VISION]` — conexión con el teléfono y toques.

### Qué hace el bot por sí solo

Aquí no tienes que presionar nada. Solo ten en cuenta que esto es normal y no arruina la sesión.

- :gauge: **Bloqueado: 5 minutos sin superar ninguna sala.** Es el «vigilante» (así se llama la comprobación que controla si el bot se ha atascado). El bot escribe `[СТОРОЖ] Бот 5 мин не прошёл ни одной комнаты ... Тревога 1 из 3.`, guarda una captura de pantalla, envía un mensaje a Telegram (si está configurado) y realiza un **«inicio inteligente»**: vuelve a mirar la pantalla y decide desde dónde continuar. Si no ayuda, tras otros 5 minutos vuelve a saltar la alarma. **Una tercera alarma consecutiva** (es decir, unos 15 minutos sin salas) provocará que el bot entre en pausa suave y te espere. El vigilante no cuenta el tiempo que el bot estuvo esperándote (ventana SOS, pausa, otra ventana sobre el juego).
- :activity: **Atascado en un mismo sitio.** La pantalla de selección de equipo no apareció en 30 segundos o la ventana de resultado no apareció en 3 minutos. En ese caso aparece `[СТОРОЖ] Зависание: ...`, se toma una captura de pantalla y se hace el mismo inicio inteligente, pero sin enviar alarma a Telegram.
- :globe: **El combate no empieza (lo más probable es que no haya conexión con el servidor del juego).** El botón "Auto" está presionado, pero el combate no empieza. El bot lo intenta dos veces más de inmediato, luego espera y lo vuelve a intentar: tras 30 segundos, 1, 2, 4 y 8 minutos. Todo esto figura en el registro como `[СЕТЬ] Бой не начался N раз(а) подряд ... Жду N с и пробую снова.` Si esto tampoco ayuda (unos 15 minutos): captura de pantalla, mensaje «Parece que el bot se ha bloqueado» y pausa suave.
- :rotate-ccw: **Se perdió la conexión durante la reversión del combate.** El bot no se rinde y **espera al juego hasta 15 minutos**: escribe `[ОТКАТ] Бой не загрузился ... Не сдаюсь`, guarda una captura de pantalla y una vez por minuto informa `Всё ещё жду игру`. Si la conexión vuelve, la reversión finalizará por sí sola (`Игра снова откликается`). Si no vuelve tras 15 minutos: «No se pudo revertir el combate», mensaje en Telegram y pausa.
- :monitor: **La computadora está bloqueada (Win+L) o la pantalla se apagó.** Windows no permite tomar capturas y el bot no ve nada. El bot **no se cierra con error**, sino que lo vuelve a intentar cada 2 segundos: `[ЭКРАН] Не удаётся сделать снимок экрана ... Похоже, ПК заблокирован`. Si pasa de un minuto: un mensaje «La pantalla del PC está bloqueada». Si desbloqueas: `[ЭКРАН] Снимок экрана снова работает`, y el bot continúa por sí solo.
- :layers: **La ventana del juego está cubierta por otra ventana.** El bot espera hasta que vuelva a ser la principal (`[ВНИМАНИЕ] Окно игры перекрыто ... Бот ждет фокуса`). Haz clic en la ventana del juego y continuará. El motivo de esto está en la sección 5.
- :target: **El toque no se registró.** Si 4 segundos después del toque la pantalla no cambia, el bot vuelve a pulsar: `[VISION] Клик по '...' не зарегистрирован сервером ... Повторяю...`. Que aparezcan estas líneas de forma aislada es normal: el teléfono a veces "piensa".
- :smartphone: **La conexión por cable con el teléfono parpadeó.** El bot escribe `[ADB] Постоянное соединение с телефоном оборвалось ... Переподключусь при следующем нажатии` y se vuelve a conectar.
- :send: **El mensaje de Telegram no se envió por problemas de internet.** El bot lo reintentará más tarde (sección 12) y seguirá trabajando.

> [!note] Cuántas veces se bloqueó el bot durante la sesión se puede ver en el bloque `[ИТОГ]` del registro (la línea con la palabra "зависания"). Los casos raros no son un problema. Si hay muchos, busca la causa en la sección «Casos frecuentes» más abajo.

### El bot se ha puesto en pausa solo: qué hacer

Se ha detenido потому что дальше без тебя нельзя. Actúa en orden:

1. **Mira la pantalla del juego.** La ventana `HeroWarsBot_Arena` muestra dónde se ha atascado el bot: ventana de resultado, combate, menú de pausa, el icono de carga o algo inesperado (otra ventana, publicidad, una solicitud del juego).
2. **Lee las últimas líneas del registro.** Abre la pestaña «Errores» y mira la parte inferior: allí pone por qué se detuvo el bot (`[СТОРОЖ]`, `[ОТКАТ] ОШИБКА`, `[СЕТЬ]`).
3. **Vuelve al corredor de la Mazmorra en el juego.** Cierra lo innecesario, espera a que el combate termine o cargue, y ve a la pantalla con la puerta y el banderín.
4. **Presiona «Continuar».** El bot volverá a examinar la pantalla (inicio inteligente) y seguirá adelante.

> [!note] La pausa tras una reversión fallida también ocurre así: el combate manual terminó, el botón "Otra vez" en la ventana de resultados ya no está y no se puede revertir. La ventana de resultados permanece en pantalla: no hace falta cerrar nada, tras presionar «Continuar» el bot presionará "OK" por sí solo. Mira en esa ventana quién ha sobrevivido.

> [!tip] El bot no entra en pausa por cualquier pequeñez, sino cuando lo ha intentado y no lo ha conseguido. Por lo tanto, antes de presionar «Continuar», averigua **qué exactamente** ha salido mal. Si la causa persiste (sin internet, juego cerrado), el bot se volverá a pausar al cabo de unos minutos.

### Casos frecuentes: qué mirar y qué hacer

**El bot no presiona nada y el registro está en silencio.** Lo más probable es que no vea el juego o no pueda encontrar nada en él. Comprueba en orden:

1. **La ventana del juego está en su sitio.** Se llama `HeroWarsBot_Arena`, no está minimizada ni cerrada. Si la ventana no existe, el bot no escribe sobre ello, sino que la comprueba en silencio cada medio segundo. Por lo tanto, el silencio en el registro cuando la ventana ha desaparecido es algo habitual. Presiona «Conectar teléfono»: la ventana se volverá a abrir.
2. **El tamaño de la ventana no ha cambiado.** El bot mide la ventana una sola vez al iniciar y luego usa esa medida. Si estiraste, maximizaste o moviste la ventana tras iniciar, detén el bot (F10), presiona «Restablecer el tamaño de la ventana del juego» y vuelve a presionar «Empezar a farmear». Los detalles están en la sección 3.
3. **En el juego estás en el corredor de la Mazmorra**, y no en el menú, la tienda, un evento ajeno o una ventana con publicidad.
4. **El idioma del programa coincide con el idioma del juego** (las dos letras en la parte inferior de la barra izquierda). De lo contrario, el bot no reconocerá los botones.
5. **Nada obstaculiza la ventana del juego.** Cualquier ventana encima del juego hará que el bot espere al foco.

**El bot «ve» y toca, pero en el juego no ocurre nada.** En el registro aparecen continuamente líneas de «Клик по ... не зарегистрирован сервером ... Повторяю...». Significa que el comando de toque no llega al teléfono. Comprueba:

- Que estén activados **ambos** ajustes de depuración en el teléfono: "Depuración por USB" y "Depuración por USB (ajustes de seguridad)". Sin el segundo, la imagen se ve pero los toques no funcionan (sección 2).
- Que el teléfono esté desbloqueado y el cable bien conectado. Prueba otro puerto USB.
- Que en la línea de comandos `adb devices` muestre `device` junto al teléfono, y no `unauthorized` ni una lista vacía.
- Si no ayuda: detén el bot, presiona «Reiniciar scrcpy» y luego «Empezar a farmear».

**El bot toca donde no debe o confunde a los titanes.** Lo más habitual es que la ventana del juego no tenga el tamaño correcto o que se haya tocado tras el inicio (restablecer el tamaño, como se indicó arriba). Si el tamaño es correcto pero el bot se sigue equivocando, guarda una captura de pantalla de ese momento y envíasela al autor junto con el registro (más abajo).

**La ventana del programa "no responde".** El programa se supervisa a sí mismo: si la ventana no responde durante 5 segundos, escribe en un archivo en qué línea de código se ha quedado atascada. El archivo se encuentra en `bot_data/debug/` y se llama `ui_freeze_<дата>_<время>.txt`. Qué hacer:

1. **Espera un minuto.** A menudo la ventana vuelve a responder por sí sola: está ocupada con tareas pesadas.
2. **El bot funciona de forma independiente a la ventana.** ¿Necesitas detenerlo pero los botones no responden? Presiona Ctrl+Shift+Q: este atajo lo escucha el propio bot y no la ventana del programa (sección 6).
3. **Si no responde, cierra la ventana con la X.** Si no se cierra, hazlo a través del Administrador de tareas (Ctrl+Shift+Esc). Luego comprueba allí mismo si `HeroWarsBot.exe` o `python` siguen en la lista: si es así, ciérralos también, de lo contrario el bot seguirá realizando toques en el juego sin la ventana.
4. **Envía el archivo `ui_freeze_...txt` al autor.** Solo contiene nombres de archivos y líneas de código del programa, nada personal.

**El bot se detuvo y tú no lo detuviste.** Abre la tarjeta «Resumen de la sesión» en la página principal (botón «Detalles») y comprueba el motivo:

- «ventana de scrcpy cerrada»: la ventana del juego se cerró o desapareció (se desconectó el cable, el teléfono se bloqueó). Vuelve a conectar el teléfono.
- «el bot terminó»: el proceso finalizó sin motivo. Si tienes Telegram configurado, el resumen llegó allí; si no, busca en el registro la línea `[ОШИБКА] Бот остановился из-за ошибки:` y el texto debajo.
- «Пак не найден в правилах» — para la sala no se ha definido una alineación principal. Abre «Maestro de reglas» → «Base y salas» y defínela en las cuatro salas (sección 7).
- «Ошибка: ...» — el programa se ha cerrado inesperadamente. Envía el registro al autor (más abajo).

> [!warning] Tras presionar «STOP» (F10), el bot no tiene tiempo de escribir el bloque `[ИТОГ]` ni envía el resumen a Telegram: se detiene de golpe (sección 6). Esto no es un error.

**El teléfono se durmió o la pantalla se apagó.** El programa ejecuta scrcpy con el modo "no permitir que el teléfono se duerma" (`--stay-awake`). El botón «Apagar la pantalla del teléfono» apaga solo la **pantalla**: el juego sigue ejecutándose y el bot lo ve todo. Pero si el teléfono se bloqueó o se desconectó del cable, la ventana del juego mostrará la pantalla de bloqueo o se quedará en blanco, y el bot no encontrará nada. Desbloquea el teléfono, comprueba el cable y presiona «Reiniciar scrcpy».

**No llegan los mensajes a Telegram.** Lo más probable es que no hayas presionado "Iniciar" en tu bot o que el token/Chat ID no sea correcto: análisis en la sección 12. Mientras tanto, el bot funciona como de costumbre.

**El bot coloca titanes incorrectos o no decide como querías.** No es un fallo, sino las reglas: revisa las secciones 7–11 (alineaciones, umbrales, reglas, «El bot decide solo»). La decisión del bot siempre se puede consultar en el registro buscando las líneas `[ТАКТИКА]`.

### Dónde se guardan los registros y capturas de pantalla

El botón **«Carpeta del bot»** en la página «Acerca de» abre la carpeta desde la que se ejecuta el programa. En ella están los archivos que crea el propio bot. Lo importante se encuentra dentro de la carpeta `bot_data`:

- :file-text: `bot_data/logs/bot_log_<дата>_<время>.txt` — **registro completo de cada inicio del bot.** El bot lo escribe por sí solo, línea por línea, por lo que se conserva incluso si el programa falla o se cierra. Es el archivo principal para analizar problemas.
- :gauge: `bot_data/logs/timings_<дата>_<время>.csv` — cuánto tiempo ha tardado cada sala (corredor, preparación, combate, resultado).
- :swords: `bot_data/logs/battle_log_<дата>_<время>.jsonl` y `battle_log.csv` — historial de combates: sala, enemigos, alineación, resultado, vida y energía de los titanes.
- :image: `bot_data/debug/` — **capturas de pantalla para diagnóstico.** El nombre indica qué ocurrió: `stuck_...` — bloqueado, `sos_...` — ventana SOS, `rollback_wait_...` — esperando al juego durante la reversión, `rollback_fail_...` — la reversión falló, `start_fail_...` — el combate no comenzó, `result_unreadable_...` — no se pudo leer la ventana de resultados. A continuación figura el número de sala, elemento y hora (`stuck_комната12_water_2026-10-19_14-03-21.png`). Allí también se encuentra `ui_freeze_...txt` si la ventana del programa se congeló.

> [!warning] El bot elimina automáticamente lo antiguo: al iniciar, en `bot_data/logs/` se conservan los 20 archivos más recientes de cada tipo (`.txt`, `.jsonl`, `timings_*.csv`), y en `bot_data/debug/` las 50 capturas más recientes. Si deseas conservar los registros tras una noche con problemas, **cópialos a otra ubicación antes del siguiente inicio del bot**. De la misma forma se borra el registro que hayas guardado con el botón «Guardar registro» en la carpeta por defecto: guárdalo en otro sitio, por ejemplo en el escritorio.

> [!warning] No elimines ni cambies de nombre a `profile.yml` (tus ajustes y Telegram) ni a la carpeta `bot_data`: contiene estadísticas, reglas aprendidas por el bot e historial de combates. Solo puedes borrar `bot_data/debug` y registros antiguos cuando ya no los necesites.

### Cómo enviar el registro al autor

Cuando no logres solucionar un problema, la vía más rápida es enviar al autor lo sucedido.

1. **Recuerda cuándo ocurrió.** La hora y la cantidad aproximada de salas (`[СТАТИСТИКА] Комнат: N`) ayudan a encontrar el lugar adecuado en un registro largo.
2. **Busca los archivos.** El registro es `bot_data/logs/bot_log_...` de esa noche, las capturas son de `bot_data/debug/` con una hora similar en el nombre y, en caso de congelación de ventana, también `ui_freeze_...txt`.
3. **Presiona «Enviar registro al autor»** debajo del registro en la página principal. El programa te ofrecerá guardar el contenido actual del registro (el archivo `gui_log_...txt`) y luego abrirá tu cliente de correo con un mensaje listo dirigido al autor.
4. **Adjunta los archivos al mensaje manualmente.** El programa no puede adjuntar archivos al mensaje: solo abre el cliente de correo. Adjunta `gui_log_...txt` o `bot_log_...txt`, las capturas de pantalla y (si ocurrió) `ui_freeze_...txt`.
5. **Describe con palabras:** qué estabas haciendo, qué esperabas, qué viste y cuándo ocurrió. Una simple frase como "no funciona" apenas ayuda al autor.

> [!warning] **Nunca adjuntes** `profile.yml` ni `bot_data/profile.yml.bak`: contienen el token de tu bot de Telegram. Si envías una captura de la ventana «Ajustes de Telegram», asegúrate también de que el token esté oculto (con puntos).

> [!note] ¿No se abrió el correo (no tienes un cliente de correo configurado)? En la página «Acerca de» hay un botón «Escribir al autor»: si no se puede abrir el correo, copiará la dirección al portapapeles y podrás escribir desde cualquier servicio de correo.

### Si nada funciona

Ve de lo simple a lo complejo, comprobando tras cada paso si el bot ha vuelto a responder:

1. **«Pausa» → vuelve a poner el juego en el corredor → «Continuar».**
2. **«STOP» (F10) → «Empezar a farmear».** El bot realizará un inicio inteligente y averiguará por sí solo dónde se encuentra.
3. **Detén el bot y presiona «Reiniciar scrcpy».** Luego vuelve a presionar «Empezar a farmear».
4. **Cierra el programa y vuelve a abrirlo.** Si el teléfono se quedó "atascado", desconecta y vuelve a conectar el cable.
5. **Reinicia la computadora y el teléfono.** Suena a broma, pero resuelve la mitad de los problemas extraños.

Los objetivos de la sesión (tiempo, salas, pisos, titanita) se vuelven a contar desde cero tras reiniciar, pero las estadísticas, alineaciones y reglas se conservan: están guardadas en archivos.

> [!done] Ahora ya sabes cómo el bot se recupera por sí solo, qué hacer cuando se detiene y cómo recopilar y enviar el registro. Solo queda la última sección: sobre el programa y cómo apoyar el proyecto. [Siguiente sección →](#15)

## Acerca de y soporte

La última página del menú izquierdo es «Acerca de». Trata sobre el propio programa: qué versión tienes, si todo está en su sitio, dónde escribir al autor y cómo darle las "gracias". No requiere configurar nada, pero aquí se encuentran dos botones muy útiles: «Buscar actualizaciones» y «Carpeta del bot».

### Qué hay en la página

- :shield-check: **Tarjeta del programa** en la parte superior. Nombre «Hero Wars: Knowledge Engine Bot», al lado — **número de versión** (por ejemplo, `v1.6.1`) y la etiqueta `Beta`. "Beta" significa "en fase de pruebas en uso real": el programa funciona, pero el autor aún lo está perfeccionando y puede haber errores. Debajo del nombre hay una breve descripción. A la derecha hay cuatro botones, de los que se habla más abajo.
- :user: **«Autor y licencia»**: имя автора, его почта и лицензия. Щёлкни по адресу почты — откроется письмо.
- :monitor: **«Estado de los componentes»**: comprobación de que la computadora tiene todo lo necesario para funcionar. Más detalles abajo.
- :heart: **«Apoyar el proyecto»**: formas de agradecer al autor. Es totalmente opcional.

> [!tip] Indica la versión al autor cuando escribas sobre un problema: muestra de inmediato qué versión exacta estás utilizando. La versión está en la tarjeta superior, junto al nombre.

### Los cuatro botones de la tarjeta

1. **«Buscar actualizaciones».** Abre en el navegador la página de versiones del proyecto en GitHub (GitHub es el sitio web donde el autor aloja el programa; una "versión" es una entrega lista para descargar). Compara allí el número más reciente con el tuyo. Si es más nuevo, puedes actualizar; si es el mismo, ya tienes la versión más reciente.
2. **«Carpeta del bot».** Abre en el Explorador de Windows la carpeta desde la que se ejecuta el programa: esa misma donde están tus ajustes y datos. Resulta útil cuando necesitas copiar archivos o buscar un registro.
3. **«Escribir al autor».** Abre un mensaje dirigido al autor en tu cliente de correo. Si no tienes un cliente de correo en la computadora, el mensaje no se abrirá. En ese caso, el programa copiará automáticamente la dirección al portapapeles (la memoria temporal donde se pega con Ctrl+V) y te avisará en la parte inferior de la ventana: «No se pudo abrir: copiado al portapapeles». Pega la dirección en un mensaje desde cualquier servicio de correo.
4. **«GitHub del proyecto».** Abre la página principal del proyecto en GitHub: allí se encuentra el código fuente y la descripción.

> [!note] El programa **no accede a internet por sí solo para buscar actualizaciones**: «Buscar actualizaciones» solo abre la página y tú decides. Está diseñado así para que nada cambie sin tu conocimiento.

### Cómo actualizar el programa

La actualización no se "instala encima": descargas la nueva versión y le transfieres tus datos. De esta forma, tus alineaciones y estadísticas no se perderán.

1. **Detén el bot y cierra el programa.** Si el bot está funcionando, al hacer clic en la X de la ventana se preguntará si deseas detenerlo.
2. **Descarga la nueva versión** en la página de versiones (botón «Buscar actualizaciones») y descomprímela en una carpeta nueva, no sobre la antigua.
3. **Transfiere tus datos.** Copia desde la carpeta antigua a la nueva el archivo `profile.yml` y la carpeta `bot_data` completa. Sin ellos, el nuevo programa empezará "desde cero": ajustes vacíos y estadísticas vacías.
4. **Ejecuta el nuevo programa** y consulta «Acerca de»: el número de versión debe ser el nuevo y los tres componentes deben estar en orden.
5. **No elimines la carpeta antigua todavía.** Trabaja un par de días con la nueva versión. Si todo va bien, puedes eliminarla.

> [!warning] No copies los archivos de `bot_data` uno a uno según "lo necesario", transfiere la carpeta completa: las reglas aprendidas por el bot, el historial de combates y las estadísticas están vinculados entre sí y no se pueden reconstruir por separado.

### «Estado de los componentes»

El programa comprueba automáticamente que esté presente todo lo necesario para que el bot funcione. La comprobación se realiza en segundo plano cada vez que se accede a la página. Mientras se ejecuta, se muestra «comprobando».

- :smartphone: **ADB** — el servicio mediante el cual la computadora realiza toques en el teléfono. Debe figurar como «encontrado».
- :monitor: **scrcpy** — el programa que muestra la pantalla del teléfono en una ventana en la computadora. Debe figurar como «encontrado».
- :image: **Base de plantillas** — las "imágenes modelo" de botones y titanes con las que el bot reconoce lo que hay en pantalla. Debe figurar como «cargada».

Qué hacer si algo figura en rojo:

- **ADB o scrcpy figura como «no encontrado».** Significa que la carpeta que los contiene no se ha añadido a la variable `PATH` (la lista de rutas donde Windows busca programas). Cómo hacerlo se explica en la sección [«Qué se necesita e instalación»](#2). Tras modificar `PATH`, cierra el programa y vuelve a abrirlo: un programa ya iniciado no detectará la nueva ruta en `PATH`.
- **La base de plantillas figura como «no encontrada».** Han desaparecido archivos de la carpeta del programa. Con frecuencia ocurre porque el archivo no se descomprimió por completo o porque el antivirus eliminó algo. Vuelve a descomprimir el archivo en una carpeta nueva y transfiere `profile.yml` y `bot_data` como se hace al actualizar.

### Qué hay en la carpeta del bot y qué no se debe eliminar

Abre la carpeta con el botón «Carpeta del bot». Hay muchos archivos allí, pero solo necesitas unos pocos. El resto son archivos del sistema necesarios para el funcionamiento del programa.

- :file-text: `HeroWarsBot.exe` — el propio programa. El bot también se ejecuta desde este archivo, no tiene un archivo independiente. Todos los demás archivos y carpetas a su lado (`guide`, `ui`, bibliotecas, archivos con extensión `.dll` y otros) forman parte del programa. **No elimines ni cambies de nombre nada de esto**, de lo contrario dejará de ejecutarse.
- :file-text: `profile.yml` — tus ajustes: objetivo de la sesión, umbrales, Telegram. **Contiene el token de tu bot de Telegram, por lo que nunca se lo envíes a nadie.** Aparece tras presionar por primera vez «Guardar ajustes».
- :folder: `bot_data` — todo lo que el programa y el bot han registrado. Es **lo más valioso** que tienes. En su interior:
  - `stats.json` — estadísticas (página «Estadísticas»);
  - carpeta `rules` — tus alineaciones y reglas, incluidas las aprendidas por el bot;
  - carpeta `logs` — historial de combates y registro del bot (`bot_log_...txt`);
  - carpeta `debug` — capturas de pantalla para diagnóstico (ventanas SOS, bloqueos, reversiones fallidas);
  - `titan_state.json` — salud y energía de los titanes durante el día de juego;
  - `profile.yml.bak` — copia de respaldo de los ajustes. De aquí toma los datos «Restaurar / Restablecer» en el «Maestro de reglas». **También contiene el token de Telegram**;
  - `ui_settings.json` — idioma seleccionado para la ventana;
  - `sos_info.json`, `temp_sos.png`, `temp_test.png` — pequeños archivos temporales para los mensajes de Telegram.
- :pause: `pause.flag` — el "indicador de pausa". Aparece cuando el bot entra en pausa suave. Si quedó de una sesión anterior, el programa lo eliminará automáticamente al iniciar.

> [!warning] **No elimines ni cambies de nombre** a `profile.yml` ni a `bot_data`. Si eliminas `bot_data`, perderás las estadísticas, alineaciones, reglas y todo lo aprendido por el bot. Si necesitas liberar espacio de forma urgente, puedes borrar el contenido de `bot_data/debug` y los registros antiguos de `bot_data/logs`. Sin embargo, el bot conserva automáticamente solo los últimos 20 registros y 50 capturas de pantalla, por lo que el espacio no suele ser un problema.

> [!tip] **Haz una copia de seguridad una vez a la semana.** Copia `profile.yml` y la carpeta `bot_data` a una memoria USB o a la nube. Si la computadora falla o reinstalas Windows, podrás volver a descargar el programa y recuperar las alineaciones y estadísticas desde tu copia. Dado que la copia contiene el token de Telegram, guárdala en un lugar privado y no en una carpeta compartida.

### Autor y licencia

El programa fue creado y es mantenido por **Platon Petrunin**. Para preguntas, errores e ideas, utiliza el botón «Escribir al autor» o la dirección que figura en la tarjeta «Autor y licencia».

La licencia se llama **PolyForm Noncommercial 1.0.0**. En pocas palabras:

- :check: se puede usar para uso personal en tu propio juego de forma gratuita, todo lo que quieras;
- :check: también se puede estudiar el código y modificarlo para uso propio;
- :x: **no se puede lucrar**: vender el programa o su archivo `.exe`, hacerlos pasar por propios con otro nombre o integrarlos en servicios de pago. Para ello se requiere la autorización por escrito del autor.

> [!note] Esto es un breve resumen y no un texto legal. Si tu caso es particular (por ejemplo, deseas distribuir el programa entre tus amigos o una comunidad), escribe primero al autor. El texto completo de la licencia se encuentra en el archivo `LICENSE` del proyecto en GitHub.

### Cómo apoyar el proyecto

El programa es gratuito y el autor lo desarrolla en su tiempo libre. Si te ahorra tiempo y molestias, puedes expresar tu agradecimiento con una aportación económica. Esto es **voluntario**: el bot funciona exactamente igual independientemente de si has pagado o no, y no existe ninguna "función de pago".

En la parte inferior de la página «Acerca de» hay tres bloques:

1. **«Criptomonedas».** Tres monederos: `USDT · TRC20`, `Bitcoin · BTC` y `Ethereum · ETH`. La dirección completa se ve en el campo. Puedes copiarla con el botón «Copiar» situado a la derecha (abajo aparecerá «Dirección copiada»), haciendo doble clic en el campo (se seleccionará todo) o haciendo clic con el botón derecho del ratón y seleccionando «Copiar».
2. **«Donar por Telegram».** Tres líneas: rublos (`RUB`), euros (`EUR`) y dólares (`USD`). En cada una hay dos botones: **«Aplicación»** abre el pago en la aplicación de Telegram, **«Navegador»** lo abre en el navegador si no tienes Telegram instalado. Elige la divisa que te resulte más cómoda.
3. **«Transferencias directas».** Los botones «Apoyar en Boosty» y «YooMoney (RUB)»: abren las páginas de estos servicios, donde el proceso es similar a un pago convencional.

> [!warning] **Ten cuidado con las criptomonedas.** Realiza las transferencias únicamente a través de la red indicada junto al monedero: para `USDT` es `TRC20` y no otra. Los fondos enviados a una red equivocada **no se pueden recuperar**. Toma la dirección exclusivamente desde el programa utilizando el botón «Copiar»: en páginas web o en mensajes de terceros podría estar alterada. La primera vez, envía una cantidad pequeña.

### Preguntas frecuentes

- **Tengo una versión antigua, ¿es un problema?** No. El programa no deja de funcionar por el hecho de que haya salido una versión nueva. Sin embargo, en las versiones recientes suelen corregirse errores, por lo que es recomendable consultar la página de publicaciones cada pocas semanas.
- **«Carpeta del bot» no se ha abierto.** Aparecerá el mensaje «No se pudo abrir la carpeta». Ábrela manualmente: abre el explorador de archivos y ve a la carpeta donde descomprimiste el programa.
- **¿Por qué no hay un botón "Actualizar"?** El programa no descarga nada por sí solo para evitar alterar tus ajustes sin tu permiso. La actualización la realizas tú manualmente siguiendo los pasos indicados anteriormente.
- **Si no realizo una aportación, ¿cambiará algo?** Nada. El bot funciona de la misma manera para todos.

> [!done] Esta es la última sección. Ahora sabes todo lo necesario para ejecutar el bot, configurarlo a tu gusto, entender sus decisiones y solucionarlo si algo sale mal. ¡Que disfrutes del juego! Si te han quedado dudas, abajo tienes el botón «Escribir al autor».
