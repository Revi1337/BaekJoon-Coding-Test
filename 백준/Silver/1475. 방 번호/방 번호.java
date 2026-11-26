import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * https://acmicpc.net/problem/1475
 */
public class Main {

    private int solution(int n) {
        int[] counter = new int[10];
        for (char ch : String.valueOf(n).toCharArray()) {
            int sign = Integer.parseInt(String.valueOf(ch));
            counter[sign]++;
        }

        int val = (counter[6] + counter[9] + 1) / 2;
        counter[6] = val;
        counter[9] = 0;

        return Arrays.stream(counter).max().getAsInt();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedReader br = new BufferedReader(new FileReader("src/baekjoon/input.txt"));
        int N = Integer.parseInt(br.readLine());

        Main main = new Main();
        System.out.println(main.solution(N));
    }

}
