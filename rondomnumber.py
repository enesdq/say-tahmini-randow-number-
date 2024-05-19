import random

def tahmin_oyunu():
    gizli_sayi = random.randint(1, 100)
    tahmin = None

    print("1 ile 100 arasında bir sayı tahmin edin.")

    while tahmin != gizli_sayi:
        tahmin = int(input("Tahmin"))

        if tahmin < gizli_sayi:
            print("Daha büyük sayı")
        elif tahmin > gizli_sayi:
            print("Daha küçük sayı")
        else:
            print(f"Tebrikler! {gizli_sayi} sayısını doğru tahmin ettiniz!")

tahmin_oyunu()
