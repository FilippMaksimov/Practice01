package BenchmarkCalculation;

import BenchmarkCalculation.BigIntegerCalculation;
import BenchmarkCalculation.Calculations;
import BenchmarkCalculation.DoubleCalculation;
import BenchmarkCalculation.IntegerCalculation;

import java.math.BigInteger;

public class CalculationsFactory<M> {
    private Class<M> calcClass;
    public CalculationsFactory(Class<M> calcClass) {
        this.calcClass = calcClass;
    }
    public Calculations<M> getSomeClass() {
        Calculations<M> calculation = null;
        if (calcClass.equals(Integer.class)) {
            calculation = (Calculations<M>) new IntegerCalculation();
        }
        else if (calcClass.equals(BigInteger.class)) {
            calculation = (Calculations<M>) new BigIntegerCalculation();
        }
        else if (calcClass.equals(Double.class)) {
            calculation = (Calculations<M>) new DoubleCalculation();
        }
        return calculation;
    }
}
