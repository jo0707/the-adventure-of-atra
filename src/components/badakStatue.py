from src.components.interactableItem import InteractableItem

class BadakStatue(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/badakStatue.png", x, y, 240, 300,
            title="Patung Badak", 
            description="Badak Sumatera, si mungil berambut yang terancam punah, merupakan harta karun dari hutan hujan dan pegunungan Sumatera dan Kalimantan. Populasinya yang kritis, kurang dari 100 ekor, berjuang melawan perburuan liar dan hilangnya habitat. Ciri khas dua culanya menjadikannya target para pemburu, mendorong upaya pelestarian gigih oleh organisasi seperti Yayasan Badak Indonesia. Masa depan Badak Sumatera bergantung pada kelestarian habitatnya dan perlindungan dari ancaman manusia. Melestarikan mereka berarti melindungi kekayaan alam Indonesia yang unik.",
            realImageName="badakSumatera.png"
        )                 
        self.rect.center = (x, y)