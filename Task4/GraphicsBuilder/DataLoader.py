import os


def csharp50_loader():
    with open(os.path.abspath('../Data/csharp50_thread0.bin'), 'rb') as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/csharp50_thread2.bin'), 'rb') as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/csharp50_thread4.bin'), 'rb') as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/csharp50_thread8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


def csharp100_loader():
    with open(os.path.abspath('../Data/csharp100_thread0.bin'), 'rb') as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/csharp100_thread2.bin'), 'rb') as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/csharp100_thread4.bin'), 'rb') as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/csharp100_thread8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


def csharp200_loader():
    with open(os.path.abspath('../Data/csharp200_thread0.bin'), 'rb') as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/csharp200_thread2.bin'), 'rb') as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/csharp200_thread4.bin'), 'rb') as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/csharp200_thread8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


def java50_loader():
    with open(os.path.abspath('../Data/java50_threads0.bin'), 'rb') as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/java50_threads2.bin'), 'rb') as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/java50_threads4.bin'), 'rb') as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/java50_threads8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


def java100_loader():
    with open(os.path.abspath('../Data/java100_threads0.bin'), 'rb') as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/java100_threads2.bin'), 'rb') as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/java100_threads4.bin'), 'rb') as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/java100_threads8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


def java200_loader():
    with open(os.path.abspath('../Data/java200_threads0.bin'), 'rb') as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/java200_threads2.bin'), 'rb') as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/java200_threads4.bin'), 'rb') as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/java200_threads8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


def python50_loader():
    with open(os.path.abspath('../Data/python50_threads0.bin'), 'rb') as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/python50_threads2.bin'), 'rb') as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/python50_threads4.bin'), 'rb') as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/python50_threads8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


def python100_loader():
    with open(os.path.abspath('../Data/python100_threads0.bin'), 'rb') as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/python100_threads2.bin'), 'rb') as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/python100_threads4.bin'), 'rb') as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/python100_threads8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


def python200_loader():
    with open(os.path.abspath('../Data/python200_threads0.bin'), "rb") as f1:
        s = f1.readline()
        th_zero_int_time = int(f1.readline().decode())
        th_zero_int_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_bigint_time = int(f1.readline().decode())
        th_zero_bigint_rc = int(f1.readline().decode())
        s = f1.readline()
        th_zero_float_time = int(f1.readline().decode())
        th_zero_float_rc = int(f1.readline().decode())
    with open(os.path.abspath('../Data/python200_threads2.bin'), "rb") as f2:
        s = f2.readline()
        th_two_int_time = int(f2.readline().decode())
        th_two_int_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_bigint_time = int(f2.readline().decode())
        th_two_bigint_rc = int(f2.readline().decode())
        s = f2.readline()
        th_two_float_time = int(f2.readline().decode())
        th_two_float_rc = int(f2.readline().decode())
    with open(os.path.abspath('../Data/python200_threads4.bin'), "rb") as f3:
        s = f3.readline()
        th_four_int_time = int(f3.readline().decode())
        th_four_int_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_bigint_time = int(f3.readline().decode())
        th_four_bigint_rc = int(f3.readline().decode())
        s = f3.readline()
        th_four_float_time = int(f3.readline().decode())
        th_four_float_rc = int(f3.readline().decode())
    with open(os.path.abspath('../Data/python200_threads8.bin'), 'rb') as f4:
        s = f4.readline()
        th_eight_int_time = int(f4.readline().decode())
        th_eight_int_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_bigint_time = int(f4.readline().decode())
        th_eight_bigint_rc = int(f4.readline().decode())
        s = f4.readline()
        th_eight_float_time = int(f4.readline().decode())
        th_eight_float_rc = int(f4.readline().decode())
    return th_zero_int_time, th_zero_int_rc, th_two_int_time, th_two_int_rc, \
        th_four_int_time, th_four_int_rc, th_eight_int_time, th_eight_int_rc, \
        th_zero_bigint_time, th_zero_bigint_rc, th_two_bigint_time, th_two_bigint_rc, \
        th_four_bigint_time, th_four_bigint_rc, th_eight_bigint_time, th_eight_bigint_rc, \
        th_zero_float_time, th_zero_float_rc, th_two_float_time, th_two_float_rc, \
        th_four_float_time, th_four_float_rc, th_eight_float_time, th_eight_float_rc


print(os.path.abspath('../Data/java50_threads0.bin'))
print(python200_loader()[0])
print(type(csharp50_loader()[1]))
print(type(csharp200_loader()[6]))

