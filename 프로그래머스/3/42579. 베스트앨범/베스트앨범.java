import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, List<int[]>> music = new HashMap<>();
        Map<String, Integer> counter = new HashMap<>();

        for (int idx = 0; idx < genres.length; idx++) {
            String genre = genres[idx];
            int play = plays[idx];

            List<int[]> songs = music.getOrDefault(genre, new ArrayList<>());
            songs.add(new int[]{idx, play});
            music.put(genre, songs);

            counter.put(genre, counter.getOrDefault(genre, 0) + play);
        }

        List<String> order = new ArrayList<>(counter.keySet());
        order.sort((a, b) -> Integer.compare(counter.get(b), counter.get(a)));

        List<Integer> answer = new ArrayList<>();
        for (String genre : order) {
            List<int[]> songs = music.get(genre);
            songs.sort((a, b) -> Integer.compare(b[1], a[1]));

            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                answer.add(songs.get(i)[0]);
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}