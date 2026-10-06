import java.util.*;

// ===== 주어진 코드. 수정하지 않는다 =====

enum SpotSize { SMALL, MEDIUM, LARGE }

abstract class Vehicle {
    private final String plate;

    protected Vehicle(String plate) {
        if (plate == null || plate.isEmpty()) {
            throw new IllegalArgumentException("plate must not be empty");
        }
        this.plate = plate;
    }

    public final String getPlate() {
        return plate;
    }

    /** Returns true if this vehicle can park in a spot of the given size. */
    public abstract boolean fits(SpotSize size);

    public abstract int hourlyRate();

    /** The most a vehicle pays for one day. Subclasses may override. */
    public int dailyCap() {
        return hourlyRate() * 10;
    }

    /** Fee for a stay of the given number of minutes. See "Fees". */
    public final long fee(int minutes) {
        if (minutes < 0) {
            throw new IllegalArgumentException("negative duration");
        }
        if (minutes <= 30) {
            return 0;
        }
        long fullDays = minutes / 1440;
        int rest = minutes % 1440;
        long hours = (rest + 59) / 60;
        return fullDays * dailyCap() + Math.min(hours * hourlyRate(), (long) dailyCap());
    }
}

// ===== 여기부터 구현. Motorcycle, Car, Bus, ParkingLot =====
class Motorcycle extends Vehicle {

    protected Motorcycle(String plate) {
        super(plate);
    }

    @Override
    public boolean fits(SpotSize size) {
        return true;
    }

    @Override
    public int hourlyRate() {
        return 500;
    }
}

class Car extends Vehicle {

    protected Car(String plate) {
        super(plate);
    }

    @Override
    public boolean fits(SpotSize size) {
        return size == SpotSize.MEDIUM || size == SpotSize.LARGE;
    }

    @Override
    public int hourlyRate() {
        return 1000;
    }
}

class Bus extends Vehicle {

    protected Bus(String plate) {
        super(plate);
    }

    @Override
    public boolean fits(SpotSize size) {
        return size == SpotSize.LARGE;
    }

    @Override
    public int hourlyRate() {
        return 3000;
    }

    @Override 
    public int dailyCap() {
        return 20000;
    }
}

class ParkingLot {
    private final SpotSize[] spots; // {LARGE, SMALL, MEDIUM, MEDIUM}
    private final Integer[] spotOrders; // {1, 2, 3, 0}
    private final Parking[] parkings;
    private final Map<String, Parking> parkedPlates;
    private int spotSize;

    private static class Parking {
        Vehicle vehicle;
        int order;
        int minute;

        Parking(Vehicle vehicle, int order, int minute) {
            this.vehicle = vehicle;
            this.order = order;
            this.minute = minute;
        }
    }
    

    ParkingLot(SpotSize[] spots) {
        this.spots = spots;
        this.spotSize = spots.length;
        this.spotOrders = new Integer[this.spotSize];
        for (int i = 0; i < this.spotSize; i++) {
            this.spotOrders[i] = i;
        }
        Arrays.sort(this.spotOrders, (a, b) -> spots[a].compareTo(spots[b]));
        this.parkings = new Parking[this.spotSize];
        this.parkedPlates = new HashMap<>();
    }

    // parks the vehicle. 
    // The vehicle takes a spot of the smallest size it fits in that still has a free spot. 
    // Among the free spots of that size, it takes the one with the lowest number. 
    // The method returns false and changes nothing if a vehicle with the same plate is already parked, or if no suitable spot is free. 
    // Otherwise it returns true.
    boolean park(Vehicle vehicle, int minute) {
        if (parkedPlates.containsKey(vehicle.getPlate())) {
            return false;
        }

        for (int order : this.spotOrders) {
            if (parkings[order] == null && vehicle.fits(spots[order])) {
                Parking parking = new Parking(vehicle, order, minute);
                parkings[order] = parking;
                parkedPlates.put(vehicle.getPlate(), parking);
                return true;
            }
        }
        return false;
    }

    // removes the vehicle with the given plate from the lot, 
    // frees its spot and returns the fee for its stay. 
    // It returns -1 if no vehicle with that plate is parked. 
    // If minute is earlier than the time at which the vehicle entered, 
    // the method throws IllegalArgumentException and the lot stays unchanged.
    long leave(String plate, int minute) {
        Parking parking = parkedPlates.get(plate);

        if (parking == null) {
            return -1;
        }

        if (minute < parking.minute) {
            throw new IllegalArgumentException("Minute must not be earlier than vehicle entered.");
        }

        parkings[parking.order] = null;
        parkedPlates.remove(plate);

        return parking.vehicle.fee(minute - parking.minute);
    }

    int freeCount(SpotSize size) {
        int freeCount = 0;
        for (int i = 0; i < spotSize; i++) {
            if (spots[i] == size && parkings[i] == null) {
                freeCount++;
            }
        }

        return freeCount;
    }
}


// ===== 풀고 나서 노션의 테스트 코드 토글을 열어 public class Main 을 아래에 붙인다 =====
public class Main {
    static int fail = 0;

    static void check(String name, Object actual, Object expected) {
        boolean ok = Objects.equals(actual, expected);
        if (!ok) fail++;
        System.out.println((ok ? "PASS " : "FAIL ") + name + " -> " + actual + (ok ? "" : " (expected " + expected + ")"));
    }

    public static void main(String[] args) {
        Car c = new Car("FEE");
        check("car 30", c.fee(30), 0L);
        check("car 31", c.fee(31), 1000L);
        check("car 61", c.fee(61), 2000L);
        check("car 601", c.fee(601), 10000L);
        check("car 1500", c.fee(1500), 11000L);
        check("bus 360", new Bus("B").fee(360), 18000L);
        check("bus 420", new Bus("B").fee(420), 20000L);
        check("moto 90", new Motorcycle("M").fee(90), 1000L);

        SpotSize[] layout = {SpotSize.LARGE, SpotSize.SMALL, SpotSize.MEDIUM, SpotSize.MEDIUM};
        ParkingLot lot = new ParkingLot(layout);
        check("park C1", lot.park(new Car("C1"), 0), true);
        check("park M1", lot.park(new Motorcycle("M1"), 0), true);
        check("park M2", lot.park(new Motorcycle("M2"), 10), true);
        check("park C2", lot.park(new Car("C2"), 10), true);
        check("park B1 full", lot.park(new Bus("B1"), 20), false);
        check("park C1 again", lot.park(new Car("C1"), 30), false);
        check("free LARGE", lot.freeCount(SpotSize.LARGE), 0);
        check("free SMALL", lot.freeCount(SpotSize.SMALL), 0);
        check("free MEDIUM", lot.freeCount(SpotSize.MEDIUM), 0);
        check("leave C2", lot.leave("C2", 71), 2000L);
        check("park B1", lot.park(new Bus("B1"), 80), true);
        check("leave unknown", lot.leave("X", 100), -1L);
        check("leave M1", lot.leave("M1", 30), 0L);
        check("free SMALL after", lot.freeCount(SpotSize.SMALL), 1);
        check("leave B1", lot.leave("B1", 500), 20000L);
        check("leave B1 twice", lot.leave("B1", 600), -1L);

        try {
            lot.leave("C1", -5);
            fail++;
            System.out.println("FAIL leave before enter -> no exception");
        } catch (IllegalArgumentException e) {
            System.out.println("PASS leave before enter -> IllegalArgumentException");
        }
        check("C1 still parked after bad leave", lot.leave("C1", 120), 2000L);

        System.out.println(fail == 0 ? "ALL PASS" : fail + " FAILED");
    }
}
