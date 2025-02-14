import os
import sys
import time
import shutil
import unittest
import subprocess
import test.conftest
from sort import alphanumeric_sort, MAX_INPUT_SIZE


class TestSort(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(alphanumeric_sort(""), "")

    def test_numbers_only(self):
        self.assertEqual(alphanumeric_sort("4321"), "4321")

    def test_uppercase_and_lowercace_letters_only(self):
        self.assertEqual(alphanumeric_sort("bCaD"), "abCD")

    def test_lowercase_letters_only(self):
        self.assertEqual(alphanumeric_sort("zggwa"), "aggwz")

    def test_uppercase_letters_only(self):
        self.assertEqual(alphanumeric_sort("FJKE"), "EFJK")

    def test_mixed_characters(self):
        self.assertEqual(alphanumeric_sort("A04B2a1"), "1204aAB")

    def test_with_special_characters(self):
        self.assertEqual(alphanumeric_sort("!3aB@1cA2"), "123acAB!@")

    def test_special_characters_only(self):
        self.assertEqual(alphanumeric_sort(",.!@%"), "!%,.@")

    def test_utf8_encoding(self):
        text = "aЯbΑ漢zé2Я1".encode("utf-8").decode("utf-8")
        self.assertEqual(alphanumeric_sort(text), "12abzéΑЯЯ漢")

    def test_latin1_encoding(self):
        text = "éèàçô".encode("latin-1").decode("latin-1")
        self.assertEqual(alphanumeric_sort(text), "àçèéô")

    def test_windows1252_encoding(self):
        text = "ØÆÅ".encode("windows-1252").decode("windows-1252")
        self.assertEqual(alphanumeric_sort(text), "ÅÆØ")

    def test_shift_jis_encoding(self):
        text = "カタカナ".encode("shift_jis").decode("shift_jis")
        self.assertEqual(alphanumeric_sort(text), "カカタナ")

    def test_mixed_encoding(self):
        text = "AéЯΩ2".encode("utf-8").decode("utf-8")
        self.assertEqual(alphanumeric_sort(text), "2éAΩЯ")

    def test_exceeds_max_size(self):
        oversized_input = "9" * (MAX_INPUT_SIZE + 1)
        with self.assertRaises(ValueError) as context:
            alphanumeric_sort(oversized_input)
        self.assertIn("Input is too large", str(context.exception))

    def test_maximum_input_performance(self):
        max_digits = sys.get_int_max_str_digits()
        large_input = "A" * MAX_INPUT_SIZE
        start_time = time.time()
        sorted_output = alphanumeric_sort(large_input)
        duration = time.time() - start_time
        self.assertEqual(len(sorted_output), len(large_input))


if __name__ == "__main__":
    unittest.main()
