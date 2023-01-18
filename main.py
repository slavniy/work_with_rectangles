from PIL import Image, ImageDraw
from math import cos, sin, pi, sqrt
alf = [str(i) for i in range(1, 49 + 1)]
# Пустой желтый фон.
width = height = 500
fon_color = (255, 255, 255)
padding = 50
im = Image.new('RGB', (width, height), fon_color)
draw = ImageDraw.Draw(im)
draw.ellipse((0 + padding, 0 + padding, width - padding, height - padding), outline=(0, 0, 0), width=2)
n = 5
xc = width // 2
yc = height // 2
r = (width // 2) - padding + 10
points = []
fi = pi/n
# запоминаем точки многоугольника на окружности
for i in range(n):
    xi = xc + r * cos(fi + (2 * pi * i) / (n))
    yi = yc + r * sin(fi + (2 * pi * i) / (n))
    points.append((xi, yi))
for i in range(n):
    draw.line((points[i - 1], points[i]), fill='blue', width=2)
    draw.text(
        (points[i][0]-5,points[i][1]-5),
        alf[i],
        fill=('#1C0606')
    )
im.show()
