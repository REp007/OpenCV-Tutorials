from functools import reduce

strings: list[str] = ['a1','b2','c3','d4','e5']
result: float = reduce(lambda x,y: f'{x} - {y}', strings) # ((((1+2)+3)+4)+5) 

print(result)