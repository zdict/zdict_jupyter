from ipykernel.kernelapp import IPKernelApp
from .kernel import ZdictKernel

IPKernelApp.launch_instance(kernel_class=ZdictKernel)
