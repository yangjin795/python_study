import array
import tempfile

arr = array.array('i', range(10))
out = tempfile.NamedTemporaryFile()
arr.tofile(out.file)
out.flush()

with open(out.name, 'rb') as inf:
    arrayin = array.array('i')
    arrayin.fromfile(inf, len(arr))
    print arrayin
