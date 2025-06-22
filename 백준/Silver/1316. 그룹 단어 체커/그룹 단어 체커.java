import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;


public class Main {

    public static int solution(int N, String[] words) {
        int answer = 0;
        for (String word : words) {
            int[] cache = new int[26];
            cache[word.charAt(0) - 97] = 1;
            boolean breaked = false;
            for (int i = 1; i < word.length(); i++) {
                if (word.charAt(i) != word.charAt(i - 1)) {
                    if (cache[word.charAt(i) - 97] == 1) {
                        breaked = true;
                        break;
                    }
                    cache[word.charAt(i) - 97] = 1;
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