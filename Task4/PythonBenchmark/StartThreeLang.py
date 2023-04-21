from subprocess import Popen, PIPE
import os


python_launch = Popen(['PythonBenchmark', os.path.abspath('PythonBenchmark/LaunchBenchmark.py')],
                      stdout=PIPE, stdin=PIPE)
print('Python Benchmark is launched')
java_launch = Popen(['JavaBenchmark', '-jar', os.path.abspath('java.jar')], stdout=PIPE, stdin=PIPE)
print('Java Benchmark is launched')
csharp_launch = Popen([os.path.abspath('x64/CSharpBenchmark.exe')], stdout=PIPE, stdin=PIPE)
print('C Sharp Benchmark is launched')


