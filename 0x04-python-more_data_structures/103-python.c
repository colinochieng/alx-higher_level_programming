#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: A pointer to a PyObject list object
 **/
void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size, i;
	const char *type;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = item->ob_type->tp_name;
		printf("Element %li: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: A pointer to a PyObject bytes object
 **/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	const char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %li bytes: ", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
		printf("%02x%c", str[i] & 0xff, i == size ? '\n' : ' ');
}
