#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - C function that prints some
 *basic info about Python lists
 * @p: python object.
 *Return: 0
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int i;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, ((PyList_GetItem(p, i))->ob_type)->tp_name);
	}
}
