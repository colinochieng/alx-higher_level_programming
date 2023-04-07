#include <stdio.h>
#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object.
 * @p: Pointer to the Python string object.
 */
void print_python_string(PyObject *p)
{
	long int str_len;

	/* Print header */
	printf("[.] string object info\n");

	/* Check if object is a string */
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Get string length */
	str_len = PyUnicode_GET_LENGTH(p);

	/* Determine if string is compact ASCII or compact Unicode */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	/* Print string length and value */
	printf("  length: %ld\n", str_len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &str_len));
}
