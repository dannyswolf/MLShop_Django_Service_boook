"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
                    A_ΟΡΟΦΟΣListView,       A_ΟΡΟΦΟΣCreateView,         A_ΟΡΟΦΟΣUpdateView,         A_ΟΡΟΦΟΣDeleteView,
                    BROTHERListView,        BROTHERCreateView,          BROTHERUpdateView,          BROTHERDeleteView,
                    CANONListView,          CANONCreateView,            CANONUpdateView,            CANONDeleteView,
                    EPSONListView,          EPSONCreateView,            EPSONUpdateView,            EPSONDeleteView,
                    KONICAListView,         KONICACreateView,           KONICAUpdateView,           KONICADeleteView,
                    KYOCERAListView,        KYOCERACreateView,          KYOCERAUpdateView,          KYOCERADeleteView,
                    LEXMARKListView,        LEXMARKCreateView,          LEXMARKUpdateView,          LEXMARKDeleteView,
                    OKIListView,            OKICreateView,              OKIUpdateView,              OKIDeleteView,
                    RICOHListView,          RICOHCreateView,            RICOHUpdateView,            RICOHDeleteView,
                    SAMSUNGListView,        SAMSUNGCreateView,          SAMSUNGUpdateView,          SAMSUNGDeleteView,
                    SHARPListView,          SHARPCreateView,            SHARPUpdateView,            SHARPDeleteView,
                    ΜΕΛΑΝΑΚΙΑListView,      ΜΕΛΑΝΑΚΙΑCreateView,        ΜΕΛΑΝΑΚΙΑUpdateView,        ΜΕΛΑΝΑΚΙΑDeleteView,
                    ΜΕΛΑΝΟΤΑΙΝΙΕΣListView,  ΜΕΛΑΝΟΤΑΙΝΙΕΣCreateView,    ΜΕΛΑΝΟΤΑΙΝΙΕΣUpdateView,    ΜΕΛΑΝΟΤΑΙΝΙΕΣDeleteView,
                    ΤΟΝΕΡListView,          ΤΟΝΕΡCreateView,            ΤΟΝΕΡUpdateView,            ΤΟΝΕΡDeleteView,
                    ΦΩΤΟΤΥΠΙΚΑListView,     ΦΩΤΟΤΥΠΙΚΑCreateView,       ΦΩΤΟΤΥΠΙΚΑUpdateView,       ΦΩΤΟΤΥΠΙΚΑDeleteView,
                    ΧΧΧListView,            ΧΧΧCreateView,              ΧΧΧUpdateView,              XXXDeleteView,
                    # Json
                    A_ΟΡΟΦΟΣ_json, BROTHER_json, CANON_json, EPSON_json, KONICA_json, KYOCERA_json, LEXMARK_json, OKI_json,
                    RICOH_json, SAMSUNG_json, SHARP_json, ΜΕΛΑΝΑΚΙΑ_json, ΜΕΛΑΝΟΤΑΙΝΙΕΣ_json, ΤΟΝΕΡ_json,
                    ΦΩΤΟΤΥΠΙΚΑ_json
                   )

