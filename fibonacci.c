#include <Python.h>

// C implementation of the Fibonacci function
long fibonacci(long n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Wrapper function to expose fibonacci to Python
static PyObject* fibonacci_wrapper(PyObject* self, PyObject* args) {
    long n;
    if (!PyArg_ParseTuple(args, "l", &n)) {
        return NULL;
    }
    return PyLong_FromLong(fibonacci(n));
}

// Method definition for the module
static PyMethodDef FibonacciMethods[] = {
    {"fibonacci", fibonacci_wrapper, METH_VARARGS, "Calculate the nth Fibonacci number."},
    {NULL, NULL, 0, NULL}  // Sentinel
};

// Module initialization function
static struct PyModuleDef fibomodule = {
    PyModuleDef_HEAD_INIT,
    "fibonacci",  // Module name
    NULL,         // Module documentation
    -1,           // Size of per-interpreter state of the module
    FibonacciMethods
};

// Module initialization macro
PyMODINIT_FUNC PyInit_fibonacci(void) {
    return PyModule_Create(&fibomodule);
}
