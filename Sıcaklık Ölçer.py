print("""**********************************************************
*     Blackjack35 Sıcaklık Çevirici                       *
*    İşlemler;                                            *
*    1-Celcius to Fahrenheit                              *
*    2-Celcius to Kelvin                                  *
*    3-Fahrenheit to Celcius                              *
*    4-Fahrenheit to Kelvin                               *
*    5-kelvin to Celcius                                  *
*    6-Kelvin To Fahrenheit                               *
*                                                         *
*    Programdan Çıkmak İçin "q" Ye Basınız.               *
**********************************************************""")


while True:
    işlem = input("Yapmak İstediğiniz İşlemi Seçiniz:  ")

    if (işlem == "q"):
        print("Her Zaman Buradayız.")
        break
    elif (işlem == "1"):

        celcius = float(input("Çevirmek İstediğiniz Celcius'u Giriniz: "))
        fahrenheit = celcius * 1.8 + 32
        print("{} Celcius {} Fahrenheit Yapar!".format(celcius,fahrenheit))
    elif (işlem == "2"):
        celcius = float(input("Çevirmek İstediğiniz Celcius'u Giriniz: "))
        kelvin = (celcius + 273.15)
        print("{} Celcius, {} Kelvin Yapar!".format(celcius, kelvin))

    elif (işlem =="3"):

        fahrenheit = float(input("Çevirmek İstediğiniz Fahrenheit'i Giriniz: "))
        celcius = (fahrenheit - 32) / 1.8
        print("{} Fahrenheit {} Celcius Yapar! ".format(fahrenheit,celcius))

    elif (işlem == "4"):
        fahrenheit = float(input("Çevirmek İstediğiniz Fahrenheit' i Giriniz: "))
        kelvin =(fahrenheit + 459.67)* 5/9
        print("{} Fahrenheit {} Kelvin yapar!".format(fahrenheit,kelvin))

    elif (işlem == "5"):

        kelvin = float(input("Çevirmek İstediğiniz Kelvin'i Giriniz: "))
        celcius = (kelvin - 273.15)
        print("{} Kelvin, {} Celcius yapar! ".format(kelvin,celcius))

    elif (işlem == "6"):
        kelvin = float(input("Çevirmek İstediğiniz Kelvin'i Giriniz: "))
        fahrenheit =  (kelvin * 9/5) -459.67
        print("{} Kelvin, {} Fahreheit Yapar ! ".format(kelvin,fahrenheit))




    else :
        print("Yanlış Bir İşlem Seçtiniz, Tekrar Deneyiniz ! ")