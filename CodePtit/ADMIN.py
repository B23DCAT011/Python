import os

def tao_file_py(prefix="PY01", start=1, end=100, folder="."):
    import os
    os.makedirs(folder, exist_ok=True)

    for i in range(start, end + 1):
        filename = os.path.join(folder, f"{prefix}{i:03}.py")
        open(filename, "w").close()

def xoa_file_py(prefix="PY01", start=2, end=100, folder="."):
    import os
    for i in range(start, end + 1):
        filename = os.path.join(folder, f"{prefix}{i:02}.py")
        if os.path.exists(filename):
            os.remove(filename)


tao_file_py(prefix="PY01", start=51, end=76)
#xoa_file_py(prefix="PY01", start=51, end=76)
