#include <Python.h>
#include <stdio.h>
void print_python_string(PyObject *p)
{
	int is_str;
	Py_ssize_t size;
	is_str = PyUnicode_Check(p);
	printf("[.] string object info\n");
	if (is_str)
	{
		/*printf("  length: %lu\n", ((PyASCIIObject *)(p))->length);*/
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %lu\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &size));

	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
