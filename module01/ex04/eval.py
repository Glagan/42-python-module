class Evaluator:
    @staticmethod
    def zip_evaluate(coeffs: list, words: list) -> float:
        if not isinstance(words, list) or not isinstance(coeffs, list):
            return -1
        if len(words) != len(coeffs):
            return -1
        if len(words) == 0:
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
        if len(words) == 0:
            return -1
        result = 0
        for i, word in enumerate(words):
            if not isinstance(word, str) or not isinstance(coeffs[i], float):
                print('ERROR')
            result += (len(word) * coeffs[i])
        return result


if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))
