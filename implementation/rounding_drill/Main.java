import java.util.*;

// 올림, 내림, 반올림 연습. 각 메서드의 return 0 을 지우고 한 줄로 채운다.
// double 을 쓰지 않는다. average 만 예외.
// 실행: javac --release 11 Main.java && java Main

class Rounding {
    // a >= 0, b > 0 에서 a / b 내림.  7/2 -> 3
    static long floorDiv(long a, long b) {
        return a / b;
    }

    // a >= 0, b > 0 에서 a / b 올림.  7/2 -> 4, 6/2 -> 3
    static long ceilDiv(long a, long b) {
        return (a + b - 1) / b;
    }

    // a >= 0, b > 0 에서 a / b 반올림 (0.5 는 올림).  7/2 -> 4, 4/3 -> 1, 5/3 -> 2
    static long roundDiv(long a, long b) {
        return b % 2 == 0 ? (a + b / 2) / b : (2 * a + b) / (2 * b);
    }

    // x >= 0 을 unit 단위로 내림.  14415, 10 -> 14410
    static long floorTo(long x, long unit) {
        return x / unit * unit;
    }

    // x >= 0 을 unit 단위로 올림.  14411, 10 -> 14420
    static long ceilTo(long x, long unit) {
        return (x + unit - 1) / unit * unit;
    }

    // x >= 0 을 unit 단위로 반올림 (unit 은 짝수).  14415, 10 -> 14420
    static long roundTo(long x, long unit) {
        return (x + unit / 2) / unit * unit;
    }

    // x 의 p% 를 원 단위로 내림.  15500, 93 -> 14415
    static long percentFloor(long x, long p) {
        return x * p / 100;
    }

    // x 의 p% 를 원 단위로 올림.  501, 1 -> 6
    static long percentCeil(long x, long p) {
        return (x * p + 99) / 100;
    }

    // x 의 p% 를 원 단위로 반올림.  149, 1 -> 1,  150, 1 -> 2
    static long percentRound(long x, long p) {
        return (x * p + 50) / 100;
    }

    // 부호와 상관없이 a / b 내림 (b > 0).  -7/2 -> -4
    static long floorDivAnySign(long a, long b) {
        return Math.floorDiv(a, b);
    }

    // 부호와 상관없이 a / b 올림 (b > 0).  -7/2 -> -3
    static long ceilDivAnySign(long a, long b) {
        return -Math.floorDiv(-a, b);
    }

    // 평균 (소수 그대로).  {1, 2} -> 1.5
    static double average(int[] a) {
        double sum = 0;
        for (int num : a) {
            sum += num;
        }

        return sum / a.length;
    }
}

// ===== 아래는 테스트. 수정하지 않는다 =====

public class Main {
    static int fail = 0;

    static void check(String name, Object actual, Object expected) {
        boolean ok = Objects.equals(actual, expected);
        if (!ok) fail++;
        System.out.println((ok ? "PASS " : "FAIL ") + name + " -> " + actual + (ok ? "" : " (expected " + expected + ")"));
    }

    public static void main(String[] args) {
        check("floorDiv 7/2", Rounding.floorDiv(7, 2), 3L);
        check("floorDiv 6/2", Rounding.floorDiv(6, 2), 3L);
        check("ceilDiv 7/2", Rounding.ceilDiv(7, 2), 4L);
        check("ceilDiv 6/2", Rounding.ceilDiv(6, 2), 3L);
        check("ceilDiv 0/5", Rounding.ceilDiv(0, 5), 0L);
        check("ceilDiv 1/1000000000", Rounding.ceilDiv(1, 1_000_000_000L), 1L);
        check("roundDiv 7/2", Rounding.roundDiv(7, 2), 4L);
        check("roundDiv 5/3", Rounding.roundDiv(5, 3), 2L);
        check("roundDiv 4/3", Rounding.roundDiv(4, 3), 1L);
        check("roundDiv 10/4", Rounding.roundDiv(10, 4), 3L);
        check("floorTo 14415,10", Rounding.floorTo(14_415, 10), 14_410L);
        check("ceilTo 14411,10", Rounding.ceilTo(14_411, 10), 14_420L);
        check("ceilTo 14410,10", Rounding.ceilTo(14_410, 10), 14_410L);
        check("roundTo 14415,10", Rounding.roundTo(14_415, 10), 14_420L);
        check("roundTo 14414,10", Rounding.roundTo(14_414, 10), 14_410L);
        check("roundTo 1250,100", Rounding.roundTo(1_250, 100), 1_300L);
        check("percentFloor 15500,93", Rounding.percentFloor(15_500, 93), 14_415L);
        check("percentFloor big", Rounding.percentFloor(2_000_000_000L, 93), 1_860_000_000L);
        check("percentCeil 501,1", Rounding.percentCeil(501, 1), 6L);
        check("percentCeil 500,1", Rounding.percentCeil(500, 1), 5L);
        check("percentRound 149,1", Rounding.percentRound(149, 1), 1L);
        check("percentRound 150,1", Rounding.percentRound(150, 1), 2L);
        check("floorDivAnySign -7/2", Rounding.floorDivAnySign(-7, 2), -4L);
        check("floorDivAnySign 7/2", Rounding.floorDivAnySign(7, 2), 3L);
        check("ceilDivAnySign -7/2", Rounding.ceilDivAnySign(-7, 2), -3L);
        check("ceilDivAnySign 7/2", Rounding.ceilDivAnySign(7, 2), 4L);
        check("ceilDivAnySign -6/2", Rounding.ceilDivAnySign(-6, 2), -3L);
        check("average 1,2", Rounding.average(new int[]{1, 2}), 1.5);
        check("average big", Rounding.average(new int[]{2_000_000_000, 2_000_000_000}), 2.0E9);
        System.out.println(fail == 0 ? "ALL PASS" : fail + " FAILED");
    }
}
