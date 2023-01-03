class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        return input_str[::-1]

    def find_longest_word(self, sentence: str) -> str:
        a=''
        for i in sentence.split():
            if len(i)>len(a):
                 a=i
        return a

    def reverse_list(self, input_list: list) -> list:
        lis=input_list.reverse()
        return lis

    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        return input_list.count(number_to_be_counted)