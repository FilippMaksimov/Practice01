package ReadingType;

import java.util.List;

public interface DataRead<T> {
    public abstract T[][] getMatrixA();
    public abstract T[][] getMatrixB();
    public abstract List<T> getScalars();
}
