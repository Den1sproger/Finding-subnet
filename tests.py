import unittest

from find_subnet import get_min_subnet



class TestRegression(unittest.TestCase):
    
    def test_single_ip(self):
        ip_list = ['192.10.2.1']
        result = get_min_subnet(ip_list)
        self.assertEqual(result, '192.10.2.1/32')


    def test_multi_ip(self):
        ip_list = ['192.168.1.2', '192.168.1.3', '192.168.1.5']
        result = get_min_subnet(ip_list)
        self.assertEqual(result, '192.168.1.0/29')


    def test_multi_ip_2octets(self):
        ip_list = ['192.168.1.2', '192.168.1.3',
                   '192.168.3.15', '192.168.5.10']
        result = get_min_subnet(ip_list)
        self.assertEqual(result, '192.168.0.0/21')


    def test_multi_ip_3octets(self):
        ip_list = ['192.135.1.2', '192.168.5.3',
                   '192.168.3.15', '192.170.5.10']
        result = get_min_subnet(ip_list)
        self.assertEqual(result, '192.128.0.0/10')


    def test_multi_ip_4octets(self):
        ip_list = ['145.135.1.2', '192.168.5.3',
                   '192.168.3.15', '227.170.5.10']
        result = get_min_subnet(ip_list)
        self.assertEqual(result, '128.0.0.0/1')


    def test_multi_ipv6(self):
        ip_list = [
            'ffe0::1:0:0:0',
            'ffe0::2:0:0:0',
            'ffe0::4:0:0:0',
            'ffe0::8:0:0:0',
            'ffe0::10:0:0:0',
            'ffe0::20:0:0:0',
            'ffe0::40:0:0:0',
            'ffe0::80:0:0:0',
        ]
        result = get_min_subnet(ip_list, 6)
        self.assertEqual(result, 'ffe0::/72')



class TestCornerCases(unittest.TestCase):

    def test_empty_ip_list(self):
        with self.assertRaises(Exception):
            ip_list = []
            get_min_subnet(ip_list)


    def test_invalid_ip(self):
        with self.assertRaises(ValueError):
            ip_list = ['invalid_ip']
            get_min_subnet(ip_list)


    def test_ip_version_mismatch(self):
        with self.assertRaises(ValueError):
            ip_list = ['ffe0::40:0:0:0', 'ffe0::80:0:0:0']
            get_min_subnet(ip_list, 4)

        with self.assertRaises(ValueError):
            ip_list = ['192.168.1.2', '192.168.1.3',]
            get_min_subnet(ip_list, 6)
    


if __name__ == '__main__':
    unittest.main()

