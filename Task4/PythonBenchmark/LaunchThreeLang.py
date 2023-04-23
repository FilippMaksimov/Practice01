import os
from subprocess import Popen, PIPE

# Python Benchmark Launch
proc_py = Popen(['python', 'LaunchBenchmark.py'], stdout=PIPE, stdin=PIPE)
output_py = proc_py.communicate()[0]
answer_py = output_py.decode('utf-8')
print('The process may take few minutes')
print('Python Benchmark')
print(answer_py)
# C sharp Benchmark Launch
proc_cs = Popen([os.path.abspath('../CSharpBenchmark/bin/x64/Debug/CSharpBenchmark.exe')],
                stdout=PIPE, stdin=PIPE)
output_cs = proc_cs.communicate()[0]
answer_cs = output_cs.decode('cp866')
print('C sharp Benchmark')
print(answer_cs)
# Java Benchmark Launch
proc_java = Popen(['java', '-jar', os.path.abspath('../JavaBenchmark/out/artifacts/Java_jar/Java.jar')],
                  stdout=PIPE, stdin=PIPE)
output_java = proc_java.communicate()[0]
answer_java = output_java.decode('cp1251')
print('Java Benchmark')
print(answer_java)
