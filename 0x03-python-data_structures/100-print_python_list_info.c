#include <Python.h>
#include <object.h>
#include <listobject.h>


void print_python_list_info(PyObject *p)
{
	int i;
	int size = PyList_Size(p);
	PyObject *obj;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
