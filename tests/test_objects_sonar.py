import unittest
import sys
import os
sys.path.append(os.path.join(os.path.abspath(os.path.curdir), "bsl-objects-to-analyze-sonar"))
import objects_sonar


class TestCheckArgs(unittest.TestCase):

    # def test_get_parser(self):
    #     parser = objects_sonar.create_parser()
    #     a = 1
    #     isinstance(parser, object)

    def test_simple_case(self):
        self.assertEqual(9, 9, 'it\'s okay')


if __name__ == "__main__":
    unittest.main()
