# 🐍 Python Object Types / Data Types

This section provides a concise overview of the core object types (data types) available in Python. It is intended as a quick reference for beginners.

---

## 1. Numbers

Used to represent numeric values.

```python
1234        # Integer
3.1415      # Float
3 + 4j      # Complex
0b111       # Binary integer
Decimal('1.25')   # Decimal (from decimal module)
Fraction(1, 3)    # Fraction (from fractions module)
```

---

## 2. Strings

Used to represent text (immutable sequence of characters).

```python
'spam'
"Bob's"
b'a\x01c'     # Bytes
u'sp\u00c4m'   # Unicode string
```

---

## 3. Lists

Ordered, mutable collections.

```python
[1, [2, 'three'], 4.5]
list(range(10))
```

---

## 4. Tuples

Ordered, immutable collections.

```python
(1, 'spam', 4, 'U')
tuple('spam')
namedtuple('Point', ['x', 'y'])
```

---

## 5. Dictionaries

Key–value pairs (unordered, mutable).

```python
{'food': 'spam', 'taste': 'yum'}
dict(hours=10)
```

---

## 6. Sets

Unordered collections of unique elements.

```python
set('abc')
{'a', 'b', 'c'}
```

---

## 7. Files

Used for file input/output operations.

```python
open('eggs.txt')
open(r'C:\\ham.bin', 'wb')
```

---

## 8. Boolean

Logical values.

```python
True
False
```

---

## 9. None

Represents the absence of a value.

```python
None
```

---

## 10. Callable & Structural Types

* **Functions**
* **Modules**
* **Classes**

---

## Advanced Topics (Coming Next)

* Decorators
* Generators
* Iterators
* Metaprogramming

---

📌 *This list is part of my Python learning journey and will be updated as I progress.*
