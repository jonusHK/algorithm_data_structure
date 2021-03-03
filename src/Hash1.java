import java.util.HashMap;

public class Hash1 {
    public static String solution(String[] participant, String[] completion) {
        HashMap map = new HashMap<String, Integer>();
        for (String val : participant) {
            if (map.containsKey(val)) {
                map.put(val, (int)map.get(val) + 1);
            } else {
                map.put(val, 1);
            }
        }

        for (String val : completion) {
            map.put(val, (int)map.get(val) - 1);
        }

        String[] answer = {""};
        map.forEach((key, value) -> {
            if ((int)value == 1) {
                answer[0] = (String) key;
            }
        });
        return answer[0];
    }

    public static void main(String[] args) {
        String[] participant = {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[] completion = {"josipa", "filipa", "marina", "nikola"};
        System.out.println(solution(participant, completion));
    }
}
