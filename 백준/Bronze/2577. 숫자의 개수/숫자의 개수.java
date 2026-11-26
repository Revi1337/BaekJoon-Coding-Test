import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * https://acmicpc.net/problem/2577
 */
public class Main {

    private void solution(int a, int b, int c) {
        int[] counter = new int[10];
        String mul = String.valueOf(a * b * c);
        for (char ch : mul.toCharArray()) {
            counter[ch - '0']++;
        }
        for (int cnt : counter) {
            System.out.println(cnt);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedReader br = new BufferedReader(new FileReader("src/baekjoon/input.txt"));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        Main main = new Main();
        main.solution(A, B, C);
    }

}
