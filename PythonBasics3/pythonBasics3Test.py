import unittest

import pythonBasics3

class TestPythonBasicsOne(unittest.TestCase):

#Test case for ends_with_consonant
    def test_ends_with_consonant(self):

        self.assertEqual(pythonBasics3.ends_with_consonant("Once upon a dark, cold night"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("What did Steve just say"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("I once swam with sharks"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("Do I know how old you are you"), False)

        self.assertEqual(pythonBasics3.ends_with_consonant("Has anyone ever as far even wanted to go do look more like"), False)

        self.assertEqual(pythonBasics3.ends_with_consonant("Who was phone"), False)

        self.assertEqual(pythonBasics3.ends_with_consonant("The dog is actually not a dog, but a BIG dog"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("What was their name again"), True)
        
        # Please add three more test cases following the order above

#Test case for ends_with_number
    def test_ends_with_number(self):

        self.assertEqual(pythonBasics3.ends_with_number("What is 3/10"), True)

        self.assertEqual(pythonBasics3.ends_with_number("It was not a cat"), False)

        self.assertEqual(pythonBasics3.ends_with_number("I once swam with sharks"), False)

        self.assertEqual(pythonBasics3.ends_with_number("Blue plus purple equals 5"), True)

        self.assertEqual(pythonBasics3.ends_with_number("This test will fail1"), True)

        self.assertEqual(pythonBasics3.ends_with_number("Bro I swear there were 13 slices of pizza cmon"), False)

        self.assertEqual(pythonBasics3.ends_with_number("In the end there were 2"), True)

        # Please add three more test cases following the order above


#Test case for binary_multiple_of_6
    def test_binary_multiple_of_6(self):

        self.assertEqual(pythonBasics3.binary_multiple_of_6("100101"), False)

        self.assertEqual(pythonBasics3.binary_multiple_of_6("110"), True)

        self.assertEqual(pythonBasics3.binary_multiple_of_6("111111"), False)

        self.assertEqual(pythonBasics3.binary_multiple_of_6("3"), False)



if __name__ == '__main__':

  unittest.main(verbosity=1)

