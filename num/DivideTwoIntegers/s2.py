class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Get the sign of the result
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign

        # Find the largest multiple of the divisor that is less than or equal to the dividend
        multiple = 1
        while dividend >= (divisor << 1):
            divisor <<= 1
            multiple <<= 1

        # Perform division using binary search
        quotient = 0
        while multiple > 0:
            if dividend >= divisor:
                dividend -= divisor
                quotient += multiple
            divisor >>= 1
            multiple >>= 1

        # Apply the sign to the result
        return sign * quotient