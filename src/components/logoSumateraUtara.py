
from src.components.interactableItem import InteractableItem

class LogoSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/logoSumut.png", x, y, 0, 0, 1,
                            title="Sumatera Utara",
                            description="""Sumatera Utara (disingkat Sumut) adalah sebuah provinsi yang berada di bagian utara Pulau Sumatra. Provinsi ini beribu kota di Kota Medan. Sumatera Utara merupakan provinsi dengan jumlah penduduk terbesar keempat di Indonesia, setelah Provinsi Jawa Barat, Jawa Timur, dan Jawa Tengah, dan terbanyak di Pulau Sumatera. Penduduk Sumatera Utara berjumlah 15.5 juta jiwa, dengan kepadatan penduduk 210 jiwa/km2. mayoritas penduduk Sumatera Utara adalah suku Batak.""",
                            realImageName="logoSumut.png"
                         )