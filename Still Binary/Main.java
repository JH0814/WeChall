public class Main {
	public static void main(String[] args){
		String s = "100001110000111001111100110010011011000110100100010100001000010100111010100111000101";
		int len = s.length()/7;
		for(int i = 0; i<len; i++) {
			int cnt = 0;
			String num;
			for(int j = 0; j<7; j++) {
				if(s.substring(7*i + j, 7*i + j +1) == "1") {
					cnt++;
				}
			}
			if(cnt % 2 == 1) {
				num = "1"+s.substring(7*i, 7*(i+1));
			}
			else {
				num = "0"+s.substring(7*i, 7*(i+1));
			}
			int exp = 1;
			int sum = 0;
			for(int j = 7; j>=0; j--) {
				sum += exp*(Integer.parseInt(num.substring(j, j+1)));
				exp *= 2;
			}
			System.out.print((char)sum);
		}
	}
}
