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
        readData(1);
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

        try(FileOutputStream fos = new FileOutputStream(fileName)) {
            int j = 0;
            byte[] intBuffer = intTitle.getBytes();
            fos.write(intBuffer, j, intBuffer.length);
            for (Long item: benchInt.benchmarkStart()) {
                String str = item.toString() + "\n";
                byte[] buffer = str.toString().getBytes();
                fos.write(buffer, j, buffer.length);
            }
            byte[] bigIntBuffer = bigIntTitle.getBytes();
            fos.write(bigIntBuffer, j, bigIntBuffer.length);
            for (Long item: benchBigInt.benchmarkStart()) {
                String str = item.toString() + "\n";
                byte[] buffer = str.toString().getBytes();
                fos.write(buffer, j, buffer.length);
            }
            byte[] doubleBuffer = doubleTitle.getBytes();
            fos.write(doubleBuffer, j, doubleBuffer.length);
            for (Long item: benchDouble.benchmarkStart()) {
                String str = item.toString() + "\n";
                byte[] buffer = str.toString().getBytes();
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