import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashSet;


public class Main {

    public static int solution(int N, String[] words) {
        int answer = 0;
        for (String word : words) {
            HashSet<Character> set = new HashSet<>();
            set.add(word.charAt(0));
            boolean breaked = false;
            for (int i = 1; i < word.length(); i++) {
                if (word.charAt(i) != word.charAt(i - 1)) {
                    if (set.contains(word.charAt(i))) {
                        breaked = true;
                        break;
                    } else {
                        set.add(word.charAt(i));
                    }
                }
            }
            if (!breaked) {
                answer += 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        BufferedReader br = new BufferedReader(new InputStreamReader(input));

        int N = Integer.parseInt(br.readLine());
        String[] words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }
        System.out.println(solution(N, words));
    }
}