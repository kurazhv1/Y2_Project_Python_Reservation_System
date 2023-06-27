import unittest
import check_reservation

class Test(unittest.TestCase):
    def test_dates(self):
        self.assertTrue(check_reservation.check_date_format("22.12.2022","23.12.2022"))
        self.assertFalse(check_reservation.check_date_format("23.12.2022","20.12.2022"))
        self.assertFalse(check_reservation.check_date_format("22.12.2022", "20.11.2022"))
        self.assertFalse(check_reservation.check_date_format("1d.12.1yyy","20.09.2023"))
        self.assertFalse(check_reservation.check_date_format("20.10.2021","21.11.2022"))
        self.assertTrue(check_reservation.check_date_format("25.12.2022", "25.12.2022"))
        self.assertFalse(check_reservation.make_reserv("10.05.2022","02.06.2022","1"))
        self.assertTrue(check_reservation.make_reserv("20.12.2022", "25.12.2022", "1"))
if __name__ == '__main__':
    unittest.main()