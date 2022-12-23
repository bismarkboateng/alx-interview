Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:<br>
<hr>
Returns an empty list if n <= 0<br>
You can assume n will be always an integer<br>
guillaume@ubuntu:~/0x00$ cat 0-main.py<br>
#!/usr/bin/python3<br>
"""<br>
0-main<br>
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle<br>

def print_triangle(triangle):<br>
    """
    Print the triangle<br>
    """
    for row in triangle:<br>
        print("[{}]".format(",".join([str(x) for x in row])))<br>


if __name__ == "__main__":<br>
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ <br>
guillaume@ubuntu:~/0x00$ ./0-main.py<br>
[1]<br>
[1,1]<br>
[1,2,1]<br>
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
