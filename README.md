# Whatsapp-Bot
Whatsapp online checker for users with selenium webdriver.

## Türkçe

### Bot Nasıl Çalışır? Ve Ne İşe Yarar?

Programı çalıştırdığınız zaman whatsapp web'e girer ve ismini verdiğiniz kişinin çevrimiçi olup olmadığını kontrol eder.

### Özellikleri Nelerdir?
1) Kişi çevrimiçi ve çevrimdışı olduğunda size sesli ve yazılı bir şekilde bildirir.
2) kişi çevrimiçi olduğunda size mail gönderir.(isteğe bağlı.)
3) sessiz çalışma özelliği bulunmaktadır.
4) tarayıcı üzerinde çalışır.(chrome ve firefox)
5) kişinin kaç saniye çevrimiçi kaldığını bildirir.
6) Türkçe ve ingilizce dil desteği bulunmaktadır.

### Gereksinimler

python 3

selenium

geckodriver(firefox için)

chromedriver(chrome için)

espeak(linux'ta kullananlar için)


### Linux İçin Kurulum
1) git clone https://github.com/espyrx/Whatsapp-Bot.git
2) pip3 install selenium
3) sudo apt-get install espeak -y
4) cd WhatsApp-Bot
5) geckodriver indirip WhatsApp-Bot dizinine taşıyın. indirme linki --> [geckodriver](https://github.com/mozilla/geckodriver/releases)
6) python3 WhatsApp-Bot.py

### Windows İçin Kurulum
1) Linkten Python kurulum dosyasını indirin ve kurun. [Python](https://www.python.org/downloads/windows/)
2) Linkten WhatsApp-Bot.exe dosyasını indirin. --> [WhatsApp-bot](https://github.com/espyrx/Whatsapp-Bot/releases/tag/WhatsApp)
3) Linkten sisteminize uygun ChromeDriver dosyasını indirin. --> [ChromeDriver](https://chromedriver.chromium.org/downloads)
4) ChromeDriver'ı zipten çıkarın.
5) WhatsApp-Bot.exe ve ChromeDriver.exe dosyalarını aynı klasöre taşıyın.
6) WhatsApp-Bot.exe dosyasını çalıştırın.

#### Dipnot: Programı sorunsuz çalıştırmak için Chrome ve ChromeDriver'ın sürümlerinin aynı olmasına özen gösterin.





## English

### How It Work? And What Does It Do?

When you run the program, WhatsApp logs into the web and checks whether the person you named is online.

### Features

1) Notifies you in voice and text when the contact is online and offline.
2) sends you an e-mail when the contact is online. (optional.)
3) It has a silent operation feature.
4) It works on the browser. (chrome and firefox)
5) It tells you how many seconds the person has been online.

### Requirements

python 3

selenium

geckodriver(for firefox)

chromedriver(for chrome)

espeak(for linux users)

### Installation For Linux
1) git clone https://github.com/espyrx/Whatsapp-Bot.git
2) pip3 install selenium
3) sudo apt-get install espeak -y
4) cd WhatsApp-Bot
5) Download geckodriver and move it to WhatsApp-Bot directory. download link --> [geckodriver](https://github.com/mozilla/geckodriver/releases)
6) python3 WhatsApp-Bot.py

### Installation For Linux
1) Download and install the Python installation file from the link. [Python](https://www.python.org/downloads/windows/)
2) Download WhatsApp-Bot.exe from the link. --> [WhatsApp-bot](https://github.com/espyrx/Whatsapp-Bot/releases/tag/WhatsApp)
3) Download the ChromeDriver file suitable for your system from the link. --> [ChromeDriver](https://chromedriver.chromium.org/downloads)
4) Extract the ChromeDriver from the zip.
5) Move the WhatsApp-Bot.exe and ChromeDriver.exe files to the same folder.
6) Run WhatsApp-Bot.exe.

#### Footnote: Make sure that the versions of Chrome and ChromeDriver are the same to run the program smoothly.
