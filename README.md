# Whatsapp-Bot
Whatsapp online checker for users with selenium webdriver

## Türkçe

### Bot Nasıl Çalışır? Ve Ne İşe Yarar?

Programı çalıştırdığınız zaman whatsapp web'e girer ve ismini verdiğiniz kişinin çevrimiçi olup olmadığını kontrol eder.

### Özellikleri Nelerdir?
1) Kişi çevrimiçi ve çevrimdışı olduğunda size sesli ve yazılı bir şekilde bildirir.(ses özelliği yalnızca linux'ta çalışmaktadır.)
2) kişi çevrimiçi olduğunda size mail gönderir(isteğe bağlı.)
3) sessiz çalışma özelliği bulunmaktadır.
4) tarayıcı üzerinde çalışır.(chrome ve firefox)

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

#### Dipnot: Programı sorunsuz çalıştırmak için Chrome ve ChromeDriver'ın son sürümünü kullanmaya özen gösterin.
