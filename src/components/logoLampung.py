
from src.components.interactableItem import InteractableItem

class LogoLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/logoLampung.png", x, y, 0, 0, 1,
                            title="Lampung",
                            description="Provinsi Lampung, yang terletak di ujung selatan Pulau Sumatera, dikenal sebagai gerbang utama antara Pulau Jawa dan Sumatera melalui Pelabuhan Bakauheni. Dikelilingi oleh pegunungan dan pantai yang indah, Lampung menawarkan keindahan alam yang memukau, seperti Taman Nasional Way Kambas yang menjadi habitat gajah Sumatera. Selain itu, provinsi ini kaya akan budaya dan tradisi, dengan masyarakatnya yang terkenal ramah dan beragam suku, termasuk Lampung dan Jawa. Ekonomi Lampung didukung oleh pertanian, perkebunan kopi dan lada, serta perikanan. Lampung juga terkenal dengan wisata budaya seperti festival Krakatau yang mempromosikan keindahan alam dan budaya setempat.",
                            realImageName="logoLampung.png"
                         )