# Mehmet ALPKAYA, Ercan UCA, Devrim ÖZÇAY

#Tıpta Dijital Görüntüleme ve İletişim 



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












#3D:

DICOM yığınını yükle,
Dilim kaydet (eksenel, sagital, koronal),
Renk haritası dönüşümü,
Kaydırıcı kaydırma,
Fareyle gezinme/tıklama,
DICOM bilgilerini göster,
Dilim indeksi koordinatını göster,
3D hacim rekonstrüksiyonu,
