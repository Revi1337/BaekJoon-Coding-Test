import java.io.*;

/**
 * https://www.acmicpc.net/problem/1427
 */
public class Main {

    public static String solution(int N) {
        String str = String.valueOf(N);
        int[] cache = new int[10];
        for (int i = 0; i < str.length(); i++) {
            cache[Character.getNumericValue(str.charAt(i))]++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 9; i > -1; i--) {
            String number = String.valueOf(i);
            sb.append(number.repeat(cache[i]));
        }
        sb.append('\n');

        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        BufferedReader br = new BufferedReader(new InputStreamReader(input));

        int N = Integer.parseInt(br.readLine());
        System.out.println(solution(N));
    }
}
