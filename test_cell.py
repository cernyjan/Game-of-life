import unittest
import cell


class Test(unittest.TestCase):
    def test_validate_type(self):
        c = cell.Cell(True)
        self.assertEqual(True, c.validate_type(10, int))
        self.assertEqual(False, c.validate_type("text", int))

    def test_create_cell(self):
        c = cell.Cell(True)
        self.assertEqual(True, c.get_life())
        c = cell.Cell(False)
        self.assertEqual(False, c.get_life())
        c = cell.Cell("text")
        self.assertEqual(False, c.get_life())
    
    def test_set_neighbors(self):
        c = cell.Cell(True)
        c.set_neighbors(8)
        self.assertEqual(8, c.get_neighbors())
        c = cell.Cell(True)
        with self.assertRaises(Exception) as context:
            c.set_neighbors(-2)
        self.assertTrue('Value has to be >= 0' in context.exception)
        with self.assertRaises(Exception) as context:
            c.set_neighbors("text")
        self.assertTrue('Value has to be >= 0' in context.exception)


           
if __name__ == "__main__":
    unittest.main()
