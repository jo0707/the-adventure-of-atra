from src.components.interactableItem import InteractableItem

class GajahStatue(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/gajahStatue.png", x, y, 240, 300,
            title="Gajah", 
            description="Gajah Sumatera, raksasa dengan kulit coklat kemerahan dan gading pendek pada jantan, hanya ditemukan di pulau Sumatera. Sayangnya, populasinya yang diperkirakan sekitar 924-1359 individu terancam punah akibat perburuan, hilangnya habitat, dan konflik dengan manusia. Upaya pelestarian seperti taman nasional dan patroli hutan terus dilakukan, karena Gajah Sumatera esensial bagi keseimbangan alam dan bermanfaat bagi masyarakat. Melestarikan mereka berarti menjaga warisan alam yang berharga untuk generasi mendatang.",
            realImageName='assets/images/real/gajahSumatera.png'
        )                 
        self.rect.center = (x, y)