import java.util.*;
import java.util.stream.Collectors;

// ===== 주어진 코드. 수정하지 않는다 =====

abstract class Parcel {
    protected final String id;
    protected final int weightGrams;

    protected Parcel(String id, int weightGrams) {
        if (id == null || id.isEmpty()) {
            throw new IllegalArgumentException("id must not be empty");
        }
        if (weightGrams <= 0) {
            throw new IllegalArgumentException("weight must be positive");
        }
        this.id = id;
        this.weightGrams = weightGrams;
    }

    /** The standard rate described in "Rates". */
    protected final long baseCost() {
        if (weightGrams <= 1000) {
            return 3000;
        }
        int extra = weightGrams - 1000;
        int steps = (extra + 499) / 500;
        return 3000 + steps * 500L;
    }

    public final String getId() {
        return id;
    }

    public abstract long shippingCost();

    public String label() {
        return id + ":" + shippingCost();
    }
}

// ===== 여기부터 구현. StandardParcel, ExpressParcel, FragileParcel, ShippingBatch =====
class StandardParcel extends Parcel {
    public StandardParcel(String id, int weightGrams) {
        super(id, weightGrams);
    }

    @Override
    public long shippingCost() {
        return baseCost();
    }
}

class ExpressParcel extends Parcel {
    public ExpressParcel(String id, int weightGrams) {
        super(id, weightGrams);
    }

    @Override
    public long shippingCost() {
        long shippingCost = baseCost() * 2;
        return shippingCost < 7000 ? 7000 : shippingCost;
    }
}

class FragileParcel extends Parcel {
    public FragileParcel(String id, int weightGrams) {
        super(id, weightGrams);

        if (weightGrams > 5000) {
            throw new IllegalArgumentException("Fragile parcel weight must not exceed 5000 grams");
        }
    }

    @Override
    public long shippingCost() {
        return baseCost() + 2000;
    }

    @Override 
    public String label() {
        return super.label() + " [FRAGILE]";
    }
}

class ShippingBatch {
    private final Map<String, Parcel> parcels;

    public ShippingBatch() {
        this.parcels = new LinkedHashMap<>();
    }

    public void add(Parcel parcel) {
        if (parcels.containsKey(parcel.getId())) {
            return; // Ignore if a parcel with the same id already exists
        }
        parcels.put(parcel.getId(), parcel);
    }

    public int size() {
        return parcels.size();
    }

    public long totalCost() {
        long totalCost = parcels.values().stream().mapToLong(Parcel::shippingCost).sum();

        if (parcels.size() >= 5) {
            totalCost = totalCost * 93 / 100; // Apply 7% discount
        }
        return (totalCost / 10) * 10; // Round down to the nearest 10
    }

    public List<String> labels() {
        return parcels.values().stream().map(Parcel::label).collect(Collectors.toList());
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

    static void checkThrows(String name, Runnable r) {
        try {
            r.run();
            fail++;
            System.out.println("FAIL " + name + " -> no exception");
        } catch (IllegalArgumentException e) {
            System.out.println("PASS " + name + " -> IllegalArgumentException");
        }
    }

    public static void main(String[] args) {
        check("standard 1000", new StandardParcel("P1", 1000).shippingCost(), 3000L);
        check("standard 1001", new StandardParcel("P1", 1001).shippingCost(), 3500L);
        check("standard 1500", new StandardParcel("P1", 1500).shippingCost(), 3500L);
        check("standard 1501", new StandardParcel("P1", 1501).shippingCost(), 4000L);
        check("express 250", new ExpressParcel("P1", 250).shippingCost(), 7000L);
        check("express 1501", new ExpressParcel("P1", 1501).shippingCost(), 8000L);
        check("fragile 1000", new FragileParcel("P1", 1000).shippingCost(), 5000L);
        check("fragile 5000", new FragileParcel("P1", 5000).shippingCost(), 9000L);
        checkThrows("fragile 5001", () -> new FragileParcel("P1", 5001));
        checkThrows("weight 0", () -> new StandardParcel("P1", 0));
        checkThrows("empty id", () -> new ExpressParcel("", 100));
        check("label standard", new StandardParcel("A7", 1200).label(), "A7:3500");
        check("label fragile", new FragileParcel("F2", 300).label(), "F2:5000 [FRAGILE]");

        ShippingBatch b1 = new ShippingBatch();
        b1.add(new StandardParcel("P1", 1000));
        b1.add(new ExpressParcel("P2", 250));
        b1.add(new FragileParcel("P3", 1000));
        check("batch3 total", b1.totalCost(), 15000L);

        ShippingBatch b2 = new ShippingBatch();
        b2.add(new StandardParcel("P1", 1001));
        b2.add(new StandardParcel("P2", 1000));
        b2.add(new StandardParcel("P3", 250));
        b2.add(new StandardParcel("P4", 999));
        b2.add(new StandardParcel("P5", 1));
        check("batch5 total", b2.totalCost(), 14410L);

        ShippingBatch b3 = new ShippingBatch();
        b3.add(new StandardParcel("P1", 1000));
        b3.add(new ExpressParcel("P1", 9000));
        check("duplicate size", b3.size(), 1);
        check("duplicate total", b3.totalCost(), 3000L);
        check("labels order", b1.labels(), List.of("P1:3000", "P2:7000", "P3:5000 [FRAGILE]"));

        check("empty total", new ShippingBatch().totalCost(), 0L);

        System.out.println(fail == 0 ? "ALL PASS" : fail + " FAILED");
    }
}
