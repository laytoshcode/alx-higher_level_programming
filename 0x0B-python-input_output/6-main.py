[A[A[A[A[A[B[B[B[B[C[C[C[C[C[C[C[C[C[C[vi cat 6-main.py[D[D[D[D[D[D[D[D[D[D[D[C[C[C[C[C[C[C[C[C[C[C[C[C[C6-main.py

[A[A[C[C[C[C[Cvi [C[C[C[C[C[Cvi 6-main.py




[A[A[A[A[A[Ccat [C[C[C[C[C[Ccat 6-main.py[D[D[D[D[D[D[Dcat 6-main.py[cat > 6-main.py

[A
[D[A
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
