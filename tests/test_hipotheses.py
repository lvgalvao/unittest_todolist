from unittest import TestCase, main
from hypothesis import given, strategies

def div(x , y):
    return x / y

class TestDiv(TestCase):
    @given(strategies.integers(),strategies.integers().filter(lambda x: x>0))
    def test_div_test_da_exlosao(self,x, y):
        print(x)
        print(y)
        # self.assertEqual(div(x,y), 0.5, msg=None)
        div(x,y)


if __name__ == '__main__':
    main()
