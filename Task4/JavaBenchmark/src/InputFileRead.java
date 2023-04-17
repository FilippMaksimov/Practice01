import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.List;

public class InputFileRead {
    public List fileRead() throws IOException {
        String fileName = "src/variable_data.bin";
        String line = "";
        File file = new File(fileName);
        List<String> fileLinesList = Files.readAllLines(file.toPath(), StandardCharsets.UTF_8);
        return fileLinesList;
    }
}

