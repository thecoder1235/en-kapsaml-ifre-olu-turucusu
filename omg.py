import random , time

def time_print(text,delay=0.05):
    
    [print(harf, end='', flush=True) or time.sleep(delay) for harf in text]
imposble="!'^+%&/()=?*\_1234567890*-q@we€rtyuıopğü,;àsdfghjklşízxcvbmöç.:<>QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ¨₺$π∞Σ√∛∜∫∬∭∮∯∰∱∲∳∀∁∂∃∄∅∆∇∈∉∊∋∌∍∎∏∐∑∓∔∕∖∗∘∙∝∟∠∡∢∣∤∥∦∧∨∩∪∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅≆≇≈≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟≠≡≢≣≤≥≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱⁺⁻⁼⁽⁾ⁿ₊₋₌₍₎♪♫♩♬♭♮♯¢$€£¥₮৲৳௹฿៛₠₡₢₣₤₥₦₧s₨₩₪₫₭₯₰₱₲₳₴₵￥﷼¤ƒ₺♙♖♘♗♔♕♟♜♞♝♚♛♡♥♢♦♤♠♧♣¹²³⁴⁵⁶⁷⁸⁹⁰Æ"
ZOR="!'^+%&/()=?*\_1234567890*-q@we€rtyuıopğü,;àsdfghjklşízxcvbmöç.:<>QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ¨₺$"
ORTA="qwertyuıopğüasdfghjklşizxcvbnmöç.1234567890*-!'^+%&/()=?_QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ:"
KOLAY="qwertyuıopğüasdfghjklşizxcvbnmöç.1234567890QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
ÇOK_KOLAY="qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
tavsiye_edilmeyen="1234567890qwertyuıopğüasdfghjklşizxcvbnmöç"
time_print("şifre kaç basamaklı olsun? ")
loop_value=int(input(""))
time_print("Zorluk seviyesi nasıl olsun (1.zor,2.orta,3.kolay,4.çok kolay,5.tavsiye edilmeyen,6.imkansız)")
zorluk=input()
time_print("şifreniz oluşturuluyor...")

time.sleep(.5)
print()
try:
    if zorluk=="1":
        zorluk=ZOR
    elif zorluk=='2':
        zorluk=ORTA
    elif zorluk=='3':
        zorluk=KOLAY
    elif zorluk=='4':
        zorluk=ÇOK_KOLAY
    elif zorluk=='5':
        zorluk=tavsiye_edilmeyen
    elif zorluk=='6':
        zorluk=imposble
except:
    print()
    time_print("yanlış yazdın")
for i in range(loop_value):
    print(random.choice(zorluk),end='')
time.sleep(1)
print()
time_print("çıkmak için entera bas")
input("")


#tüm karakterler
#!'^+%&/()=?*\_1234567890*-q@we€rtyuıopğü,;àsdfghjklşízxcvbmöç.:<>QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ¨₺$π∞Σ√∛∜∫∬∭∮∯∰∱∲∳∀∁∂∃∄∅∆∇∈∉∊∋∌∍∎∏∐∑∓∔∕∖∗∘∙∝∟∠∡∢∣∤∥∦∧∨∩∪∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅≆≇≈≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟≠≡≢≣≤≥≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱⁺⁻⁼⁽⁾ⁿ₊₋₌₍₎♪♫♩♬♭♮♯¢$€£¥₮৲৳௹฿៛₠₡₢₣₤₥₦₧s₨₩₪₫₭₯₰₱₲₳₴₵￥﷼¤ƒ₺♙♖♘♗♔♕♟♜♞♝♚♛♡♥♢♦♤♠♧♣¹²³⁴⁵⁶⁷⁸⁹⁰Æ
