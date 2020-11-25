class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_real, a_imaginary = map(int, a[:-1].split('+'))
        b_real, b_imaginary = map(int, b[:-1].split('+'))
        real = a_real * b_real - a_imaginary * b_imaginary
        imaginary = a_real * b_imaginary + a_imaginary * b_real
        return '{}+{}i'.format(real, imaginary)
