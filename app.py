
from flask import Flask

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gizemli Serüven</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    min-height: 100vh;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Arial, sans-serif;
    color: #eaf6ff;
    background:
        radial-gradient(circle at 15% 15%, rgba(0,190,220,.16), transparent 30%),
        radial-gradient(circle at 85% 80%, rgba(30,100,190,.20), transparent 35%),
        linear-gradient(135deg, #071521, #102638, #081522);
    position: relative;
    overflow-x: hidden;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    opacity: .15;
    background-image:
        linear-gradient(90deg, transparent 49%, #35c9df 50%, transparent 51%),
        linear-gradient(transparent 49%, #35c9df 50%, transparent 51%);
    background-size: 55px 55px;
}

.kutu {
    position: relative;
    z-index: 1;
    width: 100%;
    max-width: 540px;
    padding: 28px;
    text-align: center;
    border: 1px solid rgba(60,210,230,.45);
    border-radius: 24px;
    background: rgba(9,25,40,.96);
    box-shadow: 0 0 35px rgba(0,190,220,.14);
}

.ust-yazi {
    color: #5ed9e8;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: bold;
}

.ikonlar {
    font-size: 48px;
    margin: 15px 0;
}

h1 {
    color: #70e3f0;
    font-size: 30px;
    margin: 12px 0;
}

h2 {
    color: #8ce9f1;
    font-size: 22px;
}

p { line-height: 1.6; }

.aciklama { color: #b5cbd9; }

.istatistik {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 9px;
    margin: 20px 0;
}

.istatistik span {
    flex: 1;
    min-width: 105px;
    padding: 11px 7px;
    border: 1px solid #24566a;
    border-radius: 12px;
    background: #102d40;
    color: #83e6ef;
    font-size: 14px;
    font-weight: bold;
}

button {
    width: 100%;
    padding: 14px;
    margin: 7px 0;
    border: 1px solid #4bd2e2;
    border-radius: 12px;
    background: linear-gradient(135deg, #087e9c, #12618e);
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: .2s;
}

button:hover {
    background: linear-gradient(135deg, #12a8bd, #1685b5);
    transform: translateY(-2px);
}

.secim {
    background: #142f43;
    border: 1px solid #315a70;
    color: #eaf6ff;
    text-align: left;
}

.secim:hover {
    background: #1b5268;
    border-color: #61dce9;
}

.ikincil {
    background: #263b4c;
    border-color: #526a7b;
}

#soru {
    font-size: 18px;
    line-height: 1.6;
    color: #f1f8ff;
    margin: 22px 0;
}

#mesaj {
    min-height: 45px;
    margin: 15px 0;
    color: #8de7ee;
    font-weight: bold;
}

#kapi {
    color: #f4d88a;
    font-weight: bold;
    background: rgba(244,216,138,.08);
    padding: 10px;
    border-radius: 10px;
}

.cizgi {
    height: 7px;
    background: #20394b;
    border-radius: 10px;
    overflow: hidden;
    margin: 15px 0;
}

#ilerleme {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #08a9bd, #70e3f0);
    transition: width .3s;
}

.alt-bilgi {
    color: #7795a8;
    font-size: 12px;
    margin-top: 20px;
}

.gizli { display: none; }

@media(max-width: 480px) {
    .kutu { padding: 20px; }
    h1 { font-size: 25px; }
    .ikonlar { font-size: 40px; }
}
</style>
</head>

<body>

<div class="kutu">

    <div class="ust-yazi">DİJİTAL KEŞİF • BİLİŞİM MACERASI</div>
    <div class="ikonlar">💻 🔐 🐍</div>

    <h1>Gizemli Serüven</h1>

    <p class="aciklama">
    Bilginin gücünü kullan, soruları çöz ve gizemli kapıları aç!
    </p>

    <div id="baslangic">
        <p>🚀 3 Oda • 30 Soru • 300 Puan</p>
        <p>Her oyunda farklı soru sıralaması seni bekliyor!</p>
        <button onclick="oyunuBaslat()">🚀 Maceraya Başla</button>
    </div>

    <div id="oyun" class="gizli">

        <div class="istatistik">
            <span id="oda">Oda: 1/3</span>
            <span id="puan">Puan: 0</span>
            <span id="anahtarBilgi">🗝️ Anahtar: 0/3</span>
        </div>

        <div class="cizgi">
            <div id="ilerleme"></div>
        </div>

        <p id="kapi">🚪 İlk kapı seni bekliyor!</p>

        <h2 id="baslik"></h2>
        <p id="soru"></p>

        <div id="secenekler"></div>
        <div id="mesaj"></div>

        <button id="sonraki" class="gizli"
        onclick="sonrakiSoru()">
        Sonraki Soru ➜
        </button>

    </div>

    <div id="sonuc" class="gizli">

        <div class="ikonlar">🏆 🌟 🎉</div>
        <h2>Serüven Tamamlandı!</h2>

        <p id="sonPuan"></p>
        <p id="sonAnahtar"></p>
        <p id="sonMesaj"></p>

        <button onclick="yenidenBasla()">
        🔄 Yeniden Oyna
        </button>

        <button class="ikincil" onclick="anaSayfayaDon()">
        🏠 Ana Sayfaya Dön
        </button>

    </div>

    <div class="alt-bilgi">
        GİZEMLİ SERÜVEN • BİLGİYLE KEŞFET
    </div>

</div>

<script>

const odalar = [

{
ad: "💻 Dijital Dünya",
sorular: [
{soru:"Bilgisayarın beyni olarak bilinen parça hangisidir?",secenek:["RAM","CPU","SSD","GPU"],cevap:1},
{soru:"RAM belleğin temel görevi nedir?",secenek:["Geçici veri tutmak","Dosyaları kalıcı saklamak","Yazdırmak","İnternete bağlanmak"],cevap:0},
{soru:"Anakartın görevi nedir?",secenek:["Ses kaydetmek","Bileşenler arasında iletişim sağlamak","Görüntü yazdırmak","Dosya sıkıştırmak"],cevap:1},
{soru:"Bilgisayarın donanımını yöneten yazılım hangisidir?",secenek:["Paint","Tarayıcı","İşletim sistemi","Hesap makinesi"],cevap:2},
{soru:"Python nedir?",secenek:["Programlama dili","İşletim sistemi","Donanım","Tarayıcı"],cevap:0},
{soru:"1 Byte kaç bitten oluşur?",secenek:["2","4","8","16"],cevap:2},
{soru:"SSD'nin görevi nedir?",secenek:["Verileri depolamak","İşlem yapmak","Görüntü üretmek","Ses çıkarmak"],cevap:0},
{soru:"Hangisi giriş birimidir?",secenek:["Monitör","Klavye","Hoparlör","Yazıcı"],cevap:1},
{soru:"Hangisi çıkış birimidir?",secenek:["Fare","Mikrofon","Tarayıcı","Monitör"],cevap:3},
{soru:"GPU hangi işlemlerde kullanılır?",secenek:["Grafik işlemleri","Metin yazma","Dosya adlandırma","Klavye yönetimi"],cevap:0}
]
},

{
ad: "🛡️ Siber Güvenlik",
sorular: [
{soru:"Güçlü bir şifrede hangisi bulunmalıdır?",secenek:["Sadece isim","123456","Harf, sayı ve semboller","Doğum tarihi"],cevap:2},
{soru:"Kimlik avı (Phishing) nedir?",secenek:["Bilgisayar temizliği","Sahte mesajlarla bilgi çalma girişimi","Dosya sıkıştırma","Yazılım güncelleme"],cevap:1},
{soru:"Bilgisayar virüsü hangi tür yazılımdır?",secenek:["Zararlı yazılım","İşletim sistemi","Ofis programı","Sürücü"],cevap:0},
{soru:"Güvenlik duvarının görevi nedir?",secenek:["Ekranı aydınlatmak","Ağ trafiğini denetlemek","Dosya yazdırmak","Ses kaydetmek"],cevap:1},
{soru:"Kişisel veriler hangisidir?",secenek:["Rastgele sayı","Hava durumu","Kimliği belirleyen bilgiler","Bilgisayar modeli"],cevap:2},
{soru:"HTTPS neyi ifade eder?",secenek:["Şifreli web bağlantısı","Oyun türü","Dosya biçimi","İşlemci modeli"],cevap:0},
{soru:"İki aşamalı doğrulama ne sağlar?",secenek:["Ekran parlaklığı","Ek hesap güvenliği","İnternet hızı","Dosya boyutunu azaltma"],cevap:1},
{soru:"Veri yedeklemenin amacı nedir?",secenek:["Verileri silmek","Verileri korumak","Ekranı kapatmak","Virüs üretmek"],cevap:1},
{soru:"Dijital ayak izi nedir?",secenek:["İnternette bırakılan izler","Bilgisayarın ağırlığı","Klavye türü","Ekran çözünürlüğü"],cevap:0},
{soru:"Tanımadığımız bağlantı geldiğinde ne yapmalıyız?",secenek:["Hemen tıklamalıyız","Herkese göndermeliyiz","Güvenilirliğini kontrol etmeliyiz","Şifremizi girmeliyiz"],cevap:2}
]
},

{
ad: "🐍 Kodlama Laboratuvarı",
sorular: [
{soru:"Algoritma nedir?",secenek:["Bilgisayar parçası","Bir problemi çözmek için adımlar","İnternet sitesi","Dosya türü"],cevap:1},
{soru:"Python'da değişken oluşturmak için hangisi kullanılır?",secenek:["=","==","!=","//"],cevap:0},
{soru:"Python'da metin veri türü hangisidir?",secenek:["int","float","str","bool"],cevap:2},
{soru:"Koşul kontrolü için hangisi kullanılır?",secenek:["print","if","input","import"],cevap:1},
{soru:"for döngüsü ne amaçla kullanılır?",secenek:["Tekrarlı işlemler","Bilgisayarı kapatma","Dosya silme","İnternete bağlanma"],cevap:0},
{soru:"while döngüsü ne zaman çalışır?",secenek:["Koşul doğru olduğu sürece","Bir kez","Dosya açınca","Bilgisayar kapanınca"],cevap:0},
{soru:"Python'da fonksiyon tanımlamak için hangisi kullanılır?",secenek:["if","for","def","print"],cevap:2},
{soru:"return komutunun görevi nedir?",secenek:["Değer döndürmek","Ekranı kapatmak","Değişken silmek","Döngü başlatmak"],cevap:0},
{soru:"Python'da liste hangi işaretlerle oluşturulur?",secenek:["{}","[]","()","<>"],cevap:1},
{soru:"print(2 + 3) komutunun çıktısı nedir?",secenek:["23","5","2+3","Hata"],cevap:1}
]
}
];

let sorular = [];
let sira = 0;
let puan = 0;
let anahtar = 0;
let cevaplandi = false;

// Bir dizinin sırasını rastgele karıştırır.
function karistir(dizi) {

    let yeniDizi = [...dizi];

    for (let i = yeniDizi.length - 1; i > 0; i--) {

        let j = Math.floor(Math.random() * (i + 1));

        [yeniDizi[i], yeniDizi[j]] =
        [yeniDizi[j], yeniDizi[i]];

    }

    return yeniDizi;
}

function oyunuBaslat() {

    sira = 0;
    puan = 0;
    anahtar = 0;
    cevaplandi = false;

    // Her odanın sorularını ayrı ayrı karıştır.
    sorular = [];

    odalar.forEach(oda => {

        const karisikSorular = karistir(oda.sorular);

        sorular.push(...karisikSorular);

    });

    document.getElementById("baslangic").classList.add("gizli");
    document.getElementById("sonuc").classList.add("gizli");
    document.getElementById("oyun").classList.remove("gizli");

    document.getElementById("kapi").innerText =
    "🚪 İlk kapı seni bekliyor!";

    soruyuGoster();
}

function soruyuGoster() {

    cevaplandi = false;

    const q = sorular[sira];
    const odaNo = Math.floor(sira / 10);

    document.getElementById("oda").innerText =
    "Oda: " + (odaNo + 1) + "/3 | Soru: " + (sira % 10 + 1) + "/10";

    document.getElementById("puan").innerText =
    "Puan: " + puan;

    document.getElementById("anahtarBilgi").innerText =
    "🗝️ Anahtar: " + anahtar + "/3";

    document.getElementById("baslik").innerText =
    odalar[odaNo].ad;

    document.getElementById("soru").innerText = q.soru;

    document.getElementById("mesaj").innerText = "";

    document.getElementById("sonraki").classList.add("gizli");

    document.getElementById("ilerleme").style.width =
    (sira / sorular.length * 100) + "%";

    const alan = document.getElementById("secenekler");
    alan.innerHTML = "";

    // Cevap seçeneklerini de karıştır, doğru cevabı koru.
    const secenekler = q.secenek.map((metin, index) => ({
        metin: metin,
        dogru: index === q.cevap
    }));

    const karisikSecenekler = karistir(secenekler);

    karisikSecenekler.forEach(secenek => {

        const btn = document.createElement("button");

        btn.className = "secim";
        btn.innerText = secenek.metin;
        btn.onclick = () => cevapKontrol(secenek.dogru);

        alan.appendChild(btn);

    });
}

function cevapKontrol(dogruMu) {

    if (cevaplandi) return;

    cevaplandi = true;

    const mesaj = document.getElementById("mesaj");

    if (dogruMu) {

        puan += 10;

        mesaj.innerText =
        "✨ Harika! Doğru cevap. +10 puan!";

    } else {

        const dogruCevap = sorular[sira].secenek[sorular[sira].cevap];

        mesaj.innerText =
        "🔎 Bu kez olmadı. Doğru cevap: " + dogruCevap;

    }

    if ((sira + 1) % 10 === 0) {

        anahtar += 1;

        document.getElementById("kapi").innerText =
        "🚪 Kapı açıldı! Anahtar kazandın! 🗝️";

    } else {

        document.getElementById("kapi").innerText =
        "🔐 Devam et! Odanın son sorusunda anahtar kazanacaksın.";

    }

    document.getElementById("puan").innerText =
    "Puan: " + puan;

    document.getElementById("anahtarBilgi").innerText =
    "🗝️ Anahtar: " + anahtar + "/3";

    document.getElementById("sonraki").classList.remove("gizli");

    if (sira === sorular.length - 1) {

        document.getElementById("sonraki").innerText =
        "Sonucu Gör 🏆";

    } else if ((sira + 1) % 10 === 0) {

        document.getElementById("sonraki").innerText =
        "Yeni Odaya Geç ➜";

    } else {

        document.getElementById("sonraki").innerText =
        "Sonraki Soru ➜";

    }
}

function sonrakiSoru() {

    sira++;

    if (sira >= sorular.length) {

        oyunuBitir();

    } else {

        soruyuGoster();

    }
}

function oyunuBitir() {

    document.getElementById("oyun").classList.add("gizli");
    document.getElementById("sonuc").classList.remove("gizli");

    document.getElementById("ilerleme").style.width = "100%";

    document.getElementById("sonPuan").innerText =
    "Toplam puanın: " + puan + " / 300";

    document.getElementById("sonAnahtar").innerText =
    "Topladığın anahtar: " + anahtar + " / 3";

    document.getElementById("sonMesaj").innerText =

    puan === 300
    ? "Mükemmel! Bütün soruları doğru yanıtladın! 🌟"

    : puan >= 200
    ? "Çok güzel! Gerçek bir bilişim kaşifisin! 🔮"

    : "Güzel bir başlangıç! Yeniden deneyebilirsin. 💙";
}

function yenidenBasla() {

    oyunuBaslat();
}

function anaSayfayaDon() {

    document.getElementById("oyun").classList.add("gizli");
    document.getElementById("sonuc").classList.add("gizli");
    document.getElementById("baslangic").classList.remove("gizli");

    sira = 0;
    puan = 0;
    anahtar = 0;
    cevaplandi = false;
}

</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