app_name = 'warehouse'
urlpatterns = [
    # A_ΟΡΟΦΟΣ
    path('A_ΟΡΟΦΟΣ/', A_ΟΡΟΦΟΣListView.as_view(), name='A_ΟΡΟΦΟΣ'),
    path('A_ΟΡΟΦΟΣ-json', A_ΟΡΟΦΟΣ_json, name='A_ΟΡΟΦΟΣ_json'),
    path('add_A_ΟΡΟΦΟΣ/', A_ΟΡΟΦΟΣCreateView.as_view(), name='add_A_ΟΡΟΦΟΣ'),
    path('A_ΟΡΟΦΟΣ/<int:spare_part_id>', A_ΟΡΟΦΟΣUpdateView.as_view(), name='edit_A_ΟΡΟΦΟΣ'),
    path('A_ΟΡΟΦΟΣ/<int:spare_part_id>/delete', A_ΟΡΟΦΟΣDeleteView.as_view(), name='A_ΟΡΟΦΟΣ_delete_product'),
    # Brother
    path('brother/', BROTHERListView.as_view(), name='brother'),
    path('brother-json', BROTHER_json, name='brother_json'),
    path('add_brother/', BROTHERCreateView.as_view(), name='add_brother'),
    path('brother/<int:spare_part_id>', BROTHERUpdateView.as_view(), name='edit_brother'),
    path('brother/<int:spare_part_id>/delete', BROTHERDeleteView.as_view(), name='brother_delete_product'),
    # Canon
    path('canon/', CANONListView.as_view(), name='canon'),
    path('canon-json', CANON_json, name='canon_json'),
    path('add_canon/', CANONCreateView.as_view(), name='add_canon'),
    path('canon/<int:spare_part_id>', CANONUpdateView.as_view(), name='edit_canon'),
    path('canon/<int:spare_part_id>/delete', CANONDeleteView.as_view(), name='canon_delete_product'),
    # Epson
    path('epson/', EPSONListView.as_view(), name='epson'),
    path('epson-json', EPSON_json, name='epson_json'),
    path('add_epson/', EPSONCreateView.as_view(), name='add_epson'),
    path('epson/<int:spare_part_id>', EPSONUpdateView.as_view(), name='edit_epson'),
    path('epson/<int:spare_part_id>/delete', EPSONDeleteView.as_view(), name='epson_delete_product'),
    # Konica
    path('konica/', KONICAListView.as_view(), name='konica'),
    path('konica-json', KONICA_json, name='konica_json'),
    path('add_konica/', KONICACreateView.as_view(), name='add_konica'),
    path('konica/<int:spare_part_id>', KONICAUpdateView.as_view(), name='edit_konica'),
    path('konica/<int:spare_part_id>/delete', KONICADeleteView.as_view(), name='konica_delete_product'),
    # Kyocera
    path('kyocera/', KYOCERAListView.as_view(), name='kyocera'),
    path('kyocera-json', KYOCERA_json, name='kyocera_json'),
    path('add_kyocera/', KYOCERACreateView.as_view(), name='add_kyocera'),
    path('kyocera/<int:spare_part_id>', KYOCERAUpdateView.as_view(), name='edit_kyocera'),
    path('kyocera/<int:spare_part_id>/delete', KYOCERADeleteView.as_view(), name='kyocera_delete_product'),
    # Lexmark
    path('lexmark/', LEXMARKListView.as_view(), name='lexmark'),
    path('lexmark-json', LEXMARK_json, name='lexmark_json'),
    path('add_lexmark/', LEXMARKCreateView.as_view(), name='add_lexmark'),
    path('lexmark/<int:spare_part_id>', LEXMARKUpdateView.as_view(), name='edit_lexmark'),
    path('lexmark/<int:spare_part_id>/delete', LEXMARKDeleteView.as_view(), name='lexmark_delete_product'),
    # Oki
    path('oki/', OKIListView.as_view(), name='oki'),
    path('oki-json', OKI_json, name='oki_json'),
    path('add_oki/', OKICreateView.as_view(), name='add_oki'),
    path('oki/<int:spare_part_id>', OKIUpdateView.as_view(), name='edit_oki'),
    path('oki/<int:spare_part_id>/delete', OKIDeleteView.as_view(), name='oki_delete_product'),
    # Ricoh
    path('ricoh/', RICOHListView.as_view(), name='ricoh'),
    path('ricoh-json', RICOH_json, name='ricoh_json'),
    path('add_ricoh/', RICOHCreateView.as_view(), name='add_ricoh'),
    path('ricoh/<int:spare_part_id>', RICOHUpdateView.as_view(), name='edit_ricoh'),
    path('ricoh/<int:spare_part_id>/delete', RICOHDeleteView.as_view(), name='ricoh_delete_product'),
    # Samsung
    path('samsung/', SAMSUNGListView.as_view(), name='samsung'),
    path('samsung-json', SAMSUNG_json, name='samsung_json'),
    path('add_samsung/', SAMSUNGCreateView.as_view(), name='add_samsung'),
    path('samsung/<int:spare_part_id>', SAMSUNGUpdateView.as_view(), name='edit_samsung'),
    path('samsung/<int:spare_part_id>/delete', SAMSUNGDeleteView.as_view(), name='samsung_delete_product'),
    # Sharp
    path('sharp/', SHARPListView.as_view(), name='sharp'),
    path('sharp-json', SHARP_json, name='sharp_json'),
    path('add_sharp/', SHARPCreateView.as_view(), name='add_sharp'),
    path('sharp/<int:spare_part_id>',  SHARPUpdateView.as_view(), name='edit_sharp'),
    path('sharp/<int:spare_part_id>/delete',  SHARPDeleteView.as_view(), name='sharp_delete_product'),

    # melanakia
    path('melanakia/', ΜΕΛΑΝΑΚΙΑListView.as_view(), name='melanakia'),
    path('melanakia-json', ΜΕΛΑΝΑΚΙΑ_json, name='melanakia_json'),
    path('add_melanakia/', ΜΕΛΑΝΑΚΙΑCreateView.as_view(), name='add_melanakia'),
    path('melanakia/<int:spare_part_id>', ΜΕΛΑΝΑΚΙΑUpdateView.as_view(), name='edit_melanakia'),
    path('melanakia/<int:spare_part_id>/delete', ΜΕΛΑΝΑΚΙΑDeleteView.as_view(), name='melanakia_delete_product'),
    # ΜΕΛΑΝΟΤΑΙΝΙΕΣ
    path('melanotainies/', ΜΕΛΑΝΟΤΑΙΝΙΕΣListView.as_view(), name='melanotainies'),
    path('melanotainies-json', ΜΕΛΑΝΟΤΑΙΝΙΕΣ_json, name='melanotainies_json'),
    path('add_melanotainies/', ΜΕΛΑΝΟΤΑΙΝΙΕΣCreateView.as_view(), name='add_melanotainies'),
    path('melanotainies/<int:spare_part_id>', ΜΕΛΑΝΟΤΑΙΝΙΕΣUpdateView.as_view(), name='edit_melanotainies'),
    path('melanotainies/<int:spare_part_id>/delete', ΜΕΛΑΝΟΤΑΙΝΙΕΣDeleteView.as_view(), name='melanotainies_delete_product'),
    # toner
    path('toner/', ΤΟΝΕΡListView.as_view(), name='toner'),
    path('toner-json', ΤΟΝΕΡ_json, name='toner_json'),
    path('add_toner/', ΤΟΝΕΡCreateView.as_view(), name='add_toner'),
    path('toner/<int:spare_part_id>', ΤΟΝΕΡUpdateView.as_view(), name='edit_toner'),
    path('toner/<int:spare_part_id>/delete', ΤΟΝΕΡDeleteView.as_view(), name='toner_delete_product'),
    # ΦΩΤΟΤΥΠΙΚΑ
    path('fototypika/', ΦΩΤΟΤΥΠΙΚΑListView.as_view(), name='fototipika'),
    path('fototypika-json', ΦΩΤΟΤΥΠΙΚΑ_json, name='fototipika_json'),
    path('add_fototypika/', ΦΩΤΟΤΥΠΙΚΑCreateView.as_view(), name='add_fototipika'),
    path('fototypika/<int:spare_part_id>', ΦΩΤΟΤΥΠΙΚΑUpdateView.as_view(), name='edit_fototipika'),
    path('fototypika/<int:spare_part_id>/delete', ΦΩΤΟΤΥΠΙΚΑDeleteView.as_view(), name='fototipika_delete_product'),
    # Παραγγελίες
    path('xxx/', ΧΧΧListView.as_view(), name='xxx'),
    path('add_xxx/', ΧΧΧCreateView.as_view(), name='add_xxx'),
    path('xxx/<int:spare_part_id>', ΧΧΧUpdateView.as_view(), name='edit_xxx'),
    path('xxx/<int:spare_part_id>/delete', XXXDeleteView.as_view(), name='xxx_delete_product'),
]
