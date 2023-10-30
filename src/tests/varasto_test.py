import unittest
from varasto import Varasto
from io import StringIO
from unittest.mock import patch


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus(self): 
        self.varasto = Varasto(-2)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_virheellinen_saldo(self):
        self.varasto = Varasto(10, -2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_virheellinen_lisays_epaonnistuu(self):
        self.varasto.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_oikea_lisays_onnistuu(self):
        self.varasto.saldo = 4

        self.varasto.lisaa_varastoon(3)
        self.assertAlmostEqual(self.varasto.saldo, 7)

    def test_saldo_on_rajoitettu_tilavuuteen(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_negatiivinen(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-2), 0)

    def test_palauta_saldo(self):
        self.varasto.saldo = 7
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 7)

    def test_printtaus(self):
        expected_output = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(self.varasto)
            self.assertEqual(fake_output.getvalue(), expected_output)

