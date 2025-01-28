import taller1 as lc
import unittest

class Testcplxop(unittest.TestCase):

    def test_sumacplx(self):
        self.assertAlmostEqual(lc.sumacplx((3.5,6),(6.7,2)),(10.2, 8))
        self.assertAlmostEqual(lc.sumacplx((3.5, 6), (6.7, 2)), (10.2, 8))

    def test_multplx(self):
        self.assertAlmostEqual(lc.multplx((3.5, 6), (6.7, 2)), (11.45, 47.2))
        self.assertAlmostEqual(lc.multplx((3.5, 6), (-6.7, 2)), (-35.45, -33.2))

    def test_restacplx(self):
        self.assertAlmostEqual(lc.restacplx((3.5, 6), (6.7, 2)), (-3.2,4 ))
        self.assertAlmostEqual(lc.restacplx((3.5, 6), (-6.7, 3)), (10.2, 3))

    def test_divcplx(self):
        self.assertAlmostEqual(lc.divcplx((-3,-5),(-1,2)),(-1.4, 2.2))
        self.assertAlmostEqual(lc.divcplx((3, 6), (-6, 2)), (-0.15, -1.05 ))

    def test_conjugado(self):
        self.assertAlmostEqual(lc.conjugado((3.5, 6)),(3.5,-6))
        self.assertAlmostEqual(lc.conjugado((3, -12)),(3,12))

    def test_modu(self): ##perfecto
        self.assertAlmostEqual(lc.modu((1,0)),1)
        self.assertAlmostEqual(lc.modu((3,4)),5)

    def test_fas(self):
        self.assertAlmostEqual(lc.fas((2,3)),0.5880026)
        self.assertAlmostEqual(lc.fas((4, 4)), 0.78539816)

    def test_a_polar(self):
        res = lc.a_polar((2, 3))
        esperado = (3.6055512754, 0.5880026035)
        self.assertAlmostEqual(res[0], esperado[0])
        self.assertAlmostEqual(res[1], esperado[1])

        res_2 = lc.a_polar((4, 5))
        esperado_2 = (6.403124237432, 0.674740942223)
        self.assertAlmostEqual(res_2[0], esperado_2[0])
        self.assertAlmostEqual(res_2[1], esperado_2[1])

    def test_a_cartesiana(self):#####
        res = lc.a_cartesiana ((2,3))
        esperado= (-1.9799849932, 0.282240016)
        self.assertAlmostEqual(res[0],esperado[0])
        self.assertAlmostEqual(res[1],esperado[1])

        res_2 = lc.a_cartesiana((4,5))
        esperado_2 = (1.134648741852905, -3.835697098652554)
        self.assertAlmostEqual(res_2[0], esperado_2[0])
        self.assertAlmostEqual(res_2[1], esperado_2[1])



if __name__ == '__main__':
    unittest.main()