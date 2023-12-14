import discord
from discord.ext import commands
import sounddevice as sd
import wave
import speech_recognition as sr
import webbrowser 
import pyautogui
from PIL import Image


intents = discord.Intents.default()

# Mesajları okuma ayrıcalığını etkinleştirelim

intents.message_content = True

# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım

client = discord.Client(intents=intents)
# Discord botunu oluşturun
client = commands.Bot(intents=intents,command_prefix="/")

recognizer = sr.Recognizer()


@client.command(name='karbon_ayak_izi_hesapla', help='Karbon ayak izinizi hesaplar.')
async def karbon_ayak_izi_hesapla(ctx):
    await ctx.send(f'{ctx.author.mention}, karbon ayak izi hesaplamak için bazı sorulara cevap vermenizi istiyorum.')

    questions = [
        '1. Yılda kaç kilometre araç kullanıyorsunuz?',
        '2. Yılda kaç kez uçakla seyahat ediyorsunuz?',
        '3. Günlük su tüketiminiz nedir? (litre)',
        '4. Kaç saat bilgisayar başında çalışıyorsunuz?',
        '5. Geri dönüşüm yapıyor musunuz? (evet/hayır)',
    ]

    answers = []

    for question in questions:
        await ctx.send(question)
        response = await client.wait_for('message', check=lambda m: m.author == ctx.author)
        answers.append(response.content)

    # Hesaplama
    try:
        car_distance = float(answers[0])
        plane_trips = float(answers[1])
        daily_water_consumption = float(answers[2])
        computer_hours = float(answers[3])
        recycle = answers[4].lower() == 'evet'

        carbon_footprint = car_distance * 0.2 + plane_trips * 1.5 + daily_water_consumption * 0.1 + computer_hours * 0.05
        if recycle:
            carbon_footprint *= 0.8  # Geri dönüşüm yapanlar için indirim

        await ctx.send(f'{ctx.author.mention}, karbon ayak iziniz yaklaşık olarak {carbon_footprint:.2f} kgCO2.')
    except ValueError:
        await ctx.send(f'{ctx.author.mention}, lütfen sayısal değerler girin.')

@client.command(name='karbon', help='Mikrofonu dinle ve komutları algıla')
async def karbon(ctx, *args):
    await ctx.send('Dinleme başladı... Lütfen bir şeyler söyleyin.')

    try:
        # Ses kaynağını belirtin (örneğin, mikrofon veya ses dosyası)
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        # Ses dosyasını metne çevirin
        text = recognizer.recognize_google(audio, language="tr-TR")
        print("Söylenen metin: {}".format(text))
        
        
        if text == "Alfa Romeo":
                await ctx.send('Yakıt Tüketim Bilgileri Geliyor...')
                image = Image.open("sonuclar/alfa.jpg")
                
                with open("sonuclar/alfa.jpg", 'rb') as file:
                    file = discord.File(file, filename="image.jpg")
                    await ctx.send(file=file)               
                    await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 54 lt. Şehir İçi Tüketim (100 km) 7.1 lt. Şehir Dışı Tüketim (100 km) 4.7 lt. Şehir İçi Tüketim (100 km) 4.9 lt. Şehir Dışı Tüketim (100 km) 3.3 lt. Karma Tüketim (100 km) 3.9 lt.")
                    await ctx.send("-----------------------------------------------------------------------------------------------------")
                    await ctx.send("Kuruluşu 1910 yılında olan Alfa Romeo, Anonima Lombarda Fabbrica Automobili (A.L.F.A) ismiyle Milano‘da kuruldu.24 HP gücünde üretilen ilk araçtan 5 yıl sonra şirketi Nicola Romeo satın aldı ve markanın ismi ALFA ROMEO adını almış oldu. Bugün STELLANTİS otomotiv grubunde yer alan marka, kendine has karakteristik yapısı ile özel bir kullanıcı kitlesi tarafından tercih ediliyor. Ülkemizde Alfa Romeo kullanıcıları ve hayranları kendilerine “Alfisti” ismini veriyor. Genellikle Sportif yapılı ve sürüş zevki yüksek konseptler üzerine yoğunlaşan marka son dönemde SUV modelleri ile kendini göstermeye devam ediyor. Yüksek kaliteli malzemeleri, sürüş odaklı tasarım detayları ile kendine has bir yapısı olan modellerin satışı ülkemizde Koç Holding bünyesinde yapılmaktadır. Alfa Romeo modelleri ise, Tonale, Stelvio, Giulia, Stelvio Quadrifoglio, Giulia Quadrifoglio")
        elif text == "Aston Martin":
                await ctx.send('Yakıt Tüketim Bilgileri Geliyor...')
                image = Image.open("sonuclar/aston.jpg")
                
                with open("sonuclar/aston.jpg", 'rb') as file:
                    file = discord.File(file, filename="image.jpg")
                    await ctx.send(file=file)               
                    await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 54 lt. Şehir İçi Tüketim (100 km) 7.1 lt. Şehir Dışı Tüketim (100 km) 4.7 lt. Şehir İçi Tüketim (100 km) 21.6 lt. Şehir Dışı Tüketim (100 km) 10.0 lt. Karma Tüketim (100 km) 14.3 lt.")
                    await ctx.send("-----------------------------------------------------------------------------------------------------")
                    await ctx.send("İngiliz otomobil markası Aston Martin, lüks segment otomobil üreten bir markadır. Temelleri 1913 yılına kadar uzanan marka, el işçiliği ile araç üretiyor. Plastik malzemelerin oldukça az kullanılmaya özen gösterildiği araçta pek çok detay alüminyum kullanılarak üretiliyor.")
            
        elif text == "Audi":
            await ctx.send('Yakıt Tüketim Bilgileri Geliyor...')
            image = Image.open("sonuclar/audi.jpeg")                    
            with open("sonuclar/audi.jpeg", 'rb') as file:
                file = discord.File(file, filename="image.jpg")
                await ctx.send(file=file)               
                await ctx.send("1 litre benzinin yakılması ile 2,33 kg karbondioksit ve 1 lt dizel yakıtın yakılması ile 2,77 kg karbondioksit gazı açığa çıkmaktadır. Yakıt Kapasitesi 54 lt. Şehir İçi Tüketim (100 km) 7.1 lt. Şehir Dışı Tüketim (100 km) 4.7 lt.")
                await ctx.send("-----------------------------------------------------------------------------------------------------")
                await ctx.send("Alman kökenli Otomobil Markası AUDİ “Teknoloji ile Bir Adım Önde” mottosu ile tarihi 1899 yılına kadar uzanan bir yolculuğu ifade ediyor. Bugün küresel anlamda otomotiv sektörünü domine edici etkisi ile Almanya’nın en sevilen markalarından biri olarak karşımıza çıkan marka, Volkswagen otomotiv grubu içinde yer alıyor. Premium otomobil modelleri ile ön plana çıkan marka, son dönemde otomobillerinde geliştirdiği elektrifikasyon ile dikkat çekmeye devam ediyor. Sportif modelleri de bünyesinde barındıran marka “RS” isimli versiyonlar ile dinamizmi ön plana çıkartmayı başarıyor.")

        await ctx.send(f'Söyledikleriniz kaydedildi: "{text}"')

        # Dinleme sonrasında otomatik olarak karbon_ayak_izi_hesapla fonksiyonunu çağır
        await karbon_ayak_izi_hesapla(ctx)

    except sr.UnknownValueError:
        await ctx.send('Anlaşılamadı. Lütfen tekrar deneyin.')


client.run("")  # TOKEN yerine botunuzun gerçek token'ını ekleyin
    
