import os
import sys
from decimal import Decimal
from pathlib import Path

import django


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecom.settings")
django.setup()

from shop.models import Product


KEYBOARD_IMAGE = "/static/shop/img.webp"
MOUSE_IMAGE = "/static/shop/mose.jpg"
BLUETOOTH_IMAGE = "/static/shop/Bluetooth.webp"
AuroraMechanicalKEYBOARD_IMAGE ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnlEgcNbr10ePxnCTEML_q_dDHdYWPKBQmGuv1Y3sRIw&s"
CloudWaveWirelessMouse_IMAGE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjn3qhmMWbf1EyFEfbV6j671HLiaT6Khif9xnNCVH4ng&s=10"      
NeonGlowNoise_IMAGE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0Xdui4PHeMbSQ4br9qJaIJOB6JiDQjR2d6Z_tEt_tUA&s=10"      
TitanFitErgonomic_DeskChair_IMAGE = "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTblplqmZlLmFj57LphIKBmUm1HOTAV84kqYGdwwUsWuxfuyzN34WmaLydnE0GPdGntqQkJBGQis_CNB_1Kg85R4Ql2yMVDnrsLBlb_OtK0Mtg2lo_xHuGVVrI7dOS25UFbsMpFww&usqp=CAc"
PixelPro_IMAGE = "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcR72xOZj9jLD98p0QmGRKqfRqmt1F9DAHhgfJdm0XcfI5zYm2sqICOugT-1D0jsq4vamgwNJ5o2vDOPzU29liGxDBifUKEAFXJ4Mf-VQ4yxOlKPuISvvllr-ymkGPaHxIJSrQ&usqp=CAc"     
ChargeMateCharger_IMAGE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ62RvWNVKrYd-6A41sC0gL9vVYHMTgXlpfSqJPrPb_aQ&s=10"  
OrbitSmartStandingDesk_IMAGE = "data:image/webp;base64,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"
LumenLEDDeskLamp_IMAGE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-nJrCbhu9piXQjbozwj7ZJ71Vd5r2WZkHYqQrEu9XOw&s=10"
BreezeAirCoolingFan_IMAGE = "https://m.media-amazon.com/images/I/71NQp4AQeLS._AC_UF894,1000_QL80_.jpg"    
StreamLiteWebcam_IMAGE = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSH3IFwR_bXFPMLZMdq_NXcgvgZtVa0USPW4nfB630p_w&s=10"
SoundBloomPortableSpeaker_IMAGE = "https://cdn.moglix.com/p/eo5ZqwQcFNZ1W-large.jpg" 
SteelGrainUSBHub_IMAGE = "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRtf6R9m-SniU4kY8A73aqiG-ULWDdBqCMg6iekkgnDJwotxYtmVKYaWj21gMWDcRCiJ9yt8ljlNQhFt0lVFQvYgZGU8yMtsIa1U4aNVR1aTy2bODdjmD7PpNoYD2VdrjS8Wg8DAA&usqp=CAc"



