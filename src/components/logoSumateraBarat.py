
from src.components.interactableItem import InteractableItem

class LogoSumateraBarat(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/logoSumbar.png", x, y, 0, 0, 1, 
                            title="Sumatera Barat",
                            description="""Sumatera Barat (disingkat Sumbar) adalah sebuah provinsi di Indonesia yang terletak di Pulau Sumatra dengan ibu kota Padang. Provinsi Sumatera Barat terletak sepanjang pesisir barat Sumatra bagian tengah, dataran tinggi Bukit Barisan di sebelah timur, dan sejumlah pulau di lepas pantainya seperti Kepulauan Mentawai. Dari utara ke selatan, provinsi dengan wilayah seluas 42 ribu km^2. Provinsi ini berbatasan dengan empat provinsi, yakni Sumatera Utara, Riau, Jambi, dan Bengkulu.""",
                            realImageName="logoSumbar.png"
                         )