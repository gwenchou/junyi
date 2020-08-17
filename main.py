def reverse_string(string: str):
    str_to_list = list(string)
    str_to_list.reverse()

    return ''.join(str_to_list)

def reverse_word_in_sentence(sentence: str):
    splitted_sentence = sentence.split(' ')

    return ' '.join([reverse_string(word) for word in splitted_sentence])

def test_2(input: int):
    count_of_multiple_fifteen = int(input / 15)

    count_of_multiple_three = int(input/3) - count_of_multiple_fifteen
    count_of_multiple_five = int(input/5) - count_of_multiple_fifteen

    return input - count_of_multiple_three - count_of_multiple_five

def test_3():
    answer = """
        1. 先拿標示有混合的袋子，若拿到：
            鉛筆：
                標示混合的這個袋子只裝鉛筆，因為這袋絕不是混合，也沒有拿到原子筆。
                標示原子筆的則是混合，因為他絕不是原子筆，而而鉛筆已經在標示混合的袋子拿到了
                標示鉛筆的則是原子筆，因為只剩下這個可能了
            原子筆：
                標示混合的這個袋子只裝原子筆，因為這袋絕不是混合，也沒有拿到鉛筆。
                標示鉛筆的則是混合，因為他絕不是鉛筆，而原子筆已經在標示混合的袋子拿到了
                標示原子筆的則是鉛筆，因為只剩下這個可能了
    """

    print(answer)

def test_4():
    answer = """
        原本服務生應該要找 150 元給這三個人，但每個人只找給他們 30 元，服務生各從這三個人暗槓了20元走，所以：
            老闆收的錢 + (實際找的錢)*3 + 服務生的暗槓 = 900
            750 + 30*3 + 60 = 900
     """

    print(answer)
