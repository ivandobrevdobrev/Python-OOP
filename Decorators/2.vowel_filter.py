def vowel_filter(function):

    def wrapper():
        vowels = "AaEeIiOoUu"
        result = function()
        vowels_res = [v for v in result if v in vowels]
        return vowels_res

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
