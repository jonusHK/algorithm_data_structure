import java.util.*;
// ===== 주어진 코드. 수정하지 않는다 =====
/*
- Every withdrawal costs a fee of 500.
- The balance may become negative, but never lower than -100,000 after a withdrawal (including its fee).
- At the end of the month, if the balance is negative, the account is charged interest of 1% of the overdrawn amount, **rounded up** to a whole won. A balance of zero or more is not changed.

*/
abstract class Account {
    private final String id;
    protected long balance;

    protected Account(String id, long initialBalance) {
        if (id == null || id.isEmpty()) {
            throw new IllegalArgumentException("id must not be empty");
        }
        if (initialBalance < 0) {
            throw new IllegalArgumentException("initial balance must not be negative");
        }
        this.id = id;
        this.balance = initialBalance;
    }

    public final String getId() {
        return id;
    }

    public final long getBalance() {
        return balance;
    }

    public final void deposit(long amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("amount must be positive");
        }
        balance += amount;
    }

    /**
     * Withdraws the amount plus the fee for this withdrawal.
     * Returns false and changes nothing if the account cannot pay.
     */
    public final boolean withdraw(long amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("amount must be positive");
        }
        long total = amount + fee(amount);
        if (!canPay(total)) {
            return false;
        }
        balance -= total;
        afterWithdraw();
        return true;
    }

    /** The fee for a withdrawal of the given amount. */
    protected abstract long fee(long amount);

    /** Whether the account can pay the given total (amount plus fee). */
    protected abstract boolean canPay(long total);

    /** Called only after a successful withdrawal. Does nothing by default. */
    protected void afterWithdraw() {
    }

    /** Called once at the end of every month. */
    public abstract void monthEnd();
}

// ===== 여기부터 구현. CheckingAccount, SavingsAccount, Bank =====

class CheckingAccount extends Account {

    // 왜 protected 사용하는지?
    protected CheckingAccount(String id, long initialBalance) {
        super(id, initialBalance);
    }

    /*
    - Every withdrawal costs a fee of 500.
    - The balance may become negative, but never lower than -100,000 after a withdrawal (including its fee).
    - At the end of the month, if the balance is negative, the account is charged interest of 1% of the overdrawn amount, **rounded up** to a whole won. A balance of zero or more is not changed.
    */

    @Override
    protected long fee(long amount) {
        return 500;
    }

    @Override
    protected boolean canPay(long total) {
        return balance - total >= -100000;
    }

    @Override
    public void monthEnd() {
        if (balance >= 0) {
            return;
        }

        System.out.println("CheckingAccount.monthEnd() - " + balance);

        if (balance < 0) {
            long overdrawn = -balance;                // 501
            balance -= (overdrawn + 99) / 100;        // 501+99 = 600, /100 = 6
        }
    }
}

class SavingsAccount extends Account {
    private int withdrawalCount = 0;

    protected SavingsAccount(String id, long initialBalance) {
        super(id, initialBalance);
    }

    /*
    - The first three successful withdrawals in each month are free. Every further withdrawal in the same month costs a fee of 1,000. A withdrawal that fails does not count.
    - The balance can never become negative.
    - At the end of the month, the account earns interest of 0.2% of its balance, **rounded down** to a whole won. The count of withdrawals starts again from zero.
    */

    @Override
    protected long fee(long amount) {
        return withdrawalCount < 3 ? 0 : 1000;
    }

    @Override
    protected boolean canPay(long total) {
        return balance >= total;
    }

    @Override 
    protected void afterWithdraw() {
        withdrawalCount++;
    }

    @Override
    public void monthEnd() {
        balance = (long) Math.floor(balance + (balance * 2 / 1000));
        withdrawalCount = 0;
    }
}

/*
Assume that there are at most 1,000 accounts, at most 100,000 calls in total, and every amount is an integer within the range 1..1,000,000,000.
*/

class Bank {
    private final Map<String, Account> accounts = new HashMap<>();
    

    // 여기서 public 과 public 미사용의 차이는?
    // adds the account to the bank. It returns `false` and changes nothing if an account with the same id already exists.
    public boolean open(Account account) {
        if (accounts.containsKey(account.getId())) {
            return false;
        }
        accounts.put(account.getId(), account);

        return true;
    }

