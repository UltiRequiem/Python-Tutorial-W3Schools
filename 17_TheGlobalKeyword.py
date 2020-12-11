def myfunc():
  global x #esto es lo que hace que la variable sea global y no solo sirva en la funcion
  x = "fantastic"
  print("Esto se imprime por una funcion!")

myfunc()

print("Python is " + x)