PRODUCTS = [
    {
        "name": "Keyboard",
        "description": "A mechanical keyboard with customizable RGB lighting and tactile switches for a satisfying typing experience.",
        "price": Decimal("79.99"),
        "image_url": KEYBOARD_IMAGE,
    },
    {
        "name": "Mouse",
        "description": "Ergonomic wireless mouse with adjustable DPI and programmable buttons for enhanced productivity.",
        "price": Decimal("49.99"),
        "image_url": "/static/shop/mose.jpg",
    },
    {
        "name": "Headphones",
        "description": "Rich sound, deep bass, and comfortable padding for long sessions.",
        "price": Decimal("129.00"),
        "image_url": BLUETOOTH_IMAGE,
    },
    {
        "name": "Aurora Mechanical Keyboard",
        "description": "Hot-swappable switches, PBT keycaps, and smooth keystrokes for everyday coding.",
        "price": Decimal("89.99"),
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnlEgcNbr10ePxnCTEML_q_dDHdYWPKBQmGuv1Y3sRIw&s",
    },
    {
        "name": "CloudWave Wireless Mouse",
        "description": "Ergonomic design with precise tracking and a silent click experience.",
        "price": Decimal("24.50"),
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjn3qhmMWbf1EyFEfbV6j671HLiaT6Khif9xnNCVH4ng&s=10",
    },
    {
        "name": "NeonGlow Noise-Cancelling Headphones",
        "description": "Rich sound, deep bass, and comfortable padding for long sessions.",
        "price": Decimal("129.00"),
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0Xdui4PHeMbSQ4br9qJaIJOB6JiDQjR2d6Z_tEt_tUA&s=10",
    },
    {
        "name": "TitanFit Ergonomic Desk Chair",
        "description": "Supportive lumbar curve with breathable fabric and adjustable armrests.",
        "price": Decimal("179.95"),
        "image_url": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTblplqmZlLmFj57LphIKBmUm1HOTAV84kqYGdwwUsWuxfuyzN34WmaLydnE0GPdGntqQkJBGQis_CNB_1Kg85R4Ql2yMVDnrsLBlb_OtK0Mtg2lo_xHuGVVrI7dOS25UFbsMpFww&usqp=CAc",
    },
    {
        "name": 'PixelPro 27" 4K Monitor',
        "description": "Crisp 4K visuals with vivid color and an eye-friendly panel.",
        "price": Decimal("299.99"),
        "image_url": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcR72xOZj9jLD98p0QmGRKqfRqmt1F9DAHhgfJdm0XcfI5zYm2sqICOugT-1D0jsq4vamgwNJ5o2vDOPzU29liGxDBifUKEAFXJ4Mf-VQ4yxOlKPuISvvllr-ymkGPaHxIJSrQ&usqp=CAc",
    },
    {
        "name": "ChargeMate 65W USB-C Charger",
        "description": "Fast, compact charging for laptops and phones, reliable all day.",
        "price": Decimal("39.99"),
        "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ62RvWNVKrYd-6A41sC0gL9vVYHMTgXlpfSqJPrPb_aQ&s=10",
    },
    {
        "name": "OrbitSmart Standing Desk",
        "description": "Smooth electric height adjustment with a durable steel frame.",
        "price": Decimal("399.00"),
        "image_url": "data:image/webp;base64,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",
    },
    {
        "name": "LumenLED Desk Lamp",
        "description": "Warm-to-cool dimming with a minimal design that reduces glare.",
        "price": Decimal("32.75"),
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-nJrCbhu9piXQjbozwj7ZJ71Vd5r2WZkHYqQrEu9XOw&s=10",
    },
    {
        "name": "BreezeAir Cooling Fan",
        "description": "Quiet airflow and adjustable speeds for a comfortable workspace.",
        "price": Decimal("18.99"),
        "image_url":"https://m.media-amazon.com/images/I/71NQp4AQeLS._AC_UF894,1000_QL80_.jpg",
    },
    {
        "name": "StreamLite Webcam",
        "description": "Sharp 1080p video with built-in privacy cover and auto-focus.",
        "price": Decimal("54.25"),
        "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSH3IFwR_bXFPMLZMdq_NXcgvgZtVa0USPW4nfB630p_w&s=10",
    },
    {
        "name": "SoundBloom Portable Speaker",
        "description": "Big sound in a compact body with punchy bass and clean mids.",
        "price": Decimal("46.00"),
        "image_url":"https://cdn.moglix.com/p/eo5ZqwQcFNZ1W-large.jpg",
    },
    {
        "name": "SteelGrain USB Hub (7-in-1)",
        "description": "Expand your ports with reliable data transfer for daily use.",
        "price": Decimal("22.49"),
        "image_url": "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRtf6R9m-SniU4kY8A73aqiG-ULWDdBqCMg6iekkgnDJwotxYtmVKYaWj21gMWDcRCiJ9yt8ljlNQhFt0lVFQvYgZGU8yMtsIa1U4aNVR1aTy2bODdjmD7PpNoYD2VdrjS8Wg8DAA&usqp=CAc",
    },
]


def main():
    for product in PRODUCTS:
        Product.objects.update_or_create(
            name=product["name"],
            defaults={
                "description": product["description"],
                "price": product["price"],
                "image_url": product["image_url"],
            },
        )

    print(f"Seeded {len(PRODUCTS)} products.")


if __name__ == "__main__":
    main()
