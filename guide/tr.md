# Hero Wars: Knowledge Engine Bot

Selam! Bu, Hero Wars oyunundaki Titan Zindanı'nı senin yerine otomatik geçen bir programdır. Sen programı çalıştırıp kendi işlerine bakarsın; o ise kapıları açar, takımları kurar ve ödülleri toplar.

Bu kılavuz, herkesin rahatça anlayabileceği şekilde yazılmıştır. Bilinmeyen kelimeleri anında açıklıyor, her bölümün sonunda ise sıradaki adımı belirtiyoruz.

## Bot neler yapabilir

Bot sıradan bir "tıklayıcı" değildir. Oyun ekranına tıpkı senin baktığın gibi bakar ve ne yapacağına kendisi karar verir. İşte yapabildikleri:

- :eye: **Eranı görür.** Saniyenin kesirlerinde oyun penceresinin ekran görüntüsünü alır; üzerindeki butonları, kapıları ve düşmanları tanır.
- :door-open: **Kapıyı seçer.** Odalara senin belirlediğin sırayla girer ve şu an tehlikeli olan odaları teğet geçer.
- :users: **Takımı kurar.** Her oda için bir "paketi" vardır (beş titanlık takıma böyle diyoruz). Bot titanları yerlerine kendisi yerleştirir.
- :heart-pulse: **Sağlığı takip eder.** Her savaştan sonra titanların Canını (sağlığını) ve enerjisini okur, paketin bir sonraki savaşa hazır olup olmadığına karar verir.
- :swords: **Savaş kötü geçerse seni çağırır.** «Müdahale gerekiyor» penceresi görünür: savaşı başka bir paketle yeniden oynayabilir, sonucu kabul edebilir veya elle geçebilirsin. Bilgisayar başında değilsen bot kendisi karar verebilir.
- :chart-no-axes-column: **Kendi savaşlarından öğrenir.** Hangi paketin hangi düşmanları yendiğini hatırlar ve bir dahaki sefere onu doğrudan sahaya sürer.
- :send: **Telegram'a yazar.** Иstersen oturum özetini ve bir şeyler ters gittiğinde uyarı bildirimi gönderir.

> [!note] Örnek. Araji savaşa %36 canla girdi ve savaştan sonra canı %8'e düştü. Bot bunu görür, savaşın kötü geçtiğini anlar ve ya sana sorar ya da savaşı geri alıp başka bir paketle yeniden oynar.

### Bot neleri yapmaz

- **Sadece Titan Zindanı'nı** geçer. Oyunun diğer modlarını bilmez.
- **"Bulutta" oynamaz**. Oyun senin Android telefonunda çalışır; Windows bilgisayar ise USB kablosu üzerinden telefon ekranına bakarak tıklamalar yapar. Hem телефон hem de bilgisayar gereklidir.
- Sihirbaz değildir: oyunla bağlantı kesilirse dürüstçe geri gelmesini bekler ve sana bunu haber verir.

### Bu hesap için güvenli mi?

Bot bir robot gibi değil, canlı bir insan gibi davranmaya çalışır:

- her tıklama butonun hep aynı noktasına değil, **rastgele bir noktasına** yapılır;
- tıklamadan önce buton göründükten sonra 0,3 ila 0,8 saniyelik bir **reaksiyon duraklaması** verir;
- **saniyede en fazla iki kez** tıklar.

> [!warning] Hiçbir program tam garanti veremez: oyun kurallarını yayıncısı belirler. Bot "insanüstü hızlı" hiçbir şey yapmaz, ancak kullanıp kullanmama kararı sana aittir.

### Kılavuzun devamında neler var

- **Gerekenler ve kurulum** — bir defaya mahsus hazırlaman ve kurman gerekenler.
- **Telefonu bağlıyoruz** — farmın ilk başlatılması.
- **Ana sayfa ve mini çubuk** — pencereyi ve oyunun altındaki küçük paneli nasıl okumalı.
- **Duraklatma ve durdurma** — butonlar ve kısayol tuşları.
- **Kural Ustası** — bota paketlerini ve kapı sırasını nasıl öğreteceksin.
- **Savaş kötü geçtiğinde** — müdahale pencereleri ve botun kendisinin nasıl karar verdiği.
- **Telegram, istatistikler, bir şeyler ters gittiğinde** — kalan her şey.

