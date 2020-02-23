import unittest
from CompareVersions import CompareVersions


class CompareVersionsTest(unittest.TestCase):
    def test_compare_versions(self):
        compare_versions = CompareVersions("1.2.3", "1.2").compare_version()
        self.assertGreater(compare_versions, 0)

        compare_versions = CompareVersions("1.1", "1.2").compare_version()
        self.assertLess(compare_versions, 0)

        compare_versions = CompareVersions("1.2.3", "1.2.3").compare_version()
        self.assertEqual(compare_versions, 0)

        compare_versions = CompareVersions("2.3", "2.4").compare_version()
        self.assertLess(compare_versions, 0)

        compare_versions = CompareVersions("0.3", "0.3.5").compare_version()
        self.assertLess(compare_versions, 0)

        compare_versions = CompareVersions("1.1.1.0", "1.1.1").compare_version()
        self.assertEqual(compare_versions, 0)


if __name__ == "__main__":
    unittest.main()
