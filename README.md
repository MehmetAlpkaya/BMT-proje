# Mehmet ALPKAYA, Ercan UCA, Devrim ÖZÇAY

#Tıpta Dijital Görüntüleme ve İletişim 

![BMT1](https://user-images.githubusercontent.com/57410316/149544986-d4a116f9-86ff-4a0f-a20c-1f969d0d6ecd.JPG)

![BMT2](https://user-images.githubusercontent.com/57410316/149545172-7ba8ee75-d6d9-4a09-8170-6740c5905016.JPG)

#Amacımız:
Makine öğrenimi kullanarak 3DimViewer hacimsel tıbbi görüntülerin 3B görselleştirmesini
kolaylaştırmak.

#Yöntemlerimiz:
Klinik ortamlardaki sınırlı bilgi işlem kaynakları nedeniyle radyoloji görüntüleri üzerinde makine öğrenimi (ML) işlem hatlarının gerçek zamanlı yürütülmesi zordur, ancak bunları araştırma kümelerinde çalıştırmak verimli veri aktarım yetenekleri gerektirir. Hastanelerin PACS'lerinden verimli bir şekilde görüntüler alarak ve görüntülerden meta verileri çıkararak araştırma kümelerinde ML ve işleme boru hatlarını sağlayan açık kaynaklı bir Dijital Görüntüleme ve Tıpta İletişim (DICOM) çerçevesi olan Niffler'i elde edebeliriz.


#Kullandığımız araçlar:
Hastahane uygulaması üzerinden hastanın çekilen MR ve röntgenlerini hasta veritabanında tutularak XML ve Python ile yazılan  DİCOM viewer kulanılır.

#2D:

Load Image (*.dcm),
Save Image,
Gri skalaya dönüştür,
Eski haline getirmek,
Eşikleme,
Morfoloji,
Kenar Algılama,
körüntüyü Tanıma,
Hatayı minimize etme,












#3D:1

![3D_Processing](https://user-images.githubusercontent.com/57410316/149545507-45ae6653-3ce5-477f-9608-afb7a346a23f.jpg)


DICOM yığınını yükle,
Dilim kaydet (eksenel, sagital, koronal),
Renk haritası dönüşümü,
Kaydırıcı kaydırma,
Fareyle gezinme/tıklama,
DICOM bilgilerini göster,
Dilim indeksi koordinatını göster,
3D hacim rekonstrüksiyonu,
