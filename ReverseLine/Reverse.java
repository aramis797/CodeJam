import java.util.*;
public class Reverse{

	public static void main(String[] args){

		Scanner sc = new Scanner(System.in);
		int t = Integer.valueOf(sc.nextLine());
		for(int i=1;i<=t;i++){
			String line = sc.nextLine();
			String[] words = line.split(" ");
			String outString="";
			for(int j=words.length-1;j>=0;j--){
				outString+=" "+words[j];
			}
			System.out.println("Case #" + i + ":" + outString);

		}
	}
}