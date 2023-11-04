
from varasto import Varasto

def create_varasto():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def print_initial(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def print_olut_getters(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_setters(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def handle_minus_varasto():
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

def handle_minus_saldo():
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def handle_olutta_liikaa(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def handle_mehua_liian_vahan(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def handle_olutta_liian_vahan(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def handle_mehua_liikaa(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    mehua, olutta = create_varasto()
    print_initial(mehua, olutta)
    print_olut_getters(olutta)
    mehu_setters(mehua)
    handle_minus_varasto()
    handle_minus_saldo()
    handle_olutta_liikaa(olutta)
    handle_mehua_liian_vahan(mehua)
    handle_olutta_liian_vahan(olutta)
    handle_mehua_liikaa(mehua)

if __name__ == "__main__":
    main()
