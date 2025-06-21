import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * https://www.acmicpc.net/problem/1373
 */
public class Main {

    public String solution(String binary) {
        StringBuilder sb = new StringBuilder();

        int padding = (3 - binary.length() % 3) % 3;
        for (int i = 0; i < padding; i++) {
            sb.append("0");
        }
        sb.append(binary);
        String padded = sb.toString();

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < padded.length(); i += 3) {
            String chunk = padded.substring(i, i + 3);
            int decimal = Integer.parseInt(chunk, 2);
            result.append(decimal);
        }

        return result.toString();
    }

    public static void main(String[] args) throws IOException {
        InputStream input = System.in;
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(input));

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        Main joon1373 = new Main();
        String string = stringTokenizer.nextToken();

        System.out.println(joon1373.solution(string));
    }
}