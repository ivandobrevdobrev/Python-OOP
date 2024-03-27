from unittest import TestCase,main

from Test_Integer_List_3.integer_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.i_list = IntegerList(5.5,2,1,3,"hello")

    def test_correct_init_ignores_non_int_values(self):
        self.assertEqual([2,1,3],self.i_list.get_data())  # tuk testwame napravo def get_data()- zashtoto __data e private

    def test_add_non_integer_to_the_list_raises_value_error(self):
        with self.assertRaises(ValueError) as v:
            self.i_list.add(5.5)
        self.assertEqual("Element is not Integer",str(v.exception))

    def test_add_integer_if_adds_integer_to_the_list(self):
        expected_list = self.i_list.get_data().copy() + [4] # pravim copie na list, za da ne se modificira i dobavqme cifra 4 da testvame
        self.i_list.add(4)
        self.assertEqual(expected_list,self.i_list.get_data())

    def test_remove_idx_with_out_of_range_idx_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(100)  # testvame dali moje da mahmen element na index 100
        self.assertEqual("Index is out of range",str(ie.exception))

    def test_remove_valid_element_with_valid_index(self):
        self.i_list.remove_index(1)
        self.assertEqual([2,3],self.i_list.get_data())

    def test_get_out_of_range_index(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(100)
        self.assertEqual('Index is out of range',str(ie.exception))

    def test_get_with_valid_index_returns_value_on_index(self):
        result = self.i_list.get(2)
        self.assertEqual(3,result)

    def test_insert_on_invalid_index_reaises_Index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(100,5)
        self.assertEqual("Index is out of range", str(ie.exception))
    def test_insert_on_valid_index_with_non_integer_type_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(1,6.7)
        self.assertEqual("Element is not Integer",str(ve.exception))

    def test_insert_integer_on_valid_index(self):
        expected_list = self.i_list.get_data().copy() # kopirame si pyrvo expected list
        expected_list.insert(1,5)                    # testvame da dobavim chisla
        self.i_list.insert(1,5)                      # izpylnqvame realni kod

        self.assertEqual(expected_list,self.i_list.get_data())    # sravnqvame 2ta lista

    def test_get_biggest_num(self):
        results= self.i_list.get_biggest()
        self.assertEqual(3,results)

    def test_get_index(self):
        result = self.i_list.get_index(3)
        self.assertEqual(2,result)


if __name__ == "__main__":
    main()