    // withdraws `amount` (plus the fee) from the first account and deposits `amount` into the second. 
    // It returns `false` and changes nothing if either account does not exist, if both ids are the same, or if the withdrawal is not allowed. 
    // Otherwise it returns `true`.
    public boolean transfer(String fromId, String toId, long amount) {
        Account from = accounts.get(fromId);
        Account to = accounts.get(toId);

        if (from == null || to == null || from.getId().equals(to.getId())) {
            return false;
        }

        if (!from.withdraw(amount)) {
            return false;
        }

        to.deposit(amount);

        return true;
    }

    // ends the month for every account.
    public void monthEnd() {
        accounts.values().stream().forEach(Account::monthEnd);
    }

    // returns the sum of all balances.
    public long total() {
        return accounts.values().stream().mapToLong(Account::getBalance).sum();
    }

    // returns the ids of all accounts ordered by balance from **highest to lowest**. 
    // Accounts with equal balances are ordered by id in ascending (alphabetical) order.
    public List<String> ranking() {
        List<Account> list = new ArrayList<>(accounts.values());
        list.sort(Comparator.comparingLong(Account::getBalance).reversed()
            .thenComparing(Account::getId));

        List<String> ids = new ArrayList<>();
        for (Account a : list) ids.add(a.getId());
        return ids;
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
        CheckingAccount c = new CheckingAccount("C", 10_000);
        check("checking withdraw", c.withdraw(5_000), true);
        check("checking balance", c.getBalance(), 4_500L);
        check("checking to limit", c.withdraw(104_000), true);
        check("checking at limit", c.getBalance(), -100_000L);
        check("checking over limit", c.withdraw(1), false);
        check("checking unchanged", c.getBalance(), -100_000L);
        c.monthEnd();
        check("checking interest", c.getBalance(), -101_000L);
        CheckingAccount c2 = new CheckingAccount("C2", 0);
        c2.withdraw(1);
        c2.monthEnd();
        check("checking interest rounds up", c2.getBalance(), -507L);

        SavingsAccount s = new SavingsAccount("S", 10_000);
        s.withdraw(1_000);
        s.withdraw(1_000);
        s.withdraw(1_000);
        check("savings 3 free", s.getBalance(), 7_000L);
        check("savings 4th", s.withdraw(1_000), true);
        check("savings 4th fee", s.getBalance(), 5_000L);
        check("savings insufficient", s.withdraw(6_000), false);
        s.monthEnd();
        check("savings interest", s.getBalance(), 5_010L);
        s.withdraw(1_000);
        check("savings reset", s.getBalance(), 4_010L);

        SavingsAccount s2 = new SavingsAccount("S2", 3_000);
        s2.withdraw(5_000);
        s2.withdraw(5_000);
        s2.withdraw(1_000);
        s2.withdraw(1_000);
        check("failed withdrawals do not count", s2.withdraw(1_000), true);
        check("failed withdrawals balance", s2.getBalance(), 0L);

        SavingsAccount s3 = new SavingsAccount("S3", 1_499);
        s3.monthEnd();
        check("savings interest rounds down", s3.getBalance(), 1_501L);

        checkThrows("negative initial", () -> new CheckingAccount("X", -1));
        checkThrows("zero deposit", () -> new SavingsAccount("X", 0).deposit(0));

        Bank b = new Bank();
        check("open C1", b.open(new CheckingAccount("C1", 50_000)), true);
        check("open S1", b.open(new SavingsAccount("S1", 20_000)), true);
        check("open C1 again", b.open(new SavingsAccount("C1", 1)), false);
        check("transfer ok", b.transfer("C1", "S1", 10_000), true);
        check("transfer insufficient", b.transfer("S1", "C1", 40_000), false);
        check("transfer unknown", b.transfer("X", "S1", 1), false);
        check("transfer self", b.transfer("C1", "C1", 1), false);
        check("total after transfers", b.total(), 39_500L + 30_000L);
        b.open(new SavingsAccount("S2", 39_500));
        check("ranking tie by id", b.ranking(), List.of("C1", "S2", "S1"));
        b.monthEnd();
        check("ranking after month end", b.ranking(), List.of("S2", "C1", "S1"));
        check("total after month end", b.total(), 39_500L + 30_060L + 39_579L);

        System.out.println(fail == 0 ? "ALL PASS" : fail + " FAILED");
    }
}