> [!done] Artık botun neler yapabildiğini biliyorsun. Sırada bir defalık yapılması gereken kurulum var. [Sonraki bölüm →](#2)

## Gerekenler ve kurulum

Bu işlem **bir defa** yapılır. Sonrasında programı sadece çift tıklayarak çalıştırırsın. Bütün bunlara yaklaşık on beş dakika ayır — sonrası çok kolay olacak.

### Neler gerekli

- :monitor: **Windows işletim sistemli bilgisayar.** Program ve bot burada çalışır.
- :smartphone: **Hero Wars yüklü Android telefon.** Oyun telefonda çalışır, bilgisayar ise ekranına bakar ve üzerine tıklar.
- :terminal: **USB kablosu.** Telefonu şarj eden ve dosya aktaran kabloyu tercih et: sadece şarj eden kablolar da vardır, bilgisayar onların üzerinden telefonu görmez.
- :folder: **Program arşivi** (`.zip` dosyası, içinde `HeroWarsBot.exe` bulunur).

> [!note] Oyun telefonda kalır. Bot oyuna ekstra hiçbir şey yüklemez ve oyun dosyalarına müdahale etmez: tıpkı senin parmağınla yapacağın gibi sadece ekрана bakar ve tıklar.

### Adım A. Programı arşivden çıkar

1. **Arşivi çıkar** — üzerine sağ tıkla ve "Tümünü Çıkart..." seçeneğini seç. Özel karakter içermeyen basit bir klasör seç, örneğin `C:\HeroWarsBot`.
2. **Dosyaların yerinde olduğunu kontrol et** — klasörde `HeroWarsBot.exe` dosyası diğer dosya ve klasörlerin yanında durmalıdır.

> [!warning] Önce arşivi klasöre çıkar, ardından programı çalıştır. `.exe` dosyasını doğrudan arşivin içinden açarsan programın diğer dosyaları erişilemez olur ve düzgün çalışmaz.

> [!tip] Bu klasör botun "evi"dir. `HeroWarsBot.exe` dosyasının yanında kendi dosyalarını (ayarlar, istatistikler, savaş geçmişi) otomatik oluşturur. Bu yüzden `.exe` dosyasını diğer dosyalardan ayrı taşıma, başka yere taşıyacaktan klasörü bütün olarak taşı.

### Adım B. scrcpy'yi kur

scrcpy, telefon ekranını bilgisayardaki bir pencerede gösteren küçük bir programdır. Bot tam olarak bu pencereye "bakar". Onunla birlikte, botun telefon ekranına tıklamasını sağlayan yardımcı **adb** de yüklenir.

1. **scrcpy'yi indir** — [proje sayfasında](https://github.com/Genymobile/scrcpy/releases) Windows için en son sürümü seç (adında "win64" olan `.zip` arşivi).
2. **Arşivi çıkar** — en pratik olanı boşluk içermeyen basit bir klasördür, örneğin `C:\scrcpy`. İçinde `scrcpy.exe` ve `adb.exe` dosyaları bulunmalıdır.
3. **Klasörü PATH'e ekle** — böylece Windows bu programları nerede arayacağını bilir. Bunun nasıl yapılacağı aşağıda açıklanmıştır.

**Klasörü PATH'e nasıl ekleyeceğin:**

1. **Ayarları aç** — Windows tuşuna bas, "ortam değişkenleri" yaz ve "Sistem ortam değişkenlerini düzenleyin" seçeneğini seç.
2. **"Path" değişkenini bul** — açılan pencerede "Ortam Değişkenleri" düğmesine tıkla, üst listede `Path` satırını seçip "Düzenle" düğmesine tıkla.
3. **Klasörü ekle** — "Yeni" düğmesine tıkla, `C:\scrcpy` yaz (farklıysa kendi klasörünü yaz) ve tüm pencereleri "Tamam" düğmesiyle kapat.

> [!note] PATH, programları adıyla çağırdığında Windows'un onları aradığı klasörlerin listesidir. Klasörü listeye eklediğinde `scrcpy` ve `adb` her yerden bulunabilir hale gelir.

### Adım C. scrcpy'nin kurulduğunu kontrol et

1. **"Komut İstemi"ni aç** — Windows tuşu, `cmd` yaz, Enter'a bas. Kurulumдан önce pencere zaten açıksa kapatıp yeniden aç: eski pencere yeni klasörlerden haberdar olmaz.
2. **scrcpy'yi kontrol et** — `scrcpy --version` yazıp Enter'a bas. Programın sürümü görünmelidir.

Sürüm yerine Windows "iç veya dış komut olarak tanınmıyor" yazıyorsa klasör PATH'e eklenmemiş demektir. Adım B'ye dön ve `scrcpy.exe` dosyasının bulunduğu klasörün PATH'e yazıldığından emin ol.

### Adım D. Telefonu ayarla

Telefon, bilgisayarın kendisini yönetmesine izin vermelidir. Buna "USB hata ayıklama" denir (uygulama geliştiricileri için tasarlanmış bir moddur). Bot bunu ekrana tıklamak için kullanır.

1. **Geliştirici modunu aç** — "Ayarlar" → "Telefon hakkında" bölümüne gir ve **üst üste 7 kez** "Derleme numarası" üzerine tıkla. Telefon artık bir geliştirici olduğunu bildirecektir.
2. **"Geliştirici seçenekleri" menüsünü bul** — bu öğe ayarlarda görünecektir (bazen "Sistem" veya "Ek ayarlar" içinde).
3. **İki ayarı aç** — "USB hata ayıklama" **ve** "USB hata ayıklama (Güvenlik ayarları)".
4. **Kabloyu bağla** — telefon "Bu bilgisayardan USB hata ayıklamasına izin verilsin mi?" diye sorduğunda "Her zaman izin ver" seçeneğini işaretle ve "Tamam" düğmesine tıkla.

![İki hata ayıklama ayarı açık durumdaki "Geliştirici seçenekleri" bölümü](images/usb_debug.png)

> [!warning] **Her iki** ayarı da aç. Yalnızca ilki açıksa telefondan bilgisayara görüntü gelir ancak tıklamalar oyuna ulaşmaz: bot "dokunur" ama oyun hiçbir şey fark etmez.

Şimdi bağlantıyı kontrol edelim. Telefonu kabloyla bağla, "Komut İstemi"ni aç ve `adb devices` yaz. Listede telefon numarasının yanında `device` kelimesini içeren bir satır olmalıdır.

- :check: `device` — her şey yolunda, telefon hazır.
- :triangle-alert: `unauthorized` — telefon iznini bekliyor. Ekranına bakıp "İzin Ver" düğmesine tıkla.
- :triangle-alert: liste boş — bilgisayar telefonu görmüyor. Başka bir kablo veya farklı bir USB bağlantı noktası dene.

### Adım E. Programın ilk çalıştırılması

1. **Program klasörünü aç** — arşivi çıkardığın klasör.
2. **`HeroWarsBot.exe` dosyasına çift tıkla** — program penceresi açılacaktır.
3. **Etrafa bak** — solda bölümlerin bulunduğu şerit, ortada ana sayfa. Telefon bağlı değilken üst bilgide «Telefon bekleniyor» yazar — bu normaldir.

> [!tip] Programı her zaman kendi klasöründen çalıştır (veya `HeroWarsBot.exe` için bir kısayol oluştur: sağ tık → "Gönder" → "Masaüstü"). Böylece kendi ayarlarını ve dosyalarını bulacaktır.

> [!done] Her şey hazır: program arşivden çıkarıldı, scrcpy ve telefon ayarlandı. Şimdi telefonu bağlayıp ilk farmı başlatacağız. [Sonraki bölüm →](#3)

## Telefonu bağlıyoruz ve ilk farm

Şimdi telefonu bağlayıp botu ilk kez çalıştıracağız — her şey yaklaşık beş dakika sürecek. Öncelikle unutma: monitörde **iki pencere** olacak.

- :monitor: **Program penceresi** — bu kılavuzu okuduğun pencere. İçinde butonlar, ayarlar ve günlük (botun ne yaptığını kaydettiği mesaj akışının adı) bulunur.
- :smartphone: **Oyun penceresi** — telefon ekranının monitördeki "aynası", adı `HeroWarsBot_Arena`'dır. Bot tam olarak bu pencereye "bakar".

### İlk çalıştırmada ana sayfada neler var

Ayarları henüz hiç kaydetmediğin sürece ana sayfada (sol şeritteki ilk buton) «3 adım · yaklaşık 5 dakika» imzalı «Nereden başlamalı» kartı yer alır.

![İlk çalıştırma: «Nereden başlamalı» kartı, kırmızı «Telefon bekleniyor...» yazısı ve mavi «Telefonu bağla» butonu](images/connect_phone.png)

- :smartphone: **«Telefonu bağla»** — «şimdi» sözcüğüyle işaretlenmiştir. Telefon bağlandığında adım numarası yeşil bir tık işaretiyle değişir. Şimdi bunu yapacağız.
- :sliders-vertical: **«Odalara göre paketleri kontrol et»** — «Aç →» bağlantısı «Kural Ustası»na (sol şeritteki ikinci buton, kaydırıcı simgesi) götürür. Orada bota her odaya hangi titanlarla gireceğini söylersin.
- :send: **«SOS için Telegram'ı ayarla»** — isteğe bağlı. Bot yardıma ihtiyacı olduğunda sana Telegram'дан yazar.

> [!warning] Paketler — ilk farmdan önceki en önemli şeydir. Bot dört odanın her birine (su, toprak, ateş ve karma) «Kural Ustası»nda kayıtlı paketi koyar, senin titanlarını tahmin edemez. Bunu nasıl ayarlayacağın — kılavuzun devamındaki «Kural Ustası» bölümünde anlatılmıştır. «Nereden başlamalı» kartı, ayarları «Kural Ustası»nda ilk kez kaydettiğinde kaybolacaktır.

### Adım A. Telefonu bağla

1. **Telefonu hazırla** — kabloyla bağla ve экран kilidini aç. USB hata ayıklamanın her iki ayarı da [bölüm 2](#2)'deki gibi açık olmalıdır.
2. **«Telefonu bağla» butonuna tıkla** — sağ üstteki büyük mavi butondur. Program telefonu ararken üzerinde «Bağlanıyor…» yazacaktır. 20 saniyeye kadar bekleme olabilir.
3. **Oyun penceresini bul** — telefon ekranıyla birlikte yeni bir `HeroWarsBot_Arena` penceresi görünecektir. Görünmüyor mu? Program penceresinin arkasında kalmış olabilir: ekranın altındaki görev çubuğunda arayabilirsin.
4. **Üst bilgideki etiketi kontrol et** — kırmızı «Telefon bekleniyor…» ibaresi yeşil «bağlı» olmalıdır. Mavi buton ise yeşil «Farmı başlat» butonuna dönüşecektir. (Üст bilgi — pencerenin üst şeridi, etiket — yazılı dikdörtgen.)

![Telefon bağlı: yeşil «bağlı» yazısı, «Farmı başlat» butonu ve yanında oyun penceresi](images/phone_connected.png)

Pencere görünmedi ve günlükte «Окно scrcpy не появилось или утилита не найдена!» mı yazıyor? Sırayla kontrol et:

- :smartphone: Telefon ekranının kilidi açık, kablo sıkıca takılı. Başka bir USB bağlantı noktası dene.
- :terminal: Komut isteminde `adb devices` komutu telefonunun yanında `device` kelimesini gösteriyor. Orada `unauthorized` varsa telefon ekranında hata ayıklamaya izin ver.
- :terminal: Komut isteminde `scrcpy --version` sürüm ile yanıt veriyor. Yanıt vermiyor mu? scrcpy içeren klasör PATH'e eklenmemiş — [bölüm 2](#2)'ye dön. PATH'i düzenledikten sonra program kapatılıp yeniden açılmalıdır.

### Adım B. Zindan koridoruna geç

Titan Zindanı, kat kat aşağı indiğin ve her odada düşmanlarla savaştığın bir oyun modudur. **Koridor**, savaşlar arasındaki ekrandır: üzerinde bayraklı bir kapı görünür ve başka hiçbir şey açık değildir. Bot tam olarak koridordan başlar.

1. **Oyunu aç** — telefonda Hero Wars'u başlat ve Titan Zindanı'na gir.
2. **Koridorda dur** — savaş devam ediyorsa kendin tamamla ve sonuç penceresini kapat. Kapısı ve bayrağı olan sakin bir ekran gereklidir.

![Titan Zindanı Koridoru: kapının yanında bayrak görünür](images/dungeon_corridor.png)

> [!warning] Savaşın ortasında farmı başlatma. Bot önce ekranı tarar ve düzen sağlar: savaş görürse savaştan çekilir; «Ещё раз» («Tekrar») butonlu sonuç penceresi görürse bu savaşı iptal edip odayı yeniden oynar; takım seçimini görürse savaşı yapıp hemen iptal eder. Sonrasında çalışmaya devam eder ama zaferin boşa gitmiş olur.

### Adım C. Farmı başlat

> [!warning] **Program dili ile oyun dili aynı olmalıdır.** Yazılı butonları ("Saldır", "TAMAM", "Tekrar") ve kapıdaki bayrağı bot programda seçili olan dildeki görsellerden tanır. Bu, sol şeridin altındaki iki harfli ("RU") butondur. Oyun Rusça ise programda da "RU" olmalıdır. Diller farklıysa bot butonları bulamaz.

1. **«Farmı başlat» butonuna tıkla** — «Telefonu bağla» yerindeki yeşil butondur. Program oyun penceresini otomatik olarak gerekli boyuta getirecek ve ekranın sol üst köşesine yerleştirecektir.
2. **Program penceresinin kaybolmasından korkma** — görev çubuğуна küçültüldü ve oyunun altında dar bir panel olan **mini çubuk** belirdi. Üzerinde botun ne yaptığı görünür. Pencereyi geri getirmek için: mini çubuktaki «Program penceresini aç» simgesi (fareyi üzerine getir — ipucu belirir) veya görev çubuğundaki buton.
3. **Oyunu izle** — birkaç saniye sonra bot kapıya tıklayacak ve ilk oda başlayacaktır. Bir oda yaklaşık yarım dakika — bir dakika sürer.
4. **Botu nasıl durduracağını unutma** — F10 tuşu onu anında durdurur, F9 duraklatır (bot odayı tamamlar ve bekler). Tuşlar, oyun penceresi veya program penceresi etkinken çalışır.

Program penceresini açtıktan sonra günlüğe göz at. Orada her satırın önünde zaman damgası bulunur — biz onu atladık. İşte görünmesi gerekenler:

- `[УМНЫЙ СТАРТ] Сканирую экран для восстановления контекста...` — bot etrafı tarıyor.
- `[УМНЫЙ СТАРТ] Контекст не требует экстренных действий. Начинаю с HALLWAY.` — her şey yolunda, koridordan başlıyor ("HALLWAY", İngilizce'de "koridor" demektir).
- `[СТАТИСТИКА] Комнат: 1` — ilk oda geçildi. Her şey çalışıyor!
- :triangle-alert: `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` — bot oyun penceresinin yeniden öne gelmesini bekliyor. Fareyle üzerine tıkla, çalışma devam edecektir.

Bir dakika geçti ve bot hiçbir şeye tıklamıyor mu? Kontrol et:

- :gamepad-2: Oyunda şu anda menü, mağaza veya savaş değil, Titan Zindanı koridoru var.
- :globe: Program dili oyun diliyle eşleşiyor (yukarıdaki uyarı).
- :maximize-2: Oyun penceresi ekranın tamamında görünür durumda: esnetilmemiş, büyütülmemiş, kenardan dışarı kaymamış. Aksi takdirde botu durdur (F10), «Oyun penceresinin boyutunu sıfırla» butonuna tıkla ve yeniden başla.
- :terminal: Günlükte «[ОШИБКА]» içeren satırlar yok. Varsa — bunları "Bir şeyler ters gittiğinde" bölümünde ele alacağız.

### Bot çalışırken

- :monitor: Oyun penceresi görünür olmalıdır: başka pencerelerle kapatma ve küçültme. Başka bir pencereye tıklandığında bot durup bekler.
- :smartphone: Oyun penceresini kapatma ve kabloyu çekme. Pencere kaybolursa program botu kendisi durdurur ("Окно scrcpy закрыто — останавливаю бота").
- :maximize-2: Oyun penceresini esnetme ve büyütme: bot açılışta boyutunu ölçer ve sonrasında bu ölçüyü kullanır.
- :gamepad-2: Telefon ekranına kendin dokunma: bot ADB üzerinden tıklar ve birbirinize engel olursunuz. Elle oynamak istiyorsan botu duraklat (F9) ve koridorda durmasını bekle.
- :triangle-alert: Bilgisayarı kilitleme (Win+L): kilitli bir bilgisayarda bot ekranı göremez ve sen dönene kadar bekler.
- :moon: Gece farmı için bilgisayarın uyku modunu kapat: Windows "Ayarlar" menüsünden "Sistem" → "Güç" bölümünü aç, ekran ve uyku için "Hiçbir zaman" seçeneğini belirle. Uykuya geçen veya kapanan monitör, kilitli bilgisayarla aynıdır: bot durur ve bekler. Öğe adları Windows sürümüne göre farklılık gösterebilir.

### Üst bilgideki butonlar

Sağ üstte, etiketin yanında üç simge bulunur. Fareyi herhangi birinin üzerine getir — açıklama belirir.

![Pencere üst bilgisi: telefon etiketi, üç buton ve pencere butonları](images/header_buttons.png)

- :moon: **«Telefon экранını kapat»** — telefon ekranını karartır, ancak oyun çalışmaya devam eder ve bot her şeyi görür. Gece kullanımı için pratiktir: ekrana ve bataryaya daha az yük biner. Program oyun penceresini öne çıkarır ve içinde Alt+O tuşlarına basar (scrcpy ekranı böyle karartır). Ekranı geri getirmek için — telefondaki açma/kapama tuşuna basılır. Aynı buton mini çubukta da vardır.
- :refresh-cw: **«scrcpy'yi yeniden başlat»** — oyun penceresini kapatır ve yeniden açar. Telefondan gelen görüntü donarsa işe yarar. Yalnızca programın kendisinin başlattığı pencereyle çalışır. Bot çalışırken buna tıklama: kaybolan pencereyi program bağlantı kopması kabul eder ve botu durdurur.
- :maximize-2: **«Oyun penceresinin boyutunu sıfırla»** — `HeroWarsBot_Arena` penceresini 1606 × 748 boyutuna geri getirir ve sol üst köşeye yerleştirir. Bu standart boyuttur: buton arama buna göre ayarlanmıştır. Pencereyi esnettiysen veya büyüttüysen — «Farmı başlat» öncesinde bu butona tıkla (gerçi «Farmı başlat» bunu kendisi de yapar). Pencere geniştir: Full HD (1920 × 1080) monitörde tamamen sığar, bot ise sadece ekranda olanı görür.

### Windows çerçevesi olmayan program penceresi

Program penceresinin sıradan bir Windows çerçevesi yoktur, bu nedenle sağ üstte ince bir çizginin arkasında kendi butonları yer alır:

- :minus: **«Küçült»** — pencereyi görev çubuğuna gizler.
- :square: **«Büyüt»** — pencere tam экран olur; ardından buton adı «Boyutu geri yükle» olur. Üst bilgiye çift tıklamak da aynı şeyi yapar.
- :x: **«Kapat»** — programı ve onun açtığı oyun penceresini kapatır. Bot çalışıyorsa önce «Bot durdurulsun mu?» diye sorar; «Durdur ve kapat» butonu botu anında durdurur ancak oturum özeti Telegram'a gönderilmez.
- :grip-vertical: **Pencereyi taşımak** — üst bilgiden tutarak: üstteki boş alandan veya başlıktan tutarak.
- **Boyutu değiştirmek** — sağ alt köşeden tutarak (üç eğik çizgi). Pencere çok küçük bir hale gelmez.

> [!note] «Küçült» ile «Mini çubuğa küçült» seçeneklerini karıştırma. «Küçült» pencereyi sadece görev çubuğуна gizler. «Mini çubuğa küçült» — bot çalışırken ana sayfada yer alan bir butondur: ayrıca oyunun altında mini çubuğu da gösterir.

> [!done] Telefon bağlandı, bot ilk odayı geçti — temel hazır. Şimdi ana sayfanın neler gösterdiğini ve günlüğün nasıl okunacağını inceleyelim. [Sonraki bölüm →](#4)

## Ana sayfa ve günlük

Ana sayfa — sol şeritteki ilk butondur ve en sık göreceğin yer burasıdır. Bir arabanın gösterge paneline benzer: üstte sayılar ("nereye gidiyoruz" ve "nasıl gidiyoruz"), altta ise botun ne yaptığını yazdığı günlük yer alır. Nelerin nerede durduğunu ve günlük satırları arasında nasıl kaybolmayacağını inceleyelim.

### Üstteki kart: görünümünü kendisi değiştirir

Ana sayfanın üst kısmında tek bir büyük kart vardır, ancak botun o anki durumuna göre farklı şeyler gösterir:

- :sliders-vertical: **«Başlatma ayarları»** — bot duruyor ve ayarlar önceden kaydedilmiş. Bu, botun "savaşa ne ile gideceğidir": hedef, mod ve eşikler.
- :activity: **«Geçerli oturum»** — bot çalışıyor. Canlı sayılar: ne kadar toplandı, kaç kat/oda geçildi, ne kadar zaman geçti.
- :file-text: **«Oturum özeti»** — bot durdu. Kart, nelerin başarıldığını ve botun neden durduğunu gösterir.
- :list: **«Nereden başlamalı»** — yalnızca ayarları henüz hiç kaydetmediğinde görünür ([bölüm 3](#3)'te açıklanmıştır).

Oturum, botun tek bir çalıştırılmasıdır: «Farmı başlat» düğmesinden durdurmaya kadar.

### Başлатma ayarları

Dört etiket vardır ve her biri tek bir soruya yanıt verir. Sayılar senin ayarlarından alınır, bu yüzden bir şeyi değiştirmek istersen kartın sağ üstündeki «Kural sihirbazında değiştir →» butonuna tıkla: «Kural Ustası» açılacaktır.

![Başлатма öncesi ana sayfa: «Başлатма ayarları» kartı ve boş günlük](images/main_config.png)

- :target: **«Oturum hedefi»** — botun ne zaman durması gerektiğidir. Hedef **tektir**: titanit, odalar, katlar veya zaman. Ayarlarda birden fazla belirlenmişse "titanit → odalar → katlar → zaman" sırasına göre ilki alınır. Değişiklik yapmadıysan hedef 120 titanittir, bu da 10–20 odaya denk gelir. «Sınırsız» seçeneği, tüm hedeflerin sıfır olduğu ve sen durdurana kadar botun ilerleyeceği anlamına gelir.
- :shield-check: **«Mod»** — «AÇIK» veya «KAPALI» işaretli «Bot kendisi karar verir» etiketi. Açık: kötü bir savaşta bot savaşı başka bir paketle kendisi yeniden oynar. Kapalı: seni çağırır. Ayrıntılar — «Kural Ustası» bölümlerindedir.
- :heart-pulse: **«Can panik eşiği»** — örneğin %40. Savaştan sonra titanlardan birinin canı bundan az kalırsa savaş kötü kabul edilir. Paket — beş titanlık takımdır; Can — sağlıktır.
- :calendar: **«Gün sıfırlama»** — örneğin 05:00. Oyunda yeni gün bu saatte başlar: bot günlük istatistikleri hesaplar ve titanların dünkü can miktarını unutur.

> [!note] Bot ayarları **«Farmı başlat» butonuna tıkladığında bir kez** okur. Çalışma sırasında bir şeyi değiştirirsen bot bunu yalnızca bir sonraki çalıştırmada öğrenecektir. Bu nedenle bot çalışırken kartta tam olarak başladığı ayarlar gösterilir.

### Geçerli oturum

Bot çalıştırıldığında kart «Geçerli oturum» kartına dönüşür. Sağ üstte durum ışığı yanar:

- :activity: **«Farm sürüyor»** — her şey yolunda, bot çalışıyor.
- :pause: **«Duraklatıldı»** — «Duraklat» butonuna bastın (veya bot kendisi yumuşak duraklatmaya geçti). Buton bu sırada «Devam et» haline gelir.
- :triangle-alert: **«Kararını bekliyor»** — ekranda «Müdahale gerekiyor» penceresi var, bot yanıt bekliyor.
- :refresh-cw: **«Bot başlatılıyor…»** — «Farmı başlat» sonrasındaki ilk saniyeler.

![Farm sürüyor: hedefe ilerleme çubuklu oturum etiketleri](images/main_session.png)

Dört etiket vardır:

1. **«Bu oturumdaki titanit»** — botun ne kadar titanit topladığıdır. Bu bir **hesaplamadır, ekrandan okuma değildir**: oda başına 6 ve oyunda "x2" simgesi yanıyorsa 12 titanit eklenir. Hedef titanit ise yanında "toplanan / gereken", yüzdeler ve bir çubuk görünür.
2. **«Geçilen katlar»** — bot kaydetme noktasından ödülü aldığında kat sayılır (katın sonunda "Etkinleştir" ve "Topla" butonlarına basılan yerin adıdır). Yanında en son hangi kapıya girdiği yazılır: su, toprak, ateş veya karma.
3. **«Bu oturumdaki savaşlar»** — örneğin «14 savaşta 12 zafer». Zafer — geçilmiş odadır. Geri alma — botun yeniden oynadığı savaştır: o da savaş sayılır, bu yüzden "toplam" sayısı "zafer" sayısından fazla olabilir.
4. **«Oturum süresi»** — saat:dakika:saniye ve küçük yazıyla «oda ortalama 28 sn». Ortalama, kaydetme noktasındaki bekleme süresi hariç odalara göre hesaplanır.

> [!tip] Hedef odalar veya zaman ise yüzdeler sağda "100 üzerinden %35" veya "120 dk üzerinden %35" şeklinde durur — hedef sayının kendisine sığmaz. Etiketin altındaki çubuk aynıdır.

> [!note] Hedefe ulaşıldığında bot katı yarıda bırakmaz. Günlüğe `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.` yazar, kalan odaları geçer ve "Etkinleştir" butonuna basmadan kayдетme noktasının önünde durur: kat ödülünü bir sonraki çalıştırmada ilk iş olarak alacaktır. İstisna — kat hedefidir: bu durumda bot ödülü aldıktan hemen sonra durur.

### Oturum özeti

Bot durduğunda kart özeti gösterir ve pencere mini çubuktan otomatik olarak açılır. Üstte durma nedeni yazılıdır: «DUR» butonu, kapatılan scrcpy penceresi, normal çalışma tamamlanması veya botun kendisinin yazdığı neden (örneğin hedefe ulaşıldığı).

![Oturum özeti: durma nedeni, sayılar ve «Ayrıntılar» butonu](images/main_summary.png)

Oturumdaki aynı dört etiket yer alır ancak bunlar artık kesin sayılardır; "Savaşlar" kısmına "SOS pencereleri: N" (botun seni kaç kez çağırdığı) eklenmiştir. **«Ayrıntılar»** butonu botun tüm raporunu içeren bir pencere açar: aşamalara göre ortalama süreler, en uzun odalar, kaç geri alma yapıldığı ve bunlardan kaçını botun **senin yardımın olmadan** gerçekleştirdiği. Sağdaki ✕ simgesi özeti gizler ve yerine tekrar «Başлатма ayarları» görünür. «Farmı başlat» butonuna tıkladığında özet kendiliğinden kaybolur.

> [!note] Telegram ayarlanmışsa normal her durmada özet oraya otomatik olarak gelecektir. «DUR» (F10) butonu botu anında sonlandırır, bu nedenle bu durumda Telegram'a özet gönderilmez.

### Günlük: içinde neler var и как читать

Ana sayfanın alt kısmı — **«Çalışма деньliği»**dür. Bot her adımını buraya yazar, program ise bunu pencerede gösterir. Satır sayısından korkma: her şeyi okumana gerek yok; günlük bir şeyler ters gittiğinde veya merak ettiğinde gereklidir.

Her satır aynı yapıda düzenlenmiştir:

`10:26:17.486 [НАВИГАЦИЯ] Двери (слева направо): EARTH (0.98), FIRE (0.97)`

1. **Zaman** — gri renkte. Saat:dakika:saniye ve saniyenin binde birleri.
2. **Köşeli parantez içindeki etiket** — "kimin konuştuğunu" ve ne hakkında olduğunu gösterir. Renklendirilmiştir: renk, satırın günlüğün hangi bölümüne ait olduğunu ipucu verir.
3. **Metin** — tam olarak ne gerçekleştiği. Uzun satır alt satıra geçer, devamı zamanın altına değil metnin altına hizalanır.

Etiketsiz satır (örneğin ` ---> HYPERION: ХП 100%, Энергия 79%`), üstündeki satırın devamıdır ve aynı bölümde yer alır.

### "Hap" filtreler

Günlüğün üzerinde beş "hap" buton bulunur. Birine tıkla — günlükте yalnızca o bölümün satırları kalır. Seçim hatırlanır: programı yarın açtığında aynı hap seçili olacaktır.

![«Tümü», «Savaşlar», «Kurallar», «Sistem» ve «Hatalar» hap butonlu günlük](images/journal_pills.png)

- **«Tümü»** — her şey sırayla.
- **«Savaşlar»** (yeşil etiketler) — ilerleme gidişatı: odalar, zaman, titanların sağlığı, geri almalar. Etiketler: `[КОМБАТ]`, `[СТАТИСТИКА]`, `[ВРЕМЯ]`, `[СОСТОЯНИЕ]`, `[АНАЛИЗАТОР]`, `[ОТКАТ]`, `[ЛИМИТ]`, `[ИТОГ]`.
- **«Kurallar»** (sarı etiketler) — botun kararları: hangi paketi koyacağı, savaşı neden geri aldığı, neyi hatırladığı. Etiketler: `[ТАКТИКА]`, `[КОМАНДА]`, `[ПРАВИЛА]`, `[ОБУЧЕНИЕ]`, `[SOS_CLOSE]`.
- **«Sistem»** (mavi etiketler) — kalan her şey: koridor ve kapılar (`[НАВИГАЦИЯ]`), başlatma (`[УМНЫЙ СТАРТ]`), bağlantı. Programın kendisinin `[GUI]` etiketli satırları gri renktedir ancak burada yer alır.
- **«Hatalar»** (kırmızı etiketler) — dikkat gerektiren her şey: `[ОШИБКА]`, `[ВНИМАНИЕ]`, `[СТОРОЖ]`, `[SOS]`. Adının yanında bir sayı durur — kaç tane bu tür satır biriktiğini gösterir.

> [!warning] «Hatalar» üzerindeki kırmızı sayı her zaman bir arıza değildir. `[ВНИМАНИЕ] Окно игры перекрыто (...). Бот ждет фокуса...` ifadesi de oraya girer — bot sadece oyun penceresini tekrar öne getirmeni bekliyordur. Renginden korkmak yerine satır metnini oku.

### Gerçek satır örnekleri

Bunlar botun gerçek oturumundan alınmış satırlardır (kısa tutmak adına zaman atlanmıştır). Bu beşini okumayı öğren — her günlüğü anlarsın.

- `[НАВИГАЦИЯ] Выбрана комната EARTH (порядок: water → mix → earth → fire)` — bot toprak kapısını seçti. Parantez içinde — senin kapı sıran yer alır. Yukarıdaki "Kapılar (soldan sağa)" satırındaki sayı — botun kapıyı tanıdığından ne kadar emin olduğudur (1 — tamamen).
- `[ВРЕМЯ] Комната 2 (earth): коридор 12.8 с | сборка 3.3 с | бой 8.0 с | результат 9.1 с | всего 33.2 с` — oda raporu: kapıya giden yol, takım kurulumu, savaş ve sonuç penceresinin kapatılması için harcanan süre.
- `[СТАТИСТИКА] Комнат: 3 | Титанит: 36` — üçüncü oda geçildi, 36 titanit toplandı. Bu sayılar oturum etiketlerine aktarılır.
- `[ТАКТИКА] Откатываю бой сам и переиграю паком [...] (взят: ваш список запасных паков).` — savaş kötü geçti ve bot («Bot kendisi karar verir» modu) savaşı yedek paketle yeniden oynuyor. Yedek paket başarılı olursa: `[ТАКТИКА] Запасной пак [...] справился. Запоминаю его против этих врагов.`
- `[ОТКАТ] Запускаю протокол отката боя...` — geri almanın başlangıcı: "Tekrar" → duraklama → "Çekil". Bu tür her satır «Bu oturumdaki savaşlar» etiketine bir savaş ekler.

> [!tip] Her oturumun başında bot `[ТАКТИКА] Плохой бой: ХП ниже 30% | потеря больше 60% | ...` yazar — savaşları değerlendireceği eşikler. Bir şeyler "beklediğin gibi gitmediyse" önce bu satırı kendi ayarlarınla karşılaştır.

### Günlüğün altındaki butonlar

![Günlüğün altındaki butonlar: «Günlüğü kaydet», «Günlüğü yazara gönder», «Temizle»](images/journal_buttons.png)

- :save: **«Günlüğü kaydet»** — tüm günlüğü bir metin dosyasına kaydeder. Program kendisi `gui_log_...txt` adını ve `bot_data/logs` klasörünü önerecektir; başka bir klasör de seçebilirsin.
- :mail: **«Günlüğü yazara gönder»** — önce aynı kaydetme yapılır, ardından hazır bir e-posta ile e-posta istemcin açılır. **Dosyayı e-postaya kendin ekle** (ve aynı klasördeki `battle_log.csv` dosyasını): program bunu yapamaz. E-posta programın yok mu? «Hakkında» bölümündeki adresi kullanarak yazara yaz.
- :x: **«Temizle»** — penceredeki satırları kaldırır, ancak önce «Günlük temizlensin mi?» diye sorar. Bu güvenlidir: tam günlüğü bot kendisi `bot_data/logs` klasörüne kaydeder, oturum sayıları ise sıfırlanmaz.

Günlükteki metni fareyle seçebilir, Ctrl+C ile veya sağ tıkla («Kopyala») kopyalayabilirsin. Günlük değiştirilemez — salt okunurdur. Okumak için günlüğü yukarı kaydırdıysan yeni satırlarla aşağı "kaçmaz"; sonuna kadar kaydır — botla birlikte tekrar aşağı kaymaya başlar.

> [!note] Pencere son 50 000 satırı hatırlar, ancak son 4000 satırı gösterir — aksi takdirde uzun farmda yavaşlardı. Geri kalan her şey `bot_data/logs/bot_log_...txt` dosyasında bulunur: bot onu kendisi tutar, bu yüzden günlüğü elle kaydetmeye genellikle gerek yoktur.

Günlük boşken yerinde «Günlük henüz boş» yazısı yer alır. Satırlar telefon bağlandıktan sonra görünecektir. Boş bir hap «Burada henüz bir şey yok» ve «Henüz böyle satır olmadı» yazar — «Hatalar» için bu iyi bir haberdir.

> [!done] Artık ana sayfayı adeta bir gösterge paneli gibi okuyabiliyorsun: etiketlerin ve günlük etiket renklerinin ne anlama geldiğini biliyorsun. Sırada mini çubuk var — oyunun altındaki küçük panel. [Sonraki bölüm →](#5)

## Oyunun altındaki mini çubuk

Bot çalışırken, programın ana penceresine genellikle ihtiyacın olmaz. Bu yüzden pencere kendiliğinden görev çubuğuna küçülür ve oyun görüntüsünün altında dar bir panel belirir — **mini çubuk**. Bu tıpkı bir arabanın gösterge paneli gibidir: tek bir bakışta botun ilerleyip ilerlemediğini, şu an ne yaptığını, ne kadar ilerlediğini ve seni çağırıp çağırmadığını görebilirsin.

![Farm sırasında oyun penceresinin altındaki mini çubuk](images/mini_bar.png)

### Ne zaman belirir ve nerede durur

- :monitor: **Kendiliğinden belirir.** Bot başladığında («Farmı başlat») — program penceresi küçülür ve oyunun altında mini çubuk yerleşir. Program penceresini büyüttün ve bot çalışırken onu tekrar gizlemek istiyorsun — ana sayfada «Mini çubuğa küçült» düğmesine bas.
- :smartphone: **Tam oyunun altında durur** ve tam olarak oyun görüntüsüyle aynı genişliktedir. Oyun penceresini hareket ettirdiğinde — mini çubuk onu takip eder (program bunu saniyede iki kez kontrol eder).
- :eye: **Oyunu tek bir piksel bile kapatmaz.** Bu önemlidir: bot, pencerenin ekran görüntülerini alarak ekrana «bakar». Panel oyunun üzerine gelseydi, bot düğmeler yerine paneli görürdü.
- :maximize-2: **Altta yer yoksa** (oyun penceresi ekranın alt kenarındaysa) — panel pencere başlığının üstüne yerleşir. Orada da yer yoksa — görünmez, program penceresi ise görev çubuğunda kalır. Oyun penceresini küçülttüğünde — panel gizlenir ve oyunla birlikte geri gelir.

> [!tip] Mini çubuk görünmüyor ama bot çalışıyor mu? Oyun penceresini yukarı taşı: altında yaklaşık 100 piksel boş alan gerekiyor. Pencereyi taşıyabilirsin, ancak boyutunu değiştiremezsin (bunu bölüm 3'te incelemiştik).

### Panelde ne var: soldan sağa beş sütun

- :activity: **Durum.** Her şey yolundayken «nefes alan» bir kelime ve renkli nokta: «BAŞLATILIYOR», «FARM SÜRÜYOR», «DURAKLATILDI», «HATA AYIKLAMA DURAKLAMASI» veya kırmızı «SOS». Altında — **botun şu anda tam olarak ne yaptığı** ve kaç saniyedir yaptığı: örneğin, «Savaş · Ateş · 12 sn». Sonra «Odalar: 12 · katlar: 2» ve oturum süresi, örneğin «Süre 00:42:17».
- :target: **Hedef.** Hedefin adı, ne kadar yapıldığı, ne kadar gerektiği ve bir çubuk. Altında — «oda başına ~28 sn» (ortalama süre; ilk odaya kadar orada «oda süresi — ilk odadan sonra» yazar) ve «hedefe ≈ 1 sa 10 dk» tahmini. Bot tahmini **bu** oturumun hızına göre hesaplar, bu yüzden başlangıçta bocalayabilir ama sonra dengelenir. Hedef yoksa («Sınırsız») — çubuk yoktur, tahmin yerine «saatte ≈ N titanit» yazar.
- :heart-pulse: **Takımın sağlığı.** Son savaşta yer alan titanların kareleri ve savaştan sonraki Can değerleri — oyun ekranındaki sıralarıyla. İlk savaşa kadar «henüz savaş yok» yazar. Rakamın rengi ipucu verir: kırmızı — Can panik eşiğinin (genel veya kişisel) altında, sarı — botun titanı iyileştirmeye başladığı eşiğin altında, normal renk — her şey yolunda. Tire «—» işareti, sonuç penceresinde titan simgesinin bulunamadığı anlamına gelir.
- :list: **Olaylar.** En yenisi üstte ve daha büyük olmak üzere son dört satır. Solda renkli bir etiket, sağda saat.
- :gamepad-2: **Düğmeler.** 2×2 kare şeklinde dört düğme.

### Bot «şu an ne yapıyor» olabilir

İlk sütunda bot kendi aşamasını adlandırır. Bu kelimelerin anlamı şudur:

- **«Koridor»**, **«Kapı seçimi»**, **«Takım kuruluyor»**, **«Savaş»**, **«Sonuç penceresi»** — bir odanın normal döngüsü. «Takım kuruluyor», «Savaş», «Sonuç penceresi» ve «Geri çekilme» aşamalarına odanın elementi eklenir: «Savaş · Su · 12 sn».
- **«Kayıt noktası»** — kat geçildi, bot ödülü alıyor.
- **«Geri çekilme»** — savaş kötü gitti, bot geri çekiliyor ve tekrar oynamaya hazırlanıyor.
- **«Ekrana bakıyor»** — başlatıldıktan sonra bot etrafa bakar ve nereden başlayacağına karar verir (bu «akıllı başlangıç»tır).
- **«Koridorda duraklatıldı»**, **«Kararını bekliyor»**, **«Kendin oynuyorsun»** — bot duruyor çünkü sen duraklatmaya bastın, sana bir şey sorduğu için veya «Elle oyna» seçeneğini seçtiğin için.
- **«Oyun penceresi bekleniyor»** ve **«Bağlantı bekleniyor»** — bot bekliyor: ya oyun ön planda değil (aşağıya bak), ya da oyun sunucusuyla bağlantı yok.

Aynı yazı normalden daha uzun süre kalırsa — sağdaki saniye sayısı artar ve botun aslında durduğunu gösterir.

### Olaylar: etiketler ve anlamları

Soldaki etiket olayın ne hakkında olduğunu gösterir:

- **Element adı** («Su», «Toprak», «Ateş», «Karma») — oda geçildi. «Oda 45 geçildi · 28 sn · en az Can: Araji %36» gibi bir satır, odanın kaç saniye sürdüğünü ve en düşük sağlıkla kimin kaldığını söyler.
- **«Kat»** — kat geçildi («Kat geçildi, toplam 3»).
- **«Geri çekilme»** — savaş tekrar oynanıyor. **«SOS»** — çağrının nedeni basit kelimelerle.
- **«Duraklatıldı»** — «Duraklama: bot savaşı bitirip bekleyecek», ardından «Bot koridorda bekliyor».
- **«Bot»** — «Bot başlatıldı», «Duraklama kaldırıldı, bot devam ediyor», «10 dk yanıt yok — bot kendisi karar verdi».
- **«Sınır»** — oturum hedefe ulaştı, bot kayıt noktasına kadar oynamayı tamamlıyor.
- **«Dikkat»** — «Oyun penceresi etkin değil — bot bekliyor. Oyuna tıkla».
- **«Hata»** — hatanın metni botun yazdığı şekliyle.

Uzun satırlar üç noktayla kısaltılır. Tam metin her zaman ana sayfadaki günlükte bulunur.

### Düğmeler

Fareyi üzerine getir — açıklama belirir. Tüm düğmeler, ana sayfadaki ve üst bilgideki «büyük» karşılıklarıyla aynı işi yapar.

- :pause: **Duraklat / Devam Et** — «Yumuşak duraklatma: bot savaşı bitirip bekler (F9)». Duraklatıldığında simge yeşil bir üçgene dönüşür ve aynı düğme duraklatmayı kaldırır. Bot henüz başlatılırken düğme kullanılamaz.
- :square-filled: **Durdur** — «Acil durdurma: bot hemen durur, Telegram'a özet gitmez (F10)».
- :moon: **Telefon ekranı** — «Telefon ekranını kapat», bu sırada oyun devam eder.
- :maximize-2: **Büyüt** — «Program penceresini aç». Mini çubuk kaybolur. Aynı sonucu görev çubuğundaki program penceresi düğmesi de verir. Paneli geri getirmek istersen — ana sayfadaki «Mini çubuğa küçült» düğmesi.

> [!note] Bot seni çağırdığında mini çubuk kızarır ve «Müdahale gerekiyor» penceresi oyun görüntüsünün tam ortasında kendiliğinden belirir — program penceresini büyütmene gerek yoktur. Bu anda ilk düğme duraklatmaz veya «devam ettirmez»: başka pencerelerin altında kalmışsa SOS penceresini gösterir (açıklama — «SOS penceresini göster: bot kararını bekliyor»). Pencerede yanıt verdiğinde mini çubuk tekrar normale döner. Nasıl yanıt verileceğini SOS pencereleri bölümünde inceleyeceğiz.

![SOS sırasında mini çubuk](images/mini_bar_sos.png)

### Altın kural: bot yalnızca oyun ön plandayken çalışır

Bot ekran görüntüleri alır ve bu görüntülerde düğmeleri arar. Oyunun üzerine başka bir tarayıcı, mesajlaşma uygulaması veya dosya gezgini gelirse, ekran görüntüsünde oyun değil onlar yer alır: bot «yanlış yere» tıklayabilir. Bu yüzden, başka bir pencere etkinleştiği anda bot durur ve bekler. Günlükte «[ВНИМАНИЕ] Окно игры перекрыто … Бот ждет фокуса…» satırı belirir, mini çubukta ise «Dikkat» etiketi ve «Oyun penceresi bekleniyor» aşaması görünür. Oyuna tıkladığında — «[ИНФО] Окно снова активно. Продолжаем работу.»

- :monitor: **Mini çubuğa tıklamak botu durdurmaz.** Mini çubuk etkin pencere olmayacak şekilde tasarlanmıştır: paneldeki düğmelere basarken oyun «ana pencere» olarak kalır.
- :triangle-alert: **«Büyüt» botu geçici olarak durdurur.** Program penceresi etkin hale geldi ama oyun etkin değilse, bot ilk adımda durur. İşin bittiğinde oyun penceresine tıkla, bot devam edecektir. Gözetmen bu bekleme süresini «donma» olarak saymaz.
- :gamepad-2: Bot farm yaparken bilgisayarda çalışmak mı istiyorsun? Başka pencereleri oyunun üstüne değil **yanına** aç ve üzerlerine tıklama. Ya da işini duraklatmaya kadar ertele (F9).

> [!warning] F9 ve F10 kısayol tuşları yalnızca oyun penceresi veya program penceresi etkinken çalışır. Tarayıcıda F10'a bastığında bot durmaz: başka bir şeyle meşgulken tuşlar dinlemez. Ayrıntılar — duraklatma ve durdurma bölümünde.

> [!done] Artık mini çubuğu bir gösterge paneli gibi okuyabiliyor ve oyunu neden başka pencerelerin arkasına saklamaman gerektiğini biliyorsun. Sırada duraklatma, durdurma ve kısayol tuşları var. [Sonraki bölüm →](#6)

## Duraklatma, durdurma ve kısayol tuşları

Bot Zindanda kendisi gezer, ancak bazen onu yavaşlatman gerekir: kendin elle oynamak, bir iş için ayrılmak veya sadece bitirmek isteyebilirsin. Bunun için **dört yöntem** vardır ve bunlar botun **ne kadar yumuşak** durduğuyla birbirinden ayrılır. Bir araba hayal et: «duraklatma» — emniyet şeridinde durup motoru kapatmaktır, «acil durdurma» ise seyir halindeyken anahtarı çekip çıkarmaktır. İkisi de çalışır ama farklı şekilde.

### Yumuşak duraklatma: «Durakla F9»

En yumuşak yöntemdir. Ana sayfadaki, mini çuluktaki «Duraklat» düğmesine veya **F9** tuşuna bas.

1. **«Duraklat» düğmesine veya F9'a bas.** Günlükte `[GUI] Сигнал 'Мягкая пауза' отправлен. Бот остановится перед следующей дверью.` satırı görünür.
2. **Bot odayı bitirene kadar bekle.** Halihazırda devam eden savaşı bırakmaz: bitirir, sonuç penceresini kapatır ve oda sonucunu kaydeder.
3. **Bot koridorda durur.** Günlükte: `[МЯГКАЯ ПАУЗА] Бот ждет в коридоре...`. Ana sayfadaki durum — «Duraklatıldı», mini çubukta — «DURAKLATILDI», düğme yeşil «Devam et» haline gelir.
4. **İşlerini hallet ve «Devam et» (veya tekrar F9) düğmesine bas.** Bot `[ИНФО] Пауза снята. Кэш составов и здоровья очищен. Включаю механизм Умного Старта.` yazar ve devam eder.

> [!note] «Önbellek temizlendi» ifadesi, botun hangi takımların durduğunu ve titanların ne kadar canı olduğunu **unuttuğu** anlamına gelir: sen oyunla ilgilenirken her şey değişmiş olabilir. Bir sonraki savaştan önce takım seçimi ekranına tekrar bakacak ve can durumunu oradan okuyacaktır. «Akıllı başlangıç» — botun önce ekranda ne olduğuna bakıp ancak daha sonra ne yapacağına karar vermesidir (örneğin unutulmuş bir sonuç penceresini kapatır).

- :eye: **Duraklatıldığında telefona bakabilir ve program penceresindeki ayarları değiştirebilirsin.** Ancak bot yeni ayarları yalnızca bir sonraki «Farmı başlat» işleminde alacaktır (ayrıntılar — ana sayfa bölümünde).
- :door-open: **Oyunda bir şeye bastıysan — oyunu Zindan koridoruna geri getir** (kapının yanında bayrağın göründüğü yere), ardından «Devam et» düğmesine bas. Böylece bot nerede olduğunu kesinlikle anlayacaktır.
- :gauge: **Süre duraklatıldığında da ilerler.** Oturum hedefi süre ise («120 dakika»), duraklatma bu sürenin bir kısmını harcar. Öte yandan «bekçi» (botun donup donmadığını izleyen sistem) duraklatma süresini saymaz ve alarm vermez.

> [!tip] Gece boyunca veya uzun süreliğine ayrılmak mı istiyorsun? Bunun için yumuşak duraklatmaya gerek yoktur: ana sayfada bir hedef belirle (titanit, odalar, katlar veya süre); bot kayıt noktasına kadar kendisi ulaşacak, duracak ve özeti gönderecektir.

### Bot kendiliğinden ne zaman duraklatır

Bazen bot yardım ister ve kendisi yumuşak duraklatmaya geçer. Bu durumda düğme de «Devam et» olarak görünür ve günlükte nedeni açıklayan `[ВНИМАНИЕ] Бот на мягкой паузе: ...` yazısı belirir. Bu durum şu hallerde yaşanır:

- bot 5 dakika boyunca üst üste üç kez tek bir odayı bile geçemediyse (bekçi donduğuna karar vermiştir);
- savaşın geri çekilme işlemi başarısız olduysa (ekran tanınmadı, düğmelere basılamadı);
- uzun süre beklense bile savaş bir türlü başlamadıysa;
- «Uygun pak yok» penceresine yanıt vermediysen ve yedek takım yoksa.

Bu tür durumlarda önce **telefon ekranına bak**, bozulan şeyi düzelt (gereksiz pencereyi kapat, koridora dön) ve ancak bundan sonra «Devam et» düğmesine bas. Telegram ayarlanmışsa bot ekran görüntüsü içeren bir mesaj gönderecektir.

### Acil durdurma: «DUR F10»

Kırmızı «DUR» düğmesi (veya **F10** tuşu) botu **hemen** durdurur: program bot işlemini sonlandırır. Günlükte — `[GUI] ЭКСТРЕННЫЙ СТОП. Процесс убит.`, özet kartında durdurma nedeni ««DUR» düğmesiyle durduruldu» olarak görünür.

> [!warning] F10 ile ne kaybedilir: bot günlükte `[ИТОГ]` bloğunu yazmaya vakit bulamaz ve **oturum özetini Telegram'a göndermez**. O anda savaşta ise oyundaki savaş devam eder (veya ekranda kalır) — bunu telefonda görürsün. Zaten geçilmiş odalar istatistiklerde saklanır: bot bunları her odadan hemen sonra kaydeder.

Bu düğmeye tam olarak ne zaman ihtiyaç duyulur: bot garip davranıyorsa (yanlış yere basıyor, «Duraklat»a yanıt vermiyor) veya her şeyi hemen şimdi bitirmek gerekiyorsa. Diğer durumlarda duraklatma veya Ctrl+Q kullanmak daha iyidir.

### Kısayol tuşları: ne nerede çalışır

- :pause: **F9** — duraklat / «Devam et» (ana sayfadaki «Duraklat» düğmesiyle aynı).
- :square-filled: **F10** — «DUR».
- :gamepad-2: **Ctrl+Q** — **özet ile** durdurma: bot başladığı odayı bitirir, koridorda durur, durur ve oturum özetini gönderir. Günlükte: `[ИНФО] Команда 'Ctrl+Q' принята! Бот завершит бой и остановится.`, durdurma nedeni — «Kullanıcı tarafından manuel durdurma (Ctrl+Q)».
- :triangle-alert: **Ctrl+Shift+Q** — **hemen, ancak özet ile** durdurma: bot `[ЭКСТРЕННАЯ ОСТАНОВКА]` yazdırır, `[ИТОГ]` kaydeder ve özeti Telegram'a göndermek için **tek bir** deneme yapar (gecikmemek için tekrarlamadan).

Tuşların bazen «çalışmamasına» neden olan önemli detaylar:

- **F9 ve F10 tuşlarını program penceresi dinler** ve yalnızca **oyun penceresi veya program penceresi etkinken**. Tarayıcıda veya mesajlaşma uygulamasında F10'a bastın — hiçbir şey olmaz. Oyun simge durumuna küçültülmüşse veya başka bir pencereyle kapatılmışsa mini çubuktaki düğmeleri kullan: onlar her zaman çalışır çünkü mini çubuk oyundan etkinliği almaz.
- **Ctrl+Q ve Ctrl+Shift+Q kısayollarını program penceresi değil botun kendisi dinler**, bu nedenle bot çalıştığı sürece başka bir pencere etkin olsa bile çalışırlar.
- **Bu kısayolları diğer programlar da bilir.** Ctrl+Q birçok programı kapatır (Word, Telegram Desktop), Ctrl+Shift+Q ise tarayıcıları kapatır. Bot çalışırken bunları başka pencerelerde basma: bot da bunu «duyar» ve durur.
- **Bot Ctrl+Q komutunu sonraki kapının önündeki koridordayken kontrol eder.** Yumuşak duraklatmada durur ve hiçbir şeyi kontrol etmez, bu nedenle Ctrl+Q yalnızca «Devam et» düğmesinden sonra çalışır. Bot SOS penceresinde yanıtını bekliyorsa Ctrl+Q onu hemen durdurur.
- **Tuşa basılı tutmak hiçbir şeyi tekrarlamaz:** tek basış — tek komut.
- Bot çalışmıyorken F9 veya F10'a bastığında günlükte `[GUI] Нажата F9, но бот не запущен.` satırı görünür.

### Pencere kapatma çarpı işareti ve scrcpy kapatma

- :x: **Bot çalışırken program penceresinin kapatma tuşu (X).** «Bot durdurulsun mu?» sorusu açılır. «Durdur ve kapat» düğmesi programı ve botu kapatır; oyun penceresini (scrcpy) ise — programın kendisi açtıysa hemen kapatır — özet Telegram'a gitmez. Bunu istemiyorsan soru penceresini kapat ve önce botu yumuşak bir şekilde durdur.
- :smartphone: **Oyun penceresini (`HeroWarsBot_Arena`) kendin kapattın.** Program `[GUI] Окно scrcpy закрыто — останавливаю бота (он напишет итог и пришлёт его в Telegram).` yazar. Bot oturum özetini kendisi tamamlayıp Telegram'a gönderir; 10 saniye içinde yanıt vermezse program onu F10 gibi durdurur.
- :pencil: «Kural Ustası»nda kaydedilmemiş değişiklikler varsa kapatma tuşu önce «Değişiklikler kaydedilsin mi?» diye sorar.

### Ne seçilmeli

- **Mola verip geri dönmek istiyorum** — «Duraklat» (F9). Hazır olduğunda «Devam et» düğmesine bas.
- **Bitirmek ve özet almak istiyorum** — Ctrl+Q (bot odayı bitirir, durur, özeti Telegram'a gönderir).
- **Hemen şimdi durmam gerekiyor ama özet gerekli** — Ctrl+Shift+Q.
- **Bot bozuldu veya garip davranıyor** — «DUR» (F10), ardından günlükten durumu incele.
- **Bot seni SOS penceresiyle çağırdı ve bitirmek istiyorsun** — bu penceredeki «Botu durdur» düğmesi: bot kendiliğinden durur ve özeti gönderir. SOS penceresini ayrıca inceleyeceğiz.

### Telegram'da oturum özeti

Telegram ayarlanmışsa özet, **«DUR» düğmesi** ve program penceresinin kapatılması **haricindeki** tüm durdurmalarda gelir: bot onu kendin mi durdurduğunu («Bot senin tarafından durduruldu»), hedefi mi bitirdiğini («Farm tamamlandı») yoksa hatayla mı çöktüğünü, ne kadar süre geçtiğini, kaç oda, kat ve titanit kazanıldığını, geri çekilme ve SOS pencerelerinin olup olmadığını yazar. İnternet bağlantısı yoksa bot özeti iki kez daha göndermeyi dener (10 ve 30 saniye sonra) ve ardından kapanır. Telegram'ın nasıl bağlanacağı — ayrı bir bölümde.

> [!done] Artık botu nasıl yumuşak bir şekilde yavaşlatacağını, tamamen nasıl durduracağını ve hangi tuşun ne işe yaradığını biliyorsun. Sırada — kural ayarları: bota gerekli takımları koymayı nasıl öğreteceğin var. [Sonraki bölüm →](#7)

## Kural Ustası: "Temel ve odalar"

"Kural Ustası", sol şeritteki ikinci düğmedir (kaydırıcı simgeli). Burada bota üç şeyi açıklarsın: **ne zaman duracağını**, **neyin kötü savaş sayılacağını** ve **her odaya hangi takımla girileceğini**. Takım, 3–5 titandan oluşan bir gruptur. Sayfa üstte üç sekmeye ayrılmıştır: "Temel ve odalar", "Otomatik taktik ve CP" ve "Kurallar ve müdahaleler". Bu bölümde ilk ve en önemli sekme anlatılmaktadır: o olmadan bot savaşa kimi koyacağını bile bilmez.

!["Temel ve odalar" sekmesi: üstte ayarlarla iki kart, altta takımlarla dört satır](images/rules_base.png)

Üstte — "Oturum ayarları" (iki kart), altta — "Odalara göre takımlar". Sayfanın altında, her sekmede aynı şekilde düğmeler içeren gri bir şerit bulunur: "Ayarları kaydet" ve "Geri Yükle / Sıfırla". Bununla ilgili ayrıntılar bölümün sonundadır. Hemen hatırlanması gereken en önemli şey: **"Ayarları kaydet" düğmesine basana kadar hiçbir şey kaydedilmez** — hiçbir değişiklik bota ulaşmaz.

### "Hedefler ve sınırlar" kartı

- :target: **"Oturum hedefi"** — botun ne zaman bitirmesi gerektiğidir. Hedef her zaman dört seçenekten **biridir**: "Titanit", "Odalar", "Katlar" veya "Süre" (dakika cinsinden süre). Listeden türü seç ve alana bir sayı gir. Alana sadece rakamlar kabul edilir. "0 — sınırsız" yazısı: sıfırın hedefi kapattığı ve sen onu durdurana kadar botun ilerleyeceği anlamına gelir. Sağdaki yuvarlak ok ("Hedefi sıfırla") 0 yapar.
- :gem: **Titaniti bot kendisi hesaplar**, ekrandan okumaz: normal bir oda için 6 ve sonuç penceresinde "x2" simgesi varsa 12. Bu nedenle "120 titanit", "x2" olmadan yaklaşık 20 odadır. Ayarları henüz hiç kaydetmediysen bot kendisi "120 titanit" hedefini alır.
- :layers: **Bot bir katı yarıda bırakmaz.** "Titanit", "Odalar" veya "Süre" hedefine ulaştığında olduğu yerde durmaz: günlüğe `[ЛИМИТ] ... Доигрываю этаж и останавливаюсь перед точкой сохранения.` yazar, katın kalan odalarını geçer ve "Etkinleştir" düğmesine basmadan kaydetme noktasının önünde durur. Böylece kat tamamlanmamış kalmaz, bot ödülü alır ve bir sonraki başlatmada ilk iş olarak katı sayar. Kaydetme noktası 6 oda içinde bulunamazsa (bir katta 5 oda vardır), bot olduğu gibi durur. "Katlar" hedefi kaydetme noktası geçildiği anda tetiklenir.
- :gauge: **Süre duraklatıldığında da işler.** "Süre — 120" hedefi, tüm duraklatmalarla birlikte "Farmı başlat" düğmesinden itibaren 120 dakika demektir.
- :calendar: **"Gün sıfırlama saati (yerel saat)"** — senin için yeni oyun gününün ne zaman başladığıdır. Varsayılan olarak 05:00'tir. İstatistiklerdeki savaşların hangi güne ait olduğu ve botun titanların sağlığı hakkındaki hafızası buna bağlıdır: tek bir oyun günü içinde yaşar ve yeni bir günde bot temiz bir sayfadan başlar. Günü yeni kabul ettiğin saati ayarla (örneğin yatmaya gittiğinde).
- :send: **"Telegram'ı ayarla"** — mesajlaşma uygulamasıyla bağlantının açıldığı ayrı bir pencere açar. Düğmenin yanında bir nokta ve yazı bulunur: yeşil "SOS bildirimleri açık" veya gri "Telegram ayarlanmadı". Nasıl bağlanacağını Telegram ile ilgili bölümde ele alacağız. Burada önemli olan tek şey: o penceredeki "Uygula" düğmesi yalnızca bu sayfayı değiştirir. Ayarın dosyaya girmesi için ayrıca "Ayarları kaydet" düğmesine bas.

> [!tip] Hangi hedefi seçmeli? "Süre", programında bir boşluk olduğunda kullanışlıdır ("ben akşam yemeği hazırlarken bot bir saat çalışsın"). "Titanit" — belirli bir miktarda ödül toplamak gerektiğinde. "Odalar" ve "Katlar" — tam olarak belli sayıda geçmek istediğinde. Emin değilsen "Titanit" ve 120 bırak: bu kısa bir deneme çalıştırmasıdır.

### "Güvenlik ve mod" kartı

Burada **kötü savaşın ne olduğuna** karar verilir. Bot, sonuç penceresindeki titanların sağlığını okur ve iki sayıyı seninkilerle karşılaştırır.

- :heart-pulse: **"CP panik eşiği, %"** — savaştan sonra hangi sağlığın altının kötü savaş sayılacağıdır. Varsayılan olarak 40'tır.
- :swords: **"CP kayıp deltası, %"** — bir titan tek bir savaşta ne kadar sağlık kaybedebilir. Varsayılan olarak 30'dur.

Her iki alan da 0 ile 100 arasında tam sayıları kabul eder; başka bir şey yazarsan alan "0 ile 100 arasında bir sayı gir" yazısıyla kırmızıya döner ve sen düzeltine kadar ayarlar kaydedilemez.

Eşik 40 ve delta 30 ile canlı bir örnek:

- Araji savaşa %100 ile girdi, %80 ile çıktı — **her şey yolunda**: 20 kaybetti, 40'ın üzerinde kaldı.
- Araji %100 ile girdi, %55 ile çıktı — **kötü savaş**. 55 eşikten yüksek ancak 45 kaybedildi, izin verilen ise 30.
- Araji %50 ile girdi, %35 ile çıktı — **kötü savaş**. Sadece 15 kaybetti ancak 35 panik eşiğinin altında.
- Herhangi bir titan öldüyse veya sonuç penceresinde bulunamadıysa — ne ayarlarsan ayarla her zaman **kötü savaş**.

Kayıplar titanın savaşa **girdiği** sağlıktan hesaplanır, %100'den değil. Bu yüzden yaralı titan sağlıklı olandan daha önce eşiğe "takılır". Eşik ne kadar yüksek ve delta ne kadar küçükse bot o kadar katı olur ve seni o kadar sık çağırır; eşikteki sıfır "eşiğin altında" kontrolünü devre dışı bırakır (ölenler hariç), deltadaki 100 ise kayıp kontrolünü devre dışı bırakır.

> [!note] Eşik ve delta tüm titanlar için ortaktır. Ayrı bir titan için kendi eşiğini koyabilir ve ayrıca "üçü çok kaybetti — kötü savaş" kuralını açabilirsin. Bu yan sekmede yapılır: "Otomatik taktik ve CP".

Aşağıda iki anahtar bulunur:

- :shield-check: **"Bot kendisi karar verir"** ("Kötü savaşları geri alır ve takım seçer") — varsayılan olarak **kapalıdır**. Kapalı: kötü savaş → "Müdahale gerekiyor" penceresi, bot seni bekler. Açık: bot soru sormadan savaşı geri alır ve yedek takımla tekrar oynar, ayrıca titanların sağlığına göre takımı kendisi seçer. Ayrıntılar botun otonom çalışmasıyla ilgili bölümde. Botu çalışırken görüp yedek takımlara güvendiğinde aç.
- :swords: **"Angus'un ultisini elle kontrol"** ("Genel, tüm odalarda") — varsayılan olarak **kapalıdır** ve o zaman Angus dahil her savaş otomatik savaşla gider. Açtığında — Angus'lu takımlar için bot "Savaşa" basar, Angus'un ultisi için otomatik savaşı birkaç saniyeliğine açar ve tekrar kapatır. Böyle bir savaşı bot kendisi geri almaz, seni çağırır. Başlatma sırasında günlükte neyin seçildiği görünür: `[ТАКТИКА] Ангус: ...`.

### Odalara göre takımlar

"Önce ana takım girer; savaş kötü giderse yedekler sırayla" yazısının altında odalara göre dört satır bulunur: "Toprak", "Su", "Ateş" ve "Karma". Her biri ayrı bir karttır.

- :users: **Ana takım** — oda adının altındaki titan kareleridir. Aksini yapacak bir neden yoksa (örneğin "Kurallar ve müdahaleler" sekmesindeki bir kural tetiklendiğinde) bot bu takımı koyar. Titanlar soldan sağa, **oyun ekranında durdukları gibi** gösterilir. Takım yoksa kareler yerine "Pak belirlenmedi" yazısı görünür.
- :pencil: **Kalem ("Takımı değiştir")** — "Takımı kur" penceresini açar.
- :list: **"Yedek takımlar"** (sayı "N adet") — açılır liste (aşağı/yukarı ok). Savaş kötü giderse ve bot kendisi karar veriyorsa ("Bot kendisi karar verir" açık veya pencereye zamanında yanıt vermediysen) bot yedek takımları sırayla dener. Her odada bunlardan 5 taneye kadar bulunur. İçeride her yedek takım `#1`, `#2` vb. bir satırdır ve sağda çarpı işareti ("Takımı sil") vardır. "Takım ekle" düğmesi aynı "Takımı kur" penceresini açar.
- :plus: **"Koşul"** — "+ Koşul": bu oda için bir kurala hızlı yoldur, örneğin "Angus'a karşıysa bu takımı koy". Oda önceden seçilmiş olarak "Yeni kural" penceresi açılır. Nasıl doldurulacağını kurallar bölümünde ele alacağız.

**İlk farmdan önce** dört odanın hepsinde de ana takımı ayarla: bot senin titanlarını bilmez ve "kutudan çıktığı haliyle" takımları yoktur.

Takım nasıl kurulur:

1. **İstediğin odada kaleme tıkla.** "Takımı kur" penceresi açılır.
2. **Koymak istediğin titanlara tıkla.** Bir kez daha tıkladığında kaldırırsın. Üstte sayaç: "Seçilen: 3 / 5" ve ipucu "Uygulanabilir" (iki tane seçildiğinde "En az 3 · 1 tane daha gerekli" yazar).
3. **Odanın elementini dikkate al.** "Toprak", "Su" ve "Ateş" odalarına yalnızca o elementin titanları, "Karma" odasına ise Metis dahil hepsi girer (o "elarittir" ve diğer odalara gitmez: "Metis — yalnızca karışık odada"). 5 tane seçildiğinde diğer titanlar kilitlenir.
4. **"Uygula" düğmesine tıkla** (veya fikrini değiştirdiysen "İptal"; "Temizle" tüm titanları tek seferde kaldırır).

!["Su" odası için "Takımı kur" penceresi: üç titan seçilmiş, altta "Uygula"](images/rules_picker.png)

> [!warning] "Takımı kur" penceresindeki "Uygula" yalnızca sayfayı değiştirir: takım henüz dosyaya **kaydedilmemiştir**. "Ayarları kaydet" düğmesine bastığında kaydedilecektir. Her odanın ana takımı `bot_data/rules/<стихия>.yml` dosyasında, yedekler ve tüm sayılar `profile.yml` dosyasında yer alır. Bu dosyaları elle düzenlemeye gerek yoktur.

Listede zaten var olan bir yedek takım (titanların sırası ne olursa olsun) ikinci kez eklenemez: "Bu yedek takım zaten var" bildirimi görünür.

> [!tip] Yedek olarak hangi takımlar konmalı? Bota bir seçenek sun: yedek takım ana takımdan en az birkaç titanla farklı olsun. Araji savaştan sık sık yaralı çıkıyorsa yedek takıma darbelere daha iyi dayananları koy.

### Kaydetme ve "Geri Yükle / Sıfırla"

Alt şerit durumu gösterir: "Tüm değişiklikler kaydedildi" (yeşil onay işareti) veya "Kaydedilmemiş değişiklikler var" (sarı simge). Bot çalışırken yanında "Bot yeni ayarları bir sonraki başlatmada alır" yazar.

- :save: **"Ayarları kaydet"** yalnızca değiştirdiğin şeyleri kaydeder ve "Ayarlar kaydedildi" bildirimini gösterir. Düğmeye basılmadığı sürece bot düzenlemelerinden haberdar olmaz. Günlükte `[GUI] Профиль настроек сохранен!` görünür.
- :rotate-ccw: **"Geri Yükle / Sıfırla"** — kırmızı düğmedir; önce "Ayarlar geri yüklensin mi?" diye sorar. Ayarlar **son kaydedilenlere** döner (`bot_data/profile.yml.bak` kopyası). Kopya yoksa `profile.yml` silinir ve bot varsayılan değerleri alır. Kaydedilmemiş değişiklikler kaybolur. Bu düğme `bot_data/rules` dosyalarındaki ana takımlara ve kurallara dokunmaz ancak sayfa formu bunları diskten yeniden okur.
- :triangle-alert: **Sayfadan kaydedilmemiş değişikliklerle ayrılırsan** (başka bir bölüme geçerek veya pencerenin çarpı işaretiyle), "Değişiklikler kaydedilsin mi?" penceresi "Kaydet", "Kaydetme" ve "İptal" düğmeleriyle açılır.

Bot ayarları **yalnızca bir kez, "Farmı başlat" düğmesine bastığında** okur. Çalışma sırasında bunları değiştirebilirsin ancak yalnızca durdurulduktan ve yeniden başlatıldıktan sonra geçerli olurlar. "Duraklat" ve "Devam et" bile bunları güncellemez. Ana sayfadaki "Başlatma ayarları" kartı botun şu anda çalıştığı ayarları gösterir.

> [!warning] `profile.yml` dosyası bozuksa ana günlüğün üst kısmında `[ОШИБКА] Файл profile.yml поврежден!` görünür, sayfada standart değerler olur ve "Ayarları kaydet" yazmayı reddeder ("profile.yml bozuk — ayarlar kaydedilmedi"). "Geri Yükle / Sıfırla" düğmesine tıkla.

> [!done] Artık her oda için hedefi, eşikleri ve takımları nasıl ayarlayacağını biliyorsun. Sırada "Otomatik taktik ve CP" sekmesi var: kapı sırası ve botun titanları nasıl iyileştirip değiştirdiği. [Sonraki bölüm →](#8)

## Kural Sihirbazı: «Otomatik taktik ve CP»

Kural Sihirbazı'nın второй sekmesi. İlk sekmede («Temel ve odalar») takımları ve genel eşikleri belirledin. Burada bota, **ters giden bir şey olduğunda nasıl davranacağını** açıklıyorsun: önce hangi kapıya gideceğini, neyin kötü savaş sayılacağını, başka bir takımı kaç kez deneyeceğini, seni ne kadar süre bekleyeceğini ve yaralı titanları nasıl iyileştireceğini söylüyorsun. Tüm alanlar zaten mantıklı sayılarla doldurulmuştur, bu yüzden bot senin değişikliklerin olmadan da çalışır. Sadece istediğin gibi davranmadığını gördüğünde değiştir.

![«Otomatik taktik ve CP» sekmesi: üstte bant, dört kapı, yan yana iki kart ve altta kişisel eşikler](images/tactics_tab.png)

İlk sekmede olduğu gibi, **«Ayarları kaydet» butonuna basana kadar hiçbir şey kaydedilmez**, bot ise ayarları «Farmı başlat» butonuna bastığında bir kez okur. Farm sırasında değiştirirsen, durdurup yeniden başlattıktan sonra etkili olur.

### Üstteki mavi bant

İçinde, botun kötü bir savaşta ne yaptığı kısaca açıklanmıştır: savaşı geri çeker, yedek takımla tekrar oynar ve başarılı takımı bir kurala kaydeder.

İlk sekmede «Bot kendisi karar verir» anahtarı kapalıysa, banda bir cümle daha eklenir. Önemli bir cümle olduğu için bunu ayrıca ele alalım. **«Bot kendisi karar verir» olmadan iki şey çalışmaz: yedek takımlar ve iyileştirme takımı.** Bu sekmedeki diğer her şey her zaman çalışır:

- :door-open: kapı sırası;
- :gauge: SOS penceresine yanıtının beklenmesi (savaş kötü olduğunda botun seni çağırdığı pencere);
- :triangle-alert: kötü savaş ölçütleri;
- :heart-pulse: kişisel panik eşikleri.

### «Kapı önceliği»

Koridorda bot genellikle aynı anda birkaç kapı görür: her element için birer tane (su, toprak, ateş) veya «Karma». Odanın içinde seni düşmanlar bekler ve her element için ayrı bir takım vardır. Sıra, **botun önce hangi kapıyı açacağını** belirler. Varsayıлан sıra şöyledir: «Su», «Karma», «Toprak», «Ateş».

Dört konum soldan sağa doğru sıralanır, aralarında oklar vardır; her birinde 1'den 4'e kadar bir numara bulunur. Konuma tıkla ve elementi seç. Tekrar olmaz: Zaten başka bir konumda duran bir elementi seçersen, sadece **yer değiştirirler**. Önceden «Su, Karma, Toprak, Ateş» idi, ilk konuma «Ateş» seçtin — «Ateş, Karma, Toprak, Su» olur.

Oyunda şaşırmamak için iki küçük not:

- Kapı **bir «Skip» kuralı tarafından yasaklandıysa** (bunlar hakkında — «Kurallar ve müdahaleler» bölümünde), sırada ilk olsa bile bot onu atlar. Tüm kapılar yasaklıysa — sıradaki ilk kapıyı alır.
- «Bot kendisi karar verir» açıkken, bot bazen sırayı takip etmeden **kendisi başka bir kapı seçer**: yaralı titanı iyileştirebileceği bir odaya gider veya yaralılar için tehlikeli bir kapının etrafından dolanır. Bu seçim günlükte `[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...` satırıyla görünür.

### «Kötü savaş ölçütleri ve SOS» kartı

- :swords: **«Odada denenecek yedek takım»** — botun tek bir odada savaşı kendisinin kaç kez geri çekip başka bir takımla tekrar oynayabileceği. 1 ile 3 arası, varsayılan 2'dir. Hakları bitti ve savaş hâlâ kötüyse — bot seni çağırır. Yalnızca «Bot kendisi karar verir» açıkken çalışır. Üçten fazla olamaz: Tek bir savaşı on kez tekrar oynamanın anlamı yoktur ve her deneme zaman alır.
- :gauge: **«Yanıtsız SOS penceresi süresi, dk»** — botun kendisi karar vermeden önce «Müdahale gerekiyor» penceresine yanıt vermeni kaç dakika bekleyeceği. 0 ile 60 arası, varsayılan 10'dur. Alanın altındaki yazı «0 — her zaman bekle» şeklindedir: **sıfır «her zaman bekle» anlamına gelir**, bot sabaha kadar bile seni bekler. Bu «Bot kendisi karar verir» seçeneği **olmadan** da çalışır. Botun tam olarak neye kendisinin karar vereceği (savaşı geri çeker, kabul eder veya duraklatır) — SOS pencereleri bölümünde açıklanmıştır.
- :users: **«Savaşı kötü say, если»** — takımın genel kayıpları: «titan ≥ 3» ve «kaybedilen ≥ 40» «% CP her biri». Bu kontrol, **her biri tek başına dayandığı** halde takımın hep birlikte döküldüğü durumu yakalar. Üç titan %40 veya daha fazla kaybetti — hiçbir titan panik eşiğinin altına düşmemiş olsa bile savaş kötüdür. «0 titan — kontrol etme» yazısı şu anlama gelir: ilk alana 0 yazarsan kontrol kapanır. İlk alan 0 ile 5 arası, ikinci alan 0 ile 100 arasıdır.

Somut bir örnek. Takım: Araji, Hyperion, Rigel, Iyari, Lumira. Savaştan sonra Araji %45, Rigel %42, Iyari %40, diğerleri ise %10 kaybetti. Üç titan «40 ve üzeri» kaybetti — her birinin panik eşiğinden fazla CP'si kalmış olsa bile savaş kötüdür. Iyari sadece %35 kaybetmiş olsaydı, böyle iki titan olacaktı ve genel kontrolün kusur bulacağı bir şey kalmayacaktı.

> [!note] Kötü savaşın diğer belirtileri — panik eşiği ve kayıp toleransı — ilk sekmede («Temel ve odalar») yer alır. **En az bir** belirti tetiklendiyse savaş kötüdür: bir titan öldüyse veya pencerede bulunamadıysa, birinin CP'si eşiğin altındaysa, biri toleranstan fazlasını kaybettiyse veya genel kayıplar tetiklendiyse.

Yanlış bir sayı girdiysen (bir harf veya sınırların dışında bir sayı), alan kırmızıya döner, altında «... ile ... arası bir sayı» belirir ve düzeltmeden ayarları kaydedemezsin.

### «Karışık odada otomatik iyileştirme takımı» kartı

Genellikle şöyle olur: Bir titan art arda birkaç savaşta darbe alır ve yarı canla gezer. Er ya da geç eşiğin altına düşer ve savaş kötüleşir. «İyileştirme», botun yaralının iyileşmesi için **kendisi özel bir takım kurmasıdır** (takıma bir iyileştirici konur ve o yaralının sağlığını yükseltir). Bot böyle bir takımı yalnızca «Karma» oda için kurar, çünkü oraya herkes konabilir.

Bu yalnızca «Bot kendisi karar verir» açıkken ve yalnızca kendi iyileştirme kuralın çalışmadıysa çalışır (kural daha üstündür).

- :heart-pulse: **«CP şunun altındaysa titanı iyileştir, %»** — varsayılan 60'tır. Bu sayıdan daha sağlıklı olan titan sağlıklı kabul edilir. **0**, iyileştirme takımını tamamen kapatır. Ancak bir alt sınır vardır: Titanın CP'si zaten **panik eşiğinin altındaysa**, «Karma» odada iyileştirilemez ve bot ona dokunmaz.
- :users: **«Yaralı için takımdan kim çıkarılsın»** — oklu üç konum. Yaralıyı koymak gerektiğinde ve takımda yer olmadığında biri ayrılır. Konuma tıkla ve bir titan seç: Liste elementlere göre sütunlara ayrılmıştır. **«— otomatik —»** (varsayılan olarak böyledir) şu anlama gelir: Bot takımın sonundan çıkarır ama **iyileştiricilere dokunmaz**. «Hyperion, Rigel, Iyari, Lumira, Amon» takımı için bunlar Amon, ardından Lumira olacaktır. Başka bir konumda duran bir titanı seçersen yer değiştirirler.

Botun nasıl iyileştirdiği, basit kelimelerle:

1. Kimin CP'sinin %60'ın altında ama panik eşiğinin üzerinde olduğuna ve bunların hangilerinin «Skip» kurallarınca yasaklanmadığına bakar.
2. Kendi eşiğine en yakın olandan başlayarak **teker teker** iyileştirir. Önce ana titanları (temel takımlardan), sonra yedekleri.
3. Yaralı takımda yoksa — çıkarılanın yerine geçer. Ancak "kendi" odalarında zaten iyileştirilen titanları (su ve toprak: temel takımlarında iyileştirici vardır) bot, orada iki savaş üst üste eşiğin üzerine çıkmadıkları sürece «Karma» odaya çekmez. Ateş titanlarını kendi odalarında iyileştirecek bir şey yoktur, bu yüzden onlar için iyileştirme hemen devreye girer.
4. Yaralı zaten takımdaysa ama iki savaş üst üste yükselmiyorsa — çıkarılanın yerine **sağlıklı ve enerjisi dolu bir iyileştirici** geçer (CP %80'den, enerji %60'tan itibaren).
5. İçinde iyileştirici kalmadıysa, bu düşmanlara karşı kaybediyorsa, yaralılar için tehlikeliyse veya manuel savaş gerektiriyorsa (Angus) takım seçilmez.

Bot neden bu kadar dikkatlidir? Hiçbir yerde belirtmediğin birini iyileştirmez: Takımlarında ve kurallarında olmayan bir titanı bot kendisi koymaz. Takım kurulamadıysa (titan slota yerleşmediyse) — bot durmaz, normal takımı koyar ve **çalışmanın sonuna kadar bu titanı bir daha iyileştirmez**.

Günlükte bu, `[ТАКТИКА] Пак отхила (бот собрал сам): ...` ve `[ТАКТИКА] Отхил: ...` satırlarıyla görünür (yaralının neden iyileştirilmediği).

### «Titanların kişisel panik eşikleri, % CP» kartı

Genel panik eşiği (varsayılan 40) — herkes içindir. Ancak diğerlerinden daha önce kaybetmek istemeyeceğin titanlar ve düşük CP'yi rahatça atlatan titanlar vardır. Bunlar için **özel bir eşik** belirleyebilirsin.

- Altta «Diğer titanlar — ortak eşik %40» yazısı vardır (sayı ilk sekmedendir). Kişisel eşik yokken «Kişisel eşik yok — tüm titanlar ortak eşiği kullanır» yazar.
- «Bir titana kişisel eşik koy» butonuna tıkla. Küçük bir «Kişisel panik eşiği» penceresi açılır: Listeden titanı seç ve 0 ile 100 arasında bir sayı yaz. «Uygula» butonuna tıkla. Pencere, karşılaştırabilmen için «Ortak eşik — %40» şeklinde ipucu verir. Listede yalnızca henüz kişisel eşiği olmayan titanlar bulunur.
- Belirlenen her eşik, bir titan ve sarı sayı içeren bir banttır. Banda tıkla — eşiği değiştir (titan değiştirilemez, kaldırılıp yeniden eklenmelidir). Banttaki **çarpı işareti** eşiği kaldırır ve titan tekrar genel eşiğe göre yaşar.

Savaştan sonra bu titanının CP'si **kendi kişisel eşiğinin altındaysa** savaş kötüdür. Örnek: Genel eşik 40, Rigel için 60 olarak ayarlanmış. Rigel %55 ile çıktı — savaş kötüdür, oysa diğerleri için 55 normal olurdu.

> [!tip] Nereden başlamalı? Birkaç onlarca oda görene kadar hiçbir şeyi değiştirme. Botun aynı titan yüzünden seni çağırdığını fark ettiğinde — onun kişisel eşiğini daha düşük ayarla. Bot iyileştirme için takımı çok sık değiştiriyorsa — «CP şunun altındaysa titanı iyileştir, %» alanındaki sayıyı **azalt**. Hiç iyileştirmesini istemiyorsan — 0 yaz.

> [!warning] «Yanıtsız SOS penceresi süresi, dk» değerini 0 yapıp uyumaya gidersen ve bot seni pencerede çağırırsa, sabaha kadar bekler. En iyisi 10–15 dakika bırakıp Telegram'ı ayarlamaktır: Böylece sorunu hemen öğrenirsin, yetişemezsen de bot kendisi karar verir.

> [!done] Artık kapı sırasını nasıl belirleyeceğini, neyin kötü savaş sayılacağını ve botun yaralıları nasıl iyileştirdiğini biliyorsun. Sırada — Telegram ve seni yardıma çağıran pencereler var. [Sonraki bölüm →](#9)

## Kural Sihirbazı: «Kurallar ve müdahaleler»

«Kural Sihirbazı»nın üçüncü sekmesi. İlk sekmede her odanın **ana paketini** belirledin, ikincisinde ise botun tehlike anında nasıl davranacağını. Burada ona **istisnaları** öğretiyorsun: «genellikle ana paketi koy, ancak şu gerçekleşirse farklı yap». Bu tür her istisnaya **kural** denir. «Müdahale» ise kuralın paket seçimini ana paketten «devralıp» kendi paketini koymasıdır.

Kural her zaman aynı şekilde okunur: **«eğer [koşul] — o zaman [eylem]»**. Örneğin:

- :heart-pulse: «Araji'nin CP'si %50'nin altındaysa — iyileştirici Sigurd'lu paketi koy».
- :swords: «Odadaki düşmanlar Angus, Sylva ve Verdok ise — bu paketi koy».
- :door-open: «Araji'nin CP'si %30'un altındaysa — «Ateş» odasına girme».
- :users: «Odadaki düşmanlar Angus, Avalon ve Eden ise — dur ve bana sor».

![«Kurallar ve müdahaleler» sekmesi: element filtreleri, simgeli kural listesi, paketler ve anahtarlar](images/rules_intercepts.png)

Her elementin kendi kuralları vardır: «Toprak», «Su», «Ateş» ve «Karma» ayrı listelere sahiptir. Bot «Ateş» kapısına girdiğinde yalnızca «Ateş» kurallarına bakar. Diğer sekmelerde olduğu gibi, **«Ayarları kaydet» butonuna basana kadar hiçbir şey kaydedilmez**, bot ise kuralları «Farmı başlat» butonuna bastığında bir kez okur.

> [!note] Birçok kuralı hiç yazmak zorunda kalmayacaksın. Eğer «Bot kendisi karar verir» açıksa, bot geri çekilmeden sonra başarılı paketleri **kendisi hatırlar** ve «altın kuralları» kendisi ekler. Bunlar aynı listede görünecektir (bunlar hakkında aşağıda). Kendi kuralların, «bunu yapmak olmaz» veya «böyle bir durumda tam olarak bu paket lazım» diye bildiğinde gereklidir.

### Ne tür kurallar vardır

Bir kuralın koşulu üçünden biri, eylemi ise üçünden biridir. Birlikte alışılagelmiş türleri oluştururlar:

- :heart-pulse: **CP'ye veya enerjiye göre kurtarma.** Koşul — «belirli bir titan CP'si (veya enerjisi) %N altında», eylem — başka bir paket koymak. Listede simge **«İYİLEŞTİRME»** (CP'ye göre) veya **«ENERJİ»**. Can yenileme böyle yapılır: titan yaralandığında iyileştirici içeren paket konur.
- :swords: **Bu düşmanlara karşı.** Koşul — «odada tüm bu düşmanlar var», eylem — kendi paketini koymak. Simge **«DÜŞMANLAR»**. Düşmanlar, botun Zindanda tanıdığı 13 titan arasından seçilebilir.
- :door-open: **«Skip» — yasak.** Koşul — «titannın CP'si veya enerjisi %N altında», eylem — bu titanı koymamak ve bu odaya girmemek. Simge **«ATLA»**, sağda «Odayı atla» işareti.
- :users: **«Sana sor».** Herhangi bir koşul, eylem ise kendi karar vermeyip seni çağırmaktır. Sağda **«Sana sor»** işareti bulunur, simge ise koşula bağlıdır («CP», «ENERJİ», «DÜŞMANLAR»). Çalıştığında bot «Uygun paket yok» penceresini açar ve senin yanıtını bekler. «Oto-taktik» bölümünde ayarlanan süre içinde yanıt vermezsen kendi karar verir.

«CP» simgesi («İYİLEŞTİRME» değil), koşulun CP'ye göre olduğu, eylemin ise «Sana sor» olduğu anlamına gelir. Hiç koşul yoksa simge de yoktur ve adın altında «Koşul yok — kural hiç çalışmaz» yazılır.

Şimdi «Skip» hakkında, çünkü aynı anda iki görevi vardır. Örnek: «Ateş» odasında «Araji, CP %30 altında» kuralı var.

1. **Kapı.** Araji %30'un altında olduğu sürece bot «Ateş» kapısına gitmez ve başka bir kapı seçer. Tüm kapılar yasaksa bot sıradaki ilk kapıyı alır.
2. **«Kara liste».** Bu odada Araji koyulmayacaktır: içinde onun bulunduğu her paketi bot reddeder ve bir sonrakini alır. **Ana** paket de yasaklı titanı içeriyorsa, koyacak bir şey kalmaz — bot durur ve «Uygun paket yok» penceresini açar.

> [!warning] «Skip» düşmanlara göre yapılamaz. Bot düşmanları **ancak** kapıdan girdikten sonra öğrenir, bu yüzden kapıyı onlara göre seçemez. «Düşmanlara göre» kural penceresinde «Skip» kutusu kullanılamaz. Belirli düşmanların olduğu bir odayı pas geçmek istiyorsan — «Sana sor» kuralı koy, karar sana kalsın.

### Bot kuralları hangi sırada kontrol eder

Savaş başladığında bot odanın kurallarını **şu sırada** gözden geçirir:

1. **«Skip».** Önce bot titanların «kara listesini» oluşturur: tetiklenen «Skip» kuralının kimi yasakladığını belirler. Böyle bir titan içeren paket, kuralın kendisi istese bile uygun olmayacaktır (buna veto denir: yasak her kuraldan güçlüdür).
2. **Kurtarma.** Koşulunda titan CP'si veya enerjisi bulunan kurallar. «Araji %50 CP altındayken düşmanlara karşı» kuralları da buraya dahildir (düşmanlar artı CP): bunlar hemen burada, sıradan düşman kurallarından **önce** kontrol edilir.
3. **Düşmanlara karşı.** Koşulunda yalnızca düşmanlar bulunan kurallar.
4. **Odanın ana paketi** — hiçbir şey uymadıysa.

Her grubun içinde bot **yukarıdan aşağıya** doğru ilerler ve ilk tetiklenen kuralı alır. Oklar bu yüzden gereklidir: aynı grubun iki düşman kuralı aynı anda uyarsa, üstteki kazanır. Ancak «Kurtarma» kuralı, listede nerede durursa dursun, her zaman «Düşmanlara karşı» kuralından güçlüdür. **Kapalı** kurallar kontrole katılmaz.

Koşullar, botun titanların hakkında bildikleriyle karşılaştırılır (CP ve enerjiyi takım seçme ekranından ve savaşlardan sonra alır). Bot bir titanın canını henüz görmediyse, onu tam kabul eder ve «%N altında» kuralı çalışmaz. Koşulda birden fazla titan varsa (botun kendisi hatırladığı kurallarda olur), tüm koşulların **aynı anda** sağlanması gerekir. Düşmanlarda da aynıdır: kural ancak odada listelenenlerin **hepsi** varsa çalışır.

### Kural listesi: satırda ne var

Üstte — «Etkin kurallar» ve kural sayısını gösteren gri bir rozet, sağda ipucu: «Sırayı değiştirmek için bir element seç» (tümü gösterildiğinde) veya «Listede daha üstteki kural önce kontrol edilir» (tek element seçildiğinde). Aşağıda «Tümü», «Toprak», «Su», «Ateş», «Karma» filtre butonları ve «Yeni kural» butonu. Altlarında sütun başlıkları: «№», «Koşul», «Eylem», «Açık».

Her satırda soldan sağa:

- **Numara** — kendi element listesindeki yeri. Numara ne kadar küçükse, kural o kadar önce kontrol edilir. **Tek bir** element seçildiğinde numaranın yanında «Yukarı» ve «Aşağı» okları belirir. «Tümü» seçildiğinde oklar yoktur: elementler sırayla gösterilir ve kendi aralarında yarışmazlar.
- **Simgeler** — odanın elementi ve kural türü («İYİLEŞTİRME», «CP», «ENERJİ», «DÜŞMANLAR», «ATLA»).
- **Ad** ve altındaki gri satır — kelimelerle koşul, örneğin «Araji: CP %50 altında» veya «Odadaki düşmanlar: Angus, Sylva».
- **Eylem** — ok ve paketteki titan kareleri (soldan sağa, oyundaki gibi) «paket değişimi» yazısıyla. Ya da «Sana sor» / «Odayı atla» rozeti.
- **«Açık» anahtarı** — kuralı açmak veya kapatmak.
- **Kalem** «Düzenle» ve **çarpı** «Sil».

Kural yoksa, listenin yerinde şöyle yazar: «Kural yok. «Yeni kural» butonuna basın — veya bot geri çekilmeden sonra kuralı kendisi hatırlayacaktır.»

### Anahtar, oklar, çarpı ve «Temizle»

- :check: **Anahtar.** Kapalı kural soluklaşır ancak **listede kalır** ve bot onu atlar. Bu, «kuralı geçici olarak kaldırmanın» en iyi yoludur: paketi yeniden toplamak gerekmez. Başlatıldığında günlükte şu satır görünür: `[ПРАВИЛА] Выключено правил: N, бот их пропускает.`
- :chevron-up: **«Yukarı» ve «Aşağı» okları** kuralın komşusuyla yerini değiştirir. Aynı gruptaki iki kural aynı anda uyabileceğinde ve hangisinin önce kontrol edileceği önemli olduğunda gereklidir.
- :x: **«Sil» çarpı simgesi.** Aşağıda «Kural «…» silindi» bildirimi ve **«Geri al»** butonu belirir. Bildirim ekrandayken kural aynı yerine geri getirilebilir.
- :trash-2: **«Tüm kuralları temizle»** yalnızca **şu anda görünenleri** siler. «Su» seçiliyse su kuralları silinir, «Tümü» seçiliyse tümü. Önce bot tekrar sorar: «Tüm kurallar silinsin mi?» ve kaç tane olduğunu yazar («Tümünü sil» butonu). Ardından yine «Silinen kural: N» bildirimi ve «Geri al» butonu görünecektir.

Tüm bu eylemler yalnızca sayfayı değiştirir. Dosyalara ancak «Ayarları kaydet» sonrasında girerler ve **yalnızca değişiklik yapılan elementler** yazılır. Kaydetmeden sayfadan ayrılırsan pencere «Değişiklikler kaydedilsin mi?» diye sorar.

> [!tip] Bir kuralı silip silmeme konusunda tereddüt ediyorsan, anahtarla kapatmak daha iyidir. Botun kendisinin hatırladığı kurallar için bir sebep daha vardır (aşağıya bak): kapalı olan kurala bot dokunmaz ve yeniden oluşturmaz, silinen ise tekrar ortaya çıkabilir.

### Adım adım «Yeni kural» penceresi

«Yeni kural» butonuna bas (veya ilk sekmedeki oda kartının altındaki «Koşul» butonuna). Bir pencere açılacaktır. Tek bir element seçiliyse hemen onu önerir. Satırdaki kalem, «Kuralı düzenle» başlıklı aynı pencereyi açar.

![«Yeni kural» penceresi: element ve ad, üç tetikleyici, koşul alanları, eylem ve takım](images/rule_editor.png)

1. **«Odanın elementi» alanından elementi seç.** Kural yalnızca orada çalışacaktır. Hangi titanların seçilebileceği elemente bağlıdır: «Toprak» odasında yalnızca toprak titanları, «Su» odasında yalnızca su titanları, «Karma» odasında ise hepsi. Elementi daha sonra değiştirirsen pencere seçimi kendisi düzeltir.
2. **Kuralı adlandır (isteğe bağlı).** «Kural adı» alanı boş bırakılabilir: bu durumda isim koşuldan oluşturulur, örneğin «Araji: CP %50 altında». Bot bu ismi kural çalıştığında günlüğe yazar.
3. **«Tetikleyici» seç** — botun neye bakması gerektiği: «CP'ye göre», «Enerjiye göre» veya «Düşmanlara göre».
   - «CP'ye göre» ve «Enerjiye göre»: **«Titan»** seç ve «CP şunun altında, %» (veya «Enerji şunun altında, %») alanına 0 ile 100 arasında bir sayı gir. Varsayılan olarak CP — 35, enerji — 100. Sayı olmayan veya sınırların dışında bir sayı girilirse alan kırmızıya döner ve altında «0 ile 100 arası bir sayı» belirir.
   - «Düşmanlara göre»: «Odadaki tehlikeli düşmanlar» ızgarasında **birlikte** bulunması gereken herkesi işaretle. Yanında «· seçilen: N» yazar. Kimseyi seçmediysen kaydedemezsin.
4. **«Çalışınca yapılacak eylem» seç.** Birbirini dışlayan iki kutu vardır: «Dur ve bana sor» ve «Odaya girişi yasakla (Skip)». Hiçbiri işaretlenmemişse kural **paket koyacaktır**.
5. **Titanların denenmesini şart koş (isteğe bağlı).** Kural yalnızca seçilen titanlar (1 ile 5 arası, herhangi bir elementten) bu çalıştırmada zaten bir savaşa girdiyse çalışır. Örneğin paket Sigurd'u istiyor, ama sen hiç savaşmamışsa onu koymak istemiyorsun. Yanındaki çarpı denemeyi kaldırır. Deneme şartı yalnızca paket koyan kurallarda vardır. Yumuşak duraklatma ve manuel savaştan sonra bot titanların durumunu unutur ve deneme şartı baştan başlar.
6. **«Bu kural için takım» seç.** «Takım seç» butonuna bas ve «Takımı kur» penceresinde **3 ile 5 titan** seç (ana pakette olduğu gibi). «Sana sor» ve «Skip» için takım gerekmez, orada «Bu eylem için takım gerekmez» yazar.
7. **«Kuralı kaydet» butonuna bas.** Buton gri olduğu sürece pencerenin altında neyin eksik olduğu yazar: «Bir takım seç: 3 ile 5 titan», «En az bir düşman seç» veya «Sayıyı düzelt: 0 ile 100 arası». «İptal» pencereyi değişiklik yapmadan kapatır.

Yeni kural kendi elementinin **birinci sırasına** yerleşir, değiştirilen kural kendi yerinde kalır (elementi değiştirdiysen yenisinde birinci sıraya geçer). Dosyaya, diğer her şey gibi, «Ayarları kaydet» sonrasında girecektir. Pencereyi ilk sekmeden «Koşul» butonuyla açtıysan, kaydettikten sonra «Kural «…» «Kurallar ve müdahaleler» sekmesine eklendi» bildirimi görünecektir.

> [!note] Botun kendisinin hatırladığı bir kural kalemle açılıp düzenlenebilir. Pencerede görünmeyen her şey (örneğin «kayıp toleransı» veya fazladan CP koşulu) **olduğu gibi korunur**. Pencere bu koşulu gri bir satırla gösterir: «Koşulda başka ne var (olduğu gibi korunur): …».

### Botun kendisinin hatırladığı kurallar

Eğer «Bot kendisi karar verir» açıksa, listede senin yazmadığın kurallar belirir. Bunlar adından anlaşılır:

- :refresh-cw: **«Oto: odada Angus + Sylva»** — bot kötü savaşı geri çekti, başka bir paketle tekrar oynadı ve o paket başardı. Bot hatırladı: «bu düşmanlara karşı bu paketi koy». Adın altında «Bot geri çekilmeden sonra hatırladı» (veya SOS penceresinde paketi sen seçtiysen «Geri çekilme sonrası paketin, bot hatırladı») yazar. Paket bir koşul yüzünden kaybettiyse (örneğin «Araji %50 altında CP»), bu koşula eklenir. Böyle bir kural birinci sıraya yerleşir.
- :star: **«Altın: odada Angus + Sylva»** — «Paket bu düşmanları sık sık yendi». Başlatıldığında bot geçmişi gözden geçirir ve bu düşman kadrosuna karşı **5 savaş ve üzeri** yapmış ve **%80 ve üzeri** kazanmış paketi alır. Ana paket, kurtarma kurallarının paketleri ve senin yedek paketlerin «altın» kurallara girmez.

Dosyada bu kurallar farklı adlandırılır («Анти-пак против: …», «Золотое правило против: …») ve günlükte tam olarak şöyle yazılır: `[ОБУЧЕНИЕ] Новое правило '…': пак […]. Сохранено на 1-е место.` Pencere bunları kısaca ve anlaşılır şekilde gösterir. Kuralı yeniden adlandırırsan kendi verdiğin adı görürsün.

Bu kurallar hakkında bilinmesi yararlı olanlar:

- **Bot çift kural oluşturmaz.** Aynı koşula sahip kural ikinci kez oluşturulmaz: eskisinin paketi değişir ve yukarı taşınır.
- **Her başarılı geri çekilme hatırlanmaz.** Kötü savaş yalnızca titan yaralı girdiği için gerçekleştiyse ve %100 CP ile her şey yolunda olacaksa («düşmanların suçu yok»), kural oluşturulmaz.
- **Kapalı kurallara bot dokunmaz:** açmaz ve üzerine yazmaz. Aynı paketi bir daha hatırlamaz ve kapalı «altın» kural geri dönmez.
- **Silinen kurallar geri dönebilir.** «Altın kural» bir sonraki başlatmada bu düşmanlara karşı başka kural yoksa yeniden oluşturulur. Hoşuna gitmiyorsa anahtarla kapat. «Oto» kuralını geri çekilme yine aynı şekilde sonuçlanırsa bot yeniden oluşturur.
- **Pencere açıkken bot dosyaya yeni kural yazabilir.** «Ayarları kaydet» butonuna bastığında pencere dosyayı tekrar okur ve bu yeni kuralları hiçbir şey kaybetmeden üste koyar. Sekmeye hiçbir şeyi değiştirmeden baktıysan — diskten gelen taze listeyi görürsün.

> [!warning] Elementin kural dosyası bozuksa (örneğin elle düzenlendi ve girintide hata yapıldı), pencere örneğin su için şöyle yazar: «Kural dosyası bozuk: bot_data/rules/water.yml — pencere bu elementin kurallarını değiştirmez». Diğer elementler çalışır. Dosyayı elle düzenlemeye gerek yok: ana sayfada «Günlüğü yazara gönder» butonuna bas ve ne olduğunu yaz.

> [!tip] Nereden başlamalı? Önceden hiçbir şey yazma. «Bot kendisi karar verir» açıkken birkaç düzine oda oyna ve buraya bak: bot birkaç kuralı zaten hatırlamış olacaktır. Başarısız olanları kapat, iyi olanları oklarla yukarı taşı. Kendi kurallarını tekrarlayan bir sorun gördüğünde ekle: «Araji hep yaralı geziyor» — kurtarma kuralı; «bu düşman kadrosu ana paketimi her zaman öldürüyor» — düşmanlara karşı kural.

> [!done] Artık bota istisnaları öğretmeyi biliyorsun ve neden tam olarak bu paketi koyduğunu anlıyorsun. Sırada — Telegram ve seni yardıma çağıran pencereler. [Sonraki bölüm →](#10)

## Savaş kötü geçtiğinde: SOS pencereleri

Bot neredeyse her zaman kendi başına halleder. Ancak bazen insan müdahalesi olmadan ilerleyemediği bir durumla karşılaşır: savaş kazanılmıştır ama bedeli çok yüksektir ya da kurallar uygun tek bir paket bile vermiyordur. Bu durumda bot **durur ve seni çağırır** ekranın ortasındaki bir pencereyle. SOS, gemilerdeki gibi bir imdat sinyalidir: "yardım lazım". Sen yanıt verene kadar bot hiçbir şeye basmaz ve bekler (ama sonsuza kadar değil, bu konuda — aşağıda).

Üç pencere vardır ve her birinin kendi durumu bulunur:

- :triangle-alert: **«Müdahale gerekiyor»** — savaş bitti ama sonuç kötü. Bu ana penceredir, en sık bu görünür.
- :users: **«Uygun paket yok»** — bot henüz savaşa başlamadı: kurallar bu oda için ona paket vermiyor.
- :check: **«Paket başardı»** — başka bir paketi sen kendin seçtin, o kazandı ve bot onu hatırlayıp hatırlamayacağını soruyor.

![«Müdahale gerekiyor» penceresi: neden, oda, düşmanlar, CP çubuklarıyla paketiniz ve üç düğme](images/sos_window.png)

> [!note] Pencere ne zaman görünür: «Bot kendisi karar verir» **kapalıysa** (varsayılan olarak böyledir), pencere **her** kötü savaştan sonra açılır. Açıksa, bot önce sen olmadan halletmeye çalışır ve yalnızca başaramadığında çağırır: savaş manuel oynandı (Angus), sonuç penceresi okunamadı, paketi sen seçtin, odada bot izin verilen sayıda geri çekilme yaptı veya yedek paket yok. Ne tür bir savaşın "kötü savaş" olduğu ve bunun nasıl ayarlanacağı — «Temel ve odalar» ve «Otomatik taktik ve CP» bölümlerindedir.

### «Müdahale gerekiyor» penceresi

Üstte — kısaca: «Savaş kötü geçti. Ne yapıyoruz?». Aşağıda — günlüğe bakmadan karar verebilmen için gerçekler:

- **Neden.** Botun tam olarak neyi beğenmediği. Örneğin: «Kritik eşik! Araji %12 CP'ye sahip (eşik: %40)», «Kayıp Deltası aşıldı! Rigel %45 CP kaybetti (tolerans: %30)», «ÖLÜMCÜL! Iyari öldü…», «Büyük paket kayıpları!…» veya «Sonuç penceresi okunamadı: bulunamadı…». Titan isimleri — programın dilindedir.
- **Oda.** Kapının elementi ve oda numarası: «Ateş · oda 54».
- **Düşmanlar.** Karşı savaşılan titanların kareleri. Düşmanlar tanınmadıysa — bu satır olmaz.
- **Paketin.** Her titan kendi sağlık çubuğuyla ve "Savaştan önceki CP → Savaştan sonraki CP" yazısıyla: «%36 → %12». Titanın CP'si panik eşiğinin (genel veya kişisel) altındaysa, çubuk ve sayı **kırmızıdır**. Savaşa zaten yaralı girip neredeyse hiç CP olmadan çıktıysa — bu hemen görünür.
- **Zamanlayıcı.** Altta: «Yanıt vermezsen bot 9:41 sonra kendisi karar verir». Son dakika sarıdır, ardından «Bot kendisi karar verir…». «Otomatik taktik ve CP» ayarında 0 varsa bu satır yoktur: bot seni her zaman bekler.

Düğmeler (sağdan sola, ana düğme en sağdakidir):

1. **«Savaşı geri al»** (mavi). Bu savaşı başka bir paketle tekrar oyna. Pencere gizlenir, mevcut paketle «Takımı kur» açılır; titanları değiştir ve «Bu paketle geri al» düğmesine bas. Bundan sonra ne olacağı — aşağıdaki «Geri çekilme» bölümündedir. Seçim yapmadan «Takımı kur» penceresini kapattın — SOS penceresi geri döner, hiçbir şey kaybolmaz.
2. **«Yok say»** (gri). Savaşı olduğu gibi kabul et: oda sayılır, bot kalan CP ile yoluna devam eder. Kayıplar seni tatmin ettiğinde uygundur (örneğin, titan zaten yaralı girdiyse ve genel olarak her şey normalse).
3. **«Elle oyna»** (gri). Bot hiçbir şeye basmaz, bu odayı oyunda sen kendin oynarsın. Bot sen koridora dönene kadar bekler: kapı bayrağı üst üste 2 saniye görünmelidir. En son sonuç penceresiydi — oda sayılır; kazanamadan geri çekildin — sayılmaz. Tekrar oynamadan sonuç penceresini kapattın — savaş olduğu gibi sayılır. Manuel oyundan sonra bot titanların CP'sini ve yuvalardaki kadroları unutur (takım seçim ekranından kendisi tekrar okur) ve sonrasında kendisi oynamaya devam eder.

> [!warning] **Angus'un manuel ultisinin** kullanıldığı bir savaş geri alınamaz: sonuç penceresinde «Tekrar dene» düğmesi yoktur. Pencerede «Savaşı geri al» yerine kırmızı **«Botu durdur»** yer alır, geriye sadece «Yok say» veya «Elle oyna» kalır.

### Geri çekilme: seçimin ardından bot ne yapar

Pencere kapandı, komut bota gitti. Sonrasında her şeyi kendisi yapar ve günlükte bu `[ОТКАТ]` etiketiyle görünür:

1. Sonuç penceresinde **«Tekrar dene»** düğmesine basar ve savaşın yüklenmesini bekler (bazen bu 20–30 saniye ve daha uzun sürer, bu yüzden bir dakikaya kadar bekler).
2. Savaşı **duraklatır** (bir kez) ve **«Geri Çekil»** düğmesine basar.
3. Koridora döner, **aynı odaya** girer ve yeni paketini yerleştirir.

Savaş yine kötü geçtiyse — pencere geri döner. İyi geçtiyse — işte burada «Paket başardı» penceresi görünür (aşağıdadır).

Oyunla bağlantı koptuysa ("yükleniyor" görseli bitmiyorsa), bot pes etmez: oyunu 15 dakikaya kadar bekler ve bunu günlükte yazar. Yalnızca geri çekilme yine de başarısız olursa bot `bot_data/debug/` klasörüne ekran görüntüsü kaydeder, yumuşak duraklatma yapar ve sana Telegram'dan mesaj gönderir. Ayrıntılar — sorun giderme bölümündedir.

### «Uygun paket yok» penceresi

Bot kapıyı seçip düşmanlara baktığında ancak **koyacak bir şey olmadığında** görünür. İki nedenden dolayı olur, ikisi de senin kurallarından kaynaklanır:

- «Bana sor» kuralı tetiklendi (tam olarak bunun için yapılmıştır);
- odanın ana paketi, «Skip» kuralının yasakladığı bir titan içeriyor (bot «ÖLÜMCÜL: Tüm paketler reddedildi…» gibi bir şey yazar).

Pencere sorar: «Kurallar bu oda için paket vermiyor. Ne yapıyoruz?» İçinde aynı «Neden», «Oda» ve «Düşmanlar» bulunur ama CP çubukları yoktur: henüz savaş olmadı. Düğmeler:

- **«Yeni paket kur»** (mavi) — «Takımı kur» penceresini açar, oradaki düğme «Uygula» adını taşır. Bot seçilen titanları koyar ve paketi **hemen "bu düşmanlara karşı" kuralı olarak kaydeder** (burada kaydetmeden önce kontrol yoktur, dikkatli ol).
- **«Elle oyna»** — odayı sen kendin oynarsın, bot koridorda bekler. Kazandıysanız oda sayılır.
- **«Botu durdur»** (kırmızı) — bot oturum özetini yazar ve kapanır.

Burada «Yok say» düğmesi yoktur: kabul edilecek bir şey yoktur, savaş olmadı.

### «Paket başardı» penceresi

Bu pencere, savaşı **senin seçtiğin** bir paket kazandığında görünür (pencerede veya Telegram'da «Savaşı geri al» veya «Başkasını dene» üzerinden). Yedek paketi botun kendisi seçtiyse ve o başardıysa, bot onu kendisi kaydeder ve hiçbir şey sormaz.

İçinde — oda, düşmanlar (en fazla 15 dakika öncesine ait son SOS penceresinden) ve savaştan sonraki CP ile paketiniz yer alır. Soru: «Denenen paket kazandı. Bu düşmanlara karşı kural olarak kaydedilsin mi?» Düğmeler:

- **«Paketi kaydet»** (yeşil) — bot bu paketle "bu düşmanlara karşı" kuralını kaydeder. Kurallar listesinde «Oto: odada …» veya «Geri çekilme sonrası paketin, bot hatırladı» olarak görünür.
- **«Başkasını dene»** — tekrar «Takımı kur» ve geri çekilme: bot kazanılan savaşı başka bir paketle tekrar oynar.

Yanıt vermezsen — zamanlayıcıdaki sürenin ardından («Yanıt vermezsen bot paketi kendisi kaydeder…» yazısı) bot sanki «Paketi kaydet» düğmesine basmışsın gibi paketi kendisi kaydeder.

### Pencere kapatma simgesi ve «Bot durdurulsun mu?»

Pencerelerde "öylesine kapatma" yoktur: pencereyi kapatırsan bot yanıt beklemeye devam eder. Bu yüzden kapatma simgesi sorar: **«Bot durdurulsun mu?»**. "Botu durdur" dersen — bot bitirir, özeti yazar ve Telegram'a gönderir. 10 saniye içinde yanıt vermezse program kendisi durdurur. «Paket başardı» penceresinde soru farklıdır: oradaki durdurma "DUR F10" gibidir, **oturum özeti Telegram'a gitmez**. Fikrini değiştirdiysen — «İptal» düğmesine bas, pencere kalır.

### Yanıt vermezsen ne olur

«Otomatik taktik ve CP» bölümündeki süre boyunca yanıt vermediğin her defasında («Yanıtsız SOS penceresi süresi, dk»: varsayılan 10, 60'a kadar, 0 — her zaman bekle), bot `[ТАКТИКА] Ответа нет 10 мин. Решаю сам.` yazar, pencere kapanır ve sana Telegram'dan botun kendisinin karar verdiğine dair bir mesaj gelir. Bu durum «Bot kendisi karar verir» kapalıyken de çalışır. Karar pencereye bağlıdır:

- **«Müdahale gerekiyor»:** yedek paket varsa ve savaş geri alınabiliyorsa (Angus değil, odadaki denemeler bitmedi) — **geri çekilme** ve yedek paket; aksi takdirde tüm titanlar hayattaysa — savaş **kabul edilir** («Yok say»); aksi takdirde (birileri öldüyse veya pencerede bulunamadıysa) — **yumuşak duraklatma**.
- **«Uygun paket yok»:** yaralısı ve yasaklı titanı olmayan yedek paket uygunsa — bot onu koyar **ve kuralı kaydetmez**; böyle bir paket yoksa — **yumuşak duraklatma**.
- **«Paket başardı»:** paket kaydedilir.

Yumuşak duraklatma — "Duraklat F9" düğmesi gibidir: sen «Devam et» düğmesine basana kadar bot koridorda bekler.

> [!tip] Tam bot kendisi karar verdiği anda mı yanıt verdin? Sorun değil: bot eski yanıtı atlar ve `[ЛОГИКА] Пропускаю ответ ...: он пришёл на прошлое окно.` yazar.

### Telegram'dan yanıt vermek

Telegram ayarlandıysa **aynı soru** sohbete de gelir: oyun ekran görüntüsü, açıklama (oda, düşmanlar, neden, CP ile paket) ve düğmeler. Neresi uygunsa oradan yanıt verebilirsin: sohbette yanıt verdiğinde bilgisayardaki pencere kendiliğinden kapanır ve tersi de geçerlidir.

- **«Geri al (Pak kur)»** (yeşil) — bot sohbete virgül veya boşlukla ayrılmış **3–5 titan** ismi yazmanı ister, kimi tanıdığını gösterir ve "Her şey doğru mu?" diye sorar («Paketi onayla» / «Başka yaz»). Angus'un manuel savaşı için ve «Uygun paket yok» için bunun yerine kırmızı «Botu durdur» yer alır.
- **«Elle oyna»** ve **«Yoksay (Devam et)»** — penceredekinin aynısıdır. «Uygun paket yok» penceresinde «Devam et» yoktur.
- Telegram'a «Paket başardı» yalnızca paketi oradan gönderdiysen gelir: «Onayla ve Kaydet» veya «Geri Al ve Tekrar Dene».

İnternet kesildiyse mesaj daha sonra gider (bot denemeleri tekrarlar), bilgisayardaki pencere ise kalır. Telegram ayarı — ilgili bölümündedir.

### Mini çubuk ve SOS pencereleri

Program penceresi mini çubuğa küçültüldüyse SOS penceresi **oyunun ortasında** görünür. Mini çubuk bu sırada kırmızıdır ve üzerindeki «SOS» düğmesi kaybolan pencereyi oyunun üzerine çıkarır.

> [!tip] Nasıl seçim yapmalı? «Paketin» kısmına bak. Bir titan yaralı girdi ve düştü, diğerleri iyiyse — genellikle «Yok say» yeterlidir. Düşmanları tanıyorsun ve çok daha güçlülerse — başka bir paketle «Savaşı geri al». Hiçbir şey anlaşılmıyorsa — «Elle oyna». Geri çekilme zaman alır (savaşın yeniden yüklenmesi gerekir, bu 20–30 saniye ve daha uzun sürebilir), «Yok say» ise zaman almaz.

> [!done] Artık her SOS penceresinin ne anlama geldiğini, düğmelerin ne yaptığını ve botun sen yokken ne yapacağını biliyorsun. Sırada — sen yanında yokken botun nasıl kendisinin karar verdiği var. [Sonraki bölüm →](#11)

## Bot nasıl kendisi karar verir

SOS pencereleriyle ilgili bölümde, kötü bir savaştan sonra botun seni çağırdığını gördün. Ancak her zaman çağırmaz: «Bot kendisi karar verir» seçeneğini açarsan («Temel ve odalar» sekmesi, bölüm 7), bot **önce sen olmadan halletmeyi dener** ve yalnızca başaramadığında yardıma başvurur. Burada nasıl düşündüğünü inceleyeceğiz. Formül olmayacak: yalnızca botun kendine sorduğu sorular ve örnekler olacak.

Telefonun başında yanında oturan deneyimli bir takım arkadaşı hayal et. Savaş kötü geçti ve sen çay almaya gittin. Oturup beklemeyecektir. Bu tür düşmanlara karşı daha önce neyin işe yaradığını hatırlayacak, savaşı başka bir kadroyla tekrar oynayacak ve neyin işe yaradığını kaydedecektir. Bot da aşağı yukarı böyle davranır. Sadece işleri berbat etmemek için kuralları vardır.

> [!note] «Bot kendisi karar verir» varsayılan olarak **kapalıdır** ve aşağıda bahsedilecek hiçbir şey o zaman gerçekleşmez: her kötü savaştan sonra bot sadece bir SOS penceresi açar. Anahtarı açtın, «Ayarları kaydet» düğmesine bastın — bir sonraki «Farmı başlat» işleminden itibaren geçerli olur. Tam olarak neyin ayarlanabileceğini bölüm 8'de («Otomatik taktik ve CP») incelemiştik, burada ise konu **botun bu sayılarla ne yaptığıdır**.

### Kötü savaş: bot sırasıyla ne yapar

1. **Savaşın kötü geçtiğini fark eder.** Birileri öldü veya panik eşiğinin altında, toleranstan fazlasını kaybetti ya da aynı anda üçü birden döküldü (bölüm 7 ve 8). Günlükte nedeni içeren `[ТАКТИКА] Плохой бой: ...` satırı yer alır.
2. **Kendisi geri çekilip çekilemeyeceğini kontrol eder.** Dört durumda imkansızdır: savaş manuel oynandı (Angus'un ultisi, sonuç penceresinde «Tekrar dene» düğmesi yoktur), sonuç penceresi okunamadı, paketi **sen** koydun (o zaman karar da senindir) veya bot bu odadaki deneme haklarını zaten harcadı. İmkansızsa — SOS penceresi açılır ve günlükte nedeni ile birlikte `[ТАКТИКА] Сам не откатываю: ... Спрашиваю вас.` yer alır.
3. **Yedek paket arar.** Nasıl aradığı — sonraki bölümdedir. Uygun bir şey yoksa — yine SOS penceresi.
4. **Geri çekilir ve tekrar oynar.** Senin seçiminden sonraki `[ОТКАТ]` adımlarının aynısı («Tekrar dene», duraklatma, «Geri Çekil») yapılır ve aynı odaya yedek paket konur. Günlükte `[ТАКТИКА] Откатываю бой сам и переиграю паком ... (взят: ...)` yer alır.
5. **Sonuca bakar.** Yedek başardıysa — bot devam eder ve kural olarak paketi hatırlar (bu konuda — aşağıda). Savaş yine kötü geçtiyse — ikinci deneme ve denemeler bitene kadar böyle devam eder («Odada denenecek yedek takım», varsayılan 2, en fazla 3). Sonra seni çağırır.

> [!tip] Bot "anlık düzeltme" yapmak yerine her defasında savaşı tamamen geri alır. Geri çekilme zaman alır (savaşın yeniden yüklenmesi gerekir, bu 20–30 saniye ve daha uzun sürebilir), bu yüzden boş denemeleri sevmez: paketi nasıl seçtiğini aşağıda gör.

### Bot yedek paketi nereden alır

Listeyi yukarıdan aşağıya doğru tarar ve **ilk uygun olanı** alır:

1. **Senin «Yedek takımlar» listen** — «Temel ve odalar» sekmesi, oda kartı. Senin sıraladığın sırayla alınır. Günlükte kaynak "ваш список запасных паков" (senin yedek paket listen) olarak adlandırılır.
2. **Bu elementin kurallarındaki paketler** — günlükte "правила стихии" (element kuralları). Kendi içinde sırası vardır: önce "bu düşmanlara karşı" kuralları, ardından tam olarak bu düşmanları daha önce yenmiş olan paketler (kalan CP'ye göre en iyiler ilk sırada), ardından diğer "anti-paketler", ardından odanın ana paketi dahil diğer her şey.
3. **Savaş geçmişi** — günlükte "история боёв" (savaş geçmişi). Bu son sıradadır ve yalnızca bu düşmanları daha önce yenmiş olan paketler alınır. Bot son 20 çalıştırmanın savaşlarını hatırlar.

Botun **asla yedek olarak koymayacağı** şeyler:

- bu odada zaten kaybetmiş olan paket (hatayı tekrarlamamak için);
- "bu düşmanlara kaybeden" paket: geçen sefer onlara karşı savaş düşmanların yüzünden geri alındı ve paketin galibiyet sayısı mağlubiyet sayısından fazla değil. Tek bir başarısızlık **iyi bir paketi bozmaz**: bu düşmanlara karşı beş kez kazanıp bir kez kaybettiyse bot onu yine de alır;
- «Skip» kuralının yasakladığı bir titan içeren paket;
- CP'si zaten **panik eşiğinin altında** olan bir titan içeren paket: bot onu kesin bir ölüme savaşa göndermez;
- geçmişten — hiçbir yerde belirtmediğin (ne paketlerde ne kurallarda) bir titan içeren paket. Geçmişte çoktan silinmiş kuralların paketleri kalır ve bot onları yeniden canlandırmaz.

Bir de "tehlikeli" paketler vardır: geçmiş savaşlara bakılırsa yaralı titanının savaşın sonunu göremeyeceği paketler. Bot bunları **en son çare olarak**, yalnızca daha iyisi yoksa alır. Bunu nasıl belirlediği — aşağıdaki «Yaralı titan» bölümündedir.

Botun şu veya bu paketi neden almadığı günlükte görünür: `[ТАКТИКА] Не беру запасной пак ...` ve nedeni. Yedekler bittiyse ve savaş hala kötüyse — bu bir arıza değil, dürüst bir "başka ne koyacağımı bilmiyorum" durumudur.

### Hatırlamalı mı yoksa değil mi: «Oto: odada …» kuralı

Yedek paket başardı. Bot bunu "bu düşmanlara karşı — bu paketi koy" kuralı olarak kaydeder ve bir dahaki sefere aynı kadroyla karşılaştığında onu hemen koyar. Listede bu kural «Oto: odada …» olarak en başa yerleşir (bölüm 9). Günlükte: `[ТАКТИКА] Запасной пак ... справился. Запоминаю его против этих врагов.`

Ancak bazen **hatırlanmaması gerekir**. Örnek: Araji savaşa %36 sağlıkla girdi ve %5'e düştü. Ana paketin suçu yok: Araji sağlıklı olsaydı savaş normal geçerdi. Bot "bu düşmanlara karşı yedek paketi koy" kuralını kaydetseydi, ana paketin harika bir şekilde hallettiği yerlerde yedek paketi koymaya başlar ve gücünü boşa harcardı. Bu yüzden bot kontrol eder: **«herkeste %100 CP olsaydı savaş kötü geçer miydi?»** Hayır — demek ki düşmanların suçu yok, yardım tek seferlikti, kural oluşturulmaz.

Günlükte bu hemen görünür: `[ТАКТИКА] Враги ни при чём: в бой вошли раненые ...` ve ardından `Правило не запоминаю: это была разовая помощь раненым титанам`.

Diğer üç durumda da hatırlama gerçekleşmez:

- bot düşmanları tanımadıysa (`[ОБУЧЕНИЕ] Враги не распознаны — правило не сохраняю`): "düşmansız" kural her odada tetiklenirdi;
- aynı pakete sahip kuralı anahtarla kapattıysan: kapatılan kurala bot dokunmaz;
- paketi sen kendin seçtiysen: o zaman kararı senin «Paket başardı» penceren verir (bölüm 10).

### Yaralı titan: savaştan sonra değil, önceden yardım

Botun yapabildiği en değerli şey — **kötü savaşı düzeltmek değil, ona izin vermemektir**. Takım seçim ekranındayken titanların sağlığına ve geçmişe bakar: «bu odada bu paketle yapılan savaşlar nasıl bitti?» Bunun için bot, bu paketle yapılan savaşta titan genellikle ne kadar CP **kaybettiğini** saklar (son beş savaşın ortalaması, en az iki savaş gerekir). Girişteki yaralının CP'sinden normal kayıp çıkarıldığında **panik eşiğinin altına düşecekse** — bot risk almaz ve savaştan önce hemen yedek paketi koyar.

Örnek. %36 CP'ye sahip Araji ateşe gidiyor. Buradaki son savaşlarda genellikle %29 civarında kaybetti. Çıkan sonuç: 36 − 29 = %7, panik eşiği ise 40. Savaş neredeyse kesinlikle kötü bitecek ve bot **hemen**, örneğin Moloch'lu bir yedek paket koyar. Bu tek seferlik bir yardımdır, kural hatırlanmaz.

Botun garip görünmemesi için iki püf noktası:

- **Enerji de önemlidir.** Titanın şu anki enerjisi geçmiş savaşlardaki gibiyse (fark %25'ten fazla değilse), bot tahmin için tam olarak bu savaşları alır. İyi enerjiye sahip Araji ateşte az kaybeder, boş enerjiyle çok kaybeder ve tahmin bunu dikkate alır.
- **Tek savaş istatistik değildir.** İki savaştan azsa bot tahmine inanmaz ve hiçbir şeyi değiştirmez.

Kurtarma kurallarının paketlerini («Araji %50'nin altındaysa — Sigurd'u koy», bölüm 9) bot önceden değiştirmez: sen bunları tam olarak yaralı için koydun ve senin planın onun tahmininden daha önemlidir.

### Sağlığa göre kapı

Bot kendisi karar veriyorsa ve koridorda **izin verilen birden fazla kapı** görünüyorsa, sadece sıraya göre değil (bölüm 8, «Kapı önceliği»), yaralılara dikkat ederek seçim yapar:

1. Önce **arkasında yaralının iyileştirileceği** kapıya gider: senin kurtarma kuralın tetiklenecek veya botun kendisi iyileştirme paketi kuracaktır.
2. Geçmiş savaşlara bakılırsa arkasında yaralının tehlikede olduğu kapıyı, başka kapı varsa bot **atlar**.
3. Aksi takdirde her şey zamanki gibi, sırayla gerçekleşir.

`[НАВИГАЦИЯ] Выбрана комната ... по здоровью титанов: ...` satırından görünür. «Skip» kuralı tarafından yasaklanan kapıyı bot yine de asla açmaz. Kapının arkasındaki düşmanları bot henüz görmez, bu yüzden burada kapının temel paketine dayanır.

### «Karma» odada iyileştirme paketi

Yaralı iyileştirilebiliyorsa ve senin iyileştirme kuralın tetiklenmediyse, bot **iyileştirme paketini kendisi kurar**: «Karma» odaya yaralıyı ve gerekirse sağlıklı, enerjisi dolu bir şifacıyı koyar. Teker teker iyileştirirler, ana olanlar yedeklerden önce gelir, panik eşiğinin altında olanlar ise hiç iyileştirilmez. Tüm ayrıntılar («CP şunun altındaysa titanı iyileştir, %» eşiği, «Yaralı için takımdan kim çıkarılsın», Rigel için olan şu Sigurd) — bölüm 8'dedir. Burada önemli olan tek şey: bu da tıpkı tahmindeki yedek paket gibi **tek seferlik bir yardımdır**. Sonrasında kural oluşturulmaz ve sonuçta ayrı sayılır ("iyileştirme paketleri (bot kendisi kurdu)").

### «Altın kurallar»: bot tüm geçmişten öğrenir

Tüm bu kararları bot oyun sırasında alır. «Altın kurallar» sonucunu ise **bir kez, farm başlatıldığında** çıkarır. Bot savaş geçmişini tarar ve aynı düşman kadrosuna karşı **5 veya daha fazla savaş yapıp %80 veya daha fazla kazanan** paketi arar. Böyle bir paketi «Altın: odada …» kuralı olarak kaydeder (bölüm 9). Günlükte: `[ОБУЧЕНИЕ] ...: 'Золотое правило против: ...' — пак ... Сохранено на 1-е место.`

Altın kural olamayacak durumlar:

- odanın ana paketi, kurtarma kurallarının paketleri ve senin «Yedek takımlar» listen (bunlar her savaş için değil, yardım içindir);
- botun kendisinin kurduğu iyileştirme paketleri: bunlara yalnızca titan yaralı olduğu sürece ihtiyaç duyulur;
- senin paketlerinde ve kurallarında bulunmayan bir titan içeren paket;
- zaten bir kuralı bulunan düşmanlara karşı olan paket (senin, «Oto» veya kapatılmış).

«Bot kendisi karar verir» kapalı olduğu sürece altın kural yoktur. Başarısız bir kural mı belirdi? Silmek yerine **anahtarla kapat**: silinen kural bir sonraki çalıştırmada geri gelir, kapatılana ise bot dokunmaz.

### SOS penceresine yanıt vermediysen

Bu artık "bot kendisi karar verir" değil, "bot senin yerine karar verir" durumudur (bölüm 10, «Yanıt vermezsen ne olur»). «Bot kendisi karar verir» kapalıyken de çalışır: zaman aşımına göre («Yanıtsız SOS penceresi süresi, dk») bot savaşı yedek paketle geri alır, kabul eder veya yumuşak duraklatmaya geçer. Her defasında `[ТАКТИКА] Ответа нет N мин. Решаю сам.` yazar, pencereyi kapatır ve Telegram'a mesaj gönderir.

### Botun sen yokken ne yaptığını nasıl anlarsın

Oturumun sonunda «Oturum özeti» bloğunda («Ayrıntılar» düğmesi) ve `[ИТОГ]` satırında sayaçlar bulunur:

- **«geri almalar»**: toplamda kaç savaşın tekrar oynandığı;
- **«bunlardan sizsiz»**: bu geri almalardan kaç tanesini bot sormadan, hem tahmine hem de zaman aşımına göre kendisi yaptı;
- **«iyileştirme paketleri (bot kendisi kurdu)»**: yaralıyı iyileştirme paketiyle kaç kez iyileştirdiği.

Aynı özet Telegram'a da gelir: «Geri almalar: 6 (bot kendisi: 5)». "Sizsiz" kısmı neredeyse tamamsa bot hallediyor demektir. Sayı artıyor ama «Altın kurallar» belirmiyorsa, aynı düşmanlar tekrar tekrar ana paketi bozuyor demektir. Hangi kuralları hatırladığına bakmak için «Kurallar ve müdahaleler» sekmesine göz at ve ana paketi değiştirme zamanının gelip gelmediğini düşün.

> [!warning] Bot gelecekteki savaşı görmek yerine **geçmişe** ve tahmine göre karar verir. Yanılabilir: geçmişin az olduğu ilk günlerde yedek paket rastgele seçilir. «Bot kendisi karar verir» seçeneğinin ilk onlarca odada istendiğinden daha sık geri alması seni korkutmasın. Geçmişte ne kadar çok savaş olursa seçim o kadar isabetli olur.

> [!tip] Nereden başlamalı? Her odada en az bir iki **«Yedek takımlar»** belirle (bölüm 7): böylece bot körlemesine aramaz. «Bot kendisi karar verir» seçeneğini aç ve birkaç gün sadece `[ТАКТИКА]` satırlarını ve «Oturum özeti» kısmını gözlemle. Botun yaptıkları hoşuna gitmiyorsa — anahtarı kapat, her şey SOS pencerelerine geri dönsün.

> [!done] Artık botun sen yokken ne zaman ve nasıl başa çıktığını, neleri hatırladığını ve ne zaman yardıma çağırdığını anlıyorsun. Sırada — Telegram: bilgisayar başında değilken mesajların nasıl alınacağı var. [Sonraki bölüm →](#12)

## Telegram

Bot, sen bilgisayar başında değilken Telegram'dan sana yazabilir: mutfağa gittiğinde, uyumaya yattığında, işe gittiğinde. Savaşın senin yardımına ihtiyacı olursa sohbete bir ekran görüntüsü ve düğmeler gelir. Telefondan düğmeye bastın — bot söylediğini yaptı. Her şey yolunda gidiyorsa bot sessiz kalır: mesajlar **yalnızca sorun olduğunda** ve **oturum sonunda bir kez** gelir.

Gerekli olanlar: Telegram uygulaması ve beş dakika. Yalnızca bir kez ayarlamak gerekir.

> [!note] Telegram isteğe bağlıdır. O olmadan da bot aynı şekilde çalışır, sadece SOS pencerelerini yalnızca bilgisayar ekranında görürsün ve oturum özeti gelmez. Ancak botu gece boyunca açık bırakmayı planlıyorsan ayarla: böylece sorunu sabah değil, anında öğrenirsin.

### Neler hazırlamak gerekiyor

Sana iki şey gerekiyor, ikisi de Telegram'ın kendisinden alınır:

- :send: **Bot jetonu** (programın senin botuna giriş yaptığı anahtar). Bu, sayılardan ve harflerden oluşan uzun bir metindir, örneğin `123456789:AAH…`. Jetonu özel bir bot olan **@BotFather** verir.
- :user: **Chat ID** (sohbet numarası). Bu, Telegram'ın mesajı başkasına değil sana ileteceğini anladığı sayıdır.

> [!warning] Jeton, botunun şifresi gibidir. Kimseye gösterme, ekran görüntülerinde veya e-postalarda (programın yazarına bile) gönderme. «Telegram ayarları» penceresinin ekran görüntüsünü alırken jetonun noktalarla gizlenmiş olduğundan emin ol.

### Adım adım

1. **Kendi botunu oluştur.** Telegram'da **@BotFather**'ı bul (gerçek olanın yanında mavi tık simgesi vardır) ve «Başlat»'a bas. Ona `/newbot` yaz, bir isim (istediğin bir isim, sadece sen göreceksin) ve sonu `bot` ile biten bir kullanıcı adı belirle, örneğin `moi_titan_bot`. BotFather yanıt olarak jeton içeren bir mesaj gönderecektir: onu kopyala.
2. **Sohbet kimliğini (Chat ID) öğren.** **@getmyid_bot** botunu bul, «Başlat»'a bas — sana `Your user ID` satırı ve bir sayı ile yanıt verecektir. Chat ID işte bu sayıdır, sayıyı kopyala. Bu bot yanıt vermiyorsa alternatif bir yol vardır: 1. adımdaki **kendi** botuna herhangi bir kelime yaz, tarayıcıda `https://api.telegram.org/bot<твой токен>/getUpdates` adresini aç (`<твой токен>` yerine kendi jetonunu koy) ve yanıtta `"chat":{"id":` ifadesini bul — hemen ardından gelen sayı Chat ID'dir.
3. **Kendi botunda «Başlat»'a bas.** 1. adımda oluşturduğun botu bul ve «Başlat»'a bas (veya ona `/start` yaz). Bu olmadan Telegram botun sana ilk mesajı atmasına **izin vermez**. Mesajların gelmemesinin en yaygın nedeni budur.
4. **Programdaki pencereyi aç.** Soldaki çubukta Telegram noktasına veya «Temel ve odalar» sekmesindeki **«Telegram'ı ayarla»** düğmesine bas (bölüm 7). «Telegram ayarları» penceresi açılacaktır.
5. **Formu doldur.** «Telegram'a mesaj gönder» anahtarını aç. «Bot jetonu (@BotFather'dan)» alanına jetonu, «Sohbet kimliği (Chat ID)» alanına sayıyı yapıştır. En pratiği alanın yanındaki **«Yapıştır»** düğmesidir: kopyaladığın şeyi alır. Jeton noktalarla gösterilir; göz simgesi doğru yapıştırıldığını kontrol etmen için onu görünür yapar. Alan üzerinde sağ fare tuşu da «Yapıştır» seçeneğini sunar.
6. **Bağlantıyı test et.** **«Telegram'ı dene»** düğmesine bas. Birkaç saniye sonra sağda yeşil «Mesaj gönderildi — Telegram'ı kontrol edin» yazısı görünecek, botunla olan sohbette ise «Bağlantı testi: her şey çalışıyor» mesajı çıkacaktır. Mesaj geldiyse her şey hazır.
7. **Kaydet.** **«Uygula»** düğmesine, ardından sayfanın altındaki **«Ayarları kaydet»** düğmesine bas.

![«Telegram ayarları» penceresi: anahtar, jeton ve Chat ID alanları, «Yapıştır» ve «Telegram'ı dene» düğmeleri](images/telegram_window.png)

> [!warning] «Uygula» yalnızca değerleri «Kural Sihirbazı» sayfasına aktarır, dosyaya **yazılmazlar**. «Ayarları kaydet» düğmesine basana kadar altta «Kaydedilmemiş değişiklikler var» uyarısı yanar ve bot Telegram hakkında hiçbir şey bilmez. Kaydetmeden sayfadan ayrılırsan program «Değişiklikler kaydedilsin mi?» diye sorar.

> [!tip] «Telegram'ı dene», henüz hiçbir şey kaydetmemiş olsan bile şu anda pencerede yazılı olanı kontrol eder. Bu nedenle «Uygula» adımından **önce** dene: hata buldun — düzelttin — tekrar denedin. Test arka planda çalışır, pencere donmaz ve yanıt için 20 saniyeden fazla beklemek gerekmez.

### Test başarısız olursa

Düğmenin altında nedeni gösteren kırmızı «Gönderilemedi: …» satırı belirecektir. En yaygın olanlar:

- **«Jetonu ve sohbet kimliğini doldurun»** — alanlardan biri boş.
- `Unauthorized` — jeton geçersiz: bir karakter eksik, fazladan boşluk var veya tamamı kopyalanmamış. «Yapıştır» düğmesiyle yeniden yapıştır.
- `chat not found` veya `Forbidden` — Chat ID geçersiz ya da **kendi** botunda «Başlat»'a basmadın (3. adım). İki maddeyi de kontrol et.
- **«сбой связи с Telegram»** — internet yok veya Telegram bu bilgisayardan açılmıyor. Bu bilgisayarda Telegram'ın (veya telegram.org sitesinin) çalıştığını kontrol et.

Düzeltmeden sonra bile mesaj gelmiyorsa @BotFather ile yeni bir bot oluştur (1. adım) ve baştan başla: bu, yazım hatası aramaktan daha hızlıdır.

### Telegram'ın açık olduğu nasıl anlaşılır

Soldaki çubukta Telegram düğmesinin yanında bir nokta vardır: fareyle üzerine geldiğinde **«Telegram: açık»** veya **«Telegram: ayarlanmadı»** ipucu görünür. Açık — anahtarın açık olduğu ve her iki alanın da doldurulduğu anlamına gelir. Bu **bağlantı testi değildir**: jetonun çalışıp çalışmadığını yalnızca «Telegram'ı dene» düğmesi gösterir. Aynı durum «Temel и odalar» sekmesinde de görülür: «Telegram'ı ayarla» düğmesinin yanında yeşil «SOS bildirimleri açık» veya gri «Telegram ayarlanmadı» yanar. Nokta, kaydetmeden birkaç saniye sonra kendiliğinden güncellenir.

### Hangi mesajlar gelir

Mesajların dili, program penceresinde seçilen dille aynıdır.

- :swords: **SOS penceresi** — «Yardımın gerekiyor» (veya «Uygun paket yok») başlığı, oyunun ekran görüntüsü ve açıklama: oda, düşmanlar (kime gidiliyordu), neden, can ve enerji çubuklarıyla senin paketin. Altta düğmeler. Bu, bilgisayardaki pencerede sorulan sorunun aynısıdır (bölüm 10).
- :triangle-alert: **Uyarılar** — ne olduğunu ve ne yapılması gerektiğini söyleyen düğmesiz kısa mesajlar. Şunlardır: «Savaş geri alınamadı» (bot hafif duraklatmada, telefon ekranına bak), «Bot takılmış gibi görünüyor» (5 dakika oda geçilmedi) ve savaş başlatılamadığında gelen benzer bir mesaj (muhtemelen oyun sunucusuyla bağlantı yok), «Bilgisayar ekranı kilitli» (bot bir dakikadan uzun süredir oyunu görmüyor; bilgisayarın kilidini aç, kendisi devam edecektir) ve «Yanıt vermedin — bot kendisi karar verdi».
- :chart-no-axes-column: **Oturum özeti** — bot durduğunda: ne kadar zaman, oda, kat ve titanit geçtiği, geri almalar ve SOS pencereleri olup olmadığı («bot kendisi: {n}» — senin müdahalen olmadan yaptığı geri almalardır), en uzun süren odalar. Bot bir hatayla durduysa başlıkta «Bot bir hatayla durdu» ve nedeni yazacaktır.

Özet her durmada gelir: hedefe ulaştığında, Ctrl+Q veya Ctrl+Shift+Q tuşlarına bastığında, bot bir hatayla durduğunda. «DUR F10» ve «Durdur ve kapat» (bölüm 6) sonrasında **gelmez**, çünkü bunlar botu anında sonlandırır.

### SOS mesajının altındaki düğmeler

Telegram'da bunlara tıpkı bilgisayardaki pencerede olduğu gibi bas:

- **«Geri al (Pak kur)»** (yeşil). Bot şunu gönderecektir: «Напишите имена 3-5 титанов в чат». Bunları virgülle veya boşlukla sohbete yaz, örneğin `гиперион, сигурд, нова` veya kısaca ilk üç harfiyle: `гип сиг нов`. Bot kimi tespit ettiğini yanıtlayıp «Все верно?» diye soracaktır: **«Paketi onayla»** geri almayı başlatır, **«Başka yaz»** yeniden girmene izin verir. 3–5 titan bulamadıysa bot kaç tane tespit ettiğini söyleyecek ve tekrar yazmanı isteyecektir.
- **«Elle oyna»** (mavi). Bot hiçbir şeye basmaz ve odayı kendin bitirene kadar bekler.
- **«Yoksay (Devam et)»** (gri). Savaşı olduğu gibi kabul etmek ve devam etmek.
- **«Botu durdur»** (kırmızı). «Geri al» yerine, savaş manuel yürütüldüğünde (Angus ultimatomu) veya uygun paket olmadığında bu gösterilir. «Uygun paket yok» penceresinde «Devam et» düğmesi yoktur.

Senin seçtiğin paket başardığında, «Paket başardı» sorusu Telegram'a iki düğmeyle gelir: **«Onayla ve Kaydet»** (paketi kural olarak hatırla) ve **«Geri Al ve Tekrar Dene»** (başka bir tane yaz). Bu soru sohbete yalnızca paketi sen de Telegram'dan gönderdiysen gelir.

Bastıktan sonra mesajın altında tek bir yeşil «Seçildi: …» düğmesi kalır, diğerleri kaybolur. Yalnızca **bir kez** yanıt verilebilir: bot eski mesaj üzerindeki tıklamaları dinlemez. Sohbette yanıt verdin — bilgisayardaki pencere kendiliğinden kapanır, bilgisayarda yanıt verdin — bot Telegram'dan yanıt beklemeyi bırakır.

> [!tip] Sen telefonu ararken bot kendisi mi karar verdi? Sorun değil. «Yanıt vermedin — bot kendisi karar verdi» mesajı gelir ve eski sorudaki düğmeler artık hiçbir şey yapmaz. Botun seni ne kadar bekleyeceği «Otomatik taktik» kısmında ayarlanır (bölüm 8, «Yanıtsız SOS penceresi süresi, dk»).

### İnternet kesilirse

Bot durmaz ve Telegram'ı beklemez: mesaj arka planda gönderilir. Bağlantı nedeniyle gönderilemediyse **30 saniye, 1, 2, 5 ve 10 dakika** (yaklaşık 18 dakika) sonra tekrar dener, günlükte ise `Сообщение в Telegram не ушло (...). Пробую снова через N с.` ve sonunda `Сообщение в Telegram: отправлено с N-й попытки` satırları görünür. SOS penceresi için de aynısı geçerlidir: bilgisayar ekranında kalır ve bağlantı geri geldiğinde soru Telegram'a gider. Oturum özetini bot daha kısa aralıklarla tekrarlar (10 ve 30 saniye sonra), çünkü bundan sonra kapanır. Telegram'ın kendisinden kaynaklanan hataları (geçersiz jeton) bot tekrarlamaz: bunların ayarlarda düzeltilmesi gerekir.

> [!note] Bot senden «istediğin an» komut kabul etmez (sohbetten durdurma, duraklatma yapma). Telegram yalnızca botun kendisinin sorduğu sorulara yanıt verir. SOS mesajının altındaki «Botu durdur» düğmesi dışında sohbetten botu durduramazsın.

> [!done] Telegram ayarlandı ve artık nerede olursan ol bot seni çağırabilecek. Sırada istatistikler var: günlere göre ne kadar oda, kat ve titanit toplandı. [Sonraki bölüm →](#13)

## İstatistikler

«İstatistikler» sayfası «ne kadar oynadım?» sorusuna yanıt verir: bir hafta, bir ay ve tüm zamanlar boyunca ne kadar titanit, oda, kat ve titan iksiri toplandı. Soldaki çubukta **«İstatistikler»** düğmesiyle açılır, üstte «Etkinlik istatistikleri» yazar.

Bot bu sayıları oyun ekranından okumaz, **kendisi hesaplar**. Bir odayı geçti — kaydetti: **6 titanit ve 25 iksir**, sonuç penceresinde «x2» simgesi varsa — **12 titanit ve 50 iksir**. Kaydetme noktasında ödülü aldı — katı kaydetti. Elle oynayarak geçtiğin ve botun hesaba kattığı odayı da (bölüm 10) kaydeder. Sonuçlar `bot_data/stats.json` dosyasında bulunur ve «oyun günlerine göre» saklanır.

> [!note] **Oyun günü** gece yarısı değil, «Kural Sihirbazı» alanında belirlediğin sıfırlama saatinde başlar (varsayılan olarak 5:00, bölüm 7). Bu nedenle botun gece 02:30'da topladığı her şey **dünkü** güne yazılır: oyunda bu saatte hâlâ dünkü gün devam etmektedir. Sabah «Titanit (bugün)» gece oynamış olmana rağmen sıfırsa, olması gereken budur.

### Sayfada neler var

Sol üstte bir ipucu, sağda **«Dönem»** seçimi, bunların altında beş kart, grafik ve en altta «Elle düzeltme» bulunur.

- :calendar: **Dönem** — «7 gün», «14 gün», «30 gün» veya «Tüm zamanlar». Seçili olan mavi yanar. İlk açılışta «14 gün» ayarlıdır.
- :gem: **«Titanit»** — dönem toplamı.
- :calendar: **«Titanit (bugün)»** — yalnızca mevcut oyun günü için. Döneme bağlı değildir.
- :flask-conical: **«Titan iksiri»**, :door-open: **«Oda»** ve :layers: **«Kat»** — dönem toplamları.

Karttaki 100.000'e kadar olan sayılar tam olarak yazılır (`98 540`), uzun olanlar ise kısaltılır: `105.5K` yüz beş buçuk bin, `1.24M` bir milyon iki yüz kırk bindir. Fareyi kartın üzerine getirirsen tam sayı görünür. «Tüm zamanlar» sütunların toplamını değil, dosyadaki genel sayaçları alır; bu nedenle sütun sayısı çok olsa bile kartlar geçmişle uyuşur.

> [!tip] Sayfa sayıları oyun esnasında değil, **her açılışta** okur. Bot çalışıyor ama sayılar değişmiyor mu? Başka bir sayfaya geçip geri dön.

![«İstatistikler» sayfası: kartlar, günlük grafik ve bilgi kutusu olan seçili sütun](images/stats_page.png)

### Grafik: sütunlar ve tıklamalar

«Titanit etkinliği» başlığının altında sütunların nasıl toplandığını gösteren bir açıklama bulunur: «günlük», «haftalık» veya «aylık». Grafiğin karmaşıklaşmaması için sütun sayısı en fazla on beştir:

- **7 ve 14 gün** — sütun başına bir gün.
- **30 gün** — sütun başına bir hafta (pazartesiden pazara; uç haftalar eksik olabilir — yalnızca döneme denk gelen günler yer alır).
- **«Tüm zamanlar»** — veriler iki haftadan az olduğu sürece günlük; ardından haftalık ve hafta sayısı on beşi geçtiğinde aylık.

Solda kesikli çizgili ızgaraya sahip bir ölçek vardır, ölçekteki sayılar kısadır (`3.6K`, `140K`). Sütun altındaki yazılar sığmazsa birer atlayarak gösterilir; sonuncu (bugünkü) her zaman görünür. Oyun oynanmayan gün boş bir yerdir, sütun yoktur. Verisi olmayan bir dönem için grafik «Bu dönem için veri yok» diyecektir.

1. **Fareyi sütunun üzerine getir.** Üzerinde kesin titanit sayısı belirecektir. Bu sadece bir ipucudur, hiçbir şey değişmez.
2. **Sütuna tıkla.** Daha parlak hale gelecek, diğerleri soluklaşacak, yanında tarih ve sayı bulunan bir kutu belirecektir. Kutuda haftanın titaniti **günlük**, ayın titaniti ise **haftalık** olarak dökümlenir. Sol üstte mavi bir yazı yanar, örneğin «Gösterilen gün: 19.10.2026 · bugün» (veya «Gösterilen hafta», «Gösterilen ay»).
3. **Kartlara bak.** Artık bu sütunun sayılarını gösterirler: gün, hafta veya ay için titanit, iksir, oda ve katlar. «Titanit (bugün)» mevcut gün olarak kalır.
4. **Özetlere geri dön.** Aynı sütuna tekrar veya çarpı işaretli (✕) mavi yazıya tıkla. Dönemi değiştirirsen seçim de sıfırlanır.

### Tablo

Grafiğin sağ üstündeki **«Tablo»** düğmesi aynı sütunları bir liste halinde gösterir: «Tarih», «Titanit», «Oda», «Kat», «Titan iksiri». En yeni tarihler üstte, en altta **«Toplam»** satırı bulunur. Satır da tıklanarak seçilebilir ve kartlar onun sayılarını gösterir. Düğme bu sırada **«Grafik»** şekline dönüşür ve görseli geri getirir. Tablo, tüm günler için aynı anda kesin sayılar gerektiğinde kullanışlıdır.

![Tablo: tarihler, titanit, odalar, katlar ve iksir, altta «Toplam»](images/stats_table.png)

### Elle düzeltme

Bot kendi aritmetiğine göre hesaplar (oda başına 6 veya 12 titanit), ancak oyundaki sayı farklı olabilir: kendin oynadın, bot kapalıydı, program sabahın erken saatlerinden itibaren çalıştırılmadı. İstatistiklerin oyunla eşleşmesi için **«Elle düzeltme»** kartı vardır.

1. **Günü seç.** Listede — «Bugün», «Dün» ve beş geçmiş gün daha, toplam yedi gün vardır. Daha eski bir gün mü lazım? «7 gün» veya «14 gün» dönemini seç ve onun sütununa tıkla: bu gün listeye kendiliğinden eklenecektir (haftalık ve aylık sütunda eklenmez — yalnızca günlükte).
2. **Oyundaki toplam sayıyı gir.** «Günlük titanit» alanına — «ne kadar ekleneceği» değil, oyunda **bütün gün için** gösterilen sayı yazılır. Seçilen gün için şu anda kayıtlı olan değer zaten görünür.
3. **«Uygula» düğmesine bas** (veya alanda Enter'a bas).

Örnek. Bot gün için 90 titanit kaydetti, oyunda ise aynı gün için 150 var. Sen **150** giriyorsun — program 60'lık farkı ekler ve gerisini kendisi yeniden hesaplar: yaklaşık **+5 oda, +1 kat ve +250 iksir**. Bu bir tahmindir: günün ilk 10 odasının 6'şar titanit, kalanların ise 12'şer titanit verdiği varsayılır. Farklı oynadıysan odalar ve katlar gerçeğinden biraz farklı olabilir, ancak titanit tam sendeki gibi olacaktır.

Her şey başarılı olduğunda altta «19.10.2026 titaniti: 150» bildirimi belirecek, ana sayfadaki günlüğe ise `[СТАТИСТИКА] Данные за 2026-10-19 синхронизированы! Дельта: +60 тит., +5 комн., +250 зелий.` satırı düşecektir. Kayıtlı olandan daha az girdiysen sayılar azalacaktır.

Neler ters gidebilir:

- **«0 veya daha büyük tam sayı girin»** — alanda harfler, virgül, eksi var veya boş. Alan kırmızı renge dönecektir.
- **«Bot bu gün kendisi 90 topladı, daha azı girilemez»** — botun **kendisi** topladığı miktardan daha azını yazamazsın, çünkü bu dürüstçe kaydedilmiştir. Sayı ancak bu değere kadar düşürülebilir.
- **«Bu gün için zaten bu kadar kayıtlı»** — aynı sayıyı girdin, değiştirilecek bir şey yok.

> [!warning] «Uygula» sayıları **anında** `bot_data/stats.json` dosyasına yazar. «Kural Sihirbazı» bölümünde olduğu gibi (bölüm 7) burada «Ayarları kaydet» düğmesi yoktur ve gerek de yoktur. Düzeltmeyi bir düğmeyle iptal edemezsin, ancak eski sayıyı tekrar girmene hiçbir şey engel olamaz.

> [!note] Düzeltme **yalnızca istatistikleri** değiştirir. Ana sayfadaki «Oturum özeti» ve oturum hedefi (bölüm 4) ayrı olarak, botun bu çalıştırmada topladıklarına göre hesaplanır ve «İstatistikler» sayfasından bağımsızdır.

### «Sıfırla»: tüm geçmişi sil

**«Sıfırla»** düğmesi (çöp kutulu, «Elle düzeltme» kartının sağında) tüm istatistikleri sıfırlar: tüm günler için titanit, odalar, katlar ve iksir. Yanlışlıkla mı bastın? Hiçbir şey olmaz: önce program «İstatistikler sıfırlansın mı?» diye soracak ve bunun geri alınamayacağını hatırlatacaktır. Penceredeki «Sıfırla» düğmesiyle onaylarsın, «İptal» düğmesiyle reddedersin. Sıfırlamadan sonra «İstatistikler sıfırlandı» bildirimi görünecek ve günlükte `[СТАТИСТИКА] Вся история полностью сброшена!` satırı yer alacaktır.

Yalnızca istatistikler silinir. Kurallar, paketler, ayarlar, `profile.yml` ve savaş günlükleri kalır. Bot o anda çalışıyorsa devam eder ve sıfırdan saymaya başlar, oturum hedefi bozulmaz.

> [!tip] «Deneme amaçlı» sıfırlamak mı istiyorsun? Önce bir kopya kaydet: programı kapat ve `bot_data/stats.json` dosyasını başka bir yere kopyala (program klasörünü «Hakkında» sayfasındaki «Bot klasörü» düğmesi açar). Dosyayı geri koyarak geçmişi geri yükleyebilirsin.

### Sıkça sorulan sorular

- **Sayılar oyunla uyuşmuyor.** Bot ekranı okumaz, hesaplar: oda başına 6 veya 12 titanit. Başka kaynaklardan titanit aldıysan oyun daha fazlasını gösterir. Karşılaştır ve «Elle düzeltme» ile düzelt.
- **Bugünkü gün boş ama ben oynadım.** Sıfırlama saatini kontrol et: o saate kadar bot «düne» yazar (yukarıdaki «Oyun günü» kısmına bak). «Kural Sihirbazı» alanında saati değiştirdin mi? Sayfanın da bunu algılaması için programı yeniden başlat.
- **Sütun sayısı az ama dönem büyük.** Botun çalışmadığı günler grafikte boştur. «Tüm zamanlar» ve aylar varsayılan olarak grafiği sıkıştırır: belirli günleri görmek için «7 gün» veya «14 gün» seçeneğini al.
- **Günlükte `[СТАТИСТИКА] ВНИМАНИЕ: Файл stats.json поврежден`.** Geçmişi içeren dosya okunamadı (örneğin bilgisayar kayıt anında kapatıldı). Bot sıfırdan yeni bir istatistik başlatır ve dosyanın üzerine yazar. Eski geçmiş önemliyse önceden kopyasını al.

> [!done] Artık sayıları nasıl okuyacağını, dönemleri nasıl değiştireceğini, istatistikleri oyunla nasıl karşılaştıracağını ve nasıl sileceğini biliyorsun. Sırada — bir şeyler ters giderse ne yapılacağı var. [Sonraki bölüm →](#14)

## Bir şeyler ters giderse

İyi haber: Bot çoğu sorundan kendi kendine çıkabilir. Takıldıysa etrafa bakar ve yeniden başlar. İnternet kesildiyse bekler. Bilgisayarı kilitlediysen bekleyip devam eder. Sen sadece o **kendi istediğinde** (duraklatıldığında, Telegram'a yazdığında) veya hiçbir şeye tıklamadığında ve günlükten sebebini anlayamadığında lazımsın. Bu bölüm her iki durum hakkındadır: Bot sen yokken ne yapar, arızanın nerede olduğunu nasıl anlarsın ve neye basmalısın.

Her durum için kural: **panik yapma ve acele etme**. Botu durdurmaktan, yeniden başlatmaktan ve tekrar çalıştırmaktan korkma: İstatistikler, takımlar, kurallar ve ayarlar dosyalarda saklanır ve hiçbir yere kaybolmaz.

### Bir şeylerin ters gittiği nasıl anlaşılır

- :triangle-alert: Ana sayfadaki günlükte bulunan **«Hatalar» hapındaki kırmızı sayı**. Sadece arızaları saymaz: Uyarılar da buraya düşer (örneğin «oyun penceresinin üzeri kapalı»). Sayının kendisi korkmak için bir sebep değildir, hapı açıp satırları okuman gerekir.
- :pause: **Sen duraklatmaya basmadığın halde «Duraklatıldı» durumu ve yeşil «Devam et» düğmesi.** Bu, botun kendi kendine durduğu ve seni beklediği anlamına gelir. Günlükte bu sırada nedeni gösteren `[ВНИМАНИЕ] Бот на мягкой паузе: ...` satırı yer alır.
- :send: **Telegram mesajı** (ayarlanmışsa, bölüm 12): «Bot takılmış gibi görünüyor», «Savaş geri alınamadı», «Bilgisayar ekranı kilitli».
- :eye: **Sessizlik.** Günlükte bir dakika veya daha uzun süre yeni satır görünmüyor ve oyunda hiçbir şey olmuyor. Bu da bir belirtidir: Aşağıdaki «Sık karşılaşılan durumlar» bölümüne bak.

Günlükte bir soruna işaret eden etiketler:

- `[СТОРОЖ]` — Bot takıldığına karar verdi ve kendisi yeniden başladı.
- `[СЕТЬ]` — Oyun sunucusuyla bağlantı yok gibi görünüyor.
- `[ЭКРАН]` — Bilgisayar ekran görüntüsü alınmasına izin vermiyor (kilitli).
- `[ОТКАТ]` — Savaş geri alma adımları ve hataları (bölüm 10).
- `[ВНИМАНИЕ]` — Bot dikkat istiyor: Duraklatma, kapalı oyun penceresi.
- `[ОШИБКА]` — Bir şey bozuldu; yanında ne olduğu yazıyor.
- `[ADB]` ve `[VISION]` — Telefonla bağlantı ve tıklamalar.

### Bot kendi kendine ne yapar

Burada hiçbir şeye basmıyorsun. Bunun normal olduğunu ve oturumu bozmadığını bilmen yeterli.

- :gauge: **Takılma: Tek bir oda bile geçilmeden geçen 5 dakika.** Bu bir «bekçi» kontrolüdür (botun takılıp takılmadığını izleyen kontrolün adı). Bot `[СТОРОЖ] Бот 5 мин не прошёл ни одной комнаты ... Тревога 1 из 3.` yazar, ekran görüntüsü kaydeder, Telegram'a mesaj gönderir (ayarlanmışsa) ve **«akıllı başlatma»** yapar: Ekranı yeniden inceler ve nereden devam edeceğine karar verir. İşe yaramadıysa 5 dakika sonra tekrar alarm verir. **Üst üste üçüncü alarm** (yani odasız geçen yaklaşık 15 dakika) — Bot esnek duraklatmaya geçer ve seni bekler. Botun seni beklediği süre (SOS penceresi, duraklatma, oyunun üzerindeki başka bir pencere) bekçi tarafından sayılmaz.
- :activity: **Bir yerde takıldı.** Takım seçme ekranı 30 saniye içinde görünmediyse veya sonuç penceresi 3 dakika içinde çıkmadıysa, `[СТОРОЖ] Зависание: ...` yazılır, ekran görüntüsü alınır ve Telegram alarmı olmadan aynı akıllı başlatma yapılır.
- :globe: **Savaş başlamıyor (büyük olasılıkla oyun sunucusuyla bağlantı yok).** «Otomatik» düğmesine basıldı ama savaş yok. Bot hemen iki kez daha dener, ardından bekler ve tekrar dener: 30 saniye, 1, 2, 4 ve 8 dakika sonra. Tüm bunlar günlükte `[СЕТЬ] Бой не начался N раз(а) подряд ... Жду N с и пробую снова.` şeklinde görünür. Bu da işe yaramadıysa (yaklaşık 15 dakika): Ekran görüntüsü, «Bot takılmış gibi görünüyor» mesajı ve esnek duraklatma.
- :rotate-ccw: **Savaş geri alma sırasında bağlantı koptu.** Bot pes etmez, **oyunu 15 dakikaya kadar bekler**: `[ОТКАТ] Бой не загрузился ... Не сдаюсь` yazar, ekran görüntüsü kaydeder ve dakikada bir `Всё ещё жду игру` bildirir. Bağlantı geri geldiyse geri alma işlemi kendiliğinden tamamlanır (`Игра снова откликается`). 15 dakika içinde gelmediyse «Savaş geri alınamadı», Telegram mesajı ve duraklatma.
- :monitor: **Bilgisayar kilitlendi (Win+L) или ekran kapandı.** Windows ekran görüntüsü alınmasına izin vermez ve bot hiçbir şey göremez. Bot **çökmez**, her 2 saniyede bir tekrar dener: `[ЭКРАН] Не удаётся сделать снимок экрана ... Похоже, ПК заблокирован`. Bir dakikadan uzun sürerse tek bir «Bilgisayar ekranı kilitli» mesajı atılır. Kilidi açtığında — `[ЭКРАН] Снимок экрана снова работает`, bot kendiliğinden devam eder.
- :layers: **Oyun penceresinin üzeri başka bir pencereyle kapandı.** Bot tekrar ana pencere olmasını bekler (`[ВНИМАНИЕ] Окно игры перекрыто ... Бот ждет фокуса`). Oyun penceresine tıkla, devam edecektir. Neden böyle olduğu bölüm 5'te anlatılmıştır.
- :target: **Tıklama ulaşmadı.** Tıklamadan 4 saniye sonra экран değişmediyse bot tekrar tıklar: `[VISION] Клик по '...' не зарегистрирован сервером ... Повторяю...`. Nadiren çıkan bu tür satırlar normaldir: Telefon bazen «düşünür».
- :smartphone: **Kablo ile telefon bağlantısı anlık koptu.** Bot `[ADB] Постоянное соединение с телефоном оборвалось ... Переподключусь при следующем нажатии` yazar ve bir sonraki tıklamada yeniden bağlanır.
- :send: **İnternet nedeniyle Telegram mesajı gönderilemedi.** Bot bunu daha sonra tekrarlar (bölüm 12) ve çalışmaya devam eder.

> [!note] Botun oturum boyunca kaç kez takıldığı günlükteki `[ИТОГ]` bloğunda görünür ("зависания" kelimesini içeren satır). Nadir durumlar sorun değildir. Çok fazlaysa nedeni aşağıdaki «Sık karşılaşılan durumlar» bölümünde ara.

### Bot kendiliğinden duraklatıldı: Ne yapılmalı

Durdu, çünkü sensiz devam edemez. Sırayla hareket et:

1. **Oyun ekranına bak.** `HeroWarsBot_Arena` penceresi botun nerede takıldığını gösterir: Sonuç penceresi, savaş, duraklatma menüsü, yükleme "mantarı" veya beklenmeyen bir şey (başka pencere, reklam, oyun isteği).
2. **Günlüğün son satırlarını oku.** «Hatalar» hapını aç ve en alta bak: Orada botun neden durduğu yazmaktadır (`[СТОРОЖ]`, `[ОТКАТ] ОШИБКА`, `[СЕТЬ]`).
3. **Oyunu Zindan коридорuna geri getir.** Fazla şeyleri kapat, savaşın bitmesini veya yüklenmesini bekle ve kapı ile bayrağın olduğu ekрана gel.
4. **«Devam et» düğmesine bas.** Bot yeniden etrafa bakar (akıllı başlatма) ve devam eder.

> [!note] Başarısız geri alma sonrasındaki duraklatma şöyle de olabilir: Manuel savaş bitmiştir, sonuç penceresindeki «Yeniden» düğmesi artık yoktur ve geri alınamaz. Sonuç penceresi ekranda kalır — hiçbir şeyi kapatmaya gerek yoktur, «Devam et» düğmesinden sonra bot kendisi «TAMAM» düğmesine basar. Bu pencerede kimin hayatta kaldığına bak.

> [!tip] Bot her küçük şey için değil, deneyip başaramadığında duraklatmaya geçer. Bu yüzden «Devam et» düğmesine basmadan önce **tam olarak neyin** ters gittiğini anla. Neden devam ediyorsa (интернет yok, oyun kapalı), bot birkaç dakika sonra tekrar duracaktır.

### Sık karşılaşılan durumlar: Neye bakılmalı ve ne yapılmalı

**Bot hiçbir şeye basmıyor ve günlük sessiz.** Büyük olasılıkla oyunu görmüyor veya oyunda hiçbir şey bulamıyor. Sırayla kontrol et:

1. **Oyun penceresi yerinde.** `HeroWarsBot_Arena` adındadır, simge durumuna küçültülmemiş ve kapatılmamıştır. Pencere yoksa bot bunu yazmaz, her yarım saniyede bir sessizce kontrol eder. Bu yüzden pencere kaybolduğunda günlükteki sessizlik normaldir. «Telefonu bağla» düğmesine bas: Pencere yeniden açılır.
2. **Pencere boyutu değişmedi.** Bot pencereyi başlatma sırasında bir kez ölçer ve sonrasında bu ölçüyü kullanır. Başlattıktan sonra pencereyi genişlettiysen, tam ekran yaptıysan veya taşıdıysan botu durdur (F10), «Oyun penceresinin boyutunu sıfırla» düğmesine ve ardından tekrar «Farmı başlat» düğmesine bas. Ayrıntılar bölüm 3'te.
3. **Oyunda Zindan koridoru açık**, menü, mağaza, başka bir etkinlik veya reklam penceresi değil.
4. **Program dili oyun diliyle eşleşiyor** (sol çubuğun altındaki iki harf). Aksi takdirde bot düğmeleri tanıyamaz.
5. **Oyun penceresini hiçbir şey engellemiyor.** Oyunun üzerindeki herhangi bir pencere botun odak beklemesine neden olur.

**Bot «görüyor» ve basıyor ama oyunda hiçbir şey olmuyor.** Günlükte üst üste "Клик по ... не зарегистрирован сервером ... Повторяю..." satırлары yer alıyor. Bu, tıklama komutunun telefona ulaşmadığı anlamına gelir. Kontrol et:

- Telefondaki **her iki** hata ayıklama ayarı da açık: «USB hata ayıklaması» ve «USB hata ayıklaması (güvenlik ayarları)». İkincisi olmadan görüntü vardır ama tıklamalar çalışmaz (bölüm 2).
- Telefonun kilidi açık, kablo sıkıca takılı. Başka bir USB bağlantı noktası dene.
- Komut satırında `adb devices` telefonun yanında `unauthorized` veya boş liste değil `device` gösteriyor.
- İşe yaramadıysa: Botu durdur, «scrcpy'yi yeniden başlat» düğmesine, ardından «Farmı başlat» düğmesine bas.

**Bot yanlış yere basıyor или titanları karıştırıyor.** En yaygın nedeni oyun penceresinin yanlış boyutta olması veya başlatıldıktan sonra dokunulmasıdır (yukarıdaki boyut sıfırlama işlemi). Boyut doğru ama bot yine de hedefi kaçırıyorsa, o anın ekran görüntüsünü kaydet ve günlükle birlikte yazara gönder (aşağıda).

**Program penceresi «yanıt vermiyor».** Program kendi kendini izler: Pencere 5 saniye boyunca yanıt vermezse kodun hangi satırında takıldığını bir dosyaya kaydeder. Dosya `bot_data/debug/` klasöründe yer alır ve `ui_freeze_<дата>_<время>.txt` olarak adlandırılır. Ne yapılmalı:

1. **Bir dakika bekle.** Pencere genellikle kendiliğinden kendine gelir: Yoğun bir işlemle meşguldür.
2. **Bot pencereden ayrı çalışır.** Onu durdurman gerekiyorsa ve düğmeler yanıt vermiyorsa Ctrl+Shift+Q tuşlarına bas: Bu tuşu program penceresi değil botun kendisi dinler (bölüm 6).
3. **Kendine gelmediyse pencereyi çarpı işaretinden kapat.** Kapanmıyorsa Görev Yöneticisi (Ctrl+Shift+Esc) aracılığıyla kapat. Ardından orada listede `HeroWarsBot.exe` veya `python` kalıp kalmadığına bak: Kalmışsa onu da kapat, aksi takdirde bot pencere olmadan oyunda tıklamaya devam eder.
4. **`ui_freeze_...txt` dosyasını yazara gönder.** Orada sadece dosya adları ve program kod satırları vardır, kişisel hiçbir şey yoktur.

**Sen durdurmadığın halde bot durdu.** Ana sayfadaki «Oturum özeti» kartını aç («Ayrıntılar» düğmesi) ve nedene bak:

- «scrcpy penceresi kapandı» — Oyun penceresi kapatıldı veya kayboldu (kablo çekildi, telefon kilitlendi). Telefonu yeniden bağla.
- «bot çalışmayı bitirdi» — İşlem sebepsiz yere sona erdi. Telegram varsa özet oraya gelmiştir; yoksa günlükte `[ОШИБКА] Бот остановился из-за ошибки:` satırını ve altındaki metni ara.
- «Kurallarda takım bulunamadı» — Oda için ana takım ayarlanmamış. «Kural Ustası» → «Temel ve odalar» sekmesini aç ve dört odanın tümünde takımı ayarla (bölüm 7).
- «Hata: ...» — Program çöktü. Günlüğü yazara gönder (aşağıda).

> [!warning] «DUR» (F10) düğmesinden sonra bot `[ИТОГ]` bloğunu yazmaya vakit bulamaz ve Telegram'a özet göndermez: Anında sonlandırılmıştır (bölüm 6). Bu bir arıza değildir.

**Telefon «uykuya daldı» veya ekran kapandı.** Program scrcpy'yi «telefonun uykuya geçmesini engelle» moduyla (`--stay-awake`) çalıştırır. «Telefon ekranını kapat» düğmesi sadece **ekranı** kapatır: Oyun devam eder ve bot her şeyi görür. Ancak telefon kilitlendiyсе veya kablo bağlantısı kesildiyse, oyun penceresinde kilit ekranı veya boşluk olur ve bot hiçbir şey bulamaz. Telefonun kilidini aç, kabloyu kontrol et ve «scrcpy'yi yeniden başlat» düğmesine bas.

**Telegram mesajları gelmiyor.** Büyük olasılıkla kendi botunda «Başlat» düğmesine basılmadı veya jeton/Chat ID yanlış — ayrıntılar bölüm 12'de. Bot bu sırada normal şekilde çalışır.

**Bot yanlış titanları koyuyor или istediğin gibi karar vermiyor.** Bu bir arıza değil, kurallardır: 7–11 bölümlerini incele (takımlar, eşikler, kurallar, «Bot kendisi karar verir»). Botun kararı her zaman günlükteki `[ТАКТИКА]` satırlarında bulunabilir.

### Günlükler ve ekran görüntüleri nerede bulunur

«Hakkında» sayfasındaki **«Bot klasörü»** düğmesi programın çalıştırıldığı klasörü açar. İçinde botun kendisinin oluşturduğu dosyalar bulunur. Gerekli şeyler `bot_data` klasörünün içindedir:

- :file-text: `bot_data/logs/bot_log_<дата>_<время>.txt` — **Botun her çalıştırılmasının tam günlüğü.** Bot bunu kendisi satır satır yazar, bu yüzden program çöktükten veya kapatıldıktan sonra bile kalır. İnceleme için ana dosya budur.
- :gauge: `bot_data/logs/timings_<дата>_<время>.csv` — Her bir odanın ne kadar sürdüğü (koridor, kurulum, savaş, sonuç).
- :swords: `bot_data/logs/battle_log_<дата>_<время>.jsonl` ve `battle_log.csv` — Savaş geçmişi: Oda, düşmanlar, takım, sonuç, titanların Canı ve enerjisi.
- :image: `bot_data/debug/` — **İnceleme için ekran görüntüleri.** Adı ne olduğunu söyler: `stuck_...` — Takılma, `sos_...` — SOS penceresi, `rollback_wait_...` — Geri alma sırasında oyunu bekledi, `rollback_fail_...` — Geri alma başarısız, `start_fail_...` — Savaş başlamadı, `result_unreadable_...` — Sonuç penceresi okunamadı. Devamında oda numarası, element ve zaman yer alır (`stuck_комната12_water_2026-10-19_14-03-21.png`). Program penceresi takıldıysa `ui_freeze_...txt` de oradadır.

> [!warning] Bot eski dosyaları kendisi temizler: Başlatıldığında `bot_data/logs/` klasöründe her türden en yeni 20 dosya (`.txt`, `.jsonl`, `timings_*.csv`) ve `bot_data/debug/` klasöründe en yeni 50 ekran görüntüsü kalır. Sorunlu bir geceden sonra günlükleri saklamak istiyorsan, **botu bir sonraki çalıştırmadan önce bunları başka bir yere kopyala**. «Günlüğü kaydet» düğmesiyle varsayılan klasöre kaydettiğin günlük de aynı şekilde silinir: Başka bir yere, örneğin masaüstüne kaydet.

> [!warning] `profile.yml` dosyasını (ayarların ve Telegram) ve `bot_data` klasörünü silme ve yeniden adlandırma: İçinde istatistikler, botun hatırladığı kurallar ve savaş geçmişi vardır. Yalnızca `bot_data/debug` ve eski günlükler silinebilir, o da sadece ihtiyaç duyulmadığında.

### Günlük yazara nasıl gönderilir

Sorun çözülemediğinde en hızlı yol, ne olduğunu yazara göndermektir.

1. **Ne zaman olduğunu hatırla.** Zaman ve yaklaşık oda sayısı (`[СТАТИСТИКА] Комнат: N`), uzun günlükte gerekli yeri bulmaya yardımcı olur.
2. **Dosyaları bul.** Günlük — o geceye ait `bot_data/logs/bot_log_...`, ekran görüntüleri — adında benzer zaman olan `bot_data/debug/` klasöründen, pencere takıldığında ise ayrıca `ui_freeze_...txt`.
3. **Ana sayfadaki günlüğün altındaki «Günlüğü yazara gönder» düğmesine bas.** Program şu an günlükte olanları kaydetmeyi teklif eder (bu `gui_log_...txt` dosyasıdır), ardından e-postanı yazarın adresine hazırlanmış hazır bir mektupla açar.
4. **Dosyaları e-postaya kendin ekle.** Program e-postaya dosya ekleyemez: Sadece e-postayı açar. `gui_log_...txt` veya `bot_log_...txt` dosyasını, ekran görüntülerini ve (varsa) `ui_freeze_...txt` dosyasını ekle.
5. **Kelimelerle açıkla:** Ne yaptın, ne bekledin, ne gördün, ne zaman oldu. Tek bir "çalışmıyor" cümlesi yazara neredeyse hiç yardımcı olmaz.

> [!warning] `profile.yml` ve `bot_data/profile.yml.bak` dosyalarını **asla ekleme**: Bunlar Telegram botunun jetonunu içerir. «Telegram ayarları» penceresinin ekran görüntüsünü de yalnızca jeton gizlenmiş şekilde (noktalarla) gönder.

> [!note] E-posta açılmadı mı (e-posta istemcisi ayarlanmamış)? «Hakkında» sayfasında «Yazara ulaşın» düğmesi vardır: Mektup açılamadıysa adresi panoya kopyalar ve sen de istediğin e-postadan yazabilirsin.

### Hiçbir şey işe yaramazsa

Basitten karmaşığa doğru ilerle ve her adımdan sonra botun kendine gelip gelmediğini kontrol et:

1. **«Duraklatıldı» → Oyunu koridora geri getir → «Devam et».**
2. **«DUR» (F10) → «Farmı başlat».** Bot akıllı başlatma ile başlayacak ve nerede olduğunu kendisi anlayacaktır.
3. **Botu durdur ve «scrcpy'yi yeniden başlat» düğmesine bas.** Ardından tekrar «Farmı başlat».
4. **Programı kapat ve yeniden aç.** Telefon takıldıysa kabloyu çıkarıp tak.
5. **Bilgisayarı ve telefonu yeniden başlat.** Şaka gibi gelebilir ama garip sorunların yarısını çözer.

Yeniden başlatmanın ardından oturum hedefleri (süre, odalar, katlar, titanit) sıfırdan sayılır; istatistikler, takımlar ve kurallar ise kalır: Dosyalarda saklanırlar.

> [!done] Artık botun kendi kendini nasıl kurtardığını, durduğunda ne yapacağını ve günlüğü nasıl toplayıp göndereceğini biliyorsun. Son bölüm kaldı: Program hakkında ve projeyi nasıl destekleyeceğin. [Sonraki bölüm →](#15)

## Hakkında ve destek

Sol menüdeki son sayfa — «Hakkında». Bu sayfa programın kendisi hakkındadır: Sürümün nedir, her şey yerinde mi, yazara nereden yazılır ve nasıl "teşekkür" edilir. Üzerinde hiçbir şeyi ayarlaman gerekmez, ancak burada iki yararlı düğme bulunur: «Güncellemeleri denetle» ve «Bot klasörü».

### Sayfada ne var

- :shield-check: Üstte **Program kartı**. «Hero Wars: Knowledge Engine Bot» adı, yanında **sürüm numarası** (örneğin `v1.6.1`) ve `Beta` etiketi. «Beta», "iş başında test ediliyor" anlamına gelir: Program çalışıyor ama yazar henüz geliştirmeye devam ediyor ve hatalar mümkündür. Adın altında kısa bir açıklama yer alır. Sağda dört düğme vardır, bunlar aşağıda açıklanmıştır.
- :user: **«Yazar ve lisans»**: Yazarın adı, e-postası ve lisansı. E-posta adresine tıkla — mektup açılır.
- :monitor: **«Bileşenlerin durumu»**: Bilgisayarda çalışma için gerekli her şeyin olup olmadığının kontrolü. Ayrıntılar aşağıdadır.
- :heart: **«Projeyi destekle»**: Yazara teşekkür etme yolları. Bu zorunlu değildir.

> [!tip] Bir sorun hakkında yazarken yazara sürümü söyle: Hangi programı kullandığını hemen gösterir. Sürüm üstteki kartta, adın yanında yer alır.

### Karttaki dört düğme

1. **«Güncellemeleri denetle».** Tarayıcıda projenin GitHub'daki sürümler sayfasını açar (GitHub, yazarın programı sakladığı sitedir; "sürüm", indirilebilen hazır sürümdür). Oradaki en yeni numarayı kendininkiyle karşılaştır. Daha yeniyse güncelleyebilirsin, aynıysa en yeni sürüme sahipsin.
2. **«Bot klasörü».** Windows Gezgini'nde programın çalıştırıldığı klasörü açar: Ayarlarının ve verilerinin bulunduğu klasörün ta kendisi. Dosyaları kopyalaman veya günlüğü bulman gerektiğinde faydalıdır.
3. **«Yazara ulaşın».** E-posta istemcinde yazarın adresine bir e-posta açar. Bilgisayarında e-posta istemcisi yoksa e-posta açılmaz. Bu durumda program adresi panoya (Ctrl+V ile yapıştırılan geçici bellek) kendisi koyar ve pencerenin altında bunu bildirir: «Açılamadı — panoya kopyalandı». Adresi herhangi bir e-postadan mektuba yapıştır.
4. **«Proje GitHub'ı».** GitHub'da projenin ana sayfasını açar: Kaynak kod ve açıklama oradadır.

> [!note] Program **güncellemeler için kendiliğinden internete gitmez**: «Güncellemeleri denetle» sadece sayfayı açar, kararı sen verirsin. Bilgin dışında hiçbir şeyin değişmemesi için böyle tasarlanmıştır.

### Program nasıl güncellenir

Güncelleme "üzerine kurulmaz" — yeni sürümü indirir ve verilerini ona taşırsın. Böylece takımların ve istatistiklerin kaybolmaz.

1. **Botu durdur ve programı kapat.** Bot çalışıyorsa pencere çarpı işareti onu durdurup durdurmayacağını soracaktır.
2. **Yeni sürümü indir** sürüm sayfasından («Güncellemeleri denetle» düğmesi) ve eskisinin üzerine değil, yeni bir klasöre çıkar.
3. **Verilerini taşı.** Eski klasörden yenisine `profile.yml` dosyasını ve `bot_data` klasörünü tamamen kopyala. Yeni program bunlar olmadan "sıfırdan" başlar: Boş ayarlar ve boş istatistikler.
4. **Yeni programı çalıştır** ve «Hakkında» sayfasına bak: Sürüm numarası yeni olmalı ve üç bileşenin tümü düzgün olmalıdır.
5. **Eski klasörü henüz silme.** Yeni sürümde birkaç gün çalış. Her şey yolundaysa kaldırabilirsin.

> [!warning] `bot_data` içindeki dosyaları "gerekli şeyler" diye tek tek kopyalama, klasörü tamamen taşı: Botun kendisinin hatırladığı kurallar, savaş geçmişi ve istatistikler birbirine bağlıdır ve yeniden toplanamaz.

### «Bileşenlerin durumu»

Program, botun çalışması için gerekli her şeyin olup olmadığını kendisi kontrol eder. Kontrol, sayfaya her girildiğinde arka planda yapılır. Devam ederken «denetleniyor…» görünür.

- :smartphone: **ADB** — Bilgisayarın telefonda tıklama yapmasını sağlayan hizmet. «bulundu» olmalıdır.
- :monitor: **scrcpy** — Telefon ekranını bilgisayardaki bir pencerede gösteren program. «bulundu» olmalıdır.
- :image: **Şablon veritabanı** — Botun ekranda ne olduğunu tanıdığı düğmelerin ve titanların "örnek resimleri". «yüklendi» olmalıdır.

Bir şey kırmızıysa ne yapılmalı:

- **ADB veya scrcpy «bulunamadı».** Bu, bulundukları klasörün `PATH` (Windows'un programları aradığı yerlerin listesi) değişkenine eklenmediği anlamına gelir. Bunun nasıl yapılacağı [«Neler gereklidir ve kurulum»](#2) bölümündedir. `PATH` düzenlendikten sonra programı kapatıp yeniden aç: Zaten çalışan program yeni `PATH` değişkenini görmez.
- **Şablon veritabanı «bulunamadı».** Program klasöründen dosyalar kaybolmuş. En yaygın olarak arşiv tam olarak çıkarılmamış veya antivirüs bir şeyi kaldırmıştır. Arşivi yeni bir klasöre yeniden çıkar ve güncellemede olduğu gibi `profile.yml` ile `bot_data` klasörünü taşı.

### Bot klasöründe ne var ve ne silinmemelidir

«Bot klasörü» düğmesiyle aç. Orada çok dosya vardır ama sana birkaçı lazımdır. Geri kalanı hizmet dosyalarıdır ve programın çalışması için gereklidir.

- :file-text: `HeroWarsBot.exe` — Programın kendisi. Bot da onun içinden çalışır, ayrı bir dosyası yoktur. Yanındaki diğer tüm dosyalar ve klasörler (`guide`, `ui`, kütüphaneler, `.dll` uzantılı dosyalar ve diğerleri) programın bir parçasıdır. **Bunların hiçbirini silme veya yeniden adlandırma**, aksi takdirde çalışmayı durdurur.
- :file-text: `profile.yml` — Ayarların: Oturum hedefi, eşikler, Telegram. **İçinde Telegram botunun jetonu vardır, bu yüzden kimseye gönderme.** İlk «Ayarları kaydet» işleminden sonra görünür.
- :folder: `bot_data` — Programın ve botun kendilerinin kaydettiği her şey. Bu, sahip olduğun **en değerli şeydir**. İçinde:
  - `stats.json` — İstatistikler («İstatistikler» sayfası);
  - `rules` klasörü — Botun hatırladıkları da dahil olmak üzere takımların ve kuralların;
  - `logs` klasörü — Savaş geçmişi ve bot günlüğü (`bot_log_...txt`);
  - `debug` klasörü — İnceleme için ekran görüntüleri (SOS pencereleri, takılmalar, başarısız geri almalar);
  - `titan_state.json` — Oyun günü boyunca titanların sağlığı ve enerjisi;
  - `profile.yml.bak` — Ayarların yedek kopyası. «Kural Ustası» içindeki «Geri Yükle / Sıfırla» buradan çalışır. **İçinde de Telegram jetonu vardır**;
  - `ui_settings.json` — Seçilen pencere dili;
  - `sos_info.json`, `temp_sos.png`, `temp_test.png` — Telegram mesajları için küçük çalışma dosyaları.
- :pause: `pause.flag` — "Duraklatma bayrağı". Bot esnek duraklatmadayken görünür. Geçen seferden kaldıysa program başlatma sırasında bunu kendisi siler.

> [!warning] `profile.yml` ve `bot_data` öğelerini **silme ve yeniden adlandırma**. `bot_data` klasörünü silersen istatistikler, takımlar, kurallar ve botun öğrendiği her şey kaybolur. Yer açmak çok gerekliyse `bot_data/debug` içeriği ve `bot_data/logs` içindeki eski günlükler silinebilir. Ancak bot kendisi yalnızca son 20 günlüğü ve son 50 ekran görüntüsünü bıraktığından yer genellikle sorun teşkil etmez.

> [!tip] **Haftada bir yedek al.** `profile.yml` dosyasını ve `bot_data` klasörünü bir USB belleğe veya buluta kopyala. Bilgisayar bozulursa veya Windows'u yeniden kurarsan programı tekrar indirirsin, takımları ve istatistikleri ise yedekten geri yüklersin. Yedekte Telegram jetonu mevcuttur — ortak bir klasörde değil, kendinde sakla.

### Yazar ve lisans

Program **Platon Petrunin** tarafından yazılmış ve desteklenmektedir. Sorular, hatalar ve fikirler için — «Yazara ulaşın» düğmesi veya «Yazar ve lisans» kartındaki adres.

Lisans **PolyForm Noncommercial 1.0.0** olarak adlandırılır. Basit bir ifadeyle:

- :check: Kendin için, kendi oyunun için ücretsiz olarak kullanabilirsin — istediğin kadar;
- :check: Kodu inceleyebilir ve kendin için değiştirebilirsin;
- :x: **Kazanç elde edilemez**: Programı veya `.exe` dosyasını satmak, başka bir isim altında kendininmiş gibi göstermek, ücretli hizmetlere entegre etmek yasaktır. Bunun için yazarın yazılı izni gereklidir.

> [!note] Bu kısa bir özet olup hukuki bir metin değildir. Özel bir durum varsa (örneğin programı arkadaşlarına veya bir topluluğa dağıtmak istiyorsan) önce yazara yaz. Lisansın tam metni GitHub'daki projede `LICENSE` dosyasında yer almaktadır.

### Proje nasıl desteklenir

Program ücretsizdir ve yazar bunu boş zamanlarında yapmaktadır. Sana zaman ve sinir tasarrufu sağlıyorsa para ile "teşekkür" edebilirsin. Bu **gönüllüdür**: Ödeme yapmış olsan da olmasan da bot aynı şekilde çalışır ve hiçbir "ücretli özellik" yoktur.

«Hakkında» sayfasının altında üç blok yer alır:

1. **«Kripto para».** Üç cüzdan: `USDT · TRC20`, `Bitcoin · BTC` ve `Ethereum · ETH`. Tam adres alanda görünür. Sağdaki «Kopyala» düğmesiyle (altta «Adres kopyalandı» görünür), alana çift tıklayarak (hepsi seçilir) veya fareye sağ tıklayıp — «Kopyala» seçilerek kopyalanabilir.
2. **«Telegram ile bağış».** Üç satır — Ruble (`RUB`), Avro (`EUR`) ve Dolar (`USD`). Her birinde iki düğme vardır: **«Uygulama»** ödemeyi Telegram uygulamasında açar, **«Tarayıcı»** — Telegram yüklü değilse tarayıcıda açar. Rahat ettiğin para birimini seç.
3. **«Doğrudan havaleler».** «Boosty'den Destekle» ve «YooMoney (RUB)» düğmeleri: Bu hizmetlerin sayfaları açılır, gerisi normal ödemedeki gibidir.

> [!warning] **Kripto para konusunda dikkatli ol.** Yalnızca cüzdanın yanında yazan ağ üzerinden transfer yap: `USDT` için bu `TRC20` ağıdır, başkası değil. Yanlış ağa gönderilen paralar **geri alınamaz**. Adresi yalnızca programdan «Kopyala» düğmesiyle al: Sitelerde ve başkalarının mesajlarında değiştirilebilir. İlk seferinde küçük bir miktar gönder.

### Sıkça sorulan sorular

- **Sürümüm eski — bu tehlikeli mi?** Hayır. Yeni bir sürüm çıktı diye program çalışmayı durdurmaz. Ancak yeni sürümlerde genellikle hatalar düzeltilir, bu nedenle birkaç haftada bir sürümler sayfasına göz at.
- **«Bot klasörü» açılmadı.** «Klasör açılamadı» yazısı görünür. Kendin aç: Gezgin, programı çıkardığın klasör.
- **Neden «Güncelle» düğmesi yok?** Program, iznin olmadan ayarlarını bozmamak için kendiliğinden hiçbir şey indirmez. Yukarıdaki adımları izleyerek kendin güncellersin.
- **Desteklemezsem bir şey değişir mi?** Hiçbir şey. Bot herkes için aynı çalışır.

> [!done] Bu son bölümdür. Artık botu çalıştırmak, kendine göre ayarlamak, kararlarını anlamak ve bir şeyler ters giderse düzeltmek için her şeyi biliyorsun. İyi oyunlar! Soruların kaldıysa aşağıdaki «Yazara ulaşın» düğmesini kullan.
