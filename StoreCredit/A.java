import java.io.File;
import java.util.HashMap;
import java.util.Scanner;


public class A {

	public void run() {
		try {
			Scanner s = new Scanner(new File("A.in"));
			int tests = s.nextInt();
			for (int i = 0; i < tests; i++) {
				int credit = s.nextInt();
				int number = s.nextInt();
				int[] prices = new int[number];
				for (int j = 0; j < prices.length; j++) {
					prices[j] = s.nextInt();
				}
				HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
				int first = -1;
				int second = -1;
				for (int j = 0; j < prices.length; j++) {
					if (map.containsKey(prices[j])) {
						first = j;
						second = map.get(prices[j]);
						break;
					}
					else {
						map.put(credit-prices[j], j);
					}
				}
				first ++;
				second ++;
				if (first < second) {
					System.out.println("Case #" + (i+1) + ": " + first + " " + second);
				}
				else {
					System.out.println("Case #" + (i+1) + ": " + second + " " + first);
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		new A().run();
	}
}
