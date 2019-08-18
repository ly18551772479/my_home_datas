# 给python程序传递参数

```python

import sys
if __name__ == '__main__':
    print(sys.argv)
```

运行方式1:
```python

python3 main_argv.py 
```

运行结果1:

```python
['main_argv.py']
```

运行方式2:
```python

python3 main_argv.py 11 22 33
```

运行结果2:

```python
['main_argv.py', '11', '22', '33']
```