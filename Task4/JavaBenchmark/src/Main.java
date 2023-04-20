import ReadingType.DataRead;
import ReadingType.InputFileRead;
import ReadingType.IntegerRead;

import java.io.FileOutputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        //Запуск без использования потоков
        readData(8);
        //Запуск с двумя потоками
        readData(4);
        //Запуск с 4 потоками
        readData(2);
        //Запуск с 8 потоками
        readData(0);
    }
    public static void readData(int thread) throws IOException {
        //Запустить writer!
        BenchmarkLaunch<Integer> benchInt = new BenchmarkLaunch<>(Integer.class, thread);
        BenchmarkLaunch<BigInteger> benchBigInt = new BenchmarkLaunch<>(BigInteger.class, thread);
        BenchmarkLaunch<Double> benchDouble = new BenchmarkLaunch<>(Double.class, thread);
        String fileName = "java_threads" + thread + ".bin";
        String intTitle = "Java integer Data" + "\n";
        String bigIntTitle = "Java bigInteger Data" + "\n";
        String doubleTitle = "Java double Data" + "\n";

        List<String> dataInt = new ArrayList<>();
        List<String> dataBigInt = new ArrayList<>();
        List<String> dataDouble =new ArrayList<>();

        for (Integer item: benchInt.benchmarkStart()) {
            dataInt.add(item.toString());
        }
        for (Integer item: benchBigInt.benchmarkStart()) {
            dataBigInt.add(item.toString());
        }
        for (Integer item: benchDouble.benchmarkStart()) {
            dataDouble.add(item.toString());
        }

        try(FileOutputStream fos = new FileOutputStream(fileName)) {
            int j = 0;
            byte[] intBuffer = intTitle.getBytes();
            fos.write(intBuffer, j, intBuffer.length);
            for (String item: dataInt) {
                String str = item + "\n";
                byte[] buffer = str.getBytes();
                fos.write(buffer, j, buffer.length);
            }
            byte[] bigIntBuffer = bigIntTitle.getBytes();
            fos.write(bigIntBuffer, j, bigIntBuffer.length);
            for (String item: dataBigInt) {
                String str = item + "\n";
                byte[] buffer = str.getBytes();
                fos.write(buffer, j, buffer.length);
            }
            byte[] doubleBuffer = doubleTitle.getBytes();
            fos.write(doubleBuffer, j, doubleBuffer.length);
            for (String item: dataDouble) {
                String str = item + "\n";
                byte[] buffer = str.getBytes();
                fos.write(buffer, j, buffer.length);
            }
            System.out.println("Файл записан успешно");
        }
        catch (IOException ex) {
            System.out.println("Не удалось записать файл");
            System.out.println(ex.getMessage());
        }
    }
}