import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

/**
 * https://www.acmicpc.net/problem/1181
 */
public class Main {

    public static int solution(String delimiter, int N, String[] words) {
        int answer = 0;
        for (String word : words) {
            word = word.repeat(2);
            if (word.contains(delimiter)) {
                answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        BufferedReader br = new BufferedReader(new InputStreamReader(input));

        String delimiter = br.readLine();
        int N = Integer.parseInt(br.readLine());
        String[] words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }
        System.out.println(solution(delimiter, N, words));
    }
}
