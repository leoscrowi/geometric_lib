# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (ah)/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
___

## Circle examples:
```python
import circle

r = 2
circle_area = circle.area(r)
circle_perimeter = circle.perimeter(r)
print("Area: ", circle_area, "\nPerimeter: ", circle_perimeter)
```
___
## Rectangle examples:
```python
import rectangle

a, b = 2, 3
rectangle_area = rectangle.area(r)
rectangle_perimeter = rectangle.perimeter(r)
print("Area: ", rectangle_area, "\nPerimeter: ", rectangle_perimeter)
```
___
## Square examples:
```python
import square

a = 4
square_area = square.area(r)
square_perimeter = square.perimeter(r)
print("Area: ", square_area, "\nPerimeter: ", square_perimeter)
```
___
## Triangle examples:
```python
import triangle

a = 4
b = 2
c = 3
triangle_area = triangle.area(r)
triangle_perimeter = triangle.perimeter(r)
print("Area: ", triangle_area, "\nPerimeter: ", triangle_perimeter)
```


## Commits history
```bash
commit 4d791698462e5c40cd80c4c903621ec89bcdd92a (HEAD -> new_features_408770)
Author: Leonid <leonidkimschool@gmail.com>
Date:   Fri Oct 11 16:56:44 2024 +0300

    rectangle.py and triangle.py added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300
```

## К решению приложены тесты, команды для тестов:
circle.py : python.exe -m unittest circle.py
rectangle.py: python.exe -m unittest rectangle.py
square.py: python.exe -m unittest square.py
triangle.py: python.exe -m unittest triangle.py