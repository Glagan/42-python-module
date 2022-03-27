class Evaluator:
    @staticmethod
    def zip_evaluate(coeffs: list, words: list) -> float:
        if not isinstance(words, list) or not isinstance(coeffs, list):
            return -1
        if len(words) != len(coeffs):
            return -1
        result = 0
        for word, coeff in zip(words, coeffs):
            if not isinstance(word, str) or not isinstance(coeff, float):
                print('ERROR')
                return -1
            result += (len(word) * coeff)
        return result

    @staticmethod
    def enumerate_evaluate(coeffs: list, words: list) -> float:
        if not isinstance(words, list) or not isinstance(coeffs, list):
            return -1
        if len(words) != len(coeffs):
            return -1
        result = 0
        for i, word in enumerate(words):
            if not isinstance(word, str) or not isinstance(coeffs[i], float):
                print('ERROR')
            result += (len(word) * coeffs[i])
        return result